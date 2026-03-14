# Source: https://expressjs.com/en/starter/static-files.html

Title: Serving static files in Express

URL Source: https://expressjs.com/en/starter/static-files.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Serving static files in Express
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

*   [**English**](https://expressjs.com/en/starter/static-files.html)
*   [Français](https://expressjs.com/fr/starter/static-files.html)
*   [Deutsch](https://expressjs.com/de/starter/static-files.html)
*   [Español](https://expressjs.com/es/starter/static-files.html)
*   [Italiano](https://expressjs.com/it/starter/static-files.html)
*   [日本語](https://expressjs.com/ja/starter/static-files.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/starter/static-files.html)
*   [繁體中文](https://expressjs.com/zh-tw/starter/static-files.html)
*   [한국어](https://expressjs.com/ko/starter/static-files.html)
*   [Português](https://expressjs.com/pt-br/starter/static-files.html)

Serving static files in Express
===============================

To serve static files such as images, CSS files, and JavaScript files, use the 
```plaintext
express.static
```
 built-in middleware function in Express.

The function signature is:

```
express.static(root, [options])
```

The 
```plaintext
root
```
 argument specifies the root directory from which to serve static assets. For more information on the 
```plaintext
options
```
 argument, see [express.static](https://expressjs.com/en/5x/api.html#express.static).

For example, use the following code to serve images, CSS files, and JavaScript files in a directory named 
```plaintext
public
```
:

```
app.use(express.static('public'))
```

Now, you can load the files that are in the 
```plaintext
public
```
 directory:

```
http://localhost:3000/images/kitten.jpg
http://localhost:3000/css/style.css
http://localhost:3000/js/app.js
http://localhost:3000/images/bg.png
http://localhost:3000/hello.html
```

 Express looks up the files relative to the static directory, so the name of the static directory is not part of the URL. 

To use multiple static assets directories, call the 
```plaintext
express.static
```
 middleware function multiple times:

```
app.use(express.static('public'))
app.use(express.static('files'))
```

Express looks up the files in the order in which you set the static directories with the 
```plaintext
express.static
```
 middleware function.

Note

For best results, [use a reverse proxy](https://expressjs.com/en/advanced/best-practice-performance.html#use-a-reverse-proxy) cache to improve performance of serving static assets.

To create a virtual path prefix (where the path does not actually exist in the file system) for files that are served by the 
```plaintext
express.static
```
 function, [specify a mount path](https://expressjs.com/en/5x/api.html#app.use) for the static directory, as shown below:

```
app.use('/static', express.static('public'))
```

Now, you can load the files that are in the 
```plaintext
public
```
 directory from the 
```plaintext
/static
```
 path prefix.

```
http://localhost:3000/static/images/kitten.jpg
http://localhost:3000/static/css/style.css
http://localhost:3000/static/js/app.js
http://localhost:3000/static/images/bg.png
http://localhost:3000/static/hello.html
```

However, the path that you provide to the 
```plaintext
express.static
```
 function is relative to the directory from where you launch your 
```plaintext
node
```
 process. If you run the express app from another directory, it’s safer to use the absolute path of the directory that you want to serve:

```
const path = require('path')
app.use('/static', express.static(path.join(__dirname, 'public')))
```

For more details about the 
```plaintext
serve-static
```
 function and its options, see [serve-static](https://expressjs.com/resources/middleware/serve-static.html).

[Previous: Express basic routing](https://expressjs.com/en/starter/basic-routing.html)[Next: Express examples](https://expressjs.com/en/starter/examples.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/starter/static-files.md)

[](https://expressjs.com/en/starter/static-files.html#)

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
