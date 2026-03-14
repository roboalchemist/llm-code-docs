# Source: https://expressjs.com/ja/

Title: Express - Node.js web application framework

URL Source: https://expressjs.com/ja/

Markdown Content:
Express - Node.js web application framework
===============

[](https://expressjs.com/ "Go to homepage")

*   [概説](https://expressjs.com/ja/starter/installing.html)
    *   [インストール](https://expressjs.com/ja/starter/installing.html)
    *   [Hello world](https://expressjs.com/ja/starter/hello-world.html)
    *   [Express ジェネレーター](https://expressjs.com/ja/starter/generator.html)
    *   [基本的なルーティング](https://expressjs.com/ja/starter/basic-routing.html)
    *   [静的ファイル](https://expressjs.com/ja/starter/static-files.html)
    *   [More examples](https://expressjs.com/ja/starter/examples.html)
    *   [FAQ](https://expressjs.com/ja/starter/faq.html)

*   [ガイド](https://expressjs.com/ja/guide/routing.html)
    *   [ルーティング](https://expressjs.com/ja/guide/routing.html)
    *   [ミドルウェアの作成](https://expressjs.com/ja/guide/writing-middleware.html)
    *   [ミドルウェアの使用](https://expressjs.com/ja/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/ja/guide/overriding-express-api.html)
    *   [テンプレート・エンジンの使用](https://expressjs.com/ja/guide/using-template-engines.html)
    *   [エラー処理](https://expressjs.com/ja/guide/error-handling.html)
    *   [デバッグ](https://expressjs.com/ja/guide/debugging.html)
    *   [プロキシーの背後の Express](https://expressjs.com/ja/guide/behind-proxies.html)
    *   [Express 4 への移行](https://expressjs.com/ja/guide/migrating-4.html)
    *   [Express 5 への移行](https://expressjs.com/ja/guide/migrating-5.html)
    *   [データベースの統合](https://expressjs.com/ja/guide/database-integration.html)

*   [API リファレンス](https://expressjs.com/ja/5x/api.html)
    *   [5.x](https://expressjs.com/ja/5x/api.html)
    *   [4.x](https://expressjs.com/ja/4x/api.html)
    *   [3.x (非推奨)](https://expressjs.com/ja/3x/api.html)
    *   [2.x (非推奨)](https://expressjs.com/2x/)

*   [高度なトピック](https://expressjs.com/ja/advanced/developing-template-engines.html)
    *   [テンプレート・エンジン](https://expressjs.com/ja/advanced/developing-template-engines.html)
    *   [セキュリティー更新](https://expressjs.com/ja/advanced/security-updates.html)
    *   [セキュリティーに関するベスト・プラクティス](https://expressjs.com/ja/advanced/best-practice-security.html)
    *   [パフォーマンスに関するベスト・プラクティス](https://expressjs.com/ja/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/ja/advanced/healthcheck-graceful-shutdown.html)

*   [リソース](https://expressjs.com/ja/resources/community.html)
    *   [コミュニティー](https://expressjs.com/ja/resources/community.html)
    *   [用語集](https://expressjs.com/ja/resources/glossary.html)
    *   [ミドルウェア](https://expressjs.com/ja/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/ja/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/ja/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/ja/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Write a Post](https://expressjs.com/en/blog/write-post.html)

*   [English](https://expressjs.com/en/)
*   [Français](https://expressjs.com/fr/)
*   [Deutsch](https://expressjs.com/de/)
*   [Español](https://expressjs.com/es/)
*   [Italiano](https://expressjs.com/it/)
*   [**日本語**](https://expressjs.com/ja/)
*   [中文 (简体)](https://expressjs.com/zh-cn/)
*   [繁體中文](https://expressjs.com/zh-tw/)
*   [한국어](https://expressjs.com/ko/)
*   [Português](https://expressjs.com/pt-br/)

このドキュメントは英語のドキュメントに比べて古くなっている可能性があります。最新情報については、 [英語のドキュメントを参照してください](https://expressjs.com/en/).

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

*   Express@5.1.0: LTSタイムラインでnpmのデフォルトになりました

Express 5.1.0 が npm のデフォルトとなり、v4 および v5 リリース ラインの公式 LTS スケジュールが導入されます。[詳細については、最新のブログをご覧ください。](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Web Applications
----------------

 Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. 

APIs
----

 With a myriad of HTTP utility methods and middleware at your disposal, creating a robust API is quick and easy. 

Performance
-----------

 Express provides a thin layer of fundamental web application features, without obscuring Node.js features that you know and love. 

ミドルウェア
------

 Express is a lightweight and flexible routing framework with minimal core features meant to be augmented through the use of Express [middleware](https://expressjs.com/ja/ja/resources/middleware.html) modules. 

[](https://expressjs.com/ja/#)

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
