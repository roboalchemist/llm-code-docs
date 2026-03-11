# Source: https://expressjs.com/ko/

Title: Express - Node.js web application framework

URL Source: https://expressjs.com/ko/

Markdown Content:
Express - Node.js web application framework
===============

[](https://expressjs.com/ "Go to homepage")

*   [시작하기](https://expressjs.com/ko/starter/installing.html)
    *   [설치](https://expressjs.com/ko/starter/installing.html)
    *   [Hello world](https://expressjs.com/ko/starter/hello-world.html)
    *   [Express 생성기](https://expressjs.com/ko/starter/generator.html)
    *   [기본 라우팅](https://expressjs.com/ko/starter/basic-routing.html)
    *   [정적 파일](https://expressjs.com/ko/starter/static-files.html)
    *   [더 많은 예시](https://expressjs.com/ko/starter/examples.html)
    *   [자주 묻는 질문(FAQ)](https://expressjs.com/ko/starter/faq.html)

*   [안내서](https://expressjs.com/ko/guide/routing.html)
    *   [라우팅](https://expressjs.com/ko/guide/routing.html)
    *   [미들웨어 작성](https://expressjs.com/ko/guide/writing-middleware.html)
    *   [미들웨어 사용](https://expressjs.com/ko/guide/using-middleware.html)
    *   [Express API 오버라이딩](https://expressjs.com/ko/guide/overriding-express-api.html)
    *   [템플리트 엔진 사용](https://expressjs.com/ko/guide/using-template-engines.html)
    *   [오류 처리](https://expressjs.com/ko/guide/error-handling.html)
    *   [디버깅](https://expressjs.com/ko/guide/debugging.html)
    *   [프록시 환경에서 Express 사용](https://expressjs.com/ko/guide/behind-proxies.html)
    *   [Express 4로의 이전](https://expressjs.com/ko/guide/migrating-4.html)
    *   [Express 5로의 이전](https://expressjs.com/ko/guide/migrating-5.html)
    *   [데이터베이스 통합](https://expressjs.com/ko/guide/database-integration.html)

*   [API 참조](https://expressjs.com/ko/5x/api.html)
    *   [5.x](https://expressjs.com/ko/5x/api.html)
    *   [4.x](https://expressjs.com/ko/4x/api.html)
    *   [3.x(더 이상 사용되지 않음)](https://expressjs.com/ko/3x/api.html)
    *   [2.x(더 이상 사용되지 않음)](https://expressjs.com/2x/)

*   [고급 주제](https://expressjs.com/ko/advanced/developing-template-engines.html)
    *   [템플리트 엔진](https://expressjs.com/ko/advanced/developing-template-engines.html)
    *   [보안 업데이트](https://expressjs.com/ko/advanced/security-updates.html)
    *   [보안 우수 사례](https://expressjs.com/ko/advanced/best-practice-security.html)
    *   [성능 우수 사례](https://expressjs.com/ko/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/ko/advanced/healthcheck-graceful-shutdown.html)

*   [자원](https://expressjs.com/ko/resources/community.html)
    *   [커뮤니티](https://expressjs.com/ko/resources/community.html)
    *   [용어집](https://expressjs.com/ko/resources/glossary.html)
    *   [미들웨어](https://expressjs.com/ko/resources/middleware.html)
    *   [유틸리티 모듈](https://expressjs.com/ko/resources/utils.html)
    *   [Express에 기여하기](https://expressjs.com/ko/resources/contributing.html)
    *   [릴리즈 변경 로그](https://github.com/expressjs/express/releases)

*   [지원](https://expressjs.com/ko/support)
*   [블로그](https://expressjs.com/2026/02/27/security-releases.html)
    *   [최신 게시물](https://expressjs.com/2026/02/27/security-releases.html)
    *   [모든 게시물](https://expressjs.com/en/blog/posts.html)
    *   [게시물 작성](https://expressjs.com/en/blog/write-post.html)

*   [English](https://expressjs.com/en/)
*   [Français](https://expressjs.com/fr/)
*   [Deutsch](https://expressjs.com/de/)
*   [Español](https://expressjs.com/es/)
*   [Italiano](https://expressjs.com/it/)
*   [日本語](https://expressjs.com/ja/)
*   [中文 (简体)](https://expressjs.com/zh-cn/)
*   [繁體中文](https://expressjs.com/zh-tw/)
*   [**한국어**](https://expressjs.com/ko/)
*   [Português](https://expressjs.com/pt-br/)

이 문서는 영어 문서에 비해 최신 정보가 아닐 수 있습니다. 최신 내용을 확인하려면 아래의 영어 문서를 참고해 주시기 바랍니다 [영어로 된 문서](https://expressjs.com/en/).

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

*   Express@5.1.0: npm에서 기본 버전으로 채택, LTS 일정 함께 도입됨

이제 Express 5.1.0이 npm에서 기본 버전이 되었으며, v4와 v5 릴리스 라인에 대해 공식적인 LTS 일정도 도입했습니다. [자세한 내용은 최신 블로그를 확인해보세요.](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Web Applications
----------------

 Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. 

APIs
----

 With a myriad of HTTP utility methods and middleware at your disposal, creating a robust API is quick and easy. 

Performance
-----------

 Express provides a thin layer of fundamental web application features, without obscuring Node.js features that you know and love. 

미들웨어
----

 Express is a lightweight and flexible routing framework with minimal core features meant to be augmented through the use of Express [middleware](https://expressjs.com/ko/ko/resources/middleware.html) modules. 

[](https://expressjs.com/ko/#)

[](https://openjsf.org/ "OpenJS Foundation")
Copyright [OpenJS Foundation](https://openjsf.org/) and Express contributors. All rights reserved. The [OpenJS Foundation](https://openjsf.org/) has registered trademarks and uses trademarks. For a list of trademarks of the [OpenJS Foundation](https://openjsf.org/), please see our [Trademark Policy](https://trademark-policy.openjsf.org/) and [Trademark List](https://trademark-list.openjsf.org/). Trademarks and logos not indicated on the [list of OpenJS Foundation trademarks](https://trademark-list.openjsf.org/) are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.

[이용 약관](https://terms-of-use.openjsf.org/)[개인정보보호정책](https://privacy-policy.openjsf.org/)[운영 규정](https://github.com/expressjs/.github/blob/HEAD/CODE_OF_CONDUCT.md)[상표 정책](https://trademark-policy.openjsf.org/)[보안 정책](https://github.com/expressjs/express/security/policy)

[](https://github.com/expressjs/express)

[](https://www.youtube.com/channel/UCYjxjAeH6TRik9Iwy5nXw7g)

[](https://x.com/UseExpressJS)

[](https://openjs-foundation.slack.com/archives/C02QB1731FH)

[](https://opencollective.com/express)

[](https://bsky.app/profile/expressjs.bsky.social)

[![Image 1: Preview Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
