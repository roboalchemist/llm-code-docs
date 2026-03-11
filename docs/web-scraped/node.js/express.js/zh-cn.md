# Source: https://expressjs.com/zh-cn/

Title: Express - Node.js web 应用框架

URL Source: https://expressjs.com/zh-cn/

Markdown Content:
Express - Node.js web 应用框架
===============

[](https://expressjs.com/ "Go to homepage")

*   [入门](https://expressjs.com/zh-cn/starter/installing.html)
    *   [安装](https://expressjs.com/zh-cn/starter/installing.html)
    *   [Hello world](https://expressjs.com/zh-cn/starter/hello-world.html)
    *   [Express 生成器](https://expressjs.com/zh-cn/starter/generator.html)
    *   [基本路由](https://expressjs.com/zh-cn/starter/basic-routing.html)
    *   [静态文件](https://expressjs.com/zh-cn/starter/static-files.html)
    *   [More examples](https://expressjs.com/zh-cn/starter/examples.html)
    *   [常见问题及解答](https://expressjs.com/zh-cn/starter/faq.html)

*   [指南](https://expressjs.com/zh-cn/guide/routing.html)
    *   [路由](https://expressjs.com/zh-cn/guide/routing.html)
    *   [编写中间件](https://expressjs.com/zh-cn/guide/writing-middleware.html)
    *   [使用中间件](https://expressjs.com/zh-cn/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/zh-cn/guide/overriding-express-api.html)
    *   [使用模板引擎](https://expressjs.com/zh-cn/guide/using-template-engines.html)
    *   [错误处理](https://expressjs.com/zh-cn/guide/error-handling.html)
    *   [调试](https://expressjs.com/zh-cn/guide/debugging.html)
    *   [代理背后的 Express](https://expressjs.com/zh-cn/guide/behind-proxies.html)
    *   [迁移到 Express 4](https://expressjs.com/zh-cn/guide/migrating-4.html)
    *   [迁移到 Express 5](https://expressjs.com/zh-cn/guide/migrating-5.html)
    *   [数据库集成](https://expressjs.com/zh-cn/guide/database-integration.html)

*   [API 参考](https://expressjs.com/zh-cn/5x/api.html)
    *   [5.x](https://expressjs.com/zh-cn/5x/api.html)
    *   [4.x](https://expressjs.com/zh-cn/4x/api.html)
    *   [3.x (不推荐）](https://expressjs.com/zh-cn/3x/api.html)
    *   [2.x (不推荐）](https://expressjs.com/2x/)

*   [高级主题](https://expressjs.com/zh-cn/advanced/developing-template-engines.html)
    *   [模板引擎](https://expressjs.com/zh-cn/advanced/developing-template-engines.html)
    *   [安全更新](https://expressjs.com/zh-cn/advanced/security-updates.html)
    *   [安全最佳实践](https://expressjs.com/zh-cn/advanced/best-practice-security.html)
    *   [性能最佳实践](https://expressjs.com/zh-cn/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/zh-cn/advanced/healthcheck-graceful-shutdown.html)

*   [资源](https://expressjs.com/zh-cn/resources/community.html)
    *   [社区](https://expressjs.com/zh-cn/resources/community.html)
    *   [词汇表](https://expressjs.com/zh-cn/resources/glossary.html)
    *   [中间件](https://expressjs.com/zh-cn/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/zh-cn/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/zh-cn/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/zh-cn/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Write a Post](https://expressjs.com/en/blog/write-post.html)

*   [English](https://expressjs.com/en/)
*   [Français](https://expressjs.com/fr/)
*   [Deutsch](https://expressjs.com/de/)
*   [Español](https://expressjs.com/es/)
*   [Italiano](https://expressjs.com/it/)
*   [日本語](https://expressjs.com/ja/)
*   [**中文 (简体)**](https://expressjs.com/zh-cn/)
*   [繁體中文](https://expressjs.com/zh-tw/)
*   [한국어](https://expressjs.com/ko/)
*   [Português](https://expressjs.com/pt-br/)

This document might be outdated relative to the documentation in English. For the latest updates, please refer to the [documentation in english](https://expressjs.com/en/).

✖

Express[5.2.1](https://github.com/expressjs/express/releases)

快速、灵活、极简的 [Node.js](https://nodejs.org/en/) Web 框架
==================================================

`$ npm install express --save`

```
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```

*   Express@5.1.0: Now the Default on npm with LTS Timeline

Express 5.1.0 is now the default on npm, and we’re introducing an official LTS schedule for the v4 and v5 release lines. [Check out our latest blog for more information.](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Web 应用开发
--------

 Express 是一个简洁灵活的 Node.js Web 应用框架，为网页和移动应用提供了一套强大的功能特性。 

API 开发
------

 借助丰富的 HTTP 工具方法和中间件支持，快速构建健壮的 API 接口易如反掌。 

性能表现
----

 Express 提供基础的 Web 应用功能薄层封装，绝不遮蔽您熟悉且喜爱的原生 Node.js 特性。 

中间件
---

 Express是一个轻量和灵活的路由框架，核心功能最小， 将通过使用Express [中间件](https://expressjs.com/zh-cn/zh-cn/resources/middleware.html) 模块来增加。 

[](https://expressjs.com/zh-cn/#)

[](https://openjsf.org/ "OpenJS Foundation")
Copyright [OpenJS Foundation](https://openjsf.org/) and Express contributors. All rights reserved. The [OpenJS Foundation](https://openjsf.org/) has registered trademarks and uses trademarks. For a list of trademarks of the [OpenJS Foundation](https://openjsf.org/), please see our [Trademark Policy](https://trademark-policy.openjsf.org/) and [Trademark List](https://trademark-list.openjsf.org/). Trademarks and logos not indicated on the [list of OpenJS Foundation trademarks](https://trademark-list.openjsf.org/) are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.

[Terms of Use](https://terms-of-use.openjsf.org/)[Privacy Policy](https://privacy-policy.openjsf.org/)[Code of Conduct](https://github.com/expressjs/.github/blob/HEAD/CODE_OF_CONDUCT.md)[Trademark Policy](https://trademark-policy.openjsf.org/)[Security Policy](https://github.com/expressjs/express/security/policy)

[](https://github.com/expressjs/express)

[](https://www.youtube.com/channel/UCYjxjAeH6TRik9Iwy5nXw7g)

[](https://x.com/UseExpressJS)

[](https://openjs-foundation.slack.com/archives/C02QB1731FH)

[](https://opencollective.com/express)

[](https://bsky.app/profile/expressjs.bsky.social)

[![Image 1: Preview Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
