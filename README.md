# Shadow Speak Skill / 影子跟读 Skill / シャドー音読スキル

把 YouTube 链接、字幕、SRT/VTT、英文或日文文章，拆成可以朗读、跟读、复习、导出和打卡的语言学习资料。

使用说明页：

[https://estherliu-lab.github.io/shadow-speak-skill/](https://estherliu-lab.github.io/shadow-speak-skill/)

说明页支持中文、English、日本語三种语言切换，包含用途、适合人群、使用方法、输入输出和 YouTube 读取限制。

## 它适合谁

- 想用 YouTube 学英语或日语，但不知道怎么拆字幕的人
- 想练 shadowing、朗读节奏、重音和语气的人
- 想把文章或台词变成 Anki 卡片和复习包的人
- 想准备 JLPT、IELTS、TOEFL 或商务英语表达的人
- 想每天输出学习打卡内容的人

## 支持输入

- YouTube 链接
- YouTube 字幕文本
- SRT 字幕
- VTT 字幕
- 英文文章、句子或自己写的英文
- 日文文章、句子或自己写的日文
- 中文句子，例如“这句话英语和日语怎么自然表达”

## 支持输出

- 视频精学学习包
- 影子跟读朗读稿
- 句子拆解和自然替代表达
- CEFR / JLPT / IELTS / TOEFL 学习建议
- Anki CSV
- 5 分钟复习卡
- 小测验和答案解析
- 朋友圈、小红书、X、学习群打卡文案

## YouTube 读取限制

这个 skill 可以尝试读取公开可访问的 YouTube 字幕或页面可见文稿，但不会绕过平台限制，也不会假装已经读取无法访问的视频内容。

如果视频没有可访问字幕，请把 YouTube 字幕、SRT/VTT 文件或视频文稿粘贴给 Codex。Skill 会继续清理文本并生成学习包。

## 脚本

```bash
python scripts/youtube_transcript_fetcher.py "https://www.youtube.com/watch?v=VIDEO_ID" transcript.txt
python scripts/subtitle_cleaner.py tests/sample_srt.srt cleaned.txt
python scripts/anki_csv_exporter.py tests/sample_cards.json cards.csv
python scripts/markdown_exporter.py learning_pack.md --topic "morning routine"
```

## 可直接测试的提示词

```text
用影子跟读 Skill 帮我拆解这段日语字幕，适合 N3-N2 学习者。
```

```text
帮我把这段英文做成 shadowing 练习，解释用中文，并生成 Anki CSV。
```

```text
这条 YouTube 视频我想学英语。如果你无法读取字幕，请提示我粘贴字幕。
```

```text
用电影字幕老师模式拆解这段英文台词，重点讲语气和潜台词。
```

```text
这句话用英语和日语怎么自然表达？给我朋友聊天版、正式版、社交媒体版。
```
