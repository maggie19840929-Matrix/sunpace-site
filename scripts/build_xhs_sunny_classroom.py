#!/usr/bin/env python3
"""
Build Xiaohongshu content seeds from Sunny's SunPace-owned FAQ library.

This script uses `data/pte-knowledge.sunpace.json` only. It does not read or
publish OCR text, course transcripts, or purchased source material verbatim.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


SERIES = "Sunny的PTE小课堂"

TOPIC_PRIORITY = [
    "sunpace-speaking-ra",
    "sunpace-speaking-ra-breakdown",
    "sunpace-speaking-rs",
    "sunpace-listening-wfd",
    "sunpace-speaking-di",
    "sunpace-speaking-rl",
    "sunpace-reading-ro",
    "sunpace-reading-ro-mnemonic",
    "sunpace-reading-fib",
    "sunpace-reading-fib-collocations",
    "sunpace-listening-sst",
    "sunpace-listening-sst-logic-review",
    "sunpace-writing-we",
    "sunpace-writing-we-vocab-range",
    "sunpace-plan-diagnostic",
    "sunpace-plan-58-65",
    "sunpace-plan-65-79",
    "sunpace-jijing-prediction-use",
    "sunpace-speaking-accent",
    "sunpace-exam-booking-checklist",
]

TAG_MAP = {
    "RA": "#PTE口语",
    "RS": "#PTE口语",
    "DI": "#PTE口语",
    "RL": "#PTE口语",
    "ASQ": "#PTE口语",
    "WFD": "#PTE听力",
    "SST": "#PTE听力",
    "FIB": "#PTE阅读",
    "RO": "#PTE阅读",
    "WE": "#PTE写作",
    "SWT": "#PTE写作",
    "PTE Core": "#PTECore",
    "口语": "#PTE口语",
    "听力": "#PTE听力",
    "阅读": "#PTE阅读",
    "写作": "#PTE写作",
    "词汇": "#PTE词汇",
    "语法": "#PTE语法",
    "机经": "#PTE机经",
    "报考": "#PTE考试",
    "报名": "#PTE考试",
}


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[。！？；])", text)
    return [part.strip() for part in parts if part.strip()]


def compact(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def question_from_title(title: str) -> str:
    if title.endswith("吗") or title.endswith("么") or title.endswith("什么"):
        return title + "？"
    if "怎么" in title or "要不要" in title or "适合谁" in title:
        return title + "？"
    return title.replace("训练方法", "怎么练").replace("使用", "怎么用") + "？"


def cover_text(title: str) -> str:
    text = title
    replacements = {
        "Read Aloud": "RA",
        "Repeat Sentence": "RS",
        "Describe Image": "DI",
        "Retell Lecture": "RL",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return compact(text, 18)


def build_titles(title: str, question: str) -> list[str]:
    short = compact(title, 20)
    return [
        f"{short}，很多人第一步就错了",
        f"Sunny讲PTE：{question}",
        f"PTE备考别硬刷：{short}",
    ]


def build_script(entry: dict[str, Any]) -> str:
    title = entry["title"]
    answer = entry["answer"]
    sentences = split_sentences(answer)
    s1 = sentences[0] if sentences else answer
    s2 = sentences[1] if len(sentences) > 1 else "先找到失分原因，再安排训练顺序。"
    s3 = sentences[2] if len(sentences) > 2 else "练完一定要复盘，不要只看做题数量。"
    return "\n".join([
        f"开头 0-3 秒：你是不是也在问：{question_from_title(title)}",
        f"正文 3-18 秒：{compact(s1, 72)}",
        f"方法 18-35 秒：{compact(s2, 72)}",
        f"提醒 35-48 秒：{compact(s3, 72)}",
        "结尾 48-55 秒：把你的当前分数、目标分数和考试日期发给 Sunny，帮你拆训练优先级。",
    ])


def build_caption(entry: dict[str, Any]) -> str:
    question = question_from_title(entry["title"])
    sentences = split_sentences(entry["answer"])
    body = "\n".join(f"{idx + 1}. {compact(sentence, 58)}" for idx, sentence in enumerate(sentences[:3]))
    return "\n".join([
        f"{SERIES}：{question}",
        "",
        body,
        "",
        "想让 Sunny 帮你拆学习计划，可以留下当前分数、目标分数和考试时间。",
    ])


def hashtags(entry: dict[str, Any]) -> str:
    tags = ["#PTE", "#PTE备考", "#昇培教育", "#Sunny的PTE小课堂"]
    for keyword in entry.get("keywords", []):
        mapped = TAG_MAP.get(keyword)
        if mapped and mapped not in tags:
            tags.append(mapped)
    return " ".join(tags[:8])


def score(entry: dict[str, Any]) -> int:
    if entry["id"] in TOPIC_PRIORITY:
        return 1000 - TOPIC_PRIORITY.index(entry["id"])
    title = entry["title"]
    value = 0
    for key in ["RA", "RS", "WFD", "DI", "RL", "FIB", "RO", "SST", "WE", "提分", "备考", "模考"]:
        if key in title or key in " ".join(entry.get("keywords", [])):
            value += 10
    return value


def build_rows(entries: list[dict[str, Any]]) -> list[dict[str, str]]:
    sorted_entries = sorted(entries, key=score, reverse=True)
    rows = []
    for index, entry in enumerate(sorted_entries, start=1):
        question = question_from_title(entry["title"])
        titles = build_titles(entry["title"], question)
        rows.append({
            "episode": str(index),
            "source_id": entry["id"],
            "series": SERIES,
            "topic": entry["title"],
            "question": question,
            "cover_text": cover_text(entry["title"]),
            "title_option_1": titles[0],
            "title_option_2": titles[1],
            "title_option_3": titles[2],
            "video_script": build_script(entry),
            "caption": build_caption(entry),
            "hashtags": hashtags(entry),
            "production_note": "用 Sunny 卡通人物口播；不要展示课程原文；封面突出题型+痛点。",
            "status": "draft",
        })
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--knowledge", default="data/pte-knowledge.sunpace.json")
    parser.add_argument("--output-dir", default="content_exports/xiaohongshu")
    args = parser.parse_args()

    knowledge_path = Path(args.knowledge).resolve()
    entries = json.loads(knowledge_path.read_text(encoding="utf-8"))
    rows = build_rows(entries)

    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now().strftime("%Y%m%d-%H%M%S")

    csv_path = out_dir / f"sunny-pte-classroom-queue-{run_id}.csv"
    json_path = out_dir / f"sunny-pte-classroom-queue-{run_id}.json"
    latest_csv = out_dir / "sunny-pte-classroom-queue-latest.csv"
    latest_json = out_dir / "sunny-pte-classroom-queue-latest.json"

    write_csv(csv_path, rows)
    write_csv(latest_csv, rows)
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    latest_json.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "runId": run_id,
        "source": str(knowledge_path),
        "count": len(rows),
        "csv": str(csv_path),
        "json": str(json_path),
        "latestCsv": str(latest_csv),
        "latestJson": str(latest_json),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
