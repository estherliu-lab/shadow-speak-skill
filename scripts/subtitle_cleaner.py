#!/usr/bin/env python3
"""Clean SRT/VTT captions into plain study text."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TIMESTAMP_RE = re.compile(
    r"^\s*(?:\d{1,2}:)?\d{1,2}:\d{2}[\.,]\d{3}\s*-->\s*(?:\d{1,2}:)?\d{1,2}:\d{2}[\.,]\d{3}"
)
TAG_RE = re.compile(r"<[^>]+>")
SENTENCE_END_RE = re.compile(r"([.!?。！？…]+[\"'」』）)]*)\s+")


def is_noise(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped in {"WEBVTT", "Kind: captions", "Language: en", "Language: ja"}:
        return True
    if stripped.upper().startswith(("NOTE", "STYLE", "REGION")):
        return True
    if stripped.isdigit():
        return True
    if TIMESTAMP_RE.match(stripped):
        return True
    return False


def normalize_line(line: str) -> str:
    line = TAG_RE.sub("", line)
    line = line.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    line = line.replace("&quot;", '"').replace("&#39;", "'")
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def clean_captions(text: str) -> str:
    cleaned: list[str] = []
    previous = ""
    for raw_line in text.replace("\ufeff", "").splitlines():
        if is_noise(raw_line):
            continue
        line = normalize_line(raw_line)
        if not line or line == previous:
            continue
        cleaned.append(line)
        previous = line

    joined = " ".join(cleaned)
    joined = re.sub(r"\s+([,.!?;:。！？、，；：])", r"\1", joined)
    joined = SENTENCE_END_RE.sub(r"\1\n", joined)
    joined = re.sub(r"\n{3,}", "\n\n", joined)
    return joined.strip() + ("\n" if joined.strip() else "")


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean SRT/VTT captions into plain text.")
    parser.add_argument("input", help="Input .srt, .vtt, or plain text file")
    parser.add_argument("output", nargs="?", help="Output .txt file. Prints to stdout when omitted.")
    args = parser.parse_args()

    source = Path(args.input)
    text = source.read_text(encoding="utf-8-sig")
    result = clean_captions(text)

    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
    else:
        print(result, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
