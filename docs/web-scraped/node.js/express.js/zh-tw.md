# Source: https://expressjs.com/zh-tw/

Title: Express - Node.js web application framework

URL Source: https://expressjs.com/zh-tw/

Markdown Content:
Express - Node.js web application framework
===============

[](https://expressjs.com/ "Go to homepage")

*   [入門](https://expressjs.com/zh-tw/starter/installing.html)
    *   [安裝](https://expressjs.com/zh-tw/starter/installing.html)
    *   [Hello world](https://expressjs.com/zh-tw/starter/hello-world.html)
    *   [Express 產生器](https://expressjs.com/zh-tw/starter/generator.html)
    *   [基本路由](https://expressjs.com/zh-tw/starter/basic-routing.html)
    *   [靜態檔案](https://expressjs.com/zh-tw/starter/static-files.html)
    *   [More examples](https://expressjs.com/zh-tw/starter/examples.html)
    *   [常見問題 (FAQ)](https://expressjs.com/zh-tw/starter/faq.html)

*   [手冊](https://expressjs.com/zh-tw/guide/routing.html)
    *   [路由](https://expressjs.com/zh-tw/guide/routing.html)
    *   [撰寫中介軟體](https://expressjs.com/zh-tw/guide/writing-middleware.html)
    *   [使用中介軟體](https://expressjs.com/zh-tw/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/zh-tw/guide/overriding-express-api.html)
    *   [使用範本引擎](https://expressjs.com/zh-tw/guide/using-template-engines.html)
    *   [錯誤處理](https://expressjs.com/zh-tw/guide/error-handling.html)
    *   [除錯](https://expressjs.com/zh-tw/guide/debugging.html)
    *   [位於 Proxy 背後的 Express](https://expressjs.com/zh-tw/guide/behind-proxies.html)
    *   [移至 Express 4](https://expressjs.com/zh-tw/guide/migrating-4.html)
    *   [移至 Express 5](https://expressjs.com/zh-tw/guide/migrating-5.html)
    *   [資料庫整合](https://expressjs.com/zh-tw/guide/database-integration.html)

*   [API 參照](https://expressjs.com/zh-tw/5x/api.html)
    *   [5.x](https://expressjs.com/zh-tw/5x/api.html)
    *   [4.x](https://expressjs.com/zh-tw/4x/api.html)
    *   [3.x 已淘汰](https://expressjs.com/zh-tw/3x/api.html)
    *   [2.x (已淘汰）](https://expressjs.com/2x/)

*   [進階主題](https://expressjs.com/zh-tw/advanced/developing-template-engines.html)
    *   [範本引擎](https://expressjs.com/zh-tw/advanced/developing-template-engines.html)
    *   [安全更新](https://expressjs.com/zh-tw/advanced/security-updates.html)
    *   [安全最佳作法](https://expressjs.com/zh-tw/advanced/best-practice-security.html)
    *   [效能最佳作法](https://expressjs.com/zh-tw/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/zh-tw/advanced/healthcheck-graceful-shutdown.html)

*   [資源](https://expressjs.com/zh-tw/resources/community.html)
    *   [社群](https://expressjs.com/zh-tw/resources/community.html)
    *   [名詞解釋](https://expressjs.com/zh-tw/resources/glossary.html)
    *   [中介軟體](https://expressjs.com/zh-tw/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/zh-tw/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/zh-tw/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/zh-tw/support)
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
*   [中文 (简体)](https://expressjs.com/zh-cn/)
*   [**繁體中文**](https://expressjs.com/zh-tw/)
*   [한국어](https://expressjs.com/ko/)
*   [Português](https://expressjs.com/pt-br/)

This document might be outdated relative to the documentation in English. For the latest updates, please refer to the [documentation in english](https://expressjs.com/en/).

✖

Express[5.2.1](https://github.com/expressjs/express/releases)

Fast, unopinionated, minimalist web framework for [Node.js](https://nodejs.org/en/)
===================================================================================

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

Web Applications
----------------

 Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. 

APIs
----

 With a myriad of HTTP utility methods and middleware at your disposal, creating a robust API is quick and easy. 

Performance
-----------

 Express provides a thin layer of fundamental web application features, without obscuring Node.js features that you know and love. 

中介軟體
----

 Express is a lightweight and flexible routing framework with minimal core features meant to be augmented through the use of Express [middleware](https://expressjs.com/zh-tw/zh-tw/resources/middleware.html) modules. 

[](https://expressjs.com/zh-tw/#)

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
