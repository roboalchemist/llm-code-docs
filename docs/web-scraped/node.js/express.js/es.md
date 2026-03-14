# Source: https://expressjs.com/es/

Title: Express - Node.js Marco de aplicación web

URL Source: https://expressjs.com/es/

Markdown Content:
Express - Node.js Marco de aplicación web
===============

[](https://expressjs.com/ "Go to homepage")

*   [Cómo empezar](https://expressjs.com/es/starter/installing.html)
    *   [Instalando](https://expressjs.com/es/starter/installing.html)
    *   [Hola mundo](https://expressjs.com/es/starter/hello-world.html)
    *   [Generador express](https://expressjs.com/es/starter/generator.html)
    *   [Direccionamiento básico](https://expressjs.com/es/starter/basic-routing.html)
    *   [Archivos estáticos](https://expressjs.com/es/starter/static-files.html)
    *   [Más ejemplos](https://expressjs.com/es/starter/examples.html)
    *   [FAQ](https://expressjs.com/es/starter/faq.html)

*   [Guía](https://expressjs.com/es/guide/routing.html)
    *   [Direccionamiento](https://expressjs.com/es/guide/routing.html)
    *   [Escritura de middleware](https://expressjs.com/es/guide/writing-middleware.html)
    *   [Utilización del middleware](https://expressjs.com/es/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/es/guide/overriding-express-api.html)
    *   [Utilización de motores de plantilla](https://expressjs.com/es/guide/using-template-engines.html)
    *   [Manejo de errores](https://expressjs.com/es/guide/error-handling.html)
    *   [Depuración](https://expressjs.com/es/guide/debugging.html)
    *   [Express detrás de proxies](https://expressjs.com/es/guide/behind-proxies.html)
    *   [Migración a Express 4](https://expressjs.com/es/guide/migrating-4.html)
    *   [Migración a Express 5](https://expressjs.com/es/guide/migrating-5.html)
    *   [Integración de la base de datos](https://expressjs.com/es/guide/database-integration.html)

*   [Referencia de API](https://expressjs.com/es/5x/api.html)
    *   [5.x](https://expressjs.com/es/5x/api.html)
    *   [4.x](https://expressjs.com/es/4x/api.html)
    *   [3.x (obsoleto)](https://expressjs.com/es/3x/api.html)
    *   [2.x (obsoleto)](https://expressjs.com/2x/)

*   [Temas avanzados](https://expressjs.com/es/advanced/developing-template-engines.html)
    *   [Motores de plantilla](https://expressjs.com/es/advanced/developing-template-engines.html)
    *   [Actualizaciones de seguridad](https://expressjs.com/es/advanced/security-updates.html)
    *   [Mejores prácticas de seguridad](https://expressjs.com/es/advanced/best-practice-security.html)
    *   [Mejores prácticas de rendimiento](https://expressjs.com/es/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/es/advanced/healthcheck-graceful-shutdown.html)

*   [Recursos](https://expressjs.com/es/resources/community.html)
    *   [Comunidad](https://expressjs.com/es/resources/community.html)
    *   [Glosario](https://expressjs.com/es/resources/glossary.html)
    *   [Middleware](https://expressjs.com/es/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/es/resources/utils.html)
    *   [Contribuir a Express](https://expressjs.com/es/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Soporte](https://expressjs.com/es/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Escribir un post](https://expressjs.com/en/blog/write-post.html)

*   [English](https://expressjs.com/en/)
*   [Français](https://expressjs.com/fr/)
*   [Deutsch](https://expressjs.com/de/)
*   [**Español**](https://expressjs.com/es/)
*   [Italiano](https://expressjs.com/it/)
*   [日本語](https://expressjs.com/ja/)
*   [中文 (简体)](https://expressjs.com/zh-cn/)
*   [繁體中文](https://expressjs.com/zh-tw/)
*   [한국어](https://expressjs.com/ko/)
*   [Português](https://expressjs.com/pt-br/)

Este documento puede estar desactualizado en relación con la documentación en inglés. Para las últimas actualizaciones, por favor consulte la [documentación en inglés](https://expressjs.com/en/).

✖

Express[5.2.1](https://github.com/expressjs/express/releases)

Marco web rápido, sin opinión y minimalista para [Node.js](https://nodejs.org/en/)
==================================================================================

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

*   Express@5.1.0: Ahora la versión por defecto en npm con cronograma LTS

Express 5.1.0 es ahora es la versión predeterminada en npm, y estamos introduciendo un cronograma oficial de LTS para las líneas de lanzamiento v4 y v5. [Mira nuestro último blog para más información.](https://expressjs.com/2025/03/31/v5-1-latest-release.html)

Aplicaciones web
----------------

 Express es un minimalista y flexible framework de aplicaciones web de Node.js que provee un conjunto robusto de características para aplicaciones web y móviles

APIs
----

 Con una gran cantidad de métodos de utilidad HTTP y middleware a tu disposición, crear una API robusta es rápido y fácil. 

Rendimiento
-----------

 Express proporciona una capa delgada de características fundamentales de la aplicación web, sin ocultar las características de Node.js que usted conoce y ama. 

Middleware
----------

 Express es un marco de enrutamiento ligero y flexible con las características básicas mínimas destinado a aumentarse mediante el uso de módulos [middleware](https://expressjs.com/es/es/resources/middleware.html). 

[](https://expressjs.com/es/#)

[](https://openjsf.org/ "OpenJS Foundation")
Copyright [OpenJS Foundation](https://openjsf.org/) and Express contributors. All rights reserved. The [OpenJS Foundation](https://openjsf.org/) has registered trademarks and uses trademarks. For a list of trademarks of the [OpenJS Foundation](https://openjsf.org/), please see our [Trademark Policy](https://trademark-policy.openjsf.org/) and [Trademark List](https://trademark-list.openjsf.org/). Trademarks and logos not indicated on the [list of OpenJS Foundation trademarks](https://trademark-list.openjsf.org/) are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.

[Condiciones de uso](https://terms-of-use.openjsf.org/)[Política de privacidad](https://privacy-policy.openjsf.org/)[Código de conducta](https://github.com/expressjs/.github/blob/HEAD/CODE_OF_CONDUCT.md)[Política de marcas registradas](https://trademark-policy.openjsf.org/)[Política de seguridad](https://github.com/expressjs/express/security/policy)

[](https://github.com/expressjs/express)

[](https://www.youtube.com/channel/UCYjxjAeH6TRik9Iwy5nXw7g)

[](https://x.com/UseExpressJS)

[](https://openjs-foundation.slack.com/archives/C02QB1731FH)

[](https://opencollective.com/express)

[](https://bsky.app/profile/expressjs.bsky.social)

[![Image 1: Preview Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
