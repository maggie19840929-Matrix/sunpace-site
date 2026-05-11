# SunPace 官网 MVP 部署手册

目标：先上线一个稳定可用的 MVP 版本，让首页、关于我们、预定教材、大事纪、线下活动预告和 Sunny 基础问答可以正常访问。完整课程知识库、AI 回答、全站限流和缓存后续逐步打开。

## MVP 包含什么

当前 MVP 已包含：

- 首页：`index.html`
- 关于我们：`about/index.html`
- 预定教材：`order/index.html`
- 图片资源：logo、Sunny、企业微信二维码
- 大事纪模块
- 线下活动预告模块
- 大事纪 / 活动预告快速编辑器：`/admin/`
- Sunny 对话窗口
- Sunny 基础问答后端：`netlify/functions/sunny-chat.mjs`
- Sunny 本地兜底知识库：`data/pte-knowledge.json`
- 每个 IP 每 60 秒最多 6 次 Sunny 请求

MVP 暂不强依赖 OpenAI API。即使不配置 OpenAI 环境变量，Sunny 也会使用 `data/pte-knowledge.json` 返回基础答案。

## 推荐部署方式

推荐用 GitHub + Netlify 自动部署。

不建议只用 Netlify 网页拖拽压缩包作为长期方式，因为 Sunny 用到了 Netlify Functions。拖拽适合纯静态页面，函数构建和后续维护不如 Git 部署稳定。

## 第一步：准备项目文件

项目目录是：

`sunpace-site`

压缩包是：

`sunpace-site-netlify-root.zip`

如果使用 GitHub，建议把 `sunpace-site` 目录里的内容作为仓库根目录。仓库根目录打开后应该能直接看到：

- `index.html`
- `about/`
- `order/`
- `data/`
- `docs/`
- `admin/`
- `netlify/`
- `netlify.toml`
- `README.md`
- 图片文件

注意：不要让仓库结构变成 `你的仓库/sunpace-site/index.html`，否则 Netlify 的发布目录要额外调整。MVP 最省事的结构是 `index.html` 就在仓库根目录。

## 第二步：创建 GitHub 仓库

1. 登录 GitHub。
2. 创建一个新仓库，例如 `sunpace-site`。
3. 把 `sunpace-site` 目录里的所有文件上传到这个仓库。
4. 确认 GitHub 仓库首页能看到 `index.html` 和 `netlify.toml`。

如果你已经有原官网仓库，也可以把这些文件合并进去，但建议先开一个新分支或新仓库测试，不要直接覆盖线上站。

## 第三步：在 Netlify 新建或连接站点

推荐先建一个新的测试站点，不要一开始就覆盖 `sunpace.cn`。

1. 登录 Netlify。
2. 进入 Add new project。
3. 选择 Import an existing project。
4. 选择 GitHub。
5. 选择刚才的仓库。
6. 构建设置：
   - Build command：留空
   - Publish directory：`.`
   - Functions directory：`netlify/functions`
7. 点击 Deploy。

部署成功后，Netlify 会给你一个临时域名，例如：

`https://xxxx.netlify.app`

先用这个临时域名完整测试，不急着绑定正式域名。

## 第四步：测试 MVP 页面

部署成功后，依次打开：

- `/`
- `/about/`
- `/order/`

检查：

- 首页是否正常显示。
- 顶部导航是否能进入关于我们和预定教材。
- 大事纪模块是否显示。
- 线下活动预告是否显示。
- 企业微信二维码是否显示。
- 右下角 Sunny 按钮是否显示。

## 第五步：测试 Sunny 基础问答

在首页右下角打开 Sunny，输入：

`PTE 口语 RA 怎么提分？`

正常情况：

- Sunny 会返回 RA / DI 相关建议。
- 这个阶段不需要 OpenAI API。
- 答案来自 `data/pte-knowledge.json`。

如果 Sunny 提示“没有连上后台课程库”，或者浏览器请求失败，重点检查：

1. Netlify 是否真的部署了 Functions。
2. 请求路径 `/api/sunny-chat` 是否能访问。
3. 是否用了拖拽部署导致函数没有构建。

## 第六步：确认限流

当前函数里有这个配置：

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

含义：

- 同一个 IP
- 60 秒内
- 最多请求 6 次 Sunny
- 超过后 Netlify 返回 429

这是 MVP 的第一层保护，主要防止同一个访客连续狂点。

## 第七步：绑定正式域名

等临时域名测试没有问题后，再处理正式域名。

如果 `sunpace.cn` 现在已经在 Netlify 上：

1. 先确认当前线上站点是否需要保留。
2. 在 Netlify 里找到现有站点。
3. 可以把 GitHub 仓库连接到现有站点，或用 CLI 部署到现有站点。
4. 部署前先确认 Deploy Preview 没问题。
5. 再发布到 Production。

如果要把新站绑定到 `sunpace.cn`：

1. 进入 Netlify 项目 Domain settings。
2. Add custom domain。
3. 添加 `sunpace.cn` 和 `www.sunpace.cn`。
4. 按 Netlify 提示调整 DNS。
5. 等待 HTTPS 证书自动签发。

正式切换前，建议先在 Netlify 临时域名上测试完全部流程。

## 第八步：后续接入 OpenAI 课程知识库

MVP 跑稳定后，再接 OpenAI Vector Store。

需要在 Netlify 设置环境变量：

- `OPENAI_API_KEY`
- `OPENAI_VECTOR_STORE_ID`
- `OPENAI_MODEL`

建议 `OPENAI_MODEL` 先填：

`gpt-5-mini`

设置完环境变量后，重新部署。Sunny 会自动优先查 OpenAI Vector Store；如果没配置，就继续使用 `data/pte-knowledge.json`。

课程知识库整理和同步流程见：

`docs/sunny-knowledge-pipeline.md`

## 第九步：MVP 后逐步放开的功能

第一阶段：当前 MVP

- 静态官网
- 大事纪
- 活动预告
- Sunny 基础问答
- 每 IP 限流

第二阶段：课程库增强

- Mac mini 整理课程文件
- 上传 OpenAI Vector Store
- Sunny 使用课程库回答
- 保留 JSON 兜底

第三阶段：流量保护

- 设置 OpenAI 预算上限
- 增加全站共享限流，例如 Upstash Redis
- 增加常见问题缓存
- 高峰期引导用户添加企业微信

第四阶段：运营后台

- 当前已有轻量编辑器 `/admin/`
- 后续可升级成带登录的 CMS 管理
- Sunny 问题记录到表格或数据库
- 顾问可以查看高频问题

## 快速修改大事纪和活动预告

当前 MVP 已有一个轻量编辑器：

`/admin/`

使用方式：

1. 打开 Netlify 临时域名或正式域名后面的 `/admin/`。
2. 修改大事纪或线下活动预告。
3. 点击“下载 site-content.json”。
4. 到 GitHub 仓库打开 `data/site-content.json`。
5. 点击编辑或上传替换文件。
6. Commit changes。
7. Netlify 会自动重新部署。

注意：这个编辑器不会直接写入服务器。它的作用是帮你生成正确格式的 JSON 文件。真正上线生效，仍然需要把 JSON 文件提交到 GitHub。

## 常见问题

### 只上传 zip 可以吗？

纯静态页面可以，但 Sunny 后端函数不建议依赖拖拽 zip 部署。MVP 想让 Sunny 可用，推荐 GitHub + Netlify，或 Netlify CLI。

### 会不会吃 Mac mini 性能？

不会。正式访问走 Netlify 和 OpenAI。Mac mini 只负责整理课程资料和上传知识库。

### 不接 OpenAI 可以先上线吗？

可以。当前 MVP 会用 `data/pte-knowledge.json` 作为 Sunny 的基础答案库。

### 什么时候接 OpenAI？

等首页、关于我们、预定教材、活动预告和 Sunny 基础问答都稳定后再接。建议不要第一天就把所有功能都打开。
