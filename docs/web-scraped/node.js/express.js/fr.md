# Source: https://expressjs.com/fr/

Title: Express - Node.js web application framework

URL Source: https://expressjs.com/fr/

Markdown Content:
Express - Node.js web application framework
===============

[](https://expressjs.com/ "Go to homepage")

*   [Mise en route](https://expressjs.com/fr/starter/installing.html)
    *   [Installation](https://expressjs.com/fr/starter/installing.html)
    *   [Hello world](https://expressjs.com/fr/starter/hello-world.html)
    *   [Générateur Express](https://expressjs.com/fr/starter/generator.html)
    *   [Routage de base](https://expressjs.com/fr/starter/basic-routing.html)
    *   [Fichiers statiques](https://expressjs.com/fr/starter/static-files.html)
    *   [More examples](https://expressjs.com/fr/starter/examples.html)
    *   [FAQ](https://expressjs.com/fr/starter/faq.html)

*   [Guide](https://expressjs.com/fr/guide/routing.html)
    *   [Routage](https://expressjs.com/fr/guide/routing.html)
    *   [Ecriture de middleware](https://expressjs.com/fr/guide/writing-middleware.html)
    *   [Utilisation de middleware](https://expressjs.com/fr/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/fr/guide/overriding-express-api.html)
    *   [Utilisation de moteurs de modèles](https://expressjs.com/fr/guide/using-template-engines.html)
    *   [Traitement d'erreurs](https://expressjs.com/fr/guide/error-handling.html)
    *   [Débogage](https://expressjs.com/fr/guide/debugging.html)
    *   [Express derrière Proxys](https://expressjs.com/fr/guide/behind-proxies.html)
    *   [Migration vers Express 4](https://expressjs.com/fr/guide/migrating-4.html)
    *   [Migration vers Express 5](https://expressjs.com/fr/guide/migrating-5.html)
    *   [Intégration de bases de données](https://expressjs.com/fr/guide/database-integration.html)

*   [API reference](https://expressjs.com/fr/5x/api.html)
    *   [5.x](https://expressjs.com/fr/5x/api.html)
    *   [4.x](https://expressjs.com/fr/4x/api.html)
    *   [3.x (obsolète)](https://expressjs.com/fr/3x/api.html)
    *   [2.x (obsolète)](https://expressjs.com/2x/)

*   [Rubriques avancées](https://expressjs.com/fr/advanced/developing-template-engines.html)
    *   [Moteurs de modèles](https://expressjs.com/fr/advanced/developing-template-engines.html)
    *   [Mises à jour de sécurité](https://expressjs.com/fr/advanced/security-updates.html)
    *   [Meilleures pratiques en termes de sécurité](https://expressjs.com/fr/advanced/best-practice-security.html)
    *   [Meilleures pratiques en termes de performances](https://expressjs.com/fr/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/fr/advanced/healthcheck-graceful-shutdown.html)

*   [Ressources](https://expressjs.com/fr/resources/community.html)
    *   [Communauté](https://expressjs.com/fr/resources/community.html)
    *   [Glossaire](https://expressjs.com/fr/resources/glossary.html)
    *   [Middleware](https://expressjs.com/fr/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/fr/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/fr/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/fr/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Write a Post](https://expressjs.com/en/blog/write-post.html)

*   [English](https://expressjs.com/en/)
*   [**Français**](https://expressjs.com/fr/)
*   [Deutsch](https://expressjs.com/de/)
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

 Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. 

APIs
----

 With a myriad of HTTP utility methods and middleware at your disposal, creating a robust API is quick and easy. 

Performance
-----------

 Express provides a thin layer of fundamental web application features, without obscuring Node.js features that you know and love. 

Middleware
----------

 Express is a lightweight and flexible routing framework with minimal core features meant to be augmented through the use of Express [middleware](https://expressjs.com/fr/fr/resources/middleware.html) modules. 

[](https://expressjs.com/fr/#)

[](https://openjsf.org/ "OpenJS Foundation")
Copyright [OpenJS Foundation](https://openjsf.org/) and Express contributors. All rights reserved. The [OpenJS Foundation](https://openjsf.org/) has registered trademarks and uses trademarks. For a list of trademarks of the [OpenJS Foundation](https://openjsf.org/), please see our [Trademark Policy](https://trademark-policy.openjsf.org/) and [Trademark List](https://trademark-list.openjsf.org/). Trademarks and logos not indicated on the [list of OpenJS Foundation trademarks](https://trademark-list.openjsf.org/) are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.

[Conditions d’utilisation](https://terms-of-use.openjsf.org/)[Politique de Confidentialité](https://privacy-policy.openjsf.org/)[Code de Conduite](https://github.com/expressjs/.github/blob/HEAD/CODE_OF_CONDUCT.md)[Politique de Marque](https://trademark-policy.openjsf.org/)[Politique de Sécurité](https://github.com/expressjs/express/security/policy)

[](https://github.com/expressjs/express)

[](https://www.youtube.com/channel/UCYjxjAeH6TRik9Iwy5nXw7g)

[](https://x.com/UseExpressJS)

[](https://openjs-foundation.slack.com/archives/C02QB1731FH)

[](https://opencollective.com/express)

[](https://bsky.app/profile/expressjs.bsky.social)

[![Image 1: Preview Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
