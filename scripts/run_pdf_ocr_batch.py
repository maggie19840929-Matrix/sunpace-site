#!/usr/bin/env python3
"""
Run a small, prioritized OCR batch for Sunny phase 2.

The script reads `pdf-ocr-queue.csv`, renders PDF pages with pypdfium2, runs
RapidOCR locally, and writes text files for later SunPace-style rewriting.
It does not merge OCR text into the live Sunny knowledge files.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


RUNTIME_DEPS = Path(".codex_deps/python")
if RUNTIME_DEPS.exists():
    sys.path.insert(0, str(RUNTIME_DEPS.resolve()))

try:
    import pypdfium2 as pdfium
    from rapidocr_onnxruntime import RapidOCR
except Exception as exc:  # pragma: no cover - user-facing setup error
    raise SystemExit(
        "Missing OCR dependencies. Install them into .codex_deps/python with: "
        "python3 -m pip install --target .codex_deps/python pypdfium2 rapidocr-onnxruntime"
    ) from exc


def safe_slug(value: str, fallback: str = "file") -> str:
    slug = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", value).strip("-")
    return slug[:80] or fallback


def clean_lines(lines: list[str]) -> list[str]:
    cleaned = []
    seen = set()
    for line in lines:
        line = re.sub(r"\s+", " ", str(line or "")).strip()
        if not line or line in seen:
            continue
        seen.add(line)
        cleaned.append(line)
    return cleaned


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
        common_root = "/Volumes/PTE_Resources"
        hint = (
            f"None of the queued PDF files are reachable. First missing file:\n{first}\n\n"
            f"If the course drive is not mounted, reconnect it so {common_root} exists, then run this script again.\n"
            "If the drive is mounted somewhere else, use --remap-from and --remap-to."
        )
        raise SystemExit(hint)


def render_page(page: Any, scale: float):
    bitmap = page.render(scale=scale)
    return bitmap.to_pil()


def ocr_pdf(path: Path, ocr: Any, max_pages: int, scale: float) -> dict[str, Any]:
    document = pdfium.PdfDocument(str(path))
    page_count = len(document)
    processed_pages = min(max_pages, page_count)
    page_outputs = []
    total_lines = 0

    for index in range(processed_pages):
        page = document[index]
        image = render_page(page, scale)
        result, _ = ocr(image)
        lines = clean_lines([item[1] for item in (result or []) if len(item) >= 2])
        total_lines += len(lines)
        page_outputs.append({
            "page": index + 1,
            "lineCount": len(lines),
            "text": "\n".join(lines),
        })
        page.close()

    document.close()
    text = "\n\n".join(f"[Page {item['page']}]\n{item['text']}" for item in page_outputs).strip()
    return {
        "pageCount": page_count,
        "processedPages": processed_pages,
        "lineCount": total_lines,
        "characterCount": len(text),
        "text": text,
        "status": "ok" if total_lines else "empty_ocr_text",
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
    parser.add_argument("--queue", default="knowledge_exports/phase2/20260512-090856/pdf-ocr-queue.csv")
    parser.add_argument("--output-dir", default="knowledge_exports/phase2-ocr")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--max-pages", type=int, default=6)
    parser.add_argument("--scale", type=float, default=2.0)
    parser.add_argument("--remap-from", default="", help="Replace this source path prefix from the queue")
    parser.add_argument("--remap-to", default="", help="Use this mounted path prefix instead")
    args = parser.parse_args()

    queue_path = Path(args.queue).expanduser().resolve()
    if not queue_path.exists():
        raise SystemExit(f"Queue does not exist: {queue_path}")

    run_id = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = Path(args.output_dir).expanduser().resolve() / run_id
    text_dir = out_dir / "texts"
    text_dir.mkdir(parents=True, exist_ok=True)

    queue_rows = read_queue(queue_path)[: args.limit]
    require_sources(queue_rows, args.remap_from, args.remap_to)
    ocr = RapidOCR()
    result_rows: list[dict[str, Any]] = []

    for index, row in enumerate(queue_rows, start=1):
        source_path = resolve_source_path(row, args.remap_from, args.remap_to)
        title = Path(row["relative_path"]).stem
        output_name = f"{index:03d}-{safe_slug(title)}.txt"
        output_path = text_dir / output_name

        try:
            result = ocr_pdf(source_path, ocr, args.max_pages, args.scale)
            output_path.write_text(result["text"] + "\n", encoding="utf-8")
            status = result["status"]
            error = ""
        except Exception as exc:
            result = {"pageCount": 0, "processedPages": 0, "lineCount": 0, "characterCount": 0, "text": ""}
            output_path.write_text("", encoding="utf-8")
            status = f"ocr_error:{type(exc).__name__}"
            error = str(exc)[:300]

        result_rows.append({
            "relative_path": row["relative_path"],
            "source_path": row["source_path"],
            "topics": row.get("topics", ""),
            "queue_status": row.get("status", ""),
            "ocr_status": status,
            "page_count": result["pageCount"],
            "processed_pages": result["processedPages"],
            "line_count": result["lineCount"],
            "character_count": result["characterCount"],
            "text_file": str(output_path.relative_to(out_dir)),
            "error": error,
        })

        print(f"[{index}/{len(queue_rows)}] {status}: {row['relative_path']}", flush=True)

    summary = {
        "runId": run_id,
        "queue": str(queue_path),
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "limit": args.limit,
        "maxPages": args.max_pages,
        "scale": args.scale,
        "processed": len(result_rows),
        "ok": sum(1 for row in result_rows if row["ocr_status"] == "ok"),
        "outputs": {
            "resultsCsv": "ocr-results.csv",
            "resultsJson": "ocr-results.json",
            "textsDir": "texts",
            "summaryJson": "summary.json",
        },
        "nextStep": "Review OCR text and rewrite useful parts into data/pte-knowledge.sunpace.json. Do not publish source text verbatim.",
    }

    write_csv(out_dir / "ocr-results.csv", result_rows)
    (out_dir / "ocr-results.json").write_text(json.dumps(result_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    readme = [
        "# PDF OCR Batch",
        "",
        f"- Run ID: `{run_id}`",
        f"- Queue: `{queue_path}`",
        f"- Processed files: `{len(result_rows)}`",
        f"- Successful OCR files: `{summary['ok']}`",
        "",
        "## Files",
        "",
        "- `ocr-results.csv`: OCR status for each PDF",
        "- `texts/`: OCR text files",
        "- `summary.json`: run summary",
        "",
        "## Next Step",
        "",
        "Read the text files, extract useful teaching points, and rewrite them into SunPace-owned FAQ answers. Do not publish purchased course text verbatim.",
    ]
    (out_dir / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")

    print(json.dumps({"outDir": str(out_dir), "summary": summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
