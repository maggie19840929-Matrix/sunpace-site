#!/usr/bin/env python3
"""
Run a small audio/video transcription pilot for Sunny phase 2.

The script reads `media-transcription-pilot.csv`, transcribes short clips with
faster-whisper, and writes local review artifacts. It does not merge transcripts
into Sunny and does not publish source course content.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


RUNTIME_DEPS = Path(".codex_deps/python")
if RUNTIME_DEPS.exists():
    sys.path.insert(0, str(RUNTIME_DEPS.resolve()))

HF_CACHE = Path(".codex_deps/huggingface").resolve()
HF_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("HF_HOME", str(HF_CACHE))
os.environ.setdefault("HUGGINGFACE_HUB_CACHE", str(HF_CACHE / "hub"))

try:
    from faster_whisper import WhisperModel
except Exception as exc:  # pragma: no cover - user-facing setup error
    raise SystemExit(
        "Missing transcription dependencies. Install them into .codex_deps/python with: "
        "python3 -m pip install --target .codex_deps/python faster-whisper"
    ) from exc


def safe_slug(value: str, fallback: str = "media") -> str:
    slug = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", value).strip("-")
    return slug[:90] or fallback


def read_queue(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def resolve_source_path(row: dict[str, str], remap_from: str, remap_to: str) -> Path:
    original = row["source_path"]
    if remap_from and remap_to and original.startswith(remap_from):
        original = remap_to.rstrip("/") + original[len(remap_from):]
    return Path(original)


def require_sources(rows: list[dict[str, str]], remap_from: str, remap_to: str) -> None:
    missing = [row for row in rows if not resolve_source_path(row, remap_from, remap_to).exists()]
    if len(missing) == len(rows):
        first = missing[0]["source_path"] if missing else ""
        raise SystemExit(
            "None of the queued media files are reachable. First missing file:\n"
            f"{first}\n\nReconnect /Volumes/PTE_Resources or use --remap-from and --remap-to."
        )


def format_timestamp(seconds: float) -> str:
    seconds = max(0.0, float(seconds or 0.0))
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}".replace(".", ",")


def srt_block(index: int, start: float, end: float, text: str) -> str:
    return "\n".join([
        str(index),
        f"{format_timestamp(start)} --> {format_timestamp(end)}",
        text.strip(),
        "",
    ])


def build_clip_timestamps(start_seconds: int, max_seconds: int) -> str | None:
    start = max(0, start_seconds)
    if max_seconds > 0:
        return f"{start},{start + max_seconds}"
    if start > 0:
        return f"{start}"
    return None


def transcribe_media(
    model: Any,
    source: Path,
    start_seconds: int,
    max_seconds: int,
    language: str,
) -> dict[str, Any]:
    clip_timestamps = build_clip_timestamps(start_seconds, max_seconds)
    segments, info = model.transcribe(
        str(source),
        language=language or None,
        task="transcribe",
        vad_filter=True,
        beam_size=3,
        clip_timestamps=clip_timestamps,
        initial_prompt=(
            "这是一段中文 PTE 备考课程，可能包含英语术语："
            "RA, RS, DI, RL, ASQ, WFD, SST, FIB, RO, WE, SWT, PTE Core。"
        ),
    )

    rows = []
    for segment in segments:
        text = re.sub(r"\s+", " ", segment.text).strip()
        if not text:
            continue
        rows.append({
            "start": float(segment.start),
            "end": float(segment.end),
            "text": text,
        })

    transcript = "\n".join(f"[{item['start']:.1f}-{item['end']:.1f}] {item['text']}" for item in rows)
    srt = "\n".join(srt_block(i, item["start"], item["end"], item["text"]) for i, item in enumerate(rows, start=1))
    return {
        "language": getattr(info, "language", ""),
        "languageProbability": round(float(getattr(info, "language_probability", 0.0) or 0.0), 4),
        "duration": round(float(getattr(info, "duration", 0.0) or 0.0), 2),
        "startSeconds": start_seconds,
        "processedSeconds": max_seconds if max_seconds > 0 else round(float(getattr(info, "duration", 0.0) or 0.0), 2),
        "segmentCount": len(rows),
        "characterCount": len(transcript),
        "transcript": transcript,
        "srt": srt,
        "status": "ok" if rows else "empty_transcript",
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue", default="knowledge_exports/phase2/20260512-090856/media-transcription-pilot.csv")
    parser.add_argument("--output-dir", default="knowledge_exports/phase2-media")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--start-seconds", type=int, default=0, help="Skip intros and start transcribing at this timestamp")
    parser.add_argument("--max-seconds", type=int, default=300, help="0 means full media")
    parser.add_argument("--model", default="base", help="faster-whisper model size or local path")
    parser.add_argument("--language", default="zh", help="Use zh for Chinese-heavy PTE classes, or empty for auto")
    parser.add_argument("--remap-from", default="")
    parser.add_argument("--remap-to", default="")
    args = parser.parse_args()

    queue_path = Path(args.queue).expanduser().resolve()
    if not queue_path.exists():
        raise SystemExit(f"Queue does not exist: {queue_path}")

    queue_rows = read_queue(queue_path)[args.offset: args.offset + args.limit]
    require_sources(queue_rows, args.remap_from, args.remap_to)

    run_id = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = Path(args.output_dir).expanduser().resolve() / run_id
    transcript_dir = out_dir / "transcripts"
    srt_dir = out_dir / "srt"
    transcript_dir.mkdir(parents=True, exist_ok=True)
    srt_dir.mkdir(parents=True, exist_ok=True)

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    result_rows: list[dict[str, Any]] = []

    for index, row in enumerate(queue_rows, start=1):
        source = resolve_source_path(row, args.remap_from, args.remap_to)
        title = Path(row["relative_path"]).stem
        basename = f"{args.offset + index:03d}-{safe_slug(title)}"
        transcript_path = transcript_dir / f"{basename}.txt"
        srt_path = srt_dir / f"{basename}.srt"

        try:
            result = transcribe_media(model, source, args.start_seconds, args.max_seconds, args.language)
            transcript_path.write_text(result["transcript"] + "\n", encoding="utf-8")
            srt_path.write_text(result["srt"] + "\n", encoding="utf-8")
            status = result["status"]
            error = ""
        except Exception as exc:
            result = {
                "language": "",
                "languageProbability": 0,
                "duration": 0,
                "startSeconds": args.start_seconds,
                "processedSeconds": args.max_seconds,
                "segmentCount": 0,
                "characterCount": 0,
                "transcript": "",
                "srt": "",
            }
            transcript_path.write_text("", encoding="utf-8")
            srt_path.write_text("", encoding="utf-8")
            status = f"transcription_error:{type(exc).__name__}"
            error = str(exc)[:400]

        result_rows.append({
            "relative_path": row["relative_path"],
            "source_path": str(source),
            "topics": row.get("topics", ""),
            "size_mb": row.get("size_mb", ""),
            "status": status,
            "language": result["language"],
            "language_probability": result["languageProbability"],
            "duration": result["duration"],
            "start_seconds": result["startSeconds"],
            "processed_seconds": result["processedSeconds"],
            "segment_count": result["segmentCount"],
            "character_count": result["characterCount"],
            "transcript_file": str(transcript_path.relative_to(out_dir)),
            "srt_file": str(srt_path.relative_to(out_dir)),
            "error": error,
        })
        print(f"[{index}/{len(queue_rows)}] {status}: {row['relative_path']}", flush=True)

    summary = {
        "runId": run_id,
        "queue": str(queue_path),
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "offset": args.offset,
        "limit": args.limit,
        "startSeconds": args.start_seconds,
        "maxSeconds": args.max_seconds,
        "model": args.model,
        "processed": len(result_rows),
        "ok": sum(1 for row in result_rows if row["status"] == "ok"),
        "outputs": {
            "resultsCsv": "transcription-results.csv",
            "resultsJson": "transcription-results.json",
            "transcriptsDir": "transcripts",
            "srtDir": "srt",
            "summaryJson": "summary.json",
        },
        "nextStep": "Review transcripts and rewrite useful methods into SunPace-owned guidance. Do not publish transcripts verbatim.",
    }

    write_csv(out_dir / "transcription-results.csv", result_rows)
    (out_dir / "transcription-results.json").write_text(json.dumps(result_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    readme = [
        "# Media Transcription Pilot",
        "",
        f"- Run ID: `{run_id}`",
        f"- Queue: `{queue_path}`",
        f"- Processed files: `{len(result_rows)}`",
        f"- Successful transcripts: `{summary['ok']}`",
        f"- Start seconds per file: `{args.start_seconds}`",
        f"- Max seconds per file: `{args.max_seconds}`",
        "",
        "## Files",
        "",
        "- `transcription-results.csv`: status for each media file",
        "- `transcripts/`: timestamped plain text transcripts",
        "- `srt/`: subtitle files",
        "- `summary.json`: run summary",
        "",
        "## Next Step",
        "",
        "Use transcripts only as internal reference. Rewrite useful teaching points into SunPace/Sunny-owned guidance before publishing.",
    ]
    (out_dir / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")

    print(json.dumps({"outDir": str(out_dir), "summary": summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
