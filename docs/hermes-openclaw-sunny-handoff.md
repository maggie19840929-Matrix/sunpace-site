# Hermes / openclaw：Sunny 的 PTE 小课堂交接说明

## 目标

从 5 月 14 日开始，小红书小号恢复发布 `Sunny 的 PTE 小课堂`。

原有流程保持不变：

`Hermes 定时任务 -> openclaw 取素材 -> huashu.skill -> Seedance 2.0 生成短视频 -> ChatGPT Image 生成封面 -> 输出标题和正文`

本次只新增一个更干净的上游素材源：

`content_exports/xiaohongshu/sunny-pte-classroom-queue-latest.json`

## 新素材源

Sunny 的 PTE 小课堂素材来自：

`data/pte-knowledge.sunpace.json`

这个文件已经把 PDF/OCR/课程资料改写成 SunPace 自有答疑口径。

为了方便 Hermes / openclaw 读取，我已经生成：

`content_exports/xiaohongshu/sunny-pte-classroom-queue-latest.json`

以及表格版：

`content_exports/xiaohongshu/sunny-pte-classroom-queue-latest.csv`

如果 Sunny 话术库更新，重新运行：

```bash
python3 scripts/build_xhs_sunny_classroom.py
```

就会刷新最新选题队列。

## openclaw 每条任务读取字段

每条素材包含：

- `episode`：建议发布顺序
- `source_id`：对应 Sunny 知识库条目 ID
- `topic`：选题
- `question`：用户视角问题
- `cover_text`：封面主文字
- `title_option_1`：优先标题
- `title_option_2`：备用标题
- `title_option_3`：备用标题
- `video_script`：短视频口播结构
- `caption`：小红书正文草稿
- `hashtags`：标签
- `production_note`：制作注意事项
- `status`：默认 `draft`

## 推荐执行规则

Hermes 每日定时任务：

1. 读取 `sunny-pte-classroom-queue-latest.json`
2. 找到 `status = draft` 的第一条或当天指定条目
3. 交给 openclaw 执行
4. openclaw 调用 `huashu.skill`，把 `video_script` 改成更自然的 Sunny 口播稿
5. 用 Seedance 2.0 生成 Sunny 卡通人物短视频
6. 用 ChatGPT Image 生成封面
7. 输出小红书标题、正文、标签
8. 保存成待发布稿

## 给 huashu.skill 的要求

huashu.skill 应该做：

- 保留原选题观点
- 变成 40-60 秒短视频口播
- 开头 3 秒必须直接打痛点
- 每条只解决一个问题
- 语言像 Sunny，一个温和但专业的 PTE 助教
- 不要说“根据资料库”
- 不要输出课程原文、题库原文、机经原文、模板全文
- 结尾引导用户留下当前分数、目标分数、考试时间

## 给 Seedance 2.0 的方向

视频方向：

- Sunny 卡通人物口播
- 竖屏 9:16
- 40-60 秒
- 节奏轻快
- 屏幕上出现 2-4 个关键词提示
- 不展示课程 PDF 原文
- 不展示机经题目全文
- 不展示模板全文

## 给封面生成的方向

封面方向：

- 竖屏小红书封面
- Sunny 卡通人物明显
- 大字突出 `cover_text`
- 角标：`Sunny的PTE小课堂`
- 风格明亮、干净、教育感
- 不使用第三方课程 logo
- 不展示原始资料截图

## 标题和正文规则

标题：

- 优先用 `title_option_1`
- 如果太长，用 `title_option_2`
- 不要夸张承诺，比如“必过”“保分”“100%命中”

正文：

- 用 `caption` 做底稿
- 可以微调得更像小红书
- 保留 `hashtags`
- 不要贴课程原文

## 首批发布建议

小号恢复后，优先发布前 10 条：

1. Read Aloud 训练方法
2. RA 五步拆解训练
3. Repeat Sentence 训练方法
4. WFD 听写训练
5. Describe Image 模板使用
6. Retell Lecture 训练方法
7. RO 排序题训练
8. RO 速记口诀怎么用
9. FIB 阅读填空训练
10. 阅读 FIB 固定搭配怎么背

建议每天 1-2 条，先看完播率、收藏、评论问题。

## 安全边界

可以使用：

- `data/pte-knowledge.sunpace.json`
- `content_exports/xiaohongshu/sunny-pte-classroom-queue-latest.json`
- Sunny 自有话术
- openclaw / huashu.skill 改写后的口播稿

不要直接使用：

- OCR 原文
- PDF 原文
- 课程视频逐字稿
- 机经题目全文
- 模板全文
- 第三方课程 logo 或资料截图

核心原则：

`课程资料用于内部理解，公开视频只输出 SunPace / Sunny 自己的教学表达。`

## 可直接给 Hermes 的任务描述

请每天从：

`content_exports/xiaohongshu/sunny-pte-classroom-queue-latest.json`

读取一条 `status = draft` 的 Sunny 小课堂选题，按 `episode` 顺序生产小红书内容。沿用原流程：openclaw 调用 `huashu.skill` 改写口播稿，用 Seedance 2.0 生成 Sunny 竖屏短视频，用 ChatGPT Image 生成封面，并输出标题、正文和标签。

素材字段使用规则：

- 封面文字用 `cover_text`
- 视频脚本用 `video_script`
- 标题优先用 `title_option_1`
- 正文用 `caption`
- 标签用 `hashtags`
- 制作注意事项看 `production_note`

要求：不要发布课程原文、OCR 原文、机经全文或模板全文。所有内容必须保持 SunPace / Sunny 自己的表达方式。
