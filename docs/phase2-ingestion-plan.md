# Sunny Phase 2 Knowledge Ingestion

目标：把 PDF 图片版资料和视频课程逐步整理成 Sunny 可用的 SunPace 自有答疑知识，而不是把第三方课程原文直接发布到官网。

## 当前结论

第一阶段已经完成：

- 文档类资料已做一次夜间索引。
- 成功抽取文字的文档进入 `data/pte-knowledge.generated.json`。
- Sunny 已接入 `data/pte-knowledge.sunpace.json`，并优先使用 SunPace 自有话术。

第二阶段建议分两条线推进：

1. PDF OCR 增强：处理图片版 PDF、扫描版 PDF、抽取失败 PDF、大文件 PDF。
2. 视频转写试点：先挑 10-20 个高价值视频，把音频转成文字，再总结成 SunPace 自有话术。

## 已生成的队列

本次队列目录：

`knowledge_exports/phase2/20260512-090856`

里面有：

- `pdf-ocr-queue.csv`：需要 OCR 或重试抽取的 PDF，按优先级排序。
- `media-transcription-pilot.csv`：建议先转写的视频/音频，按优先级排序。
- `summary.json`：本次统计结果。

本次结果：

- PDF 二次处理候选：67 个。
- 视频/音频试点候选：80 个。
- PDF 候选包括：44 个图片版 PDF、14 个超大 PDF、9 个抽取报错 PDF。

## PDF OCR 试点结果

已完成第一批小规模 OCR：

`knowledge_exports/phase2-ocr/20260512-092854`

本次试点：

- 处理 PDF：5 个。
- 每个 PDF 最多识别前 6 页。
- 成功 OCR：5 个。
- 识别内容已用于整理第一批 SunPace 自有答疑话术。

新增到 `data/pte-knowledge.sunpace.json` 的话术方向：

- 听力 FIB 高频词怎么用
- RL 高频思维导图怎么用
- DI/RL 专有名词怎么准备
- RA 五步拆解训练
- 阅读易混淆词怎么积累

注意：OCR 文字只作为内部理解材料，不能直接发布原文。

已完成第二批 PDF OCR：

`knowledge_exports/phase2-ocr/20260512-172646`

本次结果：

- 处理 PDF：20 个。
- 每个 PDF 最多识别前 8 页。
- 成功 OCR：20 个。
- 识别内容已继续改写成 SunPace 自有答疑话术。

第二批新增到 `data/pte-knowledge.sunpace.json` 的话术方向：

- 阅读 FIB 固定搭配怎么背
- SST 逻辑速刷怎么用
- RS 按话题分类怎么练
- FIB 速刷资料怎么用
- RO 速记口诀怎么用
- SST 和 LFIB 怎么一起练
- ASQ 机经要不要背
- WE 大作文如何提升词汇多样性
- 改革后 DI/RL 还能用模板吗
- PTE 数字反应怎么练

## PDF OCR 顺序

优先处理 `pdf-ocr-queue.csv` 前 20-40 行。

这些通常是：

- 2026 改革后资料
- 全科备考资料
- RA / RS / DI / RL / WFD / SST / FIB / RO / WE / SWT
- 高频词、固定搭配、评分、模板类内容

OCR 之后不要直接把识别文字放进 Sunny。正确流程是：

1. OCR 得到文字。
2. 按题型和问题拆主题。
3. 改写成 SunPace 自己的答疑话术。
4. 合并到 `data/pte-knowledge.sunpace.json`。

## 视频转写顺序

先处理 `media-transcription-pilot.csv` 前 10-20 行。

视频处理流程：

1. 从视频提取音频。
2. 音频转文字稿。
3. 按题型切分重点。
4. 总结成 SunPace 自有话术。
5. 只把总结后的答疑内容接给 Sunny。

不要让官网用户访问时实时解析视频。视频转写必须是后台批处理，适合夜间或云端执行。

## 建议架构

Sunny 的知识优先级保持：

1. `data/pte-knowledge.sunpace.json`：SunPace 自有话术，最高优先级。
2. `data/pte-knowledge.json`：人工基础库。
3. OpenAI Vector Store：托管知识库，大模型检索兜底。
4. `data/pte-knowledge.generated.json`：自动索引兜底。

## 版权和口径

淘宝购买课程、PDF、视频转写稿都不要原文发布。

Sunny 可以吸收这些资料里的主题、训练方法和常见问题，但最终回答必须改写成 SunPace 自己的表达，重点服务官网访客：

- 回答要短。
- 方法要具体。
- 不输出大段讲义。
- 遇到个性化问题，引导用户提供当前分数、目标分数和考试日期。

## 重新生成队列

如果资料库变化，可以重新运行：

```bash
python3 scripts/plan_phase2_ingestion.py --media-limit 80
```

默认读取：

- 源资料：`/Volumes/PTE_Resources`
- 第一阶段清单：`knowledge_exports/nightly/20260512-045207/manifest.csv`

这个脚本只生成队列，不做 OCR，不转写视频。

如果要继续 OCR 队列前 20 个 PDF，可以运行：

```bash
/Users/cookie/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/run_pdf_ocr_batch.py --limit 20 --max-pages 8 --scale 2.0
```

OCR 依赖安装在项目本地的 `.codex_deps/python`，不要上传到 GitHub。
