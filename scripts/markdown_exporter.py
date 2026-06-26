#!/usr/bin/env python3
"""Save a learning package as a dated Markdown file."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\u3040-\u30ff\u3400-\u9fff]+", "_", value, flags=re.UNICODE)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "learning_pack"


def main() -> int:
    parser = argparse.ArgumentParser(description="Save a learning package as Markdown.")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("--topic", default="shadow speak", help="Topic used in output filename")
    parser.add_argument("--output-dir", default="exports", help="Directory for exported Markdown")
    args = parser.parse_args()

    source = Path(args.input)
    content = source.read_text(encoding="utf-8-sig")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    date = dt.date.today().strftime("%Y%m%d")
    output = output_dir / f"shadow_speak_{date}_{slugify(args.topic)}.md"
    output.write_text(content.rstrip() + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
