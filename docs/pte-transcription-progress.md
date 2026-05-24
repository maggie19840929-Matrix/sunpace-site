# PTE Transcription Progress

本文件记录 Sunny PTE 本地转写进度。原始课程逐字转写稿与队列产物保留在本地 `knowledge_exports/`，该目录被 `.gitignore` 忽略；GitHub 只同步进度摘要和可公开的工程记录。

## 同步规则

- 每完成 2 批转写后，同步一次 GitHub。
- 每批默认 8 个音视频候选。
- GitHub 不提交第三方课程逐字稿。
- 可提交内容包括：进度摘要、队列统计、脚本/流程修正，以及改写后的 SunPace 自有知识库内容。

## 2026-05-19 Sync 1

- 队列：`20260519-resume-3`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-3`
- 覆盖批次：第 1-2 批，`seq 4001-4016`
- 本次处理：16 条
- 成功转写：4 条
- 跳过：12 条，原因均为 `skip_duration_too_short`

成功转写条目：

- `4001` 周末名师刷题室 `181-WFD带练.mp4`，1499 字
- `4002` 周末名师刷题室 `183-WFD带练.mp4`，1391 字
- `4003` 周末名师刷题室 `182-WFD带练.mp4`，2042 字
- `4004` 周末名师刷题室 `180-WFD带练.mp4`，2702 字

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：457
- 成功可用转写：438
- 低文本：2
- 时长过短跳过：17
- 尚未尝试：1562
- 尚未成功：1581

备注：`resume-3` 的前两批暴露出周末名师刷题室存在大量几秒钟短视频，后续队列应降低这类短视频优先级，优先继续处理完整课时、PTE Core、改革后技巧课和 WFD/SST/FIB/RA 等高价值长视频。

## 2026-05-19 Sync 2

- 队列：`20260519-resume-3`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-3`
- 覆盖批次：第 3-4 批，主要覆盖 `seq 4017-4030`
- 本次处理尝试：16 次
- 去重新源文件：14 条
- 成功转写：6 条
- 低文本：2 条，`4023`、`4024`
- 跳过：6 条，原因均为 `skip_duration_too_short`

成功转写条目：

- `4025` SST 高频微课 `015-globalization and detraditionalization近似.mp4`，2967 字
- `4026` SST 高频微课 `085-The separation of power不完整题型.mp4`，3045 字
- `4027` 周末名师刷题室 `034-听力刷题.mp4`，3272 字
- `4028` 周末名师刷题室 `026-阅读刷题.mp4`，1504 字
- `4029` 周末名师刷题室 `014-听力刷题.mp4`，2678 字
- `4030` 周末名师刷题室 `011-听力刷题.mp4`，2187 字

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：471
- 成功可用转写：444
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1548
- 尚未成功：1575

备注：当前脚本会重试 `low_text` 条目，因此第 4 批里 `4023`、`4024` 被重复处理了一次。后续应在继续跑队列前绕开或修正该行为，把算力留给完整课时。

## 2026-05-19 Sync 3

- 队列：`20260519-resume-3`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-3`
- 覆盖批次：第 5-6 批，覆盖 `seq 4031-4040`
- 本次处理：10 条
- 成功转写：10 条
- 低文本：0 条
- 跳过：0 条

成功转写条目：

- `4031` 周末名师刷题室 `088-听力刷题.mp4`，2003 字
- `4032` 周末名师刷题室 `003-阅读刷题.mp4`，4835 字
- `4033` 周末名师刷题室 `017-听力刷题.mp4`，880 字
- `4034` 周末名师刷题室 `024-口语刷题.mp4`，1130 字
- `4035` 周末名师刷题室 `019-口语刷题.mp4`，2123 字
- `4036` 周末名师刷题室 `082-听力刷题.mp4`，2405 字
- `4037` 周末名师刷题室 `013-口语刷题.mp4`，4240 字
- `4038` 周末名师刷题室 `005-听力刷题.mp4`，3923 字
- `4039` 周末名师刷题室 `028-听力刷题.mp4`，975 字
- `4040` 周末名师刷题室 `100-听力刷题.mp4`，1605 字

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：481
- 成功可用转写：454
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1538
- 尚未成功：1565

备注：`resume-3` 队列已跑完。最后 10 条质量较好，说明周末名师刷题室并非整体不可用，但短视频切片需要在后续队列中预筛掉。

## 2026-05-19 Sync 4

- 队列：`20260519-resume-4`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-4`
- 覆盖批次：第 1-2 批，覆盖 `seq 5001-5016`
- 建队列改进：预先用 `ffprobe` 过滤 60 秒以下短视频
- 本次处理：16 条
- 成功转写：16 条
- 低文本：0 条
- 跳过：0 条

成功转写条目：

- `5001` 公益包 `DI避雷坑.mp4`，3025 字
- `5002` 公益包 `为什么听不懂SST.mp4`，2631 字
- `5003` 公益包 `SST你会刷题吗？.mp4`，1547 字
- `5004` 本地第三方公益包 RA 提分详解录屏，1116 字
- `5005` 公益包 `WE论点小技巧代入法.mp4`，3455 字
- `5006-5016` SST 高频真题训练微课 11 条，全部成功

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：497
- 成功可用转写：470
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1522
- 尚未成功：1549

备注：`resume-4` 的时长预筛效果很好，前两批成功率从 `resume-3` 的波动状态恢复到 100%。后续应继续使用时长预筛队列。

## 2026-05-19 Sync 5

- 队列：`20260519-resume-4`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-4`
- 覆盖批次：第 3-4 批，覆盖 `seq 5017-5032`
- 本次处理：16 条
- 成功转写：16 条
- 低文本：0 条
- 跳过：0 条

成功转写条目：

- `5017-5028` SST 高频真题训练微课 12 条，全部成功
- `5029` 真经班 `第27课口语特训5.mp4`，917 字
- `5030` 真经班 `第23课口语特训1.mp4`，3501 字
- `5031` 真经班 `第26课口语特训4.mp4`，2448 字
- `5032` 真经班 `第24课口语特训2.mp4`，2572 字

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：513
- 成功可用转写：486
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1506
- 尚未成功：1533

备注：`resume-4` 第 3-4 批继续保持 100% 成功率，SST 高频微课和完整口语特训课适合作为后续高优先级素材。

## 2026-05-19 Sync 6

- 队列：`20260519-resume-4`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-4`
- 覆盖批次：第 5 批，覆盖 `seq 5033-5040`
- 本次处理：8 条
- 成功转写：8 条
- 低文本：0 条
- 跳过：0 条
- 队列结论：`resume-4` 全部 40 条均成功

成功转写条目：

- `5033` 外部改革说明视频，4171 字
- `5034` 公益包官方 Listening webinar，3468 字
- `5035` 真经班 `第22课阅读练习.mp4`，3557 字
- `5036` 真经班 `第25课口语特训3.mp4`，2885 字
- `5037` 真经班 `第19课口语练习2.mp4`，2980 字
- `5038` 真经班 `第18课口语练习1.mp4`，4057 字
- `5039` 公开课 `PTE口语满分技巧五步拆解训练..mp4`，2812 字
- `5040` SST 高频微课 `042-Online research(不完整题型）.mp4`，1119 字

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：521
- 成功可用转写：494
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1498
- 尚未成功：1525

备注：`resume-4` 预筛队列验证通过，后续队列应继续保留 `ffprobe` 时长检查，并优先完整课程、SST 高频微课、改革后技巧课和可复用题型训练。

## 2026-05-19 Sync 7

- 队列：`20260519-resume-5`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-5`
- 覆盖批次：第 1-2 批，覆盖 `seq 6001-6016`
- 本次处理：16 条
- 成功转写：16 条
- 低文本：0 条
- 跳过：0 条

成功转写条目：

- `6001-6016` SST 高频真题训练微课 16 条，全部成功
- 代表主题包括：Sound of words、sleep、Money、stock market、stability of mood、smart city、bees' genes、paper rejection、MPA marine campaign、Air pollution、Adam Smith、Global market

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：537
- 成功可用转写：510
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1482
- 尚未成功：1509

备注：SST 高频真题训练微课连续两轮保持高成功率，可继续优先转写；后续再把内容蒸馏成 SunPace 自有表达的 SST 备考知识点。

## 2026-05-20 Sync 8

- 队列：`20260519-resume-5`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-5`
- 覆盖批次：第 3-4 批，覆盖 `seq 6017-6032`
- 本次处理：16 条
- 成功转写：16 条
- 低文本：0 条
- 跳过：0 条

成功转写条目：

- `6017-6032` SST 高频真题训练微课 16 条，全部成功
- 代表主题包括：Internet and journalism、canned foods、Face recognition、renewable energy、sign language、hospital design、email system、decline of bees、Origin of Species、automation、Sugar、history of English

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：553
- 成功可用转写：526
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1466
- 尚未成功：1493

备注：SST 高频微课继续保持 100% 成功率。当前可优先把这批内容蒸馏成 SST 高频主题库，再进入更长的综合刷题课。

## 2026-05-20 Sync 9

- 队列：`20260519-resume-5`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260519-resume-5`
- 覆盖批次：第 5 批，覆盖 `seq 6033-6040`
- 本次处理：8 条
- 成功转写：8 条
- 低文本：0 条
- 跳过：0 条
- 队列结论：`resume-5` 全部 40 条均成功

成功转写条目：

- `6033-6040` SST 高频真题训练微课 8 条，全部成功
- 代表主题包括：humans and animals、absolutism、negative emotions、HTML、Fight or flight response、global economy、artificial intelligence、Tree rings

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：561
- 成功可用转写：534
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1458
- 尚未成功：1485

备注：`resume-5` 继续验证预筛策略有效，40 条全成功；SST 高频微课已形成较大可用转写池。

## 2026-05-20 Sync 10

- 队列：`20260520-resume-6`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260520-resume-6`
- 覆盖批次：第 1-2 批，覆盖 `seq 7001-7016`
- 本次处理：16 条
- 成功转写：16 条
- 低文本：0 条
- 跳过：0 条

成功转写条目：

- `7001-7016` SST 高频真题训练微课 16 条，全部成功
- 代表主题包括：The market economy、Gene development、Food crisis、language in danger、mathematicians、Studying law、London ugly architecture、smile of mother and baby、organization study、dancing bees、global warming、modern poetry、chimpanzee、history of software、recycling water、Student loan

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：577
- 成功可用转写：550
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1442
- 尚未成功：1469

备注：`resume-6` 前两批继续保持 100% 成功率；SST 高频微课的可用转写池已超过 550 条，可继续按“两批一同步”节奏推进。

## 2026-05-20 Sync 11

- 队列：`20260520-resume-6`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260520-resume-6`
- 覆盖批次：第 3-4 批，覆盖 `seq 7017-7032`
- 本次处理：16 条
- 成功转写：16 条
- 低文本：0 条
- 跳过：0 条

成功转写条目：

- `7017-7020` SST 高频真题训练微课 4 条，主题包括 biology application、DNA and RNA、human rights in UK、Industrial Revolution V2
- `7021-7032` 真经班/周末名师刷题室听口练习与刷题课 12 条，覆盖口语、听力长课抽样
- 注意：`7026`、`7028` 达到成功阈值但文本量接近下限，后续蒸馏时应优先人工复核

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：593
- 成功可用转写：566
- 低文本：4
- 时长过短跳过：23
- 尚未尝试：1426
- 尚未成功：1453

备注：`resume-6` 已完成 32 条，全部成功；队列开始从短微课切入长课，单批耗时上升，但多 offset 抽样仍能稳定取得可用文本。

## 2026-05-21 Sync 12

- 模式：夜间本地转写，GitHub 上传暂停后恢复同步
- 覆盖队列：`20260520-resume-6` 至 `20260520-resume-26`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260520-resume-*`
- 本次快照范围：从 `resume-6` 完整队列到 `resume-26` 已落盘 `seq 27001-27039`
- 本次新增落盘处理：839 条
- 成功转写：692 条
- 低文本：147 条
- 本地跳过策略：低文本、过短和损坏素材继续本地记录，不上传原始逐字稿

夜间转写概况：

- `resume-6`、`resume-8`、`resume-9`、`resume-12`、`resume-16`、`resume-24`、`resume-25` 均为 40/40 成功
- `resume-7` 至 `resume-26` 期间，队列从 SST/RA/口语/听力高频课逐步进入周末名师刷题室长课和低优先级素材
- `resume-26` 截至本次同步时已落盘 39 条，39 条均成功；后台 runner 仍在本地继续处理后续条目
- 夜间建队列已识别大量 60 秒以下或损坏素材，并保留在本地跳过记录中，后续不再优先消耗转写算力

全盘累计状态：

- 可转写音视频总数：2019
- 已处理去重源文件：1400
- 成功可用转写：1226
- 低文本：151
- 时长过短跳过：23
- 尚未尝试：619
- 尚未成功：793

备注：本次 GitHub 同步仍只包含公开进度摘要；`knowledge_exports/` 下的第三方课程队列、逐字转写稿、夜间日志继续保留本地并由 `.gitignore` 忽略。

## 2026-05-21 Sync 13

- 模式：白天模式恢复 GitHub 同步
- 覆盖队列：`20260520-resume-26` 最后一条补齐，以及 `20260520-resume-27` 至 `20260520-resume-35`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260520-resume-*`
- 本次快照范围：`seq 27040-36040`
- 本次新增落盘处理：361 条
- 成功转写：300 条
- 低文本：61 条
- 队列预筛新增短音频/损坏素材跳过：250 条

夜间转写概况：

- `resume-27`、`resume-33`、`resume-34`、`resume-35` 均为 40/40 成功
- `resume-28` 为 39 条成功、1 条低文本
- `resume-29` 为 38 条成功、2 条低文本
- `resume-30` 为 25 条成功、15 条低文本
- `resume-31` 为 15 条成功、25 条低文本
- `resume-32` 为 22 条成功、18 条低文本
- 后半段队列逐步进入 18-23 年历史网课、语法/词汇课、旧托福音频和低优先级长视频；低文本主要集中在短 MP3、低语音密度素材和部分模考/练习录屏
- `resume-36` 已在白天模式后自动生成 8 条剩余候选，本次夜间同步边界暂定到 `resume-35` 完整完成

全盘累计状态：

- 可转写音视频总数：2019
- 已处理/预筛去重源文件：2011
- 成功可用转写：1526
- 低文本：212
- 时长过短或损坏素材跳过：273
- 尚未尝试：8
- 尚未成功：493

备注：本次仍只同步公开进度摘要；原始课程逐字稿、夜间队列、跳过清单和本地日志继续保留在 `knowledge_exports/`，不提交到 GitHub。

## 2026-05-21 Sync 14

- 模式：白天模式收口剩余候选
- 覆盖队列：`20260520-resume-36`
- 本地结果目录：`knowledge_exports/overnight-transcription/next-priority-20260520-resume-36`
- 本次快照范围：`seq 37001-37008`
- 本次新增落盘处理：8 条
- 成功转写：7 条
- 低文本：1 条
- 队列状态：`No queued candidates left`

收口概况：

- `resume-36` 是 PTE_Resources 当前扫描出的最后 8 条候选，主要为低优先级长视频和历史网课素材
- 7 条取得可用文本，1 条第三方精听课录屏为 `low_text`
- 队列生成器返回 `freshCandidateCount: 0`、`queuedCount: 0`，说明当前音视频候选已清空

全盘最终状态：

- 可转写音视频总数：2019
- 已处理/预筛去重源文件：2019
- 成功可用转写：1533
- 低文本：213
- 时长过短或损坏素材跳过：273
- 尚未尝试：0
- 尚未成功：486

备注：PTE_Resources 当前音视频转写队列已完成一轮全量处理；后续工作重点应转向把成功转写内容蒸馏为 SunPace 自有表达的知识库条目，而不是上传或发布原始课程逐字稿。

## 2026-05-21 Knowledge Distillation 1

- 模式：白天模式，GitHub 可同步
- 输入来源：本地已完成转写池，重点参考 `resume-35`、`resume-36` 末段成功转写
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：16 条
- 覆盖主题：考场噪音与草稿纸、成绩单诊断、WE 例子与模板风险、阶段训练、听力泛听与优先级、Personal Introduction、DI 流程图、阅读 FIBR 语法与搭配判断

备注：本次仍不提交 `knowledge_exports/` 下任何第三方课程逐字稿；新增内容为改写后的公开答疑知识条目。

## 2026-05-21 Knowledge Distillation 2

- 模式：白天模式，继续按每 2 批沉淀后同步
- 输入来源：本地已完成转写池，重点参考 `resume-33`、`resume-34` 中的题型概览、基础提升、语法、发音、听力选择题与考场流程素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：16 条
- 覆盖主题：口语新题型开口时机、语法跨题型作用、听力选择题预读与排除、词根词缀、发音问题分类、成绩单总分、考场纸笔/耳机/麦克风检查、基础课训练顺序、RA 录音基线

备注：继续只提交公开知识库与进度摘要；原始逐字稿、队列与日志仍保留本地并由 `.gitignore` 忽略。

## 2026-05-21 Knowledge Distillation 3

- 模式：白天模式，恢复“每 2 轮处理同步一次 GitHub”
- 输入来源：本地已完成转写池，重点参考 `resume-27` 的 RTS/RA/阅读刷题素材，以及 `resume-30` 的阅读选择题、语法、词汇和旧课复用素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：16 条
- 覆盖主题：RTS 提示文字、RTS 作答时长、RTS 与 SGD 区别、RA 练习分数、RA 一句话模式、错音自查、阅读主旨题细节干扰、MCQ 定位策略、名词性从句、句子主干修复、旧词汇/听力课复用边界

备注：本次仍只提交公开知识库与进度摘要；没有提交 `knowledge_exports/` 下任何第三方课程逐字稿、队列、日志或跳过清单。

## 2026-05-21 Knowledge Distillation 4

- 模式：白天模式，继续“每 2 轮处理同步一次 GitHub”
- 输入来源：本地已完成转写池，重点参考 `resume-28` 的 PTE Core/口语评分/ASQ/DI/写作素材，以及 `resume-29` 的听力、精听、语法、RA 和定语从句素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：16 条
- 覆盖主题：PTE Core RS/WFD 优先级、Core 考试流程、RTS 场景边界、Core RA 准备时间、口语不回读、continuous speech、ASQ 高频刷题与低权重边界、WFD 三轮刷题、HIW 训练眼速、精听闭环、WE 三类题、写作语法准确度、主谓一致自救、定语从句先行词、DI 40 秒使用

备注：本次同步继续只包含公开进度摘要与 SunPace 自有表达的知识库内容；原始课程逐字稿、队列、结果 CSV/JSONL 和日志仍留在本地 `knowledge_exports/`。

## 2026-05-21 Knowledge Distillation 5

- 模式：白天模式，继续“每 2 轮处理同步一次 GitHub”
- 输入来源：本地已完成转写池，重点参考 `resume-28` 的 PTE Core 写邮件/RTS/阅读素材，以及 `resume-29` 的语法、听力、发音、写作素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：16 条
- 覆盖主题：PTE Core Write Email 时间与评分、RTS 三步作答、阅读泛读材料选择、阅读背景知识和时间压力、语法跨题型作用、一般现在时、HIW 倍速、Listening FIB 语法检查、主系表、口语重音、连读失爆、WE 常见低级错与高频题练习

备注：继续只提交公开知识库和进度摘要；`knowledge_exports/` 内原始逐字稿、队列、日志与结果文件不进入 GitHub。

## 2026-05-21 Knowledge Distillation 6

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-29` 的句子结构、简单句、动名词、强调句、写作和精听素材，以及 `resume-28` 的 PTE Core 写邮件/RTS 素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：16 条
- 覆盖主题：阅读长句从句拆分、引导词与谓语归属、简单句结构、宾语补足语、动名词作主语/介词宾语/固定搭配、强调句与形式主语、阅读先去修饰语、WE 长句控制、报告题练习优先级、PTE Core 邮件语气与任务点、RTS 自然表达、精听与泛听边界

备注：本轮先保留为本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`，没有进入 Git。

## 2026-05-21 Knowledge Distillation 7

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-29` 的阅读入门、长句分析、发音纠错、连读规则、强调句和 RO/FIB 素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：16 条
- 覆盖主题：阅读 MCQ 控时与多选扣分、RO/FIB 优先级、阅读先读题再通读、英文长句树状结构、英文逗号拼接错误、th 音、词尾辅音、双元音、辅音接元音连读、相同辅音连读、强调句主格与宾语/状语强调、嵌套从句拆分、RO 段落衔接、FIB 短语搭配积累

备注：本轮继续只修改公开知识库和进度摘要；不提交、不推送，也不把 `knowledge_exports/` 下原始转写产物加入 Git。

## 2026-05-21 Knowledge Distillation 8

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-29` 的听力选择题、SST 复盘、阅读入门、词法和标点定位素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：16 条
- 覆盖主题：听力 MCQ 预读题干、同义替换、音频后快速决策、否定题干、整体印象、HCS 主问题、SST 重点筛选与检查、不可数名词类型、furniture 用法、不可数可数转换、形容词顺序、后置形容词短语、阅读专有名词定位、细节题找到答案后控时、冒号/分号列表线索

备注：本轮继续只保留为本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`，等待 GitHub 权限恢复后统一提交同步。

## 2026-05-21 Knowledge Distillation 9

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-31`、`resume-32` 和 `round3-night-20260518` 中的听力讲座、RA/RS 带练和 DI 纠音素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：保险历史类 SST 结构、risk/interest/trade 因果链、讲座开头提示、列表预告笔记法、RA 复合名词重音、RA 动词重音、DI 结尾避免重复开头、DI 图表词 capacity 发音

备注：本轮继续只保留为本地公开文件修改；没有提交或推送，也没有把 `knowledge_exports/` 下原始转写产物加入 Git。

## 2026-05-21 Knowledge Distillation 10

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-32` 中的 PTE 考试结构与考试流程旧课素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：旧课 Optional Break 规则核对、考场 check-in 提前量、独立/整体计时意识、口语到写作状态切换、成绩单官方发送、考后等成绩复盘、重考间隔以官方为准、End Test 与监考确认

备注：本轮把可能过时的流程信息改写成“以官方和考场当日说明为准”的公开提醒；继续不提交、不推送，也不把 `knowledge_exports/` 下原始转写产物加入 Git。

## 2026-05-21 Knowledge Distillation 11

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-32` 的讲座型 SST 素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：thatched roof 传统工艺优点、旧工艺正向态度识别、科学实验 method/result/application、火星与月球重力对比、硬币收藏历史与价值、生物生命周期与进化逻辑、演讲声音三要素、pause 的过渡功能

备注：本轮继续只保留为本地公开文件修改；原始逐字稿、队列和日志仍留在 `knowledge_exports/`，没有提交或推送。

## 2026-05-21 Knowledge Distillation 12

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-32` 的艺术史、志愿者项目、户外安全和学生报告类讲座素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：摄影是否为艺术、人物传记题主题归纳、电脑艺术中技术与表达关系、志愿者项目开头识别、猛禽迁徙记录、户外安全 advice list、学生报告口吻识别、低质量音频/转写保分 triage

备注：本轮继续只保留为本地公开文件修改；不提交、不推送，也不把 `knowledge_exports/` 下原始逐字稿、队列或日志加入 Git。

## 2026-05-21 Knowledge Distillation 13

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-33` 的备考心态、阶段检测、PTE 扫盲、PTE vs IELTS 和发音基础素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：备考睡眠与状态、负面干扰控制、阶段检测查漏补缺、检测后分层复习、官方材料与界面熟悉、Academic English 正式表达、机器评分与交叉供分、元音和音节发音基础

备注：本轮继续只保留为本地公开文件修改；没有提交或推送，也没有把 `knowledge_exports/` 下原始转写产物加入 Git。

## 2026-05-21 Knowledge Distillation 14

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-33`、`resume-34`、`resume-35` 和 `resume-36` 的 DI 图表描述、口语试音、RO 排序与听力选择题技巧素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 纵轴横轴与单位表达、图表近似数值、项目对比句、麦克风喷麦试音词、RO 长句主干阅读、RO 最后逻辑检查、听力选择题 7 秒预读、however 转折逻辑判断

备注：本轮继续只保留为本地公开文件修改；原始逐字稿、队列和日志仍留在 `knowledge_exports/`，没有提交或推送。

## 2026-05-21 Knowledge Distillation 15

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-33` 的听力选择题、RO 排序、阅读 FIB 和 DI 数字单位素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：听力选择题 most important 题干、听力多选选项差异扫描、背景信息后的答案定位、RO 冠词新旧信息、RO 时间参照词、FIB regarded as 搭配、DI 温度单位读法、DI 年龄组读法

备注：本轮继续只保留为本地公开文件修改；没有提交或推送，也没有把 `knowledge_exports/` 下原始逐字稿、队列或日志加入 Git。

## 2026-05-21 Knowledge Distillation 16

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-33` 和 `resume-34` 的 DI 表格、RO 指代、听力 SST/FIB 与共享计时素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 表格分类 and so on、表格第一行兜底、年份 earliest/latest、RO 指示代词加名词、单独 this 的指代风险、SST 10 分钟包含音频、听力 FIB 草稿纸与词形、听力音频不能提前跳过

备注：本轮继续只保留为本地公开文件修改；原始逐字稿、队列和日志仍只保存在 `knowledge_exports/`，没有提交或推送。

## 2026-05-21 Knowledge Distillation 17

- 模式：本地继续处理；GitHub 403 未恢复前暂不新增提交
- 输入来源：本地已完成转写池，重点参考 `resume-34` 的 SST 复盘、阅读 RO、DI 图片题、RL 笔记和 WFD 复习素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SST 零散笔记成句、because/because of、because 前逗号、RO similar event 回指、DI 图片题无背景处理、RL 开头与例子/数据、WFD 试词数量、WFD 高频句意思预过

备注：本轮继续只保留为本地公开文件修改；没有提交或推送，也没有把 `knowledge_exports/` 下原始逐字稿、队列或日志加入 Git。

## 2026-05-21 Knowledge Distillation 18

- 模式：本地继续处理；当前白天模式允许每两轮同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-34` 的 SWT 写作、听力流程、阅读长句/词汇和 WFD 训练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SWT by/with 连接、听力耳机与马克笔检查、SMW beep 与全文大意、阅读段落功能题、长句插入语跳读、英英词典与搭配、阅读按题型顺序练习、WFD 有音频机经听写

备注：本轮继续只保留公开知识库和进度文档修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。当前为两轮同步周期的第 1 轮，下一轮完成后再提交并尝试推送 GitHub。

## 2026-05-21 Knowledge Distillation 19

- 模式：本地继续处理；当前白天模式允许每两轮同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-34` 的 DI 技巧、阅读 RO 和 RA/RS 口语训练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 25 秒准备清单、文字型 DI、DI 40 秒前完整收尾、RO he or she 泛指、RO apply to another field 线索、RA 生词不断流、RS 不能试词乱序、RS 50% 复述目标

备注：本轮继续只保留公开知识库和进度文档修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。本轮为两轮同步周期的第 2 轮，校验通过后提交并尝试推送 GitHub。

## 2026-05-21 Knowledge Distillation 20

- 模式：本地继续处理；当前白天模式允许每两轮同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的 WFD 精细规则、阅读统一计时/低权重题控时、RA 发音复盘和预测复盘素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WFD 缩写按原音频、首词漏听处理、WFD 原始词分与加权、WFD 英美拼写一致、阅读统一计时与混合顺序、阅读单选多选目标分控时、RA 权威发音复盘、阅读预测不要只背答案

备注：本轮继续只保留公开知识库和进度文档修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。当前为两轮同步周期的第 1 轮，下一轮完成后再提交并尝试推送 GitHub。

## 2026-05-21 Knowledge Distillation 21

- 模式：本地继续处理；当前白天模式允许每两轮同步 GitHub
- 输入来源：本地已完成转写池，继续参考 `resume-35` 的 WFD、阅读 FIB、HCS、WE 写作和学习节奏素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WFD 错词与小分关系、FIB 并列被动线索、FIB 人群名词并列、reports/editorials 语域区分、project 动词义、冠词与可数/不可数判断、HCS 听结构、WE 单边与 own experience

备注：本轮继续只保留公开知识库和进度文档修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。本轮为两轮同步周期的第 2 轮，校验通过后提交并尝试推送 GitHub。

## 2026-05-21 Knowledge Distillation 22

- 模式：本地继续处理；当前白天模式允许每两轮同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-36` 的成绩单/考后流程素材和 `resume-35` 的 RA 弱读、语调与阶段学习素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：成绩复核预期、出分延迟不等于异常、成绩单沟通分与技能画像、90 分容错、10 分不等于零、RA 弱读反哺 RS/WFD、RA 词组尾音下收、第一阶段检查点

备注：本轮继续只保留公开知识库和进度文档修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。当前为两轮同步周期的第 1 轮，下一轮完成后再提交并尝试推送 GitHub。

## 2026-05-21 Knowledge Distillation 23

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-36` 的转考/备考节奏、DI 口语、RA 语调与 WE 模板素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：备考周期按基础定、备考过长与换题风险、雅思转 PTE 先诊断、DI 不照搬雅思小作文、DI 趋势词稳定优先、RA 不做真人聊天式语调、RA ed 尾音轻收、WE 模板只是地基

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-21 Knowledge Distillation 24

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的阅读 FIB 词性/并列/语义判断素材和 `resume-36` 的 WE 模板风险素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：FIB 职业并列与 an、assembly 名词词性、ability to 接动词原形、lonely/lone/alone 区分、选大不选小、for example 反推 argue、句子缺谓语判断、WE 预背材料内容风险

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 25

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的阅读多选策略、阅读 FIB 题库/笔记方法、冒号指代、非谓语搭配和短语动词素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：80 分以下阅读多选保守策略、FIB 题库词汇/语法交错、阅读课自有笔记、以题目承载技巧、冒号 this way 指代、being presented topic、refer to as 固定搭配、diverge from 同类差异

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 26

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的阅读 FIB 下拉练习素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：并列过去式谓语、in detail 与引用线索、逗号后分词 covering、own responsibility 指向 sovereignty、cannot be overemphasized、implement/implementation 区分、although + not sufficiently 正负方向、combined 后置定语

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 27

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的阅读概览、拖拽 FIB、RA 带练和 Personal Introduction/考试流程素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：阅读 FIB 对写作分的影响、RA 对阅读交叉供分、两种阅读填空主力训练、高频命中率不能按每场一半理解、拖拽 FIB 选项可移动、拖拽 FIB 多选项缩范围、RA 预读避免看错熟词、后鼻音/舌位对 RA 清晰度的影响

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 28

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-34` 的 SWT 写作评分/连接方法和口语题型流程素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SWT 评分小项检查清单、关键词拼写与内容风险、and/but 简单连接、安全避开不熟的定语从句/同位语、SWT 预留检查时间、SWT 阅读交叉供分、RS 无 beep 时看进度条开口、口语整体计时与 Next 节奏

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 29

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-33` 的阅读精讲、口语新题型、发音突破和 DI 带练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：阅读破折号/括号解释区、反复陌生专有名词作主题标签、冒号分号列表计数、口语新题型按目标分取舍、长短元音、开口元音、DI 固定短语不断开、阶段检测防止错误方法重复

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 30

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-33` 的听力大课、Apple 听力/口语、自我介绍、DI 数字和图片描述素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：听力文段型/句子型输入、SST 未用完时间不顺延、听力选择题选项预读、备考小目标拆解、自我介绍链条、自我介绍兼麦克风检查、DI 小数百分比读法、DI 图片细节库

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 31

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-30` 的口语模板、RS 讲解、DI/RL 界面区分和考场设备/笔记板操作素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI/RL 无唯一标准答案、DI/RL 说错后继续、DI/RL 界面框数区分、试笔不写模板词、白板笔变浅及时更换、笔记板居中减少头部晃动、RS 短词可模仿长词可放弃、RS 不必复制原音频语调

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 32

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-30` 的 RS 发音/流利度讲解、DI/RL 关键词与模板使用、考场候考和试音素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RS 实词清晰输出、RS 小语法词取舍、RS something 衔接、DI/RL 关键词与连续性、DI 标题词组填充、DI 颜色方位说错继续、候考卡片口语热身、试音电流声/杂音检查

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 33

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-29` 的口语顺滑度、听力选择题、HCS/SMW 和 `resume-30` 的试音素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：麦克风自然音量、试音背景声判断、试音模板热身、口语顺滑度反哺 RS/WFD、SMW 进度条与最后一句、HCS 不边听边选、听力选择题不靠选项规律猜、五秒预读抓主题

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 34

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-29` 的 RA/RS/DI/RL 概览、RA 练习方法、HCS 选项精讲和发音连读规则素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RA/RS 少丢分策略、RS 必须听音频练、练习平台严格评分校准、RA 单句到整段循环、RA 质量优先于篇幅、HCS 近义词语义精度、the 连读模式、词尾 s 清浊处理

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 35

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-28` 的 RA 生词处理、ASQ 讲解、阅读词性训练、写作语法和 PTE Core SWT 素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RA 不用无关词替换生词、顽固错音单词单独 drill、ASQ 固定答案与可替换答案、ASQ 不确定答案小清单、阅读生词优先意思和词性、FIB be 动词后介词线索、动名词/不定式主语的主谓一致、PTE Core SWT 短词数下删修饰保主干

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 36

- 模式：夜间模式本地继续处理；不提交 GitHub、不推送、不请求权限
- 输入来源：本地已完成转写池，重点参考 `resume-27` 的 RA 下半讲、发音 day52、DI/口语刷题、WFD/SST 听力刷题和 RO 阅读排序素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：flap t 闪音、s 后爆破辅音轻化、DI 按图型准备模板模块、DI 颜色作为次级救场信息、WFD 高频句前几个词触发整句记忆、SST 缩写笔记可读性、SST 填词模板里的冠词/复数、RO 区分 as a result 与 as a result of

备注：夜间模式下，本轮只保留本地公开文件修改；原始逐字稿、队列和日志仍只在 `knowledge_exports/`。不提交、不推送、不上传 GitHub。

## 2026-05-22 Knowledge Distillation 37

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-26` 的 SST/WFD 听力刷题和 RA 口语带练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SST 至少十个内容词组、SST 纸笔笔记密度、SST 填词模板顺序弹性、SST 模板按语法水平选择、WFD 目标正确率、WFD 音频后检查、RA 吞音词组录音复盘、RA 声音从喉咙里送出来

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-22 Knowledge Distillation 38

- 模式：白天同步模式；第 37、38 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-26` 的 RO/FIB 阅读刷题、DI 图表带练和 RL 答疑素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RO 首句两个条件、RO 总分框架、RO 三分钟时间分配、阅读 FIB 第一句主题锚点、阅读交叉供分优先级、DI 复杂数字近似说、RL 开头主题锚点、RL 笔记过滤无效细节

备注：两轮新增后将执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，再只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。

## 2026-05-22 Knowledge Distillation 39

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-25` 的 WFD/SST 听力刷题素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WFD 每周错题库、WFD 简单句/难句练习遍数、WFD 试词顺序与形式、WFD 提交前检查、SST 高频开头触发熟练度、SST 按难度调整练习流程、SST 笔记强时减少模板、SST 写作前复习个人易错词

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-22 Knowledge Distillation 40

- 模式：白天同步模式；第 39、40 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-25` 的 DI/RA/RS/RO/FIB 口语和阅读刷题素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 简化模板但保留维度、DI 常见标签读音库、RA 语速不牺牲会读词、RA 后半句保持力度、RS 中段缺失后的重组、RO these 复数指代范围、FIB 下拉题上下文判断、阅读 FIB 限时核心练习

备注：两轮新增后执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，并只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。

## 2026-05-23 Knowledge Distillation 55

- 模式：白天同步模式；开始 PDF/文档素材萃取，严格执行品牌脱敏和 SunPace 自有表达
- 输入来源：本地 PDF 文档审计结果，优先使用可直接提取文本的评分、考试流程、阅读/写作/听力训练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：成绩单分项诊断、总分与小分训练用途、考前邮件与证件确认、考场签到与储物柜流程、FIB 固定搭配训练、WE 词汇搭配主动使用、RO 高频顺序材料安全用法、SST 与听力 FIB 三刷复盘

备注：本轮不发布第三方品牌名、来源机构名或原文内容；所有公开答案均改写为 SunPace 自有指导。原始 OCR、PDF 队列和审计文件继续保留在本地忽略目录或 `/private/tmp`，不会提交。

## 2026-05-23 Knowledge Distillation 56

- 模式：白天同步模式；第 55、56 两轮完成后准备 GitHub 同步
- 输入来源：本地 PDF 文档审计结果，继续使用可直接提取文本的阅读词汇、拼写、数字反应、RA 和 SST 训练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：阅读近义词按语境区分、PTE 词汇按题型拆分、英美拼写一致性、大数字三位分组反应、题型交叉评分地图、RA 高频材料迁移训练、FIBRW 生词表转做题能力、SST 思维导图先看逻辑

备注：两轮 PDF/文档萃取均已做公开品牌脱敏；仅保留 SunPace 自有指导，不提交原始 PDF 文本、OCR 队列或第三方逐字内容。

## 2026-05-23 Knowledge Distillation 57

- 模式：白天同步模式；继续 PDF/文档素材萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 PDF 文档审计结果，重点参考词根词缀、同义词辨析、官方搭配/词表和辅音发音素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：词根词缀猜词后回语境验证、词族卡片、同义词组三问、搭配表按结构记、学术词主动/被动词汇分层、RA 词尾爆破音轻收、s 后辅音不要过度送气、摩擦音气流与声带自查

备注：本轮只写入 SunPace 自有公开知识条目；来源品牌名、水印、课程名和逐字材料均不进入公开文件。

## 2026-05-23 Knowledge Distillation 58

- 模式：白天同步模式；第 57、58 两轮完成后同步 GitHub
- 输入来源：本地 PDF 文档审计结果，重点参考报考手册、PTE Core 题型概览和考生手册素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：报名邮箱管理、付款前核对证件资料、PTE Core 每日三项训练、方法型题与日练型题区分、阅读共享时间保护高价值题、听力保护 WFD、WFD 错题本记录小词、先熟悉官方题型流程再重模板

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要。

## 2026-05-23 Knowledge Distillation 59

- 模式：白天同步模式；继续 PDF/文档素材萃取，并补跑一小批本地 OCR，只保留 SunPace 自有表达
- 输入来源：本地 PDF 文档审计结果、可直接提取的题型练习材料，以及新生成的本地 OCR 小批次摘要
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：题型技巧按模块使用、口语离线练习录音复盘、听力只放一遍时先抓结构、离线练习与真实界面时间差、阅读离线错题分类、RO 与 FIB 同块训练、听力 FIB 词表按拼写和词族整理、刷题前先看评分项
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单保留在 ignored `knowledge_exports/`，不会提交

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 60

- 模式：白天同步模式；第 59、60 两轮完成后同步 GitHub
- 输入来源：本地 PDF 文档审计结果、写作连接词、FIB 语法信号、听力 FIB、SST 和 RO 训练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：连接词按功能记、不要堆叠连接词、FIB 中 due to/because 结构判断、条件句时态信号、听力 FIB 播放前预测词性、听力 FIB 错题分类、SST 用主题加关键细节、RO 先找代词/因果/例子链

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 61

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 3 的 3 个候选，以及前序 PDF/文档审计结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RA 四层练习、RA 高频材料迁移、RA 陌生词恢复、RA 连读不吞词、阅读易混词语境判断、易混词小卡片、FIB 固定搭配从错题积累、介词作为 FIB 信号
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 62

- 模式：白天同步模式；第 61、62 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、阅读 FIB 固定搭配素材、阅读易混词素材、RL/DI 口语词汇处理素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：FIB 原因结果搭配、整块识别 role/part 结构、known 后介词差异、表格清单类熟词精确含义、数量词可数不可数线索、RL 话题分支图、DI/RL 专有名词处理、阅读词汇长期和短期策略

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 63

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 6 的 3 个候选，以及前序 PDF/文档审计结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SST 逻辑速刷不能代替刷题、SST 话题库框架、SST 中文理逻辑后转英文、SST 范文后置复盘、RS 话题分类、RS 先切结构、RS 翻译只做意思锚点、RS 话题词预热
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 64

- 模式：白天同步模式；第 63、64 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、SST 逻辑复盘素材、RS 话题分类素材、FIBRW 生词难词和搭配素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：FIBRW 按题目场景整理生词、词汇卡四要素、长期备考和短期冲刺策略、专有名词作为背景线索、学术动词库、主题簇复习、公开知识改写原则、SST/RS 话题库服务新题迁移

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 65

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 9 的 3 个候选，以及前序 PDF/文档审计结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：FIBR 速刷不是答案银行、空格词固定搭配标记、先看题目场景、中文概括后回到英文句子、SST 详细逻辑三种使用场景、SST 练习前内容预判、SST 目录只看范围、FIBR 高频题按新题标准做
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 66

- 模式：白天同步模式；第 65、66 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、FIBR 生词固定搭配素材、FIBR 速刷素材、SST 详细逻辑复盘素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：FIBR 词性栏、either/or 并列结构、动词介词整组记、文化和科学题语义框架、短语动词整体意思、多空题语义链、SST 碎片时间复习、FIBR 速刷后回到完整练习

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 67

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 12 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：FIBRW 速刷语法验证、抽象名词论证场景、FIBRW 小词、RO 顺口溜后置、RO 指代关系图、RO 标题不是答案、SST+LFIB 三刷法、SST/LFIB 关键词共用
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 68

- 模式：白天同步模式；第 67、68 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、FIBRW 速刷素材、RO 排序复盘素材、SST+LFIB 双练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SST 不完整回忆使用边界、SST 听后画思维导图、LFIB 拼写语法检查、LFIB 关键词词性、FIBRW 中文理解转英文结构、RO 先总后分、RO 例子跟观点、SST+LFIB 内容和形式分开复盘

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 69

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 15 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：ASQ 轻量复习、ASQ 短准直接回答、ASQ 常识分类、WE 题干关键词替换、WE 语言广度清楚优先、WE 按题型选结构、WE 观点表达控制、WE 利弊与解决方案搭配库
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 70

- 模式：白天同步模式；第 69、70 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、ASQ 轻量复习素材、WE 词汇表达素材、SST 关键词素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SST 关键词表使用、SST 话题关键词簇、专有名词作为标签、关键词练成句子、词性辅助 SST 笔记、WE 近义词准确优先、WE 解决方案动词库、ASQ 放在核心题型后复习

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 71

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 18 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI/RL 有效内容比例、DI/RL 自然停顿、DI 第一句主题时间、DI 先说轴线再报数、最大值不机械套用、RL 框架灵活替换、英文大数字三位分组、听数字先转阿拉伯数字
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 72

- 模式：白天同步模式；第 71、72 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、DI/RL 框架素材、数字反应训练素材、学术词汇搭配素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：小数分数同义反应、数字扫视训练、学术搭配组件记忆、搭配按词性分类、academic 词族搭配、写作搭配升级、数字训练服务 DI、学术搭配迁移到阅读 FIB

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 73

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 21 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：名词前形容词信号、副词修饰动词/形容词、to 的介词/不定式判断、be 后四类结构、情态动词后原形、FIB 先看主干还是修饰、拼写体系一致性、英美拼写后缀模式
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 74

- 模式：白天同步模式；第 73、74 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、词性搭配公式、英美拼写差异、基础语法句型素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：连系动词补语、宾语补语 be 测试、及物/不及物和被动、不定式与动名词语气、使役/感官动词结构、-ing/-ed 主被动、介词和连接词区别、only 类副词位置

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 75

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 24 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：听说读写词汇选择性学习、主动/被动词汇分层、发音与拼写绑定、词汇按主题学习、词根词缀用途、前缀三类功能、后缀词性线索、词族复习
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 76

- 模式：白天同步模式；第 75、76 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、听说读写词汇手册、基础语法参考、词根词缀素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：语法书查漏补缺、语法术语对应、从错题反推语法、词根词缀帮助拼写、生词配例句、猜词后语境验证、写作词汇可控扩大、口语词汇先会读再使用

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 77

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 27 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：爆破音清浊、爆破音轻收、s 后 p/t/k 不过度送气、摩擦音气流与声带、th 舌齿位置、基础语法接回题目、练习数据转行动、平台练习记录闭环
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 78

- 模式：白天同步模式；第 77、78 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、辅音发音资料、基础语法参考、练习平台使用素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：练习记录闭环、高频题配专项、题目搜索复盘错题、AI 反馈作第二意见、题型模块轮换、辅音录音对比、练习进度不等于分数、学习工具按任务选择

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 79

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 30 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WE 词汇广度不是堆难词、题干关键词改写、同意不同意表达、利弊题权重比较、解决方案动作和结果、阅读写作一词多义、先标词性再记意思、熟词学术语境新用法
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 80

- 模式：白天同步模式；第 79、80 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、WE 写作表达、阅读写作词表、DI 易错词表
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 易错词预热、地名国名顺口、能源环境词成组预热、单位标签发音、阅读写作词表按任务筛选、商业/科学主题分簇、WE 替换词先查搭配、词汇卡片四项

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 81

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 33 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WE 全文段落分工、段内句子功能、连接词服务逻辑、少用谚语和口语化表达、复杂句与简单句搭配、字数安全区间、拼写低容错、正式书面文体
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 82

- 模式：白天同步模式；第 81、82 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、WE 写作结构、SWT 概括样例、基础语法功能化素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：同意题开头两件事、让步段一观点三支撑、自己观点段证据链、SWT 一句话压缩影响、定语从句少而准、对比结构合并信息、因果链压主线、语法术语映射考试功能

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 83

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 36 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SWT 题库按主题分组、高频题不只背答案、先抓主角动作、优先保留因果结果、一句概括有清楚主句、避免专有名词堆积、压缩后语法检查、范文复盘抽规则
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 84

- 模式：白天同步模式；第 83、84 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、SWT 题库目录、小作文概括样例、WE 教育类写作素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：教育类 WE 两条价值线、课程设置成本收益、SWT 定语从句压缩背景、分词结构补充状态、负相关表达、多因素趋势归类、多版本资料按主题去重、提纲素材低置信处理

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 85

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 39 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SWT 目录作为主题地图、月份版本只补差异、主题广度变认知框架、目录不能替代正文训练、图表数据词、学术管理词、证据判断类词、范围边界词
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 86

- 模式：白天同步模式；第 85、86 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、SWT 题库索引、阅读写作词汇表、基础词汇素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：词族复习、熟词多义、人文科学主题分簇、文化迁移词、政策动作词、发音辅助词汇记忆、词表重复项清理、识别词和输出词分层

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 87

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 42 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：模板只能当骨架、SWT 保护主题关系、SST 关键词信息链、RL 短骨架、RL 内容和连续性优先、DI 开头定位图表、静态图按排名、线图抓方向和端点
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 88

- 模式：白天同步模式；第 87、88 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、DI/RL/SST/WE 模板类素材，以及前序写作结构素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 避免空泛结尾、一边倒 WE 两个理由、平衡式 WE 结尾判断、主体段可复用发动机、连接短语有目的、考前模板个人化、限时输出检验模板、避免来源风格外露

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 89

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 45 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：大题库目录转能力地图、版本结构漂移、按分数影响排序、RA 主题广度预热、RA 标题作为预判线索、口语按输出类型分练、阅读填空下拉和拖拽分开复盘、WFD 最后一公里
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 90

- 模式：白天同步模式；第 89、90 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、整合题库目录、题型分区和版本索引素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：编号和主题去重、按题型区块记录进度、大 PDF 先抽样、题库复盘主题标签、RA 科学社会词汇预加载、月更变化清单、整合题库不等于学习计划、题库内容入库先改写成方法

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 91

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 48 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：周预测先读更新表、预测不是考试保证、变化分成新增/回流/剔除、预测回扣核心能力、预测复习限时、新增题快速熟悉、回流题查历史错因、剔除题降优先级
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 92

- 模式：白天同步模式；第 91、92 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、周预测更新表、新题型目录和题型变化素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SGD 小组信息摘要、RTS 情境目标、RTS 礼貌和行动、WFD 高影响闭环、FIB 词性搭配筛选、RS 短时记忆链、DI 图表主题预热、预测新增与个人弱项平衡

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 93

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 51 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：题库区块扩展后更新计划、页码不能当复习锚点、题型区块大小估算训练负荷、稳定主题跨版本追踪、FIB 大区块切片、按能力模式轮换、新任务区块早期诊断、整合目录作老师复盘导航
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 94

- 模式：白天同步模式；第 93、94 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、整合题库目录、新任务区块和题型分布素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RTS/SGD 分开设评分关注点、ASQ 快速回忆、DI/RL 抽样覆盖题型、SWT/WE 分清输出目标、RO 顺序逻辑、听力填空和 HIW 音文同步、WFD 区块靠后不代表低优先级、题库增长后的删减策略

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 95

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 54 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WE 模板匹配题型、模板空位填真实论点、例子可信不硬编权威、反方观点不写稻草人、问题解决题先原因后措施、解决方案写执行主体、结尾回答题目、模板字数和时间检查
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 96

- 模式：白天同步模式；第 95、96 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、泛听训练资料、精听/泛听区分素材和发音训练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：泛听建立在精听基础上、精听分词语和句子任务、泛听抓篇章大意、SST 听写两阶段、发音少量高频练习、镜子练习修口型、IPA 作发音地图、节奏重音语调提升清晰度

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 97

- 模式：白天同步模式；继续 PDF OCR 小批处理，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 57 的 3 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：口语 65 到 79 四类卡点、元音辅音和重音、流利度停顿预算、节奏和短语组、内容缺失诊断、按音和语境记录发音扭曲、清楚高级而非追求母语化、录音按评分维度复盘
- 本地 OCR 进展：新跑 3 个 PDF OCR 候选，3 个成功；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 98

- 模式：白天同步模式；第 97、98 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、报考流程资料、考前流程清单和词汇补充素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：报名证件姓名核对、报名邮箱确认、考试用途和类型检查、考位备选、成绩发送接收方检查、正式预约前风险模考、词汇主题标签、词汇例句改成自己的句子

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 99

- 模式：白天同步模式；完成当前 PDF OCR 队列最后一个候选，并将可用内容改写为 SunPace 自有知识条目
- 输入来源：本地 PDF OCR 队列 offset 60 的 1 个候选，以及前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：听力译文放在第一次听后、看完译文后不看稿复听、译文复盘做错因图、长听力材料少量每日练、理解后跟读、讲座听力记角色动作、历史类听力抓时间线、商业风险类听力抓因果
- 本地 OCR 进展：新跑 1 个 PDF OCR 候选，1 个成功；当前 PDF OCR 队列 61 个候选已全部处理；原始 OCR 文本和结果清单继续留在 ignored `knowledge_exports/`

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 100

- 模式：白天同步模式；第 99、100 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要、双语听力复习材料、队列收尾检查和前序 PDF/OCR 结果
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：译文不是公开知识库答案、双语材料作诊断工具、双语对照看句子结构、听漏句转词汇卡、跟读录音对比、学术听力主题框架、听力材料质量检查、OCR 队列完成后收尾检查

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 101

- 模式：白天同步模式；当前 PDF OCR 队列已完成，转为从本地已完成媒体转写池继续萃取公开知识
- 输入来源：本地已完成转写池，重点参考 `resume-36` 的考试现场流程、备考周期和学习计划素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：考场可带物品确认、草稿纸板使用规划、阅读到听力切换检查、考场噪音预案、口语后按规则使用降噪工具、与工作人员沟通保持节奏、备考周期匹配基础和目标、每天学习时长按弱项分配

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 102

- 模式：白天同步模式；第 101、102 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-36` 的 RA 带练、口语节奏、雅思转考与 DI 表达素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RA 一口气短语流、虚词弱读、词尾辅音轻收不丢、语调稳定不过度上扬、先单词再句子修发音、雅思口语习惯转 PTE 调整、DI 不是雅思小作文口头版、DI 趋势词可稳定重复

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始转写、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 103

- 模式：白天同步模式；无新 raw 队列，继续从本地已完成媒体转写池萃取公开知识
- 输入来源：本地已完成转写池，重点参考 `resume-36` 的写作模板风险、听力题型贡献和备考策略素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WE 模板只是地基、模板填空位语法风险、大量背诵材料内容分风险、只抄题干关键词不等于扣题、模板配自己的论点库、听力按题型贡献排序、听力大题小题分层训练、听力小题不能直接放弃

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 104

- 模式：白天同步模式；第 103、104 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-36` 的成绩单解读、复议预期和分数诊断素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：小分项不等于总分项、成绩单看不到所有评分因素、成绩复议预期管理、出分延迟不等于成绩异常、满分不代表完全没有错、低发音分说明距离远不是零能力、先看分数模式再定方案、成绩单和答题复盘一起看

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始转写、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 105

- 模式：白天同步模式；无新 raw 队列，继续从本地已完成媒体转写池萃取公开知识
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的 WFD 格式细节、WE 例证和短篇论证素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WFD 句子长度影响可拿词数、WFD 按听到形式还原、WFD 大小写匹配、WFD 词形影响有效词、WE 短篇先保立场、WE 个人例子服务观点、不真实经历换证据角度、个人经历不写成长故事

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 106

- 模式：白天同步模式；第 105、106 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的口语开场、阅读题型识别、交叉供分诊断和阶段备考素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：Personal Introduction 不沉默开场、自我介绍建立音量基线、旧分数实验只作优先级线索、阅读低分回听 RA、阅读 FIB 可能拖写作、阅读选择题快速识别单选多选、阅读扫读要带目标、基础框架跑通后做实战检查

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始转写、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 107

- 模式：白天同步模式；无新 raw 队列，继续从本地已完成媒体转写池萃取公开知识
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的听力小题、听力填空、阅读下拉和阅读课堂复盘素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：HIW 漏点和误点风险不同、SMW 缺失可能是一组词、听力 FIB 本质是听音题、听力 FIB 要适应口音噪声、阅读下拉 FIB 最吃功夫、阅读 FIB 不能盲刷、阅读 FIB 要形成个人笔记、阅读 FIB 方法要通过题目讲透

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 108

- 模式：白天同步模式；第 107、108 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的口语题型导入、学习复盘和 DI 图表/流程图方法素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：学口语技巧前先认识题型名称、录播适合复盘不替代主动学习、提问要站在自己的分数和基础上、DI 数据图先扫标题项目单位、DI 看不懂图时用流程框架救场、DI 流程图起点按可见线索定、DI 模板核心固定但内容随图换、流程步骤数量按稳定度加

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始转写、队列、日志和第三方材料不进入 GitHub。

## 2026-05-23 Knowledge Distillation 109

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考已完成的听力流程、SST 记笔记、听力小题和听力 FIB 复盘素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：听力前休息按考场时间返回、听力后段仍有交叉评分风险、SST 前段是信息收集、SST 笔记方式匹配打字速度、听力选择题不空着交、听力多选第二选项高门槛、HCS 长选项保护音频记忆、听力 FIB 草稿转填词形核对

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-23 Knowledge Distillation 110

- 模式：白天同步模式；第 109、110 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考已完成的 RA 纠音、功能词弱读、熟词预读、练习设备检查和口语声音支撑素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RA 短主语后不硬停、功能词串轻读但保留、ed 词尾轻收、熟词预读确认词形、口语练习先查本机麦克风、纠正发音当天成组复读、声音有支撑但不喊、嘴型问题用录音和镜子一起查

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始转写、OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 111

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考已完成的阅读 FIB 语法判断、可数性、谓语数量和非谓语修正素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：可数单数名词不能裸放、可数名词复数修正、FIB 选项导致两个谓语、第二动词变非谓语、疑问词加不定式做主语、抽象名词可作不可数、相近选项比较可数性、FIB 改错先看形式再看意思

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 112

- 模式：白天同步模式；第 111、112 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和已完成流程类素材，重点参考考试账户、预约、考位、成绩发送和预约前模考检查素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：报名账户使用长期可用邮箱、报名姓名拼写顺序核对、考试账户密码提前确认、考试类型按申请要求确认、查考位留出分和补考缓冲、预约确认信息留档、发送成绩核对接收方、正式预约前做风险模考

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始转写、OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 113

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和已完成口语素材，重点参考口语评分、发音清晰度、连读节奏、嘴型和句重音训练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：口语提分先分层诊断、发音目标是清楚可懂、流利度先稳意群、失误后不回头重读、嘴型问题用镜子定位、音标对照定点纠音、连读服务清晰度、句重音优先压内容词

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 114

- 模式：白天同步模式；第 113、114 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和写作/词汇素材，重点参考 WE 结构、立场规划、反方让步、例证风险和词汇标签化素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：大作文模板只保留逻辑骨架、先定立场再开段落、反方观点只用于让步、例子要解释论点、问题解决类按原因到措施推进、段落字数控制节奏、不依赖虚构调查撑论点、词汇积累按主题和词性双标签

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 115

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和听力训练素材，重点参考精听/泛听边界、SST/HCS/MCQ/SMW 训练和译文辅助复盘素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：听力先练准确再扩大输入量、听力题分清大题和小题、SST 先听结构再写摘要、HCS 先保留音频记忆再看选项、听力选择题先看问题目的、SMW 关注结尾功能、译文只在首轮听后使用、跟读连接听力和口语

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 116

- 模式：白天同步模式；第 115、116 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和词汇/阅读/写作素材，重点参考图表词、学术词、词族、FIB 词性槽位和跨题型词汇复习素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：图表词绑定 DI 和阅读、学术词记使用场景、词族比单词清单更有用、FIB 空格先判词性槽位、写作词汇按话题成组准备、RA 预读标陌生词风险、长名词链从核心名词拆开、词汇复习跨听读写循环

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 117

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和题型更新/题库索引素材，重点参考预测材料使用、RS/WFD 句库、DI 图型分类、SGD/RTS 场景口语、阅读话题词汇和听力拼写复盘素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：预测材料只能当练习地图、临考前不要被更新列表带乱、RS 句库练记忆和语法、WFD 句库先过意思再练拼写、DI 题目列表转成图型训练、新口语任务先搭场景框架、阅读题单变成话题词汇图、HIW 和听力 FIB 连接声音和拼写

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 118

- 模式：白天同步模式；第 117、118 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和 SWT/写作素材，重点参考摘要主旨、从句控制、例子删减、译文辅助使用、语法检查和教育类论证素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SWT 先压出一句主旨、SWT 合并信息控制从句、例子只留功能不留细节、SWT 练习按话题轮换、译文辅助理解不能当答案、最后十秒检查句子完整、教育类作文避免绝对化、真题主题用于识别不是死背

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 119

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和听力 FIB/RA 素材，重点参考听力填空主旨预判、词形检查、反应速度、RA 意群、失爆、单词重音和训练顺序素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：听力 FIB 先抓主旨再等空格、高频词表用于查漏、边听边判断词形、反应速度短组训练、RA 先划意群再追求声音、RA 失爆轻处理、易错词先标重音、RA 拆解建立在读音已知上

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 120

- 模式：白天同步模式；第 119、120 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和阅读 FIB/近义词/固定搭配素材，重点参考近义词语境、介词信号、因果搭配、作用类短语、数量短语、对比信号和正式程度素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：近义词放回语境区分、FIB 固定搭配做自己的错题库、介词是搭配信号、因果搭配成组记、作用类短语看后接结构、数量短语连可数性一起判断、对比短语提示句子方向、近义词比较正式程度

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 121

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和 RS/SST 训练素材，重点参考 RS 话题分类、结构划分、翻译辅助、校园句型、SST 逻辑速刷、关键词结构化和短期复盘素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RS 按话题成组记忆、RS 先拆结构再复述、RS 翻译只辅助理解、校园句型形成听觉模板、SST 逻辑速刷只做考前复盘、SST 关键词串成结构、SST 复习方式匹配记忆习惯、备考时间短时 SST 做短循环

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 122

- 模式：白天同步模式；第 121、122 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和 FIBR/FIBRW 速刷素材，重点参考空格词功能、翻译版复习风险、固定搭配、语义语法双查、态度词、科学类搭配和指代追踪素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：FIBR 速刷建立在理解上、FIBR 空格词标功能、翻译版复习回到英文句子、固定搭配和空格一起记、FIBRW 同时过意思和语法、批判意识类文章抓态度词、科学类 FIBRW 注意动词名词搭配、政策类文章追踪 this 指代

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 123

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和 RO/SST+LFIB 复盘素材，重点参考 RO 指代链、旧新信息流、转折因果信号，以及 SST+LFIB 双练、关键词拼写和不完整素材使用边界
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RO 不脱离刷题死背顺序、RO 先找指代链、按旧信息到新信息排序、转折和因果词决定方向、SST+LFIB 双练分清目的、SST 思维导图用于回忆逻辑、SST 关键词查拼写和词性、不完整素材只用于逻辑熟悉

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 124

- 模式：白天同步模式；第 123、124 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和 DI/RL 框架、数字反应训练素材，重点参考去模板化、有效内容比例、图型匹配、RL 逻辑链、自然停顿、英文数字三位分组、小数和分数反应素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI/RL 减少无脑模板依赖、DI 有效内容比例大于套话比例、DI 先匹配图型再选表达、RL 不能只堆关键词、口语自然停顿比硬塞内容更稳、英文数字按三位一组训练、听到数字先转阿拉伯数字、小数和分数单独练反应

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 125

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和词性搭配/英美拼写素材，重点参考词性公式、冠词名词结构、副词修饰、to 后形式、be 后结构、简单句主干和拼写体系一致性素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：词性搭配用公式复盘、冠词后看名词结构、副词位置提示后面词性、to 后形式先判断、be 动词后看三种可能、简单句先找主谓宾、英美拼写保持体系一致、常见英美拼写差异成组记

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 126

- 模式：白天同步模式；第 125、126 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和 DI 词汇/WE 替换表达素材，重点参考 DI 主题词、地名读法、数字单位、WE 词汇范围、复杂句清晰度、题干改写、立场程度和优缺点权重素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 主题词按领域分组、DI 地名读法先保证稳定、DI 数字和单位一起说、WE 词汇多样性不是堆高级词、复杂句先保证清楚、作文先改写题干关键词、同意不同意有程度表达、优缺点题比较权重

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 127

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和 ASQ/SST 关键词素材，重点参考短问短答备考权重、短答案、类别化记忆、触发词反应、SST 关键词分组和词性功能标注素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：ASQ 按低权重轻量练习、ASQ 回答越短越稳、ASQ 小题库按类别记忆、ASQ 同义答案先固定一个、ASQ 数量题先抓比例和单位、ASQ 用触发词定位答案、SST 关键词先用于识别话题、SST 关键词要标注词性和功能

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 128

- 模式：白天同步模式；第 127、128 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和 SST/WE/RW 词汇素材，重点参考经济、建筑设计、领导力话题词汇链，解决方案动词搭配，优缺点表达强弱和阅读写作多义词语境判断素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SST 经济话题按链条记词、SST 建筑设计题抓文化与功能、SST 领导力话题抓定义和对比、WE 解决方案动词要和宾语匹配、WE 缺点词要区分语气、WE 优点表达要体现强弱、RW 多义词必须放回句子判断、RW 词表要做主动回忆

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 129

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和词汇/词根词缀素材，重点参考听说读写词汇分配、词性搭配、主题词群、正式度、词根词缀推断、前缀意义家族、后缀词性线索和词族扩展素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：词汇手册按题型选择学习、单词卡包含词性和搭配、阅读词汇按主题成组吸收、词汇区分正式度和使用场景、词根词缀辅助推断但不替代语境、前缀按意义家族记忆、后缀是判断词性的快捷线索、词汇扩展优先做词族链

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 130

- 模式：白天同步模式；第 129、130 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和辅音发音/DI 易错词素材，重点参考爆破音清浊与送气、词尾轻收、s 后辅音连缀、摩擦音对比、能源环境词汇、地名发音、多音节重音和 DI 词汇功能判断素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：爆破音先分清清浊和送气、词尾爆破音可轻收但不能消失、s 后的 p/t/k 不要过度送气、摩擦音训练听清清浊对比、DI 能源环境词汇按场景准备、DI 地名单独建发音清单、DI 多音节词先标重音、DI 词汇先记功能再记细释义

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 131

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和写作结构/语法表达素材，重点参考段落功能、主体段句子角色、连接词逻辑、关键词替换、固定搭配、复杂句清晰度、拼写检查和正式书面表达素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WE 每个段落先确定功能、主体段句子各司其职、连接词先看逻辑再选择、作文先替换关键词再列提纲、写作优先固定搭配而不是稀有词、复杂句必须先保证清楚、作文最后 60 秒只查拼写和形式、作文保持正式书面表达

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 132

- 模式：白天同步模式；第 131、132 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和 SWT/小作文总结素材，重点参考主题库结构预热、一句话主旨合并、连接方式跟随原文逻辑、专有名词筛选、段落功能压缩、健康社会影响、教育质量公平张力和伦理争议对比素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：SWT 主题库用于预测结构而非背答案、SWT 一句话优先合并两个主信息、SWT 连接方式跟随原文逻辑、SWT 不要被专名拖走主旨、SWT 先压缩段落功能再成句、健康社会类 SWT 抓影响对象、教育类 SWT 常抓质量与公平张力、伦理争议类 SWT 用对比框架

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 133

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和篇章泛听训练素材，重点参考精听与泛听分工、篇章主旨、SST/HCS/选择题迁移、听力小题选项干扰、SMW 结尾功能、RL/SST 输出差异、听力错题本和听写到写作迁移素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：泛听训练以前先有精听底座、篇章泛听目标是主旨不是逐词复述、SST/HCS 和选择题共享主旨训练、听力小题先保护音频印象、SMW 要听结尾功能而不是赌词、RL 和 SST 听同一段但输出不同、听力错题本分词句和篇章两栏、泛听材料要反哺写作摘要

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 134

- 模式：白天同步模式；第 133、134 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和口语评分/发音训练/报名流程素材，重点参考发音清晰度、流利度短语节奏、卡顿恢复、日常发音纠正、IPA 诊断、句子重音、账号姓名核对和报名邮箱通知素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：口语发音目标是清楚而不是装母语、流利度看节奏短语不是越快越好、口语卡顿后要顺着句子恢复、发音纠正要少量高频练、IPA 用来定位问题不是背符号、句子重音优先落在内容词上、报名账号姓名必须和证件一致、报名邮箱要能稳定接收考试通知

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 135

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和大作文框架素材，重点参考模板脚手架、观点题立场、主体段论证步骤、例子可信度、让步反驳、问题解决题原因影响方案、方案层级和结尾重述素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：作文模板只能当脚手架、观点题开头要早亮立场、主体段按论点解释例子结果推进、作文例子要可信不要硬造数据、让步段要承认再反驳、问题解决题按原因影响方案走、解决方案层级要匹配问题范围、结尾要重述理由而不是复制开头

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 136

- 模式：白天同步模式；第 135、136 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和 SWT/阅读写作词汇素材，重点参考教育体育平衡、文化课程价值与时间成本、屏幕时间相关关系、全球化原因链、图表词族、判断核实评估词汇、academic 词族和政策管理词汇流程素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：教育与体育题不要做假二选一、文化课程题抓价值和时间成本、屏幕时间题先抓相关关系、全球化类材料抓定义和原因链、graph 和 chart 要同时记名词动词、判断核实评估三类词要分清、academic 词族按身份和性质区分、政策管理词汇按流程成组记

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-24 Knowledge Distillation 137

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地 OCR 摘要和 DI/RL/SST/WE 模板素材，重点参考图表模板真实数据、图型语言匹配、线图趋势、RL 内容占位风险、RL 三点复述、SST 关键词关系、作文模板空位审题和口语模板语法清晰度素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 模板必须填真实数据、DI 图型决定表达方式、线图先说趋势再说排名、RL 模板不能替代听懂内容、RL 复述抓三点比堆五点更稳、SST 不能把关键词硬塞进模板、作文模板每个空位都要审题填充、口语模板也要避免明显语法错

备注：本轮不发布来源品牌名、课程名、路径信息或第三方逐字文本；公开答案均改写为 SunPace/Sunny 自有指导。

## 2026-05-24 Knowledge Distillation 138

- 模式：白天同步模式；第 137、138 两轮完成后同步 GitHub
- 输入来源：本地 OCR 摘要和听力译文/阅读写作词汇素材，重点参考译文核对顺序、跟读训练顺序、每日篇章听力量、校园服务讲座结构、历史概念时间线、领域标签词汇、法律政府词群和网络安全风险链素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：译文只能在听后核对使用、跟读要建立在理解之后、高分听力要有稳定篇章量、校园服务讲座抓任务和收益、历史概念讲座按时间线记、词汇表要加领域标签、法律政府词汇按权力关系记、网络安全词汇按风险链记

备注：两轮完成后执行 JSON 校验、重复 ID 检查、公开品牌敏感词扫描、Sunny 回归，并只提交公开知识库和进度摘要；原始 OCR 文本、队列、日志和第三方材料不进入 GitHub。

## 2026-05-22 Knowledge Distillation 41

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-25` 后半段的 DI/RA/WFD 口语与听力刷题素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 准备时间先定口播顺序、标签图先标签后数字、坐标/量尺范围补充、DI 有力但不尖的声音、RA 小卡顿后的心态恢复、RA 过度卷舌修正、RA 词尾语调控制、WFD 长句选择性记笔记

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-22 Knowledge Distillation 42

- 模式：白天同步模式；第 41、42 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-24` 写作精讲、阅读计时/RO/FIB 方法，以及前序口语刷题素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WE 相关词扣题、一边倒作文里的反方材料、讨论题段落功能、SWT 字数显示仍需自查、PTE 独立计时与总计时区别、阅读总计时结束不能返回、RO 按段落数控时、RO 代词两两配对

备注：两轮新增后执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，并只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。

## 2026-05-22 Knowledge Distillation 43

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-24` 的 RA/RS/SST/WFD/DI 核心技巧与带练素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RA 用 RS 跟读找节奏、RA 元音嘴型舌位、RS 长短句分层目标、RS 少量记词时用连接块保持连续、SST 内容和格式门槛、SST 优先使用原文词、WFD 五类检查、DI 混合图两边覆盖

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-22 Knowledge Distillation 44

- 模式：白天同步模式；第 43、44 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-24` 的 DI 流程图/图片题、SWT 写作技巧和阅读选择题策略素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：DI 不读 source、DI 分支流程图先排路线、DI 颜色不确定时简单处理、SWT 四步工作流、SWT 隐形信号词、SWT 分段抽核心句、SWT 不能依赖原文复制粘贴、阅读单选和多选不同策略

备注：两轮新增后执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，并只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。

## 2026-05-23 Knowledge Distillation 45

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-23` 的句子主干、从句、词性和主谓一致基础语法素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：并列句主干重组、状语从句先找主句、定语从句修饰对象、现在分词作修饰、宾语从句连接、形容词/副词修饰目标、each/every/many a 单数谓语、each of 与 they each 区分

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-23 Knowledge Distillation 46

- 模式：白天同步模式；第 45、46 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-23` 的主谓一致专项、DI 模板/信息提取和 RA/RS 交叉供分素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：none of 单复数判断、a pair of 与复数名词一致、news/physics 等形式复数实为单数、DI 视线流程预演、DI 少即是多、DI 模板熟练加内容提取、RA 意群保护阅读分、RS 实词优先

备注：两轮新增后执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，并只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。

## 2026-05-23 Knowledge Distillation 47

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-23` 的插入语、强调句、倒装句和虚拟语气语法素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：插入语与同位语删除测试、not until 强调结构、谓语动词 do/does/did 强调、地点提前代词主语不倒装、否定词提前部分倒装、only 加状语句首倒装、虚拟语气时态退格意义、过去反事实 if 判断

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-23 Knowledge Distillation 48

- 模式：白天同步模式；第 47、48 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-23` 后段与 `resume-24/25` 交叉素材中的 RA 发音/意群、PTE 口语评分和 DI 图表带练内容
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：RA 名动词重音差异、RA 重音标记到内化、RA 长主语意群停顿、口语内容分门槛、短期优先修流利度、DI 坐标轴单位范围、which is around 后接数值、DI 图例标签替代复杂颜色

备注：两轮新增后执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，并只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。

## 2026-05-23 Knowledge Distillation 49

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-23` 的 WE/SWT 写作评分、审题、句子拼接和词汇替换素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WE 复杂句安全优先、题干例子范围判断、PTE 大作文四段式、主体段双角度拆分、SWT 先拆简单句再合句、SWT 保留内容关键词、写作最后检查打字错误、very 替换为精确词

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-23 Knowledge Distillation 50

- 模式：白天同步模式；第 49、50 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-23` 的发音课、听力场景词和 DI 流程图/准备步骤素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：连读保留尾音、重弱读靠速度差、长短 i 口型区别、辅音气流与舌位、爆破音放松不喷麦、听力字母确认、DI 信息试读、流程图多步骤压缩表达

备注：两轮新增后执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，并只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。

## 2026-05-23 Knowledge Distillation 51

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-23` 的核心词性、形容词/副词、比较级和构词法基础素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：形容词三种句法位置、afraid 形容词用法、-ing/-ed 形容词区别、复合形容词连字符、比较级修饰模式、前缀改意义后缀改词性、合成词猜义、转化法按上下文判词性

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-23 Knowledge Distillation 52

- 模式：白天同步模式；第 51、52 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-23` 的动词时态、名词性从句和状语从句语法素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：主将从现、实义动词否定借 do、be going to 完整结构、现在进行时表将来、现在完成时看现在影响、形式主语 it、名词性从句替换测试、where 地点状语从句判断

备注：两轮新增后执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，并只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。

## 2026-05-23 Knowledge Distillation 53

- 模式：白天同步模式；继续本地萃取，并按“两轮一同步”节奏准备 GitHub 提交
- 输入来源：本地已完成转写池，重点参考 `resume-35` 的阅读选择题、RO 排序和 FIB 词性判断素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：阅读单选/多选图标区分、选择题先看题干关键词、阅读单选按目标控时、RO 不确定句先搁置、RO 抽象总结句判断、FIB 缺谓语识别、句子完整后找非谓语/修饰成分、FIB 主谓单复数互推

备注：本轮只写入 SunPace 自有公开知识条目；原始逐字稿、队列和日志继续留在 `knowledge_exports/`，不会提交。

## 2026-05-23 Knowledge Distillation 54

- 模式：白天同步模式；第 53、54 两轮完成后同步 GitHub
- 输入来源：本地已完成转写池，重点参考 `resume-35/36` 的 WFD、Personal Introduction、RA/RS 预测、RL/SST 泛听和写作预测使用素材
- 输出文件：`data/pte-knowledge.sunpace.json`
- 本次新增 SunPace 自有知识条目：8 条
- 覆盖主题：WFD 按听到形式写、WFD 单词格式决定有效词、自我介绍作噪音环境声音基线、RA 不能只靠预测、RS 与 WFD 一起过句子熟悉度、RL/SST 题海练听记、听力 FIB/HIW 加速训练、写作预测看思路不背全文

备注：两轮新增后执行 JSON 校验、重复 ID 检查、公开 Sunny 回归，并只提交 `data/pte-knowledge.sunpace.json` 和 `docs/pte-transcription-progress.md`。
