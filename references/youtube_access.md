# YouTube Access Rules

Use this reference whenever the user gives a YouTube link.

## Safe Attempts

Try only accessible information:

1. Public page title and description.
2. Visible transcript text if the browsing environment exposes it.
3. Public caption metadata through `scripts/youtube_transcript_fetcher.py`.
4. User-provided captions, SRT, VTT, or copied transcript.

## Do Not

- Do not claim the video was read when only the title was visible.
- Do not infer full transcript content from title, comments, thumbnail, or summary.
- Do not bypass login, private videos, region locks, paid content, or disabled captions.
- Do not download video/audio as a workaround.

## Fallback Message

Use this Chinese fallback:

```text
我暂时无法直接读取这条视频的完整字幕。你可以粘贴 YouTube 字幕、上传 SRT/VTT 字幕，或复制视频文稿，我会继续帮你生成学习包。
```

Then offer the next action:

```text
你贴上字幕后，我会先清理时间轴和重复行，再帮你生成：内容摘要、重点句、句子拆解、影子跟读稿、Anki CSV 和打卡文案。
```
