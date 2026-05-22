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
