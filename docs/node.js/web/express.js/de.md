# Source: https://expressjs.com/de/

Title: Express - Node.js Web Application Framework

URL Source: https://expressjs.com/de/

Markdown Content:
Express - Node.js Web Application Framework
===============

[](https://expressjs.com/ "Go to homepage")

*   [Einführung](https://expressjs.com/de/starter/installing.html)
    *   [Installation](https://expressjs.com/de/starter/installing.html)
    *   [Hello world](https://expressjs.com/de/starter/hello-world.html)
    *   [Express generator](https://expressjs.com/de/starter/generator.html)
    *   [Basisrouting](https://expressjs.com/de/starter/basic-routing.html)
    *   [Statische Dateien](https://expressjs.com/de/starter/static-files.html)
    *   [Weitere Beispiele](https://expressjs.com/de/starter/examples.html)
    *   [Häufig gestellte Fragen](https://expressjs.com/de/starter/faq.html)

*   [Leitfaden](https://expressjs.com/de/guide/routing.html)
    *   [Weiterleitung (Routing)](https://expressjs.com/de/guide/routing.html)
    *   [Middleware schreiben](https://expressjs.com/de/guide/writing-middleware.html)
    *   [Middleware verwenden](https://expressjs.com/de/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/de/guide/overriding-express-api.html)
    *   [Template-Engines verwenden](https://expressjs.com/de/guide/using-template-engines.html)
    *   [Fehlerbehandlung](https://expressjs.com/de/guide/error-handling.html)
    *   [Debugging](https://expressjs.com/de/guide/debugging.html)
    *   [Express hinter Proxys](https://expressjs.com/de/guide/behind-proxies.html)
    *   [Wechsel zu Express 4](https://expressjs.com/de/guide/migrating-4.html)
    *   [Wechsel zu Express 5](https://expressjs.com/de/guide/migrating-5.html)
    *   [Datenbankintegration](https://expressjs.com/de/guide/database-integration.html)

*   [API-Referenz](https://expressjs.com/de/5x/api.html)
    *   [5.x](https://expressjs.com/de/5x/api.html)
    *   [4.x](https://expressjs.com/de/4x/api.html)
    *   [3.x (veraltet)](https://expressjs.com/de/3x/api.html)
    *   [2.x (veraltet)](https://expressjs.com/2x/)

*   [Themen für Fortgeschrittene](https://expressjs.com/de/advanced/developing-template-engines.html)
    *   [Template-Engines](https://expressjs.com/de/advanced/developing-template-engines.html)
    *   [Sicherheitsupdates](https://expressjs.com/de/advanced/security-updates.html)
    *   [Sicherheitsspezifische Best Practices](https://expressjs.com/de/advanced/best-practice-security.html)
    *   [Leistungsspezifische Best Practices](https://expressjs.com/de/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/de/advanced/healthcheck-graceful-shutdown.html)

*   [Ressourcen](https://expressjs.com/de/resources/community.html)
    *   [Community](https://expressjs.com/de/resources/community.html)
    *   [Glossar](https://expressjs.com/de/resources/glossary.html)
    *   [Middleware](https://expressjs.com/de/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/de/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/de/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/de/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Write a Post](https://expressjs.com/en/blog/write-post.html)

*   [English](https://expressjs.com/en/)
*   [Français](https://expressjs.com/fr/)
*   [**Deutsch**](https://expressjs.com/de/)
*   [Español](https://expressjs.com/es/)
*   [Italiano](https://expressjs.com/it/)
*   [日本語](https://expressjs.com/ja/)
*   [中文 (简体)](https://expressjs.com/zh-cn/)
*   [繁體中文](https://expressjs.com/zh-tw/)
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

 Express ist ein minimalistisches und flexibles Node.js Web Application Framework, das eine robustes Reihe an Funktionen für Web- und mobile Anwendungen bereitstellt. 

APIs
----

 With a myriad of HTTP utility methods and middleware at your disposal, creating a robust API is quick and easy. 

Performance
-----------

 Express provides a thin layer of fundamental web application features, without obscuring Node.js features that you know and love. 

Middleware
----------

 Express is a lightweight and flexible routing framework with minimal core features meant to be augmented through the use of Express [middleware](https://expressjs.com/de/de/resources/middleware.html) modules. 

[](https://expressjs.com/de/#)

[](https://openjsf.org/ "OpenJS Foundation")
Copyright [OpenJS Foundation](https://openjsf.org/) and Express contributors. All rights reserved. The [OpenJS Foundation](https://openjsf.org/) has registered trademarks and uses trademarks. For a list of trademarks of the [OpenJS Foundation](https://openjsf.org/), please see our [Trademark Policy](https://trademark-policy.openjsf.org/) and [Trademark List](https://trademark-list.openjsf.org/). Trademarks and logos not indicated on the [list of OpenJS Foundation trademarks](https://trademark-list.openjsf.org/) are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.

[Nutzungsbedingungen](https://terms-of-use.openjsf.org/)[Datenschutzerklärung](https://privacy-policy.openjsf.org/)[Verhaltenskodex](https://github.com/expressjs/.github/blob/HEAD/CODE_OF_CONDUCT.md)[Trademark Policy](https://trademark-policy.openjsf.org/)[Security Policy](https://github.com/expressjs/express/security/policy)

[](https://github.com/expressjs/express)

[](https://www.youtube.com/channel/UCYjxjAeH6TRik9Iwy5nXw7g)

[](https://x.com/UseExpressJS)

[](https://openjs-foundation.slack.com/archives/C02QB1731FH)

[](https://opencollective.com/express)

[](https://bsky.app/profile/expressjs.bsky.social)

[![Image 1: Preview Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
