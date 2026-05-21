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
- `5004` 公益包 `羊驼RA提分详解.mp4`，1116 字
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

- `5033` 印度小哥改革后视频 `PTE学术英语考试更新：朗读评分取消？你需要知道什么.mp4`，4171 字
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
- 7 条取得可用文本，1 条萤火虫精听课录屏为 `low_text`
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
