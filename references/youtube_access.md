# YouTube Access Rules

Use this reference only when the user gives a YouTube link. This is an optional path, not the primary onboarding or first-test workflow.

## Safe Attempts

Try only accessible information:

1. Public page title and description.
2. Visible transcript text if the browsing environment exposes it.
3. Public caption metadata through `scripts/youtube_transcript_fetcher.py <url> --json --timeout 5`, only when the user explicitly asks to try fetching and network access is already available without repeated prompts.
4. User-provided captions, SRT, VTT, or copied transcript.

## Fast Recognition Rule

For a plain YouTube link, default to the pasted Transcript/SRT/VTT path first. Do not run network caption fetching automatically if it would trigger permission prompts or make the workflow feel slow.

If the user explicitly asks to try the link, make one quick caption attempt. The helper checks both:

- watch page `captionTracks`
- YouTube public `timedtext` track list

If it succeeds, continue directly to the learning package. If it fails, do not keep trying multiple unrelated routes in front of the user. Give the fallback and ask for pasted captions/SRT/VTT.

If the environment would require a network permission prompt, default to the pasted Transcript/SRT/VTT path instead of asking for permission automatically. The user can still explicitly request one public-caption attempt.

For Japanese videos, prefer Japanese captions before English captions. For songs and music videos, be clear that lyrics are often not exposed as public caption tracks even when text appears on screen.

## Do Not

- Do not claim the video was read when only the title was visible.
- Do not infer full transcript content from title, comments, thumbnail, or summary.
- Do not bypass login, private videos, region locks, paid content, or disabled captions.
- Do not download video/audio as a workaround.
- Do not run OCR or audio transcription on music videos as a workaround.
- Do not invent lyrics from the title, description, thumbnail, or comments.
- Do not reproduce full song lyrics. If a user provides a short excerpt, keep quoted lyrics brief and focus on explanation, vocabulary, grammar, and practice tasks.

## Fallback Message

Use this Chinese fallback:

```text
我暂时无法直接读取这条视频的完整字幕。你可以粘贴 YouTube 字幕、上传 SRT/VTT 字幕，或复制视频文稿，我会继续帮你生成学习包。
```

## Clear Music Video Fallback

Use this clearer Chinese fallback for music videos and normal user-facing replies:

```text
我暂时无法直接读取这条 YouTube 视频的公开字幕。很多日语歌的视频只有画面歌词或关闭了字幕轨，YouTube 不会把它们暴露成可读取字幕。

最快方式：打开 YouTube 的“显示文字稿/Transcript”，复制字幕贴给我；或者上传 SRT/VTT。我拿到文字后会直接生成 N3-N2 学习包、假名、中文意思、句子拆解、跟读稿、小测验和 Anki CSV。
```

Then offer the next action:

```text
你贴上字幕后，我会先清理时间轴和重复行，再帮你生成：内容摘要、重点句、句子拆解、跟读稿、Anki CSV 和打卡文案。
```
