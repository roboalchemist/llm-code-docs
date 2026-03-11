# Source: https://expressjs.com/it/

Title: Express - Node.js web application framework

URL Source: https://expressjs.com/it/

Markdown Content:
Express - Node.js web application framework
===============

[](https://expressjs.com/ "Go to homepage")

*   [Introduzione](https://expressjs.com/it/starter/installing.html)
    *   [Installazione](https://expressjs.com/it/starter/installing.html)
    *   [Hello world](https://expressjs.com/it/starter/hello-world.html)
    *   [Programma di creazione Express](https://expressjs.com/it/starter/generator.html)
    *   [Routing di base](https://expressjs.com/it/starter/basic-routing.html)
    *   [File statici](https://expressjs.com/it/starter/static-files.html)
    *   [More examples](https://expressjs.com/it/starter/examples.html)
    *   [FAQ](https://expressjs.com/it/starter/faq.html)

*   [Guide](https://expressjs.com/it/guide/routing.html)
    *   [Routing](https://expressjs.com/it/guide/routing.html)
    *   [Scrittura del middleware](https://expressjs.com/it/guide/writing-middleware.html)
    *   [Utilizzo del middleware](https://expressjs.com/it/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/it/guide/overriding-express-api.html)
    *   [Utilizzo dei motori di template](https://expressjs.com/it/guide/using-template-engines.html)
    *   [Gestione degli errori](https://expressjs.com/it/guide/error-handling.html)
    *   [Debugging](https://expressjs.com/it/guide/debugging.html)
    *   [Express con i proxy](https://expressjs.com/it/guide/behind-proxies.html)
    *   [Passaggio a Express 4](https://expressjs.com/it/guide/migrating-4.html)
    *   [Passaggio a Express 5](https://expressjs.com/it/guide/migrating-5.html)
    *   [Integrazione database](https://expressjs.com/it/guide/database-integration.html)

*   [Riferimento API](https://expressjs.com/it/5x/api.html)
    *   [5.x](https://expressjs.com/it/5x/api.html)
    *   [4.x](https://expressjs.com/it/4x/api.html)
    *   [3.x (deprecato)](https://expressjs.com/it/3x/api.html)
    *   [2.x (deprecato)](https://expressjs.com/2x/)

*   [Argomenti avanzati](https://expressjs.com/it/advanced/developing-template-engines.html)
    *   [Motori di template](https://expressjs.com/it/advanced/developing-template-engines.html)
    *   [Aggiornamenti sulla sicurezza](https://expressjs.com/it/advanced/security-updates.html)
    *   [Best practice sulla sicurezza](https://expressjs.com/it/advanced/best-practice-security.html)
    *   [Best practice sulle prestazioni](https://expressjs.com/it/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/it/advanced/healthcheck-graceful-shutdown.html)

*   [Risorse](https://expressjs.com/it/resources/community.html)
    *   [Community](https://expressjs.com/it/resources/community.html)
    *   [Glossario](https://expressjs.com/it/resources/glossary.html)
    *   [Middleware](https://expressjs.com/it/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/it/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/it/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/it/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Write a Post](https://expressjs.com/en/blog/write-post.html)

*   [English](https://expressjs.com/en/)
*   [Français](https://expressjs.com/fr/)
*   [Deutsch](https://expressjs.com/de/)
*   [Español](https://expressjs.com/es/)
*   [**Italiano**](https://expressjs.com/it/)
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

 Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. 

APIs
----

 With a myriad of HTTP utility methods and middleware at your disposal, creating a robust API is quick and easy. 

Performance
-----------

 Express provides a thin layer of fundamental web application features, without obscuring Node.js features that you know and love. 

Middleware
----------

 Express is a lightweight and flexible routing framework with minimal core features meant to be augmented through the use of Express [middleware](https://expressjs.com/it/it/resources/middleware.html) modules. 

[](https://expressjs.com/it/#)

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
