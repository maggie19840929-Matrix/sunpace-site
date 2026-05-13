# Sunny 的 PTE 小课堂内容流程

目标：把官网 Sunny 知识库变成小红书短视频素材，供小号发布 `Sunny 的 PTE 小课堂`。

## 内容来源

使用这个文件作为主素材库：

`data/pte-knowledge.sunpace.json`

这个文件里的内容已经从 PDF/OCR/课程资料中改写成 SunPace 自己的答疑口径，适合二次改造成短视频脚本。

不要直接使用：

- OCR 原文
- 课程 PDF 原文
- 视频转写逐字稿
- 机经题目全文
- 模板全文

这些只能作为内部理解材料，最终发布内容必须改写成 SunPace/Sunny 自己的话术。

## 已生成的内容队列

运行：

```bash
python3 scripts/build_xhs_sunny_classroom.py
```

会生成：

`content_exports/xiaohongshu/sunny-pte-classroom-queue-latest.csv`

以及：

`content_exports/xiaohongshu/sunny-pte-classroom-queue-latest.json`

每条包含：

- 选题
- 提问角度
- 封面文字
- 3 个标题备选
- 短视频结构脚本
- 小红书正文草稿
- 标签
- 制作备注

## 和 Hermes / openclaw 的衔接方式

推荐把 `sunny-pte-classroom-queue-latest.json` 作为上游选题输入。

每条内容可以交给 Hermes 调度 openclaw 生成：

1. 封面：使用 `cover_text` 和 `topic`。
2. 视频：使用 `video_script`，让 Sunny 卡通人物口播。
3. 标题：优先使用 `title_option_1`，必要时 A/B 测 `title_option_2`。
4. 正文：使用 `caption`，再加 `hashtags`。
5. 发布备注：参考 `production_note`。

## 小号恢复后的建议节奏

5 月 14 日小号恢复发布后，建议先连续发高转化题型：

1. RA 怎么练
2. RA 五步拆解
3. RS 怎么练
4. WFD 怎么练
5. DI 模板怎么用
6. RL 怎么练
7. RO 排序怎么练
8. FIB 固定搭配怎么背
9. SST 逻辑速刷怎么用
10. PTE 机经和预测怎么用

建议一天 1-2 条，先看完播率、收藏、评论问题，再决定是否加量。

## 内容风格

Sunny 的小红书口径建议：

- 每条只解决一个问题。
- 开头 3 秒直接打痛点。
- 正文不要讲大课，讲一个可执行动作。
- 不输出课程原文。
- 结尾引导用户留下当前分数、目标分数、考试日期。

## 适合的封面结构

封面建议：

- 第一行：题型或痛点，例如 `RA总卡顿？`
- 第二行：Sunny 的一句判断，例如 `先别急着练速度`
- 角标：`Sunny的PTE小课堂`

## 账号分工

大号：

- 品牌背书
- 活动预告
- 成功案例
- 正式课程介绍

小号：

- Sunny 的 PTE 小课堂
- 高频题型答疑
- PTE 备考误区
- 评论区问题二创

这样大号负责信任，小号负责内容触达和日更。
