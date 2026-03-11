# Source: https://expressjs.com/en/starter/basic-routing.html

Title: Express basic routing

URL Source: https://expressjs.com/en/starter/basic-routing.html

Markdown Content:
Express basic routing
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

*   [**English**](https://expressjs.com/en/starter/basic-routing.html)
*   [Français](https://expressjs.com/fr/starter/basic-routing.html)
*   [Deutsch](https://expressjs.com/de/starter/basic-routing.html)
*   [Español](https://expressjs.com/es/starter/basic-routing.html)
*   [Italiano](https://expressjs.com/it/starter/basic-routing.html)
*   [日本語](https://expressjs.com/ja/starter/basic-routing.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/starter/basic-routing.html)
*   [繁體中文](https://expressjs.com/zh-tw/starter/basic-routing.html)
*   [한국어](https://expressjs.com/ko/starter/basic-routing.html)
*   [Português](https://expressjs.com/pt-br/starter/basic-routing.html)

Basic routing
=============

_Routing_ refers to determining how an application responds to a client request to a particular endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).

Each route can have one or more handler functions, which are executed when the route is matched.

Route definition takes the following structure:

```
app.METHOD(PATH, HANDLER)
```

Where:

*   ```plaintext
app
```
 is an instance of 
```plaintext
express
```
.
*   ```plaintext
METHOD
```
 is an [HTTP request method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods), in lowercase.
*   ```plaintext
PATH
```
 is a path on the server.
*   ```plaintext
HANDLER
```
 is the function executed when the route is matched.

This tutorial assumes that an instance of 
```plaintext
express
```
 named 
```plaintext
app
```
 is created and the server is running. If you are not familiar with creating an app and starting it, see the [Hello world example](https://expressjs.com/en/starter/hello-world.html).

The following examples illustrate defining simple routes.

Respond with 
```plaintext
Hello World!
```
 on the homepage:

```
app.get('/', (req, res) => {
  res.send('Hello World!')
})
```

Respond to a POST request on the root route (
```plaintext
/
```
), the application’s home page:

```
app.post('/', (req, res) => {
  res.send('Got a POST request')
})
```

Respond to a PUT request to the 
```plaintext
/user
```
 route:

```
app.put('/user', (req, res) => {
  res.send('Got a PUT request at /user')
})
```

Respond to a DELETE request to the 
```plaintext
/user
```
 route:

```
app.delete('/user', (req, res) => {
  res.send('Got a DELETE request at /user')
})
```

For more details about routing, see the [routing guide](https://expressjs.com/en/guide/routing.html).

[Previous: Express application generator](https://expressjs.com/en/starter/generator.html)[Next: Serving static files in Express](https://expressjs.com/en/starter/static-files.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/starter/basic-routing.md)

[](https://expressjs.com/en/starter/basic-routing.html#)

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
