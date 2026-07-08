# Lingua Pack Skill / 语境学习包 Skill / リンガパック Skill

**Language / 语言 / 言語:** [中文](#中文) | [English](#english) | [日本語](#日本語)

Turn short articles, dialogues, subtitle text, SRT/VTT files, English or Japanese text into shadowing scripts, sentence breakdowns, review cards, Anki CSV, quizzes, and daily study posts.

## English Introduction

Lingua Pack Skill is a Codex skill for English and Japanese language learners who want to turn real study material into practice-ready learning packs. Instead of only translating text, it helps learners understand useful sentences, speak them aloud, review them later, and export them into reusable study formats.

The most reliable workflow is simple: paste a short article, dialogue, subtitle text, or SRT/VTT captions, then ask Codex to create a shadowing pack. The skill can generate Chinese summaries, key expressions, sentence breakdowns, pronunciation and rhythm notes, quizzes, Anki CSV cards, and short daily study posts.

This project is designed for learners who want a smooth first experience. The recommended first test uses 2-5 short sentences, not a video link. YouTube is treated as an optional last step because many videos do not expose public caption tracks; when using video material, copied transcript text or SRT/VTT captions are much more reliable.

说明页 / Website:
[https://estherliu-lab.github.io/shadow-speak-skill/](https://estherliu-lab.github.io/shadow-speak-skill/)

Download ZIP:
[https://github.com/estherliu-lab/shadow-speak-skill/archive/refs/heads/main.zip](https://github.com/estherliu-lab/shadow-speak-skill/archive/refs/heads/main.zip)

---

## 中文

### 这是什么

Lingua Pack 是一个 Codex skill，中文名是“语境学习包”。它不是普通翻译器，而是把真实材料拆成可练习的语言学习包：

- 把短文章、台词、字幕文本、SRT/VTT 变成影子跟读稿
- 自动整理重点句、词汇、语法、语气和自然替代表达
- 生成 Anki CSV、5 分钟复习卡、小测验和打卡文案
- 支持英语和日语学习，默认用中文解释

### 最快最稳的用法

最推荐：直接粘贴一段短文章、台词、字幕文本，或上传/粘贴 SRT/VTT 字幕。

第一次测试建议使用 2-5 句的短文章或台词，这样不用等待抓取，也不会遇到权限询问，能马上看到学习包效果。

```text
$shadow-speak-skill 把下面这段短日文做成 N3-N2 学习包：假名、中文意思、句子拆解、跟读稿、小测验、Anki CSV 都要。

最近、短い文章を声に出して読む練習をしています。意味が全部わからなくても、何度も読んでいるうちに、少しずつ自然な言い方が身についてきました。
```

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
$shadow-speak-skill 帮我把这段英文短文章做成影子跟读学习包，并生成 Anki CSV：

When I first started learning a new language, I thought progress meant memorizing more words every day. Later I realized that words only become useful when I can use them in a real situation.
```

你会得到类似这样的学习资料：

```markdown
# 影子跟读学习包

## 输入识别
- 学习语言：英语
- 内容类型：短文章 / 学习反思
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

### 完整案例：一段短文章如何变成学习包

这个案例适合第一次测试：用户只需要贴一段短文章或台词，Skill 会把它变成可以跟读、复习、测试和导出的学习资料。

**用户输入**

```text
$shadow-speak-skill 帮我把这段英文短文章做成影子跟读学习包，并生成 Anki CSV：

When I first started learning a new language, I thought progress meant memorizing more words every day. Later I realized that words only become useful when I can use them in a real situation.
```

**Skill 处理过程**

1. 判断语言和难度：英语，短文章/学习反思类内容，适合 B1-B2。
2. 提取核心表达：`progress meant...`、`Later I realized that...`、`only become useful when...`。
3. 拆解句子：解释自然意思、结构、语气和可替换表达。
4. 生成跟读稿：用 `/` 标出停顿，用 `**bold**` 标出重音。
5. 生成复习材料：5 分钟复习卡、小测验、答案解析、Anki CSV。

**学习包输出片段**

```markdown
## 输入识别
- 学习语言：英语
- 内容类型：短文章 / 个人学习反思
- 适合等级：B1-B2

## 重点句子拆解
原句：Later I realized that words only become useful when I can use them in a real situation.
中文意思：后来我才明白，单词要能在真实场景里用出来，才算真的有用。
结构：Later I realized that... + words only become useful when...
可替换表达：I eventually understood that words are useful only when they work in real life.

## 影子跟读
**Later** I **realized** that / words only become **useful** / when I can **use them** / in a **real situation**.

## 复述任务
用 “Later I realized that...” 说一个你后来才明白的学习道理。
```

**Anki CSV 是可选导出**

Anki 是一款间隔重复记忆卡片软件。普通用户不用安装 Anki 也能直接看学习包练习；已经使用 Anki 的用户，可以把 CSV 导入成卡片长期复习。

```csv
Front,Back,Tags
"Later I realized that...","后来我意识到……|引出认知转变|Later I realized that speaking takes daily practice.|english,B1-B2,pattern"
```

### 更多可直接测试的提示词

```text
$shadow-speak-skill 把下面这段英文短文章做成 B1-B2 学习包：中文摘要、重点表达、句子拆解、跟读稿、小测验、Anki CSV 都要。

I used to think learning meant collecting more words. Now I try to choose a few sentences I can actually use in my life.
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

短文章、台词、字幕文本、SRT/VTT 是最稳定的输入。只给视频链接通常不稳定，不建议作为第一次测试。

### 可选：如果你一定想用 YouTube 视频

最稳方法不是复制视频链接，而是复制字幕文字：

1. 打开 YouTube 视频页面。
2. 找到视频下方标题/简介区域附近的 `...`、`更多` 或 `Show transcript / 显示文字稿`。
3. 打开文字稿后，手动选中字幕文本并复制。
4. 把复制出来的字幕贴给 Codex，并告诉它你想要的等级，比如 N3-N2、B1-B2。

如果你有自己的字幕文件，也可以直接上传或粘贴 SRT/VTT。

只有当视频本身有公开字幕轨时，才可以尝试复制视频链接让 Skill 快速检测一次。复制链接的方法是：点 YouTube 的 `Share / 分享` → `Copy / 复制链接`。但如果没有公开字幕轨，只贴链接无法生成学习包。

---

## English

### What It Does

Lingua Pack Skill is a Codex skill for language learners. It turns short articles, dialogues, subtitle text, SRT/VTT files, English or Japanese passages, and learner-written sentences into practice-ready study material.

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
$shadow-speak-skill Turn this short English article into a shadowing pack with sentence breakdowns and Anki CSV:

I used to think learning meant collecting more words. Now I try to choose a few sentences I can actually use in my life.
```

```text
$shadow-speak-skill Break down this short dialogue for speaking practice. Explain tone, pauses, useful phrases, and make Anki CSV cards.
```

```text
$shadow-speak-skill Break down this Japanese subtitle excerpt for an N3-N2 learner, with kana, Chinese meanings, shadowing rhythm, and quiz questions.
```

---

## 日本語

### これは何ですか

Lingua Pack Skill は Codex 用の skill です。短い文章、会話文、字幕テキスト、SRT/VTT、英語・日本語の文章や文を、音読・シャドーイング・復習に使える学習パックへ変換します。

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
