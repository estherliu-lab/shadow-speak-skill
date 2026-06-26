#!/usr/bin/env python3
"""Try to fetch public YouTube caption text without bypassing restrictions."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def extract_video_id(value: str) -> str:
    value = value.strip()
    if VIDEO_ID_RE.match(value):
        return value

    parsed = urllib.parse.urlparse(value)
    host = parsed.netloc.lower()
    if host.endswith("youtu.be"):
        candidate = parsed.path.strip("/").split("/")[0]
        if VIDEO_ID_RE.match(candidate):
            return candidate
    if "youtube.com" in host:
        query_id = urllib.parse.parse_qs(parsed.query).get("v", [""])[0]
        if VIDEO_ID_RE.match(query_id):
            return query_id
        parts = [part for part in parsed.path.split("/") if part]
        for marker in ("shorts", "embed", "live"):
            if marker in parts:
                index = parts.index(marker) + 1
                if index < len(parts) and VIDEO_ID_RE.match(parts[index]):
                    return parts[index]
    raise ValueError("Could not find an 11-character YouTube video ID.")


def fetch_url(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 caption-fetcher; educational transcript access only",
            "Accept-Language": "en-US,en;q=0.8,ja;q=0.7,zh-CN;q=0.6",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def find_caption_tracks(page_html: str) -> list[dict]:
    patterns = [
        r'"captionTracks":(\[.*?\])\s*,\s*"audioTracks"',
        r'"captionTracks":(\[.*?\])\s*,\s*"translationLanguages"',
    ]
    for pattern in patterns:
        match = re.search(pattern, page_html)
        if not match:
            continue
        raw_json = match.group(1)
        raw_json = raw_json.encode("utf-8").decode("unicode_escape")
        return json.loads(raw_json)
    return []


def choose_track(tracks: list[dict], languages: list[str]) -> dict:
    if not tracks:
        raise RuntimeError("No public caption tracks were found.")
    for language in languages:
        for track in tracks:
            if track.get("languageCode", "").lower().startswith(language.lower()):
                return track
    return tracks[0]


def captions_to_text(caption_xml: str) -> str:
    root = ET.fromstring(caption_xml)
    chunks: list[str] = []
    previous = ""
    for node in root.iter():
        if node.tag not in {"text", "p"}:
            continue
        text = "".join(node.itertext())
        text = html.unescape(text)
        text = re.sub(r"\s+", " ", text).strip()
        if text and text != previous:
            chunks.append(text)
            previous = text
    return "\n".join(chunks).strip() + ("\n" if chunks else "")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Attempt to fetch public YouTube captions. Does not bypass restrictions."
    )
    parser.add_argument("url_or_id", help="YouTube URL or video ID")
    parser.add_argument("output", nargs="?", help="Optional output transcript file")
    parser.add_argument("--lang", action="append", default=["en", "ja"], help="Preferred caption language")
    args = parser.parse_args()

    try:
        video_id = extract_video_id(args.url_or_id)
        page = fetch_url(f"https://www.youtube.com/watch?v={video_id}")
        tracks = find_caption_tracks(page)
        track = choose_track(tracks, args.lang)
        base_url = track.get("baseUrl")
        if not base_url:
            raise RuntimeError("Caption track did not include a public caption URL.")
        caption_xml = fetch_url(base_url)
        text = captions_to_text(caption_xml)
        if not text:
            raise RuntimeError("Caption file was accessible but contained no readable text.")
    except Exception as exc:
        print(
            "Unable to fetch a public transcript. Ask the user to paste captions or upload SRT/VTT. "
            f"Reason: {exc}",
            file=sys.stderr,
        )
        return 2

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
