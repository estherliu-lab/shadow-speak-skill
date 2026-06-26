#!/usr/bin/env python3
"""Export structured learning cards to Anki-compatible CSV."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


CARD_RE = re.compile(
    r"Front:\s*(?P<front>.+?)\nBack:\s*(?P<back>.+?)(?:\nTags:\s*(?P<tags>.+?))?(?=\n-{3,}|\Z)",
    re.DOTALL | re.IGNORECASE,
)


def normalize_card(card: dict[str, Any], default_tags: str) -> dict[str, str]:
    front = str(card.get("front") or card.get("Front") or "").strip()
    back = str(card.get("back") or card.get("Back") or "").strip()
    tags_value = card.get("tags") or card.get("Tags") or default_tags
    if isinstance(tags_value, list):
        tags = ",".join(str(tag).strip() for tag in tags_value if str(tag).strip())
    else:
        tags = str(tags_value).strip()
    if not front or not back:
        raise ValueError("Each card needs non-empty front and back fields.")
    return {"Front": front, "Back": back.replace("\n", " | "), "Tags": tags}


def load_cards(path: Path, default_tags: str) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        payload = None

    raw_cards: list[dict[str, Any]]
    if isinstance(payload, list):
        raw_cards = payload
    elif isinstance(payload, dict):
        raw_cards = payload.get("cards") or payload.get("anki") or []
    else:
        raw_cards = [
            {
                "front": match.group("front").strip(),
                "back": match.group("back").strip(),
                "tags": (match.group("tags") or default_tags).strip(),
            }
            for match in CARD_RE.finditer(text)
        ]

    if not raw_cards:
        raise ValueError("No cards found. Use JSON cards or Markdown blocks with Front/Back/Tags.")
    return [normalize_card(card, default_tags) for card in raw_cards]


def write_csv(cards: list[dict[str, str]], output: Path, limit: int) -> None:
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Front", "Back", "Tags"])
        writer.writeheader()
        writer.writerows(cards[:limit])


def main() -> int:
    parser = argparse.ArgumentParser(description="Export learning cards to Anki CSV.")
    parser.add_argument("input", help="Input JSON or Markdown card file")
    parser.add_argument("output", help="Output CSV path")
    parser.add_argument("--limit", type=int, default=30, help="Maximum cards to export")
    parser.add_argument("--tags", default="shadowing", help="Default comma-separated tags")
    args = parser.parse_args()

    cards = load_cards(Path(args.input), args.tags)
    write_csv(cards, Path(args.output), args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
