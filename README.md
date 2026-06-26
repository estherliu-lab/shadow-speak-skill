# Shadow Speak Skill / 影子跟读 Skill / シャドー音読スキル

**Language / 语言 / 言語:** [中文](#中文) | [English](#english) | [日本語](#日本語)

Turn YouTube captions, SRT/VTT subtitles, English or Japanese text into shadowing scripts, sentence breakdowns, review cards, Anki CSV, quizzes, and daily study posts.

说明页 / Website:
[https://estherliu-lab.github.io/shadow-speak-skill/](https://estherliu-lab.github.io/shadow-speak-skill/)

Download ZIP:
[https://github.com/estherliu-lab/shadow-speak-skill/archive/refs/heads/main.zip](https://github.com/estherliu-lab/shadow-speak-skill/archive/refs/heads/main.zip)

---

## 中文

### 这是什么

Shadow Speak 是一个 Codex skill。它不是普通翻译器，而是把真实材料拆成可练习的语言学习包：

- 把 YouTube 字幕、SRT/VTT、文章、台词变成影子跟读稿
- 自动整理重点句、词汇、语法、语气和自然替代表达
- 生成 Anki CSV、5 分钟复习卡、小测验和打卡文案
- 支持英语和日语学习，默认用中文解释

### 三种安装方法

#### 方法 1：让 Codex 自动安装

把下面这句话发给 Codex：

```text
请帮我安装这个 Codex skill：
https://github.com/estherliu-lab/shadow-speak-skill

安装后告诉我怎么重启并测试。
```

Codex 通常会把仓库下载到你的 `.codex/skills` 目录。安装后重启 Codex，再开新对话使用。

#### 方法 2：下载 ZIP

1. 打开仓库右上角 `Code`
2. 点击 `Download ZIP`
3. 解压后把文件夹改名为 `shadow-speak-skill`
4. 放到：

```text
C:\Users\你的用户名\.codex\skills\shadow-speak-skill
```

macOS / Linux:

```text
~/.codex/skills/shadow-speak-skill
```

#### 方法 3：命令行安装

Windows PowerShell:

```powershell
git clone https://github.com/estherliu-lab/shadow-speak-skill.git "$env:USERPROFILE\.codex\skills\shadow-speak-skill"
```

macOS / Linux:

```bash
git clone https://github.com/estherliu-lab/shadow-speak-skill.git ~/.codex/skills/shadow-speak-skill
```

安装后重启 Codex。

### 第一次怎么测试

新开一个 Codex 对话，输入：

```text
$shadow-speak-skill 帮我把这段英文字幕做成影子跟读学习包，并生成 Anki CSV：

When I first started learning a new language, I thought progress meant memorizing more words every day. Later I realized that words only become useful when I can use them in a real situation.
```

你会得到类似这样的学习资料：

```markdown
# 影子跟读学习包

## 输入识别
- 学习语言：英语
- 内容类型：短视频/字幕文本
- 适合等级：B1-B2

## 今天最值得学的表达
1. progress meant memorizing more words
2. words become useful in a real situation
3. I later realized that...

## 句子拆解
原句：Later I realized that words only become useful when I can use them in a real situation.
自然意思：后来我才意识到，词只有在真实场景里用得出来，才真正有用。
值得学的点：I realized that... 很适合表达“我后来才明白”。

## 影子跟读
Later I **realized** / that words only become **useful** / when I can use them / in a real **situation**.

## Anki CSV
Front,Back,Tags
"I later realized that...","我后来才意识到...|表达认知变化|I later realized that practice matters more than speed.|english,B1,reflection"
```

### 更多可直接测试的提示词

```text
$shadow-speak-skill 这条 YouTube 视频我想学英语。如果你无法读取字幕，请提示我粘贴字幕：
https://www.youtube.com/watch?v=VIDEO_ID
```

```text
$shadow-speak-skill 帮我清理这段 SRT 字幕，选出 10 个最值得跟读的句子，并生成 Anki CSV。
```

```text
$shadow-speak-skill 用电影字幕老师模式拆解这段英文台词，重点讲语气、停顿、重音和潜台词。
```

```text
$shadow-speak-skill 把这段日语字幕做成 N3-N2 学习包：假名、中文意思、句子拆解、跟读稿、小测验都要。
```

```text
$shadow-speak-skill 这句话用英语和日语怎么自然表达？给我朋友聊天版、正式版、社交媒体版、温柔版。
```

```text
$shadow-speak-skill 帮我把这段英文文章整理成 IELTS Speaking 可用表达，并给 5 个替换练习。
```

```text
$shadow-speak-skill 生成今天的学习打卡文案，适合朋友圈、小红书和 X，内容不要太像 AI。
```

```text
$shadow-speak-skill 用严格老师模式检查我写的英文，指出不自然的地方，再给我更自然版本。
```

### 注意

如果只给 YouTube 链接，Skill 会尝试读取公开可访问的字幕，但不会绕过限制，也不会假装知道视频内容。读不到时，把字幕、SRT/VTT 或文稿贴给 Codex 即可。

---

## English

### What It Does

Shadow Speak is a Codex skill for language learners. It turns accessible YouTube captions, SRT/VTT subtitles, English or Japanese passages, and learner-written sentences into practice-ready study material.

It can generate:

- Shadowing scripts with pauses, stress, rhythm, and tone
- Sentence breakdowns with meaning, structure, nuance, and alternatives
- Vocabulary and phrase notes
- CEFR / JLPT / IELTS / TOEFL study guidance
- Anki CSV cards, quizzes, review cards, and daily study posts

### Install

Ask Codex to install it:

```text
Please install this Codex skill:
https://github.com/estherliu-lab/shadow-speak-skill

After installation, tell me how to restart Codex and test it.
```

Or install manually:

```bash
git clone https://github.com/estherliu-lab/shadow-speak-skill.git ~/.codex/skills/shadow-speak-skill
```

Windows PowerShell:

```powershell
git clone https://github.com/estherliu-lab/shadow-speak-skill.git "$env:USERPROFILE\.codex\skills\shadow-speak-skill"
```

Restart Codex after installation.

### Try It

```text
$shadow-speak-skill Turn this English transcript into a shadowing pack with sentence breakdowns and Anki CSV:

I used to think learning meant collecting more words. Now I try to choose a few sentences I can actually use in my life.
```

```text
$shadow-speak-skill Try this YouTube link first. If captions are unavailable, ask me to paste the transcript.
```

```text
$shadow-speak-skill Break down this Japanese subtitle excerpt for an N3-N2 learner, with kana, Chinese meanings, shadowing rhythm, and quiz questions.
```

---

## 日本語

### これは何ですか

Shadow Speak は Codex 用の skill です。YouTube 字幕、SRT/VTT、英語・日本語の文章や文を、音読・シャドーイング・復習に使える学習パックへ変換します。

できること：

- 区切り、強調、間、声のトーンつきの音読台本
- 文の意味、構造、ニュアンス、自然な言い換え
- 語彙・フレーズ整理
- JLPT / CEFR / IELTS / TOEFL 向けの学習ポイント
- Anki CSV、復習カード、クイズ、学習投稿文

### インストール

Codex に以下を送ると、インストールを依頼できます。

```text
Please install this Codex skill:
https://github.com/estherliu-lab/shadow-speak-skill

After installation, tell me how to restart Codex and test it.
```

手動の場合：

```bash
git clone https://github.com/estherliu-lab/shadow-speak-skill.git ~/.codex/skills/shadow-speak-skill
```

Windows PowerShell:

```powershell
git clone https://github.com/estherliu-lab/shadow-speak-skill.git "$env:USERPROFILE\.codex\skills\shadow-speak-skill"
```

インストール後、Codex を再起動してください。

### 試すプロンプト

```text
$shadow-speak-skill この日本語字幕を N3-N2 向けのシャドーイング教材にしてください。かな、中文解释、文解説、Anki CSV も入れてください。
```

```text
$shadow-speak-skill この英語スクリプトを音読練習、文解説、復習カードにしてください。
```
