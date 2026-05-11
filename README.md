# SunPace 官网新增模块版本

这个目录是基于当前线上首页整理出的 Netlify 静态站版本，已加入：

- 首页“大事纪”模块
- 首页“线下活动预告”模块
- Sunny PTE 问答面板
- Netlify Function：`/api/sunny-chat`
- 本地课程知识库示例：`data/pte-knowledge.json`
- Sunny 问答限流：默认每个 IP 每 60 秒最多 6 次请求
- Sunny 可接 OpenAI Vector Store 托管知识库

## 更新课程库

把淘宝购买的 PTE 精品课程资料整理成 JSON 条目，追加到 `data/pte-knowledge.json`。建议每条包含：

```json
{
  "id": "unique-id",
  "title": "题型或知识点标题",
  "keywords": ["PTE", "RA", "口语"],
  "answer": "Sunny 可以直接回答给学生看的内容"
}
```

建议只放你有权用于官网服务的内容，不要整段复制受版权保护的课程原文。

如果要把 Mac mini 上的完整课程资料同步给 Sunny，推荐使用 OpenAI Vector Store，详细流程见：

`docs/sunny-knowledge-pipeline.md`

## 修改首页内容

首页内容在 `index.html`。

- 大事纪：搜索 `修改大事纪内容`
- 线下活动预告：搜索 `修改线下活动预告`

新增一条大事纪时，复制一整块 `timeline-item`；新增一条活动时，复制一整块 `event-card`。每块里的标题、日期、地点、标签和说明文字都可以直接替换。

## 页面路径

这个版本已经包含：

- 首页：`index.html`
- 关于我们：`about/index.html`
- 预定教材：`order/index.html`

## Sunny 访问限制

Sunny 后端函数在 `netlify/functions/sunny-chat.mjs`。

当前设置：

```js
export const config = {
  path: '/api/sunny-chat',
  rateLimit: {
    windowLimit: 6,
    windowSize: 60,
    aggregateBy: ['ip', 'domain']
  }
};
```

含义：同一个 IP 在 60 秒内最多提问 6 次，超过后 Netlify 会返回 429，前端会提示用户稍等一分钟。

这个限制适合控制“同一个人连续狂点”。如果后续接入真正的大模型，建议再加一个云端总量控制，例如：

- Netlify 企业版 High-Performance Edge 的全域限流
- Upstash Redis / Cloudflare KV / Supabase 这类云端计数器
- AI 服务商后台的每日预算和每分钟调用上限

不要把 Sunny 后端跑在本地电脑上；正式访问应全部走 Netlify Functions 或其他云端服务。

如果在 Netlify 设置了 `OPENAI_API_KEY` 和 `OPENAI_VECTOR_STORE_ID`，Sunny 会优先使用 OpenAI 托管知识库；否则使用 `data/pte-knowledge.json` 作为兜底。

## 部署

完整 MVP 部署流程见：

`docs/mvp-deployment-guide.md`

如果这个目录作为 Netlify 站点根目录，构建设置可以保持为空：

- Publish directory: `.`
- Functions directory: `netlify/functions`

推荐部署方式：

1. Git 部署：把整个 `sunpace-site` 目录推到 GitHub，再在 Netlify 连接仓库。
2. Netlify CLI 部署：在这个目录下执行 `netlify deploy --prod`。

说明：我可以提供压缩包，但如果只用 Netlify 网页拖拽上传，静态页面通常没问题，Sunny 的 Netlify Function 可能不会按预期构建。要让 Sunny 问答稳定生效，推荐 Git 或 Netlify CLI。

也可以把 `index.html`、`about/`、`order/`、`data/`、`netlify/` 和 `netlify.toml` 合并到现有官网仓库。
