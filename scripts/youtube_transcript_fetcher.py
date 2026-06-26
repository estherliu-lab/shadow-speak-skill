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
DEFAULT_LANGS = ["ja", "en"]
WATCH_URL = "https://www.youtube.com/watch?v={video_id}"
TIMEDTEXT_LIST_URL = "https://www.youtube.com/api/timedtext?type=list&v={video_id}"


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


def fetch_url(url: str, timeout: int = 10) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 caption-fetcher; educational transcript access only",
            "Accept-Language": "ja,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def json_array_after_key(text: str, key: str) -> str | None:
    marker = f'"{key}":'
    start = text.find(marker)
    if start < 0:
        return None
    array_start = text.find("[", start + len(marker))
    if array_start < 0:
        return None

    depth = 0
    in_string = False
    escaped = False
    for index in range(array_start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return text[array_start : index + 1]
    return None


def find_caption_tracks(page_html: str) -> list[dict]:
    raw_json = json_array_after_key(page_html, "captionTracks")
    if not raw_json:
        return []
    for candidate in (raw_json, html.unescape(raw_json), raw_json.encode("utf-8").decode("unicode_escape")):
        try:
            tracks = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        for track in tracks:
            track.setdefault("source", "playerResponse")
        return tracks
    return []


def timedtext_track_list(video_id: str) -> list[dict]:
    xml_text = fetch_url(TIMEDTEXT_LIST_URL.format(video_id=video_id))
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []

    tracks: list[dict] = []
    for node in root.findall("track"):
        lang = node.attrib.get("lang_code", "")
        if not lang:
            continue
        query = {
            "v": video_id,
            "lang": lang,
            "fmt": "srv3",
        }
        if node.attrib.get("name"):
            query["name"] = node.attrib["name"]
        if node.attrib.get("kind"):
            query["kind"] = node.attrib["kind"]
        tracks.append(
            {
                "languageCode": lang,
                "name": {"simpleText": node.attrib.get("name", "")},
                "kind": node.attrib.get("kind", ""),
                "source": "timedtext",
                "baseUrl": "https://www.youtube.com/api/timedtext?" + urllib.parse.urlencode(query),
            }
        )
    return tracks


def find_public_caption_tracks(video_id: str, page_html: str) -> list[dict]:
    tracks = find_caption_tracks(page_html)
    seen = {track.get("baseUrl", "") for track in tracks}
    for track in timedtext_track_list(video_id):
        if track.get("baseUrl") not in seen:
            tracks.append(track)
            seen.add(track.get("baseUrl", ""))
    return tracks


def track_label(track: dict) -> str:
    name = track.get("name", "")
    if isinstance(name, dict):
        name = name.get("simpleText") or name.get("runs", [{}])[0].get("text", "")
    return str(name or track.get("languageCode") or "unknown")


def choose_track(tracks: list[dict], languages: list[str]) -> dict:
    if not tracks:
        raise RuntimeError("No public caption tracks were found.")
    normalized_languages = [language.lower() for language in languages]

    def score(track: dict) -> tuple[int, int]:
        code = track.get("languageCode", "").lower()
        kind = track.get("kind", "")
        language_rank = len(normalized_languages) + 1
        for index, language in enumerate(normalized_languages):
            if code == language:
                language_rank = index
                break
            if code.startswith(language):
                language_rank = min(language_rank, index + 1)
        auto_rank = 1 if kind == "asr" else 0
        return language_rank, auto_rank

    best = sorted(tracks, key=score)[0]
    if score(best)[0] <= len(normalized_languages):
        return best
    return tracks[0]


def captions_to_text(caption_xml: str) -> str:
    if caption_xml.lstrip().startswith("WEBVTT"):
        lines = []
        for line in caption_xml.splitlines():
            stripped = line.strip()
            if not stripped or stripped == "WEBVTT" or "-->" in stripped:
                continue
            if re.match(r"^\d+$", stripped):
                continue
            stripped = re.sub(r"<[^>]+>", "", stripped)
            if stripped:
                lines.append(html.unescape(stripped))
        return "\n".join(dict.fromkeys(lines)).strip() + ("\n" if lines else "")

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
    parser.add_argument("--lang", action="append", default=[], help="Preferred caption language")
    parser.add_argument("--list", action="store_true", help="List public caption tracks and exit")
    parser.add_argument("--json", action="store_true", help="Print machine-readable status JSON")
    parser.add_argument("--timeout", type=int, default=10, help="Network timeout in seconds")
    args = parser.parse_args()
    languages = args.lang or DEFAULT_LANGS

    try:
        video_id = extract_video_id(args.url_or_id)
        page = fetch_url(WATCH_URL.format(video_id=video_id), timeout=args.timeout)
        tracks = find_public_caption_tracks(video_id, page)
        if args.list:
            if not tracks:
                print(
                    "NO_PUBLIC_CAPTION_TRACKS: YouTube did not expose public caption tracks for this video.",
                    file=sys.stderr,
                )
                return 2
            for track in tracks:
                print(
                    "\t".join(
                        [
                            track.get("languageCode", ""),
                            "auto" if track.get("kind") == "asr" else "manual",
                            track.get("source", ""),
                            track_label(track),
                        ]
                    )
                )
            return 0

        track = choose_track(tracks, languages)
        base_url = track.get("baseUrl")
        if not base_url:
            raise RuntimeError("Caption track did not include a public caption URL.")
        caption_xml = fetch_url(base_url, timeout=args.timeout)
        text = captions_to_text(caption_xml)
        if not text:
            raise RuntimeError("Caption file was accessible but contained no readable text.")
    except Exception as exc:
        message = (
            "NO_PUBLIC_CAPTIONS: Unable to fetch a public transcript quickly. "
            "Ask the user to paste captions, upload SRT/VTT, or provide the script. "
            "For music videos, subtitles may be disabled, embedded in the video, or not exposed as caption tracks."
        )
        if args.json:
            print(json.dumps({"ok": False, "error": str(exc), "message": message}, ensure_ascii=False))
            return 2
        print(
            f"{message} Reason: {exc}",
            file=sys.stderr,
        )
        return 2

    if args.json:
        print(
            json.dumps(
                {
                    "ok": True,
                    "video_id": video_id,
                    "language": track.get("languageCode", ""),
                    "track": track_label(track),
                    "source": track.get("source", ""),
                    "lines": len([line for line in text.splitlines() if line.strip()]),
                    "text": text,
                },
                ensure_ascii=False,
            )
        )
        return 0

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
