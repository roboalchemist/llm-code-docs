# Source: https://expressjs.com/en/guide/migrating-5.html

Title: Migrating to Express 5

URL Source: https://expressjs.com/en/guide/migrating-5.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Migrating to Express 5
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

*   [**English**](https://expressjs.com/en/guide/migrating-5.html)
*   [Français](https://expressjs.com/fr/guide/migrating-5.html)
*   [Deutsch](https://expressjs.com/de/guide/migrating-5.html)
*   [Español](https://expressjs.com/es/guide/migrating-5.html)
*   [Italiano](https://expressjs.com/it/guide/migrating-5.html)
*   [日本語](https://expressjs.com/ja/guide/migrating-5.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/guide/migrating-5.html)
*   [繁體中文](https://expressjs.com/zh-tw/guide/migrating-5.html)
*   [한국어](https://expressjs.com/ko/guide/migrating-5.html)
*   [Português](https://expressjs.com/pt-br/guide/migrating-5.html)

Moving to Express 5
===================

Overview
--------

Express 5 is not very different from Express 4; although it maintains the same basic API, there are still changes that break compatibility with the previous version. Therefore, an application built with Express 4 might not work if you update it to use Express 5.

To install this version, you need to have a Node.js version 18 or higher. Then, execute the following command in your application directory:

```
npm install "express@5"
```

You can then run your automated tests to see what fails, and fix problems according to the updates listed below. After addressing test failures, run your app to see what errors occur. You’ll find out right away if the app uses any methods or properties that are not supported.

Express 5 Codemods
------------------

To help you migrate your express server, we have created a set of codemods that will help you automatically update your code to the latest version of Express.

Run the following command for run all the codemods available:

```
npx codemod@latest @expressjs/v5-migration-recipe
```

If you want to run a specific codemod, you can run the following command:

```
npx codemod@latest @expressjs/name-of-the-codemod
```

You can find the list of available codemods [here](https://codemod.link/express).

Changes in Express 5
--------------------

**Removed methods and properties**

*   [app.del()](https://expressjs.com/en/guide/migrating-5.html#app.del)
*   [app.param(fn)](https://expressjs.com/en/guide/migrating-5.html#app.param)
*   [Pluralized method names](https://expressjs.com/en/guide/migrating-5.html#plural)
*   [Leading colon in name argument to app.param(name, fn)](https://expressjs.com/en/guide/migrating-5.html#leading)
*   [req.param(name)](https://expressjs.com/en/guide/migrating-5.html#req.param)
*   [res.json(obj, status)](https://expressjs.com/en/guide/migrating-5.html#res.json)
*   [res.jsonp(obj, status)](https://expressjs.com/en/guide/migrating-5.html#res.jsonp)
*   [res.redirect('back') and res.location('back')](https://expressjs.com/en/guide/migrating-5.html#magic-redirect)
*   [res.redirect(url, status)](https://expressjs.com/en/guide/migrating-5.html#res.redirect)
*   [res.send(body, status)](https://expressjs.com/en/guide/migrating-5.html#res.send.body)
*   [res.send(status)](https://expressjs.com/en/guide/migrating-5.html#res.send.status)
*   [res.sendfile()](https://expressjs.com/en/guide/migrating-5.html#res.sendfile)
*   [router.param(fn)](https://expressjs.com/en/guide/migrating-5.html#router.param)
*   [express.static.mime](https://expressjs.com/en/guide/migrating-5.html#express.static.mime)
*   [express:router debug logs](https://expressjs.com/en/guide/migrating-5.html#express:router-debug-logs)

**Changed**

*   [Path route matching syntax](https://expressjs.com/en/guide/migrating-5.html#path-syntax)
*   [Rejected promises handled from middleware and handlers](https://expressjs.com/en/guide/migrating-5.html#rejected-promises)
*   [express.urlencoded](https://expressjs.com/en/guide/migrating-5.html#express.urlencoded)
*   [express.static dotfiles](https://expressjs.com/en/guide/migrating-5.html#express.static.dotfiles)
*   [app.listen](https://expressjs.com/en/guide/migrating-5.html#app.listen)
*   [app.router](https://expressjs.com/en/guide/migrating-5.html#app.router)
*   [req.body](https://expressjs.com/en/guide/migrating-5.html#req.body)
*   [req.host](https://expressjs.com/en/guide/migrating-5.html#req.host)
*   [req.params](https://expressjs.com/en/guide/migrating-5.html#req.params)
*   [req.query](https://expressjs.com/en/guide/migrating-5.html#req.query)
*   [res.clearCookie](https://expressjs.com/en/guide/migrating-5.html#res.clearCookie)
*   [res.status](https://expressjs.com/en/guide/migrating-5.html#res.status)
*   [res.vary](https://expressjs.com/en/guide/migrating-5.html#res.vary)

**Improvements**

*   [res.render()](https://expressjs.com/en/guide/migrating-5.html#res.render)
*   [Brotli encoding support](https://expressjs.com/en/guide/migrating-5.html#brotli-support)

Removed methods and properties
------------------------------

If you use any of these methods or properties in your app, it will crash. So, you’ll need to change your app after you update to version 5.

### app.del()

Express 5 no longer supports the 
```plaintext
app.del()
```
 function. If you use this function, an error is thrown. For registering HTTP DELETE routes, use the 
```plaintext
app.delete()
```
 function instead.

Initially, 
```plaintext
del
```
 was used instead of 
```plaintext
delete
```
, because 
```plaintext
delete
```
 is a reserved keyword in JavaScript. However, as of ECMAScript 6, 
```plaintext
delete
```
 and other reserved keywords can legally be used as property names.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/route-del-to-delete
```

```
// v4
app.del('/user/:id', (req, res) => {
  res.send(`DELETE /user/${req.params.id}`)
})

// v5
app.delete('/user/:id', (req, res) => {
  res.send(`DELETE /user/${req.params.id}`)
})
```

### app.param(fn)

The 
```plaintext
app.param(fn)
```
 signature was used for modifying the behavior of the 
```plaintext
app.param(name, fn)
```
 function. It has been deprecated since v4.11.0, and Express 5 no longer supports it at all.

### Pluralized method names

The following method names have been pluralized. In Express 4, using the old methods resulted in a deprecation warning. Express 5 no longer supports them at all:

```plaintext
req.acceptsCharset()
```
 is replaced by 
```plaintext
req.acceptsCharsets()
```
.

```plaintext
req.acceptsEncoding()
```
 is replaced by 
```plaintext
req.acceptsEncodings()
```
.

```plaintext
req.acceptsLanguage()
```
 is replaced by 
```plaintext
req.acceptsLanguages()
```
.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/pluralize-method-names
```

```
// v4
app.all('/', (req, res) => {
  req.acceptsCharset('utf-8')
  req.acceptsEncoding('br')
  req.acceptsLanguage('en')

  // ...
})

// v5
app.all('/', (req, res) => {
  req.acceptsCharsets('utf-8')
  req.acceptsEncodings('br')
  req.acceptsLanguages('en')

  // ...
})
```

### Leading colon (:) in the name for app.param(name, fn)

A leading colon character (:) in the name for the 
```plaintext
app.param(name, fn)
```
 function is a remnant of Express 3, and for the sake of backwards compatibility, Express 4 supported it with a deprecation notice. Express 5 will silently ignore it and use the name parameter without prefixing it with a colon.

This should not affect your code if you follow the Express 4 documentation of [app.param](https://expressjs.com/en/4x/api.html#app.param), as it makes no mention of the leading colon.

### req.param(name)

This potentially confusing and dangerous method of retrieving form data has been removed. You will now need to specifically look for the submitted parameter name in the 
```plaintext
req.params
```
, 
```plaintext
req.body
```
, or 
```plaintext
req.query
```
 object.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/explicit-request-params
```

```
// v4
app.post('/user', (req, res) => {
  const id = req.param('id')
  const body = req.param('body')
  const query = req.param('query')

  // ...
})

// v5
app.post('/user', (req, res) => {
  const id = req.params.id
  const body = req.body
  const query = req.query

  // ...
})
```

### res.json(obj, status)

Express 5 no longer supports the signature 
```plaintext
res.json(obj, status)
```
. Instead, set the status and then chain it to the 
```plaintext
res.json()
```
 method like this: 
```plaintext
res.status(status).json(obj)
```
.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/status-send-order
```

```
// v4
app.post('/user', (req, res) => {
  res.json({ name: 'Ruben' }, 201)
})

// v5
app.post('/user', (req, res) => {
  res.status(201).json({ name: 'Ruben' })
})
```

### res.jsonp(obj, status)

Express 5 no longer supports the signature 
```plaintext
res.jsonp(obj, status)
```
. Instead, set the status and then chain it to the 
```plaintext
res.jsonp()
```
 method like this: 
```plaintext
res.status(status).jsonp(obj)
```
.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/status-send-order
```

```
// v4
app.post('/user', (req, res) => {
  res.jsonp({ name: 'Ruben' }, 201)
})

// v5
app.post('/user', (req, res) => {
  res.status(201).jsonp({ name: 'Ruben' })
})
```

### res.redirect(url, status)

Express 5 no longer supports the signature 
```plaintext
res.redirect(url, status)
```
. Instead, use the following signature: 
```plaintext
res.redirect(status, url)
```
.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/redirect-arg-order
```

```
// v4
app.get('/user', (req, res) => {
  res.redirect('/users', 301)
})

// v5
app.get('/user', (req, res) => {
  res.redirect(301, '/users')
})
```

### res.redirect('back') and res.location('back')

Express 5 no longer supports the magic string 
```plaintext
back
```
 in the 
```plaintext
res.redirect()
```
 and 
```plaintext
res.location()
```
 methods. Instead, use the 
```plaintext
req.get('Referrer') || '/'
```
 value to redirect back to the previous page. In Express 4, the 
```plaintext
res.redirect('back')
```
 and 
```plaintext
res.location('back')
```
 methods were deprecated.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/back-redirect-deprecated
```

```
// v4
app.get('/user', (req, res) => {
  res.redirect('back')
})

// v5
app.get('/user', (req, res) => {
  res.redirect(req.get('Referrer') || '/')
})
```

### res.send(body, status)

Express 5 no longer supports the signature 
```plaintext
res.send(obj, status)
```
. Instead, set the status and then chain it to the 
```plaintext
res.send()
```
 method like this: 
```plaintext
res.status(status).send(obj)
```
.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/status-send-order
```

```
// v4
app.get('/user', (req, res) => {
  res.send({ name: 'Ruben' }, 200)
})

// v5
app.get('/user', (req, res) => {
  res.status(200).send({ name: 'Ruben' })
})
```

### res.send(status)

Express 5 no longer supports the signature 
```plaintext
res.send(status)
```
, where 
```plaintext
status
```
 is a number. Instead, use the 
```plaintext
res.sendStatus(statusCode)
```
 function, which sets the HTTP response header status code and sends the text version of the code: “Not Found”, “Internal Server Error”, and so on. If you need to send a number by using the 
```plaintext
res.send()
```
 function, quote the number to convert it to a string, so that Express does not interpret it as an attempt to use the unsupported old signature.

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/status-send-order
```

```
// v4
app.get('/user', (req, res) => {
  res.send(200)
})

// v5
app.get('/user', (req, res) => {
  res.sendStatus(200)
})
```

### res.sendfile()

The 
```plaintext
res.sendfile()
```
 function has been replaced by a camel-cased version 
```plaintext
res.sendFile()
```
 in Express 5.

**Note:** In Express 5, 
```plaintext
res.sendFile()
```
 uses the 
```plaintext
mime-types
```
 package for MIME type detection, which returns different Content-Type values than Express 4 for several common file types:

*   JavaScript files (.js): now “text/javascript” instead of “application/javascript”
*   JSON files (.json): now “application/json” instead of “text/json”
*   CSS files (.css): now “text/css” instead of “text/plain”
*   XML files (.xml): now “application/xml” instead of “text/xml”
*   Font files (.woff): now “font/woff” instead of “application/font-woff”
*   SVG files (.svg): now “image/svg+xml” instead of “application/svg+xml”

Note

You can replace the deprecated signatures with the following command:

```plain-text
npx codemod@latest @expressjs/camelcase-sendfile
```

```
// v4
app.get('/user', (req, res) => {
  res.sendfile('/path/to/file')
})

// v5
app.get('/user', (req, res) => {
  res.sendFile('/path/to/file')
})
```

### router.param(fn)

The 
```plaintext
router.param(fn)
```
 signature was used for modifying the behavior of the 
```plaintext
router.param(name, fn)
```
 function. It has been deprecated since v4.11.0, and Express 5 no longer supports it at all.

### express.static.mime

In Express 5, 
```plaintext
mime
```
 is no longer an exported property of the 
```plaintext
static
```
 field. Use the [```plaintext mime-types ``` package](https://github.com/jshttp/mime-types) to work with MIME type values.

**Important:** This change affects not only direct usage of 
```plaintext
express.static.mime
```
 but also other Express methods that rely on MIME type detection, such as 
```plaintext
res.sendFile()
```
. The following MIME types have changed from Express 4:

*   JavaScript files (.js): now served as “text/javascript” instead of “application/javascript”
*   JSON files (.json): now served as “application/json” instead of “text/json”
*   CSS files (.css): now served as “text/css” instead of “text/plain”
*   HTML files (.html): now served as “text/html; charset=utf-8” instead of just “text/html”
*   XML files (.xml): now served as “application/xml” instead of “text/xml”
*   Font files (.woff): now served as “font/woff” instead of “application/font-woff”

```
// v4
express.static.mime.lookup('json')

// v5
const mime = require('mime-types')
mime.lookup('json')
```

### express:router debug logs

In Express 5, router handling logic is performed by a dependency. Therefore, the debug logs for the router are no longer available under the 
```plaintext
express:
```
 namespace. In v4, the logs were available under the namespaces 
```plaintext
express:router
```
, 
```plaintext
express:router:layer
```
, and 
```plaintext
express:router:route
```
. All of these were included under the namespace 
```plaintext
express:*
```
. In v5.1+, the logs are available under the namespaces 
```plaintext
router
```
, 
```plaintext
router:layer
```
, and 
```plaintext
router:route
```
. The logs from 
```plaintext
router:layer
```
 and 
```plaintext
router:route
```
 are included in the namespace 
```plaintext
router:*
```
. To achieve the same detail of debug logging when using 
```plaintext
express:*
```
 in v4, use a conjunction of 
```plaintext
express:*
```
, 
```plaintext
router
```
, and 
```plaintext
router:*
```
.

```
# v4
DEBUG=express:* node index.js

# v5
DEBUG=express:*,router,router:* node index.js
```

Changed
-------

### Path route matching syntax

Path route matching syntax is when a string is supplied as the first parameter to the 
```plaintext
app.all()
```
, 
```plaintext
app.use()
```
, 
```plaintext
app.METHOD()
```
, 
```plaintext
router.all()
```
, 
```plaintext
router.METHOD()
```
, and 
```plaintext
router.use()
```
 APIs. The following changes have been made to how the path string is matched to an incoming request:

*   The wildcard 
```plaintext
*
```
 must have a name, matching the behavior of parameters 
```plaintext
:
```
, use 
```plaintext
/*splat
```
 instead of 
```plaintext
/*
```

```
// v4
app.get('/*', async (req, res) => {
  res.send('ok')
})

// v5
app.get('/*splat', async (req, res) => {
  res.send('ok')
})
```

Note

```plaintext
*splat
```
 matches any path without the root path. If you need to match the root path as well 
```plaintext
/
```
, you can use 
```plaintext
/{*splat}
```
, wrapping the wildcard in braces.

```
// v5
app.get('/{*splat}', async (req, res) => {
  res.send('ok')
})
```

*   The optional character 
```plaintext
?
```
 is no longer supported, use braces instead.

```
// v4
app.get('/:file.:ext?', async (req, res) => {
  res.send('ok')
})

// v5
app.get('/:file{.:ext}', async (req, res) => {
  res.send('ok')
})
```

*   Regexp characters are not supported. For example: ```
app.get('/[discussion|page]/:slug', async (req, res) => {
res.status(200).send('ok')
})
```  
should be changed to:

```
app.get(['/discussion/:slug', '/page/:slug'], async (req, res) => {
res.status(200).send('ok')
})
```  
*   Some characters have been reserved to avoid confusion during upgrade (
```plaintext
()[]?+!
```
), use 
```plaintext
\
```
 to escape them.
*   Parameter names now support valid JavaScript identifiers, or quoted like 
```plaintext
:"this"
```
.

### Rejected promises handled from middleware and handlers

Request middleware and handlers that return rejected promises are now handled by forwarding the rejected value as an 
```plaintext
Error
```
 to the error handling middleware. This means that using 
```plaintext
async
```
 functions as middleware and handlers are easier than ever. When an error is thrown in an 
```plaintext
async
```
 function or a rejected promise is 
```plaintext
await
```
ed inside an async function, those errors will be passed to the error handler as if calling 
```plaintext
next(err)
```
.

Details of how Express handles errors is covered in the [error handling documentation](https://expressjs.com/en/guide/error-handling.html).

### express.urlencoded

The 
```plaintext
express.urlencoded
```
 method makes the 
```plaintext
extended
```
 option 
```plaintext
false
```
 by default.

### express.static dotfiles

In Express 5, the 
```plaintext
express.static
```
 middleware’s 
```plaintext
dotfiles
```
 option now defaults to 
```plaintext
"ignore"
```
. This is a change from Express 4, where dotfiles were served by default. As a result, files inside a directory that starts with a dot (
```plaintext
.
```
), such as 
```plaintext
.well-known
```
, will no longer be accessible and will return a **404 Not Found** error. This can break functionality that depends on serving dot-directories, such as Android App Links, and Apple Universal Links.

Example of breaking code:

```
// v4
app.use(express.static('public'))
```

After migrating to Express 5, a request to 
```plaintext
/.well-known/assetlinks.json
```
 will result in a **404 Not Found**.

To fix this, serve specific dot-directories explicitly using the 
```plaintext
dotfiles: "allow"
```
 option:

```
// v5
app.use('/.well-known', express.static('public/.well-known', { dotfiles: 'allow' }))
app.use(express.static('public'))
```

This approach allows you to safely serve only the intended dot-directories while keeping the default secure behavior for other dotfiles, which remain inaccessible.

### app.listen

In Express 5, the 
```plaintext
app.listen
```
 method will invoke the user-provided callback function (if provided) when the server receives an error event. In Express 4, such errors would be thrown. This change shifts error-handling responsibility to the callback function in Express 5. If there is an error, it will be passed to the callback as an argument. For example:

```
const server = app.listen(8080, '0.0.0.0', (error) => {
  if (error) {
    throw error // e.g. EADDRINUSE
  }
  console.log(`Listening on ${JSON.stringify(server.address())}`)
})
```

### app.router

The 
```plaintext
app.router
```
 object, which was removed in Express 4, has made a comeback in Express 5. In the new version, this object is a just a reference to the base Express router, unlike in Express 3, where an app had to explicitly load it.

### req.body

The 
```plaintext
req.body
```
 property returns 
```plaintext
undefined
```
 when the body has not been parsed. In Express 4, it returns 
```plaintext
{}
```
 by default.

### req.host

In Express 4, the 
```plaintext
req.host
```
 function incorrectly stripped off the port number if it was present. In Express 5, the port number is maintained.

### req.params

The 
```plaintext
req.params
```
 object now has a **null prototype** when using string paths. However, if the path is defined with a regular expression, 
```plaintext
req.params
```
 remains a standard object with a normal prototype. Additionally, there are two important behavioral changes:

**Wildcard parameters are now arrays:**

Wildcards (e.g., 
```plaintext
/*splat
```
) capture path segments as an array instead of a single string.

```
app.get('/*splat', (req, res) => {
  // GET /foo/bar
  console.dir(req.params)
  // => [Object: null prototype] { splat: [ 'foo', 'bar' ] }
})
```

**Unmatched parameters are omitted:**

In Express 4, unmatched wildcards were empty strings (
```plaintext
''
```
) and optional 
```plaintext
:
```
 parameters (using 
```plaintext
?
```
) had a key with value 
```plaintext
undefined
```
. In Express 5, unmatched parameters are completely omitted from 
```plaintext
req.params
```
.

```
// v4: unmatched wildcard is empty string
app.get('/*', (req, res) => {
  // GET /
  console.dir(req.params)
  // => { '0': '' }
})

// v4: unmatched optional param is undefined
app.get('/:file.:ext?', (req, res) => {
  // GET /image
  console.dir(req.params)
  // => { file: 'image', ext: undefined }
})

// v5: unmatched optional param is omitted
app.get('/:file{.:ext}', (req, res) => {
  // GET /image
  console.dir(req.params)
  // => [Object: null prototype] { file: 'image' }
})
```

### req.query

The 
```plaintext
req.query
```
 property is no longer a writable property and is instead a getter. The default query parser has been changed from “extended” to “simple”.

### res.clearCookie

The 
```plaintext
res.clearCookie
```
 method ignores the 
```plaintext
maxAge
```
 and 
```plaintext
expires
```
 options provided by the user.

### res.status

The 
```plaintext
res.status
```
 method only accepts integers in the range of 
```plaintext
100
```
 to 
```plaintext
999
```
, following the behavior defined by Node.js, and it returns an error when the status code is not an integer.

### res.vary

The 
```plaintext
res.vary
```
 throws an error when the 
```plaintext
field
```
 argument is missing. In Express 4, if the argument was omitted, it gave a warning in the console

Improvements
------------

### res.render()

This method now enforces asynchronous behavior for all view engines, avoiding bugs caused by view engines that had a synchronous implementation and that violated the recommended interface.

### Brotli encoding support

Express 5 supports Brotli encoding for requests received from clients that support it.

[Previous: Migrating to Express 4](https://expressjs.com/en/guide/migrating-4.html)[Next: Express database integration](https://expressjs.com/en/guide/database-integration.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/guide/migrating-5.md)

[](https://expressjs.com/en/guide/migrating-5.html#)

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
