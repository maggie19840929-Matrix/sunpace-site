# Sunny 课程知识库同步方案

目标：Mac mini 只做课程资料整理和上传，不承接官网用户访问。官网用户提问时，Sunny 运行在 Netlify Functions，通过 OpenAI 托管的向量知识库检索课程内容。

## 推荐架构

1. 课程资料放在 Mac mini 本地。
2. Mac mini 定期把课程资料整理成可上传文件，例如 `.txt`、`.md`、`.pdf`、`.docx`。
3. 上传到 OpenAI Vector Store。
4. 在 Netlify 设置环境变量：
   - `OPENAI_API_KEY`
   - `OPENAI_VECTOR_STORE_ID`
   - `OPENAI_MODEL`，建议先用 `gpt-5-mini`
5. 官网访客问 Sunny 时，请求只到 Netlify 和 OpenAI，不会访问 Mac mini。

## 可上传资料格式

优先建议整理成：

- `.txt`
- `.md`
- `.pdf`
- `.docx`

如果课程是视频或音频，先转写成文字，再上传文字稿。不要直接把整套未经授权的课程原文公开到网页前端。

## 课程整理建议

每个文件建议只放一个主题：

- `pte-speaking-ra.md`
- `pte-speaking-di.md`
- `pte-writing-we.md`
- `pte-listening-wfd.md`
- `pte-study-plan-58-65.md`
- `pte-campus-bootcamp.md`

每个文件开头建议写清楚：

```md
# PTE Read Aloud 提分方法

适用人群：PTE 50-65 分段
关联题型：RA, Repeat Sentence, Describe Image
课程来源：内部课程整理

## 核心方法
...
```

## 上传到 OpenAI Vector Store

可以用 OpenAI 官方后台或 API 创建 Vector Store，并上传课程文件。上传后记录 Vector Store ID，形如 `vs_...`。

然后在 Netlify 项目里添加环境变量：

- Key: `OPENAI_API_KEY`
- Value: 你的 OpenAI API Key

- Key: `OPENAI_VECTOR_STORE_ID`
- Value: 你的 Vector Store ID

- Key: `OPENAI_MODEL`
- Value: `gpt-5-mini`

保存后重新部署 Netlify。

## Sunny 当前逻辑

Sunny 后端函数在：

`netlify/functions/sunny-chat.mjs`

逻辑顺序：

1. 如果 Netlify 配了 `OPENAI_API_KEY` 和 `OPENAI_VECTOR_STORE_ID`，优先查 OpenAI Vector Store。
2. 如果没有配置，使用 `data/pte-knowledge.json` 作为本地兜底知识库。
3. 同一个 IP 每 60 秒最多 6 次请求，超过后 Netlify 返回 429。

## 瓶颈在哪里

不会在 Mac mini。

主要瓶颈会在：

- Netlify Functions 的调用次数和并发能力
- OpenAI API 的每分钟请求数、每分钟 token 数和账户预算
- Vector Store 文件体积和检索成本
- 如果活动推广带来突发流量，需要全站级限流

## 大流量时的增强方案

基础版：

- 保留当前每 IP 限流
- 在 OpenAI 平台设置用量预算
- Sunny 回答控制在 500 tokens 内

进阶版：

- 用 Upstash Redis 做全站共享限流，例如全站每分钟最多 100 次 Sunny 请求
- 对常见问题做缓存，例如“58 到 65 怎么备考”直接返回缓存答案
- 高峰期把 Sunny 切成表单收集模式，引导用户加企业微信

企业版：

- 使用 Netlify High-Performance Edge 的 per-domain 全域限流
- 单独接 API Gateway 或 Cloudflare Workers 做总闸门

## 版权提醒

如果课程来自淘宝购买，请确认你有权把内容用于企业官网服务。建议上传“内部整理版”“知识点总结版”和“答疑版”，不要把课程原文、讲义全文或付费资料直接暴露给访客。

