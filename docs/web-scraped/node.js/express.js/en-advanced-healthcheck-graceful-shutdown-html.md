# Source: https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html

Title: Health Checks and Graceful Shutdown

URL Source: https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html

Markdown Content:
Health Checks and Graceful Shutdown
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

*   [**English**](https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html)
*   [Français](https://expressjs.com/fr/advanced/healthcheck-graceful-shutdown.html)
*   [Deutsch](https://expressjs.com/de/advanced/healthcheck-graceful-shutdown.html)
*   [Español](https://expressjs.com/es/advanced/healthcheck-graceful-shutdown.html)
*   [Italiano](https://expressjs.com/it/advanced/healthcheck-graceful-shutdown.html)
*   [日本語](https://expressjs.com/ja/advanced/healthcheck-graceful-shutdown.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/advanced/healthcheck-graceful-shutdown.html)
*   [繁體中文](https://expressjs.com/zh-tw/advanced/healthcheck-graceful-shutdown.html)
*   [한국어](https://expressjs.com/ko/advanced/healthcheck-graceful-shutdown.html)
*   [Português](https://expressjs.com/pt-br/advanced/healthcheck-graceful-shutdown.html)

Health Checks and Graceful Shutdown
===================================

Graceful shutdown
-----------------

When you deploy a new version of your application, you must replace the previous version. The process manager you’re using will first send a SIGTERM signal to the application to notify it that it will be killed. Once the application gets this signal, it should stop accepting new requests, finish all the ongoing requests, clean up the resources it used, including database connections and file locks then exit.

### Example

```
const server = app.listen(port)

process.on('SIGTERM', () => {
  debug('SIGTERM signal received: closing HTTP server')
  server.close(() => {
    debug('HTTP server closed')
  })
})
```

Health checks
-------------

A load balancer uses health checks to determine if an application instance is healthy and can accept requests. For example, [Kubernetes has two health checks](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/):

*   ```plaintext
liveness
```
, that determines when to restart a container.
*   ```plaintext
readiness
```
, that determines when a container is ready to start accepting traffic. When a pod is not ready, it is removed from the service load balancers.

[Previous: Performance Best Practices Using Express in Production](https://expressjs.com/en/advanced/best-practice-performance.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/advanced/healthcheck-graceful-shutdown.md)

[](https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html#)

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
