# Source: https://expressjs.com/en/resources/middleware.html

Title: Express middleware

URL Source: https://expressjs.com/en/resources/middleware.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Express middleware
===============

[](https://expressjs.com/ "Go to homepage")

*   [Getting started](https://expressjs.com/en/starter/installing.html)
    *   [Installing](https://expressjs.com/en/starter/installing.html)
    *   [Hello world](https://expressjs.com/en/starter/hello-world.html)
    *   [Express generator](https://expressjs.com/en/starter/generator.html)
    *   [Basic routing](https://expressjs.com/en/starter/basic-routing.html)
    *   [Static files](https://expressjs.com/en/starter/static-files.html)
    *   [More examples](https://expressjs.com/en/starter/examples.html)
    *   [FAQ](https://expressjs.com/en/starter/faq.html)

*   [Guide](https://expressjs.com/en/guide/routing.html)
    *   [Routing](https://expressjs.com/en/guide/routing.html)
    *   [Writing middleware](https://expressjs.com/en/guide/writing-middleware.html)
    *   [Using middleware](https://expressjs.com/en/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/en/guide/overriding-express-api.html)
    *   [Using template engines](https://expressjs.com/en/guide/using-template-engines.html)
    *   [Error handling](https://expressjs.com/en/guide/error-handling.html)
    *   [Debugging](https://expressjs.com/en/guide/debugging.html)
    *   [Express behind proxies](https://expressjs.com/en/guide/behind-proxies.html)
    *   [Moving to Express 4](https://expressjs.com/en/guide/migrating-4.html)
    *   [Moving to Express 5](https://expressjs.com/en/guide/migrating-5.html)
    *   [Database integration](https://expressjs.com/en/guide/database-integration.html)

*   [API reference](https://expressjs.com/en/5x/api.html)
    *   [5.x](https://expressjs.com/en/5x/api.html)
    *   [4.x](https://expressjs.com/en/4x/api.html)
    *   [3.x (deprecated)](https://expressjs.com/en/3x/api.html)
    *   [2.x (deprecated)](https://expressjs.com/2x/)

*   [Advanced topics](https://expressjs.com/en/advanced/developing-template-engines.html)
    *   [Building template engines](https://expressjs.com/en/advanced/developing-template-engines.html)
    *   [Security updates](https://expressjs.com/en/advanced/security-updates.html)
    *   [Security best practices](https://expressjs.com/en/advanced/best-practice-security.html)
    *   [Performance best practices](https://expressjs.com/en/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html)

*   [Resources](https://expressjs.com/en/resources/community.html)
    *   [Community](https://expressjs.com/en/resources/community.html)
    *   [Glossary](https://expressjs.com/en/resources/glossary.html)
    *   [Middleware](https://expressjs.com/en/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/en/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/en/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/en/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Write a Post](https://expressjs.com/en/blog/write-post.html)

*   [**English**](https://expressjs.com/en/resources/middleware.html)
*   [Français](https://expressjs.com/fr/resources/middleware.html)
*   [Deutsch](https://expressjs.com/de/resources/middleware.html)
*   [Español](https://expressjs.com/es/resources/middleware.html)
*   [Italiano](https://expressjs.com/it/resources/middleware.html)
*   [日本語](https://expressjs.com/ja/resources/middleware.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/resources/middleware.html)
*   [繁體中文](https://expressjs.com/zh-tw/resources/middleware.html)
*   [한국어](https://expressjs.com/ko/resources/middleware.html)
*   [Português](https://expressjs.com/pt-br/resources/middleware.html)

### _Middlewares_

Middlewares ►

    *   [body-parser](https://expressjs.com/resources/middleware/body-parser.html)
    *   [compression](https://expressjs.com/resources/middleware/compression.html)
    *   [connect-rid](https://expressjs.com/resources/middleware/connect-rid.html)
    *   [cookie-parser](https://expressjs.com/resources/middleware/cookie-parser.html)
    *   [cookie-session](https://expressjs.com/resources/middleware/cookie-session.html)
    *   [cors](https://expressjs.com/resources/middleware/cors.html)
    *   [errorhandler](https://expressjs.com/resources/middleware/errorhandler.html)
    *   [method-override](https://expressjs.com/resources/middleware/method-override.html)
    *   [morgan](https://expressjs.com/resources/middleware/morgan.html)
    *   [multer](https://expressjs.com/resources/middleware/multer.html)
    *   [response-time](https://expressjs.com/resources/middleware/response-time.html)
    *   [serve-favicon](https://expressjs.com/resources/middleware/serve-favicon.html)
    *   [serve-index](https://expressjs.com/resources/middleware/serve-index.html)
    *   [serve-static](https://expressjs.com/resources/middleware/serve-static.html)
    *   [session](https://expressjs.com/resources/middleware/session.html)
    *   [timeout](https://expressjs.com/resources/middleware/timeout.html)
    *   [vhost](https://expressjs.com/resources/middleware/vhost.html)

Express middleware
------------------

The Express middleware modules listed here are maintained by the [Expressjs team](https://github.com/orgs/expressjs/people).

| Middleware module | Description |
| --- | --- |
| [body-parser](https://expressjs.com/en/resources/middleware/body-parser.html) | Parse HTTP request body. |
| [compression](https://expressjs.com/en/resources/middleware/compression.html) | Compress HTTP responses. |
| [connect-rid](https://expressjs.com/en/resources/middleware/connect-rid.html) | Generate unique request ID. |
| [cookie-parser](https://expressjs.com/en/resources/middleware/cookie-parser.html) | Parse cookie header and populate ```plaintext req.cookies ``` . See also [cookies](https://github.com/jed/cookies). |
| [cookie-session](https://expressjs.com/en/resources/middleware/cookie-session.html) | Establish cookie-based sessions. |
| [cors](https://expressjs.com/en/resources/middleware/cors.html) | Enable cross-origin resource sharing (CORS) with various options. |
| [errorhandler](https://expressjs.com/en/resources/middleware/errorhandler.html) | Development error-handling/debugging. |
| [method-override](https://expressjs.com/en/resources/middleware/method-override.html) | Override HTTP methods using header. |
| [morgan](https://expressjs.com/en/resources/middleware/morgan.html) | HTTP request logger. |
| [multer](https://expressjs.com/en/resources/middleware/multer.html) | Handle multi-part form data. |
| [response-time](https://expressjs.com/en/resources/middleware/response-time.html) | Record HTTP response time. |
| [serve-favicon](https://expressjs.com/en/resources/middleware/serve-favicon.html) | Serve a favicon. |
| [serve-index](https://expressjs.com/en/resources/middleware/serve-index.html) | Serve directory listing for a given path. |
| [serve-static](https://expressjs.com/en/resources/middleware/serve-static.html) | Serve static files. |
| [session](https://expressjs.com/en/resources/middleware/session.html) | Establish server-based sessions (development only). |
| [timeout](https://expressjs.com/en/resources/middleware/timeout.html) | Set a timeout perioHTTP request processing. |
| [vhost](https://expressjs.com/en/resources/middleware/vhost.html) | Create virtual domains. |

Additional middleware modules
-----------------------------

These are some additional popular middleware modules.

Warning

This information refers to third-party sites, products, or modules that are not maintained by the Expressjs team. Listing here does not constitute an endorsement or recommendation from the Expressjs project team.

| Middleware module | Description |
| --- | --- |
| [helmet](https://github.com/helmetjs/helmet) | Helps secure your apps by setting various HTTP headers. |
| [passport](https://github.com/jaredhanson/passport) | Authentication using “strategies” such as OAuth, OpenID and many others. See [passportjs.org](https://passportjs.org/) for more information. |

[](https://expressjs.com/en/resources/middleware.html#)

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
