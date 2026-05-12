#!/usr/bin/env python3
"""
Create a prioritized phase-2 ingestion queue for Sunny.

This script does not OCR PDFs or transcribe videos. It only builds reviewable
queues so heavier jobs can run later in small batches or on cloud machines.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


MEDIA_EXTS = {".mp4", ".m4v", ".mov", ".mp3", ".m4a", ".wav", ".aac"}
PDF_RETRY_STATUSES = {"empty_pdf_text", "skipped_large_file"}
PDF_RETRY_PREFIXES = ("pdf_error:",)

TOPIC_RULES = [
    ("RA", ["ra", "read aloud", "朗读"]),
    ("RS", ["rs", "repeat sentence", "复述"]),
    ("DI", ["di", "describe image", "图表"]),
    ("RL", ["rl", "retell lecture", "复述讲座"]),
    ("ASQ", ["asq", "answer short question"]),
    ("SWT", ["swt", "summarize written text", "小作文"]),
    ("WE", ["we", "essay", "大作文", "写作"]),
    ("WFD", ["wfd", "write from dictation", "听写"]),
    ("SST", ["sst", "summarize spoken text"]),
    ("FIB", ["fib", "fill in", "填空"]),
    ("RO", ["ro", "re-order", "排序"]),
    ("HIW", ["hiw", "highlight incorrect words"]),
    ("口语", ["口语", "speaking"]),
    ("听力", ["听力", "listening"]),
    ("阅读", ["阅读", "reading"]),
    ("写作", ["写作", "writing"]),
    ("词汇", ["词汇", "vocab", "vocabulary", "单词"]),
    ("语法", ["语法", "grammar"]),
    ("模板", ["模板", "模版", "template", "框架"]),
    ("评分", ["评分", "score guide", "分数"]),
    ("学习计划", ["学习计划", "备考计划", "study plan"]),
]

HIGH_VALUE = [
    "2026",
    "改革后",
    "优先",
    "技巧直播课",
    "技巧真经班",
    "备考资料包",
    "全科备考",
    "内部资料",
    "最新模板",
    "score guide",
    "高频",
]

LOW_VALUE = [
    "2024年技巧课程汇总",
    "改革前",
    "历史",
    "旧",
    "赠品",
]


def normalize(text: str) -> str:
    return text.lower()


def detect_topics(text: str) -> list[str]:
    haystack = normalize(text)
    topics = []
    for topic, needles in TOPIC_RULES:
        if any(needle.lower() in haystack for needle in needles):
            topics.append(topic)
    return topics


def value_score(path_text: str, topics: list[str], size_mb: float) -> int:
    haystack = normalize(path_text)
    score = 0
    for key in HIGH_VALUE:
        if key.lower() in haystack:
            score += 5
    for key in LOW_VALUE:
        if key.lower() in haystack:
            score -= 4
    score += min(len(topics), 8)
    if any(topic in topics for topic in ("RA", "RS", "DI", "RL", "WFD", "SST", "FIB", "RO", "WE", "SWT")):
        score += 4
    if size_mb > 500:
        score -= 3
    elif size_mb > 120:
        score -= 1
    return score


def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(float(value))
    except Exception:
        return default


def safe_float(value: Any, default: float = 0) -> float:
    try:
        return float(value)
    except Exception:
        return default


def should_retry_pdf(status: str) -> bool:
    return status in PDF_RETRY_STATUSES or any(status.startswith(prefix) for prefix in PDF_RETRY_PREFIXES)


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def find_media(root: Path) -> list[Path]:
    return [
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in MEDIA_EXTS and path.name != ".DS_Store"
    ]


def build_pdf_queue(manifest_rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    queue = []
    for row in manifest_rows:
        status = row.get("status", "")
        if row.get("extension", "").lower() != ".pdf" or not should_retry_pdf(status):
            continue

        rel = row.get("relative_path", "")
        size_mb = safe_float(row.get("size_mb"))
        topics = [item for item in row.get("tags", "").split(";") if item]
        if not topics:
            topics = detect_topics(rel)

        score = value_score(rel, topics, size_mb) + safe_int(row.get("priority"))
        if status == "empty_pdf_text":
            action = "ocr_pdf"
        elif status == "skipped_large_file":
            action = "split_then_extract_or_ocr"
        else:
            action = "retry_extract_then_ocr"

        queue.append({
            "relative_path": rel,
            "source_path": row.get("path", ""),
            "size_mb": size_mb,
            "status": status,
            "priority_score": score,
            "topics": topics,
            "recommended_action": action,
            "publish_policy": "convert_to_sunpace_guidance_do_not_publish_verbatim",
        })

    return sorted(queue, key=lambda item: (item["priority_score"], -item["size_mb"]), reverse=True)


def build_media_queue(root: Path, limit: int = 80) -> list[dict[str, Any]]:
    queue = []
    for path in find_media(root):
        try:
            rel = str(path.relative_to(root))
            size_mb = round(path.stat().st_size / 1024 / 1024, 2)
        except Exception:
            continue

        topics = detect_topics(rel)
        score = value_score(rel, topics, size_mb)
        ext = path.suffix.lower()
        if ext in {".mp3", ".m4a", ".wav", ".aac"}:
            action = "transcribe_audio"
        else:
            action = "extract_audio_then_transcribe"

        queue.append({
            "relative_path": rel,
            "source_path": str(path),
            "extension": ext,
            "size_mb": size_mb,
            "priority_score": score,
            "topics": topics,
            "recommended_action": action,
            "pilot_policy": "start_with_top_10_to_20_files",
            "publish_policy": "summarize_to_sunpace_guidance_do_not_publish_verbatim",
        })

    return sorted(queue, key=lambda item: (item["priority_score"], -item["size_mb"]), reverse=True)[:limit]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return

    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: ";".join(value) if isinstance(value, list) else value for key, value in row.items()})


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", default="/Volumes/PTE_Resources")
    parser.add_argument("--manifest", default="knowledge_exports/nightly/20260512-045207/manifest.csv")
    parser.add_argument("--output-dir", default="knowledge_exports/phase2")
    parser.add_argument("--media-limit", type=int, default=80)
    args = parser.parse_args()

    root = Path(args.source_root).expanduser().resolve()
    manifest_path = Path(args.manifest).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Source root does not exist: {root}")
    if not manifest_path.exists():
        raise SystemExit(f"Manifest does not exist: {manifest_path}")

    run_id = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = Path(args.output_dir).expanduser().resolve() / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest_rows = read_manifest(manifest_path)
    pdf_queue = build_pdf_queue(manifest_rows)
    media_queue = build_media_queue(root, args.media_limit)

    pdf_status_counts = Counter(item["status"] for item in pdf_queue)
    media_ext_counts = Counter(item["extension"] for item in media_queue)
    summary = {
        "runId": run_id,
        "sourceRoot": str(root),
        "manifest": str(manifest_path),
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "pdfRetryCount": len(pdf_queue),
        "mediaPilotCount": len(media_queue),
        "pdfStatusCounts": dict(pdf_status_counts.most_common()),
        "mediaExtensionCountsInPilot": dict(media_ext_counts.most_common()),
        "outputs": {
            "pdfOcrQueueCsv": "pdf-ocr-queue.csv",
            "pdfOcrQueueJson": "pdf-ocr-queue.json",
            "mediaTranscriptionPilotCsv": "media-transcription-pilot.csv",
            "mediaTranscriptionPilotJson": "media-transcription-pilot.json",
            "summaryJson": "summary.json",
        },
        "notes": [
            "This is a queue only. No OCR or transcription was performed.",
            "Prioritize top PDF OCR entries before processing all scanned PDFs.",
            "Start media transcription with 10-20 files before scaling to the full library.",
            "Do not publish third-party course text verbatim; rewrite outputs into SunPace-owned guidance.",
        ],
    }

    write_csv(out_dir / "pdf-ocr-queue.csv", pdf_queue)
    write_json(out_dir / "pdf-ocr-queue.json", pdf_queue)
    write_csv(out_dir / "media-transcription-pilot.csv", media_queue)
    write_json(out_dir / "media-transcription-pilot.json", media_queue)
    write_json(out_dir / "summary.json", summary)

    readme = [
        "# Sunny Phase 2 Ingestion Queue",
        "",
        f"- Run ID: `{run_id}`",
        f"- Source root: `{root}`",
        f"- PDF OCR/retry candidates: `{len(pdf_queue)}`",
        f"- Media pilot candidates: `{len(media_queue)}`",
        "",
        "## Files",
        "",
        "- `pdf-ocr-queue.csv`: scanned, failed, or oversized PDFs sorted by priority",
        "- `media-transcription-pilot.csv`: highest-value audio/video files for a transcription pilot",
        "- `summary.json`: counts and run metadata",
        "",
        "## Recommended Order",
        "",
        "1. OCR the first 20-40 rows in `pdf-ocr-queue.csv`.",
        "2. Convert useful OCR output into `data/pte-knowledge.sunpace.json` style answers.",
        "3. Transcribe the first 10-20 rows in `media-transcription-pilot.csv`.",
        "4. Summarize transcripts into SunPace-owned guidance before exposing them to Sunny.",
        "",
        "## Safety",
        "",
        "Do not publish purchased course text or transcripts verbatim. Use them to identify topics, methods, and common student problems, then rewrite in SunPace's own words.",
    ]
    (out_dir / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")

    print(json.dumps({"outDir": str(out_dir), "summary": summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
