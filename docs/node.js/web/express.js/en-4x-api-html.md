# Source: https://expressjs.com/en/4x/api.html

Title: Express 4.x - API Reference

URL Source: https://expressjs.com/en/4x/api.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Express 4.x - API Reference
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

*   [**English**](https://expressjs.com/en/4x/api.html)
*   [Français](https://expressjs.com/fr/4x/api.html)
*   [Deutsch](https://expressjs.com/de/4x/api.html)
*   [Español](https://expressjs.com/es/4x/api.html)
*   [Italiano](https://expressjs.com/it/4x/api.html)
*   [日本語](https://expressjs.com/ja/4x/api.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/4x/api.html)
*   [繁體中文](https://expressjs.com/zh-tw/4x/api.html)
*   [한국어](https://expressjs.com/ko/4x/api.html)
*   [Português](https://expressjs.com/pt-br/4x/api.html)

### _On this page_

On this page
*   [express()](https://expressjs.com/en/4x/api.html#express)
    *   _Methods_
    *   [express.json()](https://expressjs.com/en/4x/api.html#express.json)
    *   [express.raw()](https://expressjs.com/en/4x/api.html#express.raw)
    *   [express.Router()](https://expressjs.com/en/4x/api.html#express.router)
    *   [express.static()](https://expressjs.com/en/4x/api.html#express.static)
    *   [express.text()](https://expressjs.com/en/4x/api.html#express.text)
    *   [express.urlencoded()](https://expressjs.com/en/4x/api.html#express.urlencoded)

*   [Application](https://expressjs.com/en/4x/api.html#app)
    *   _Properties_
    *   [app.locals](https://expressjs.com/en/4x/api.html#app.locals)
    *   [app.mountpath](https://expressjs.com/en/4x/api.html#app.mountpath)
    *   _Events_
    *   [mount](https://expressjs.com/en/4x/api.html#app.onmount)
    *   _Methods_
    *   [app.all()](https://expressjs.com/en/4x/api.html#app.all)
    *   [app.delete()](https://expressjs.com/en/4x/api.html#app.delete.method)
    *   [app.disable()](https://expressjs.com/en/4x/api.html#app.disable)
    *   [app.disabled()](https://expressjs.com/en/4x/api.html#app.disabled)
    *   [app.enable()](https://expressjs.com/en/4x/api.html#app.enable)
    *   [app.enabled()](https://expressjs.com/en/4x/api.html#app.enabled)
    *   [app.engine()](https://expressjs.com/en/4x/api.html#app.engine)
    *   [app.get()](https://expressjs.com/en/4x/api.html#app.get)
    *   [app.get()](https://expressjs.com/en/4x/api.html#app.get.method)
    *   [app.listen()](https://expressjs.com/en/4x/api.html#app.listen)
    *   [app.METHOD()](https://expressjs.com/en/4x/api.html#app.METHOD)
    *   [app.param()](https://expressjs.com/en/4x/api.html#app.param)
    *   [app.path()](https://expressjs.com/en/4x/api.html#app.path)
    *   [app.post()](https://expressjs.com/en/4x/api.html#app.post.method)
    *   [app.put()](https://expressjs.com/en/4x/api.html#app.put.method)
    *   [app.render()](https://expressjs.com/en/4x/api.html#app.render)
    *   [app.route()](https://expressjs.com/en/4x/api.html#app.route)
    *   [app.set()](https://expressjs.com/en/4x/api.html#app.set)
    *   [app.use()](https://expressjs.com/en/4x/api.html#app.use)

*   [Request](https://expressjs.com/en/4x/api.html#req)
    *   _Properties_
    *   [req.app](https://expressjs.com/en/4x/api.html#req.app)
    *   [req.baseUrl](https://expressjs.com/en/4x/api.html#req.baseUrl)
    *   [req.body](https://expressjs.com/en/4x/api.html#req.body)
    *   [req.cookies](https://expressjs.com/en/4x/api.html#req.cookies)
    *   [req.fresh](https://expressjs.com/en/4x/api.html#req.fresh)
    *   [req.hostname](https://expressjs.com/en/4x/api.html#req.hostname)
    *   [req.ip](https://expressjs.com/en/4x/api.html#req.ip)
    *   [req.ips](https://expressjs.com/en/4x/api.html#req.ips)
    *   [req.method](https://expressjs.com/en/4x/api.html#req.method)
    *   [req.originalUrl](https://expressjs.com/en/4x/api.html#req.originalUrl)
    *   [req.params](https://expressjs.com/en/4x/api.html#req.params)
    *   [req.path](https://expressjs.com/en/4x/api.html#req.path)
    *   [req.protocol](https://expressjs.com/en/4x/api.html#req.protocol)
    *   [req.query](https://expressjs.com/en/4x/api.html#req.query)
    *   [req.res](https://expressjs.com/en/4x/api.html#req.res)
    *   [req.route](https://expressjs.com/en/4x/api.html#req.route)
    *   [req.secure](https://expressjs.com/en/4x/api.html#req.secure)
    *   [req.signedCookies](https://expressjs.com/en/4x/api.html#req.signedCookies)
    *   [req.stale](https://expressjs.com/en/4x/api.html#req.stale)
    *   [req.subdomains](https://expressjs.com/en/4x/api.html#req.subdomains)
    *   [req.xhr](https://expressjs.com/en/4x/api.html#req.xhr)
    *   _Methods_
    *   [req.accepts()](https://expressjs.com/en/4x/api.html#req.accepts)
    *   [req.acceptsCharsets()](https://expressjs.com/en/4x/api.html#req.acceptsCharsets)
    *   [req.acceptsEncodings()](https://expressjs.com/en/4x/api.html#req.acceptsEncodings)
    *   [req.acceptsLanguages()](https://expressjs.com/en/4x/api.html#req.acceptsLanguages)
    *   [req.get()](https://expressjs.com/en/4x/api.html#req.get)
    *   [req.is()](https://expressjs.com/en/4x/api.html#req.is)
    *   [req.param()](https://expressjs.com/en/4x/api.html#req.param)
    *   [req.range()](https://expressjs.com/en/4x/api.html#req.range)

*   [Response](https://expressjs.com/en/4x/api.html#res)
    *   _Properties_
    *   [res.app](https://expressjs.com/en/4x/api.html#res.app)
    *   [res.headersSent](https://expressjs.com/en/4x/api.html#res.headersSent)
    *   [res.locals](https://expressjs.com/en/4x/api.html#res.locals)
    *   _Methods_
    *   [res.append()](https://expressjs.com/en/4x/api.html#res.append)
    *   [res.attachment()](https://expressjs.com/en/4x/api.html#res.attachment)
    *   [res.cookie()](https://expressjs.com/en/4x/api.html#res.cookie)
    *   [res.clearCookie()](https://expressjs.com/en/4x/api.html#res.clearCookie)
    *   [res.download()](https://expressjs.com/en/4x/api.html#res.download)
    *   [res.end()](https://expressjs.com/en/4x/api.html#res.end)
    *   [res.format()](https://expressjs.com/en/4x/api.html#res.format)
    *   [res.get()](https://expressjs.com/en/4x/api.html#res.get)
    *   [res.json()](https://expressjs.com/en/4x/api.html#res.json)
    *   [res.jsonp()](https://expressjs.com/en/4x/api.html#res.jsonp)
    *   [res.links()](https://expressjs.com/en/4x/api.html#res.links)
    *   [res.location()](https://expressjs.com/en/4x/api.html#res.location)
    *   [res.redirect()](https://expressjs.com/en/4x/api.html#res.redirect)
    *   [res.render()](https://expressjs.com/en/4x/api.html#res.render)
    *   [res.send()](https://expressjs.com/en/4x/api.html#res.send)
    *   [res.sendFile()](https://expressjs.com/en/4x/api.html#res.sendFile)
    *   [res.sendStatus()](https://expressjs.com/en/4x/api.html#res.sendStatus)
    *   [res.set()](https://expressjs.com/en/4x/api.html#res.set)
    *   [res.status()](https://expressjs.com/en/4x/api.html#res.status)
    *   [res.type()](https://expressjs.com/en/4x/api.html#res.type)
    *   [res.vary()](https://expressjs.com/en/4x/api.html#res.vary)

*   [Router](https://expressjs.com/en/4x/api.html#router)
    *   _Methods_
    *   [router.all()](https://expressjs.com/en/4x/api.html#router.all)
    *   [router.METHOD()](https://expressjs.com/en/4x/api.html#router.METHOD)
    *   [router.param()](https://expressjs.com/en/4x/api.html#router.param)
    *   [router.route()](https://expressjs.com/en/4x/api.html#router.route)
    *   [router.use()](https://expressjs.com/en/4x/api.html#router.use)

4.x API
=======

Note

Express 4.0 requires Node.js 0.10 or higher.

[](https://expressjs.com/en/4x/api.html)

express()
---------

Creates an Express application. The 
```plaintext
express()
```
 function is a top-level function exported by the 
```plaintext
express
```
 module.

```
var express = require('express')
var app = express()
```

### Methods

### express.json([options])

This middleware is available in Express v4.16.0 onwards.

This is a built-in middleware function in Express. It parses incoming requests with JSON payloads and is based on [body-parser](https://expressjs.com/resources/middleware/body-parser.html).

Returns middleware that only parses JSON and only looks at requests where the 
```plaintext
Content-Type
```
 header matches the 
```plaintext
type
```
 option. This parser accepts any Unicode encoding of the body and supports automatic inflation of 
```plaintext
gzip
```
 and 
```plaintext
deflate
```
 encodings.

A new 
```plaintext
body
```
 object containing the parsed data is populated on the 
```plaintext
request
```
 object after the middleware (i.e. 
```plaintext
req.body
```
), or an empty object (
```plaintext
{}
```
) if there was no body to parse, the 
```plaintext
Content-Type
```
 was not matched, or an error occurred.

As 
```plaintext
req.body
```
’s shape is based on user-controlled input, all properties and values in this object are untrusted and should be validated before trusting. For example, 
```plaintext
req.body.foo.toString()
```
 may fail in multiple ways, for example 
```plaintext
foo
```
 may not be there or may not be a string, and 
```plaintext
toString
```
 may not be a function and instead a string or other user-input.

The following table describes the properties of the optional 
```plaintext
options
```
 object.

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| ```plaintext inflate ``` | Enables or disables handling deflated (compressed) bodies; when disabled, deflated bodies are rejected. | Boolean | ```plaintext true ``` |
| ```plaintext limit ``` | Controls the maximum request body size. If this is a number, then the value specifies the number of bytes; if it is a string, the value is passed to the [bytes](https://www.npmjs.com/package/bytes) library for parsing. | Mixed | ```plaintext "100kb" ``` |
| ```plaintext reviver ``` | The ```plaintext reviver ``` option is passed directly to ```plaintext JSON.parse ``` as the second argument. You can find more information on this argument [in the MDN documentation about JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#Example.3A_Using_the_reviver_parameter). | Function | ```plaintext null ``` |
| ```plaintext strict ``` | Enables or disables only accepting arrays and objects; when disabled will accept anything ```plaintext JSON.parse ``` accepts. | Boolean | ```plaintext true ``` |
| ```plaintext type ``` | This is used to determine what media type the middleware will parse. This option can be a string, array of strings, or a function. If not a function, ```plaintext type ``` option is passed directly to the [type-is](https://www.npmjs.org/package/type-is#readme) library and this can be an extension name (like ```plaintext json ``` ), a mime type (like ```plaintext application/json ``` ), or a mime type with a wildcard (like ```plaintext */* ``` or ```plaintext */json ``` ). If a function, the ```plaintext type ``` option is called as ```plaintext fn(req) ``` and the request is parsed if it returns a truthy value. | Mixed | ```plaintext "application/json" ``` |
| ```plaintext verify ``` | This option, if supplied, is called as ```plaintext verify(req, res, buf, encoding) ``` , where ```plaintext buf ``` is a ```plaintext Buffer ``` of the raw request body and ```plaintext encoding ``` is the encoding of the request. The parsing can be aborted by throwing an error. | Function | ```plaintext undefined ``` |

### express.raw([options])

This middleware is available in Express v4.17.0 onwards.

This is a built-in middleware function in Express. It parses incoming request payloads into a 
```plaintext
Buffer
```
 and is based on [body-parser](https://expressjs.com/resources/middleware/body-parser.html).

Returns middleware that parses all bodies as a 
```plaintext
Buffer
```
 and only looks at requests where the 
```plaintext
Content-Type
```
 header matches the 
```plaintext
type
```
 option. This parser accepts any Unicode encoding of the body and supports automatic inflation of 
```plaintext
gzip
```
 and 
```plaintext
deflate
```
 encodings.

A new 
```plaintext
body
```

```plaintext
Buffer
```
 containing the parsed data is populated on the 
```plaintext
request
```
 object after the middleware (i.e. 
```plaintext
req.body
```
), or an empty object (
```plaintext
{}
```
) if there was no body to parse, the 
```plaintext
Content-Type
```
 was not matched, or an error occurred.

As 
```plaintext
req.body
```
’s shape is based on user-controlled input, all properties and values in this object are untrusted and should be validated before trusting. For example, 
```plaintext
req.body.toString()
```
 may fail in multiple ways, for example stacking multiple parsers 
```plaintext
req.body
```
 may be from a different parser. Testing that 
```plaintext
req.body
```
 is a 
```plaintext
Buffer
```
 before calling buffer methods is recommended.

The following table describes the properties of the optional 
```plaintext
options
```
 object.

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| ```plaintext inflate ``` | Enables or disables handling deflated (compressed) bodies; when disabled, deflated bodies are rejected. | Boolean | ```plaintext true ``` |
| ```plaintext limit ``` | Controls the maximum request body size. If this is a number, then the value specifies the number of bytes; if it is a string, the value is passed to the [bytes](https://www.npmjs.com/package/bytes) library for parsing. | Mixed | ```plaintext "100kb" ``` |
| ```plaintext type ``` | This is used to determine what media type the middleware will parse. This option can be a string, array of strings, or a function. If not a function, ```plaintext type ``` option is passed directly to the [type-is](https://www.npmjs.org/package/type-is#readme) library and this can be an extension name (like ```plaintext bin ``` ), a mime type (like ```plaintext application/octet-stream ``` ), or a mime type with a wildcard (like ```plaintext */* ``` or ```plaintext application/* ``` ). If a function, the ```plaintext type ``` option is called as ```plaintext fn(req) ``` and the request is parsed if it returns a truthy value. | Mixed | ```plaintext "application/octet-stream" ``` |
| ```plaintext verify ``` | This option, if supplied, is called as ```plaintext verify(req, res, buf, encoding) ``` , where ```plaintext buf ``` is a ```plaintext Buffer ``` of the raw request body and ```plaintext encoding ``` is the encoding of the request. The parsing can be aborted by throwing an error. | Function | ```plaintext undefined ``` |

### express.Router([options])

Creates a new [router](https://expressjs.com/en/4x/api.html#router) object.

```
var router = express.Router([options])
```

The optional 
```plaintext
options
```
 parameter specifies the behavior of the router.

| Property | Description | Default | Availability |
| --- | --- | --- | --- |
| ```plaintext caseSensitive ``` | Enable case sensitivity. | Disabled by default, treating “/Foo” and “/foo” as the same. |  |
| ```plaintext mergeParams ``` | Preserve the ```plaintext req.params ``` values from the parent router. If the parent and the child have conflicting param names, the child’s value take precedence. | ```plaintext false ``` | 4.5.0+ |
| ```plaintext strict ``` | Enable strict routing. | Disabled by default, “/foo” and “/foo/” are treated the same by the router. |  |

You can add middleware and HTTP method routes (such as 
```plaintext
get
```
, 
```plaintext
put
```
, 
```plaintext
post
```
, and so on) to 
```plaintext
router
```
 just like an application.

For more information, see [Router](https://expressjs.com/en/4x/api.html#router).

### express.static(root, [options])

This is a built-in middleware function in Express. It serves static files and is based on [serve-static](https://expressjs.com/resources/middleware/serve-static.html).

Note

For best results, [use a reverse proxy](https://expressjs.com/en/advanced/best-practice-performance.html#use-a-reverse-proxy) cache to improve performance of serving static assets.

The 
```plaintext
root
```
 argument specifies the root directory from which to serve static assets. The function determines the file to serve by combining 
```plaintext
req.url
```
 with the provided 
```plaintext
root
```
 directory. When a file is not found, instead of sending a 404 response, it calls 
```plaintext
next()
```
 to move on to the next middleware, allowing for stacking and fall-backs.

The following table describes the properties of the 
```plaintext
options
```
 object. See also the [example below](https://expressjs.com/en/4x/api.html#example.of.express.static).

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| ```plaintext dotfiles ``` | Determines how dotfiles (files or directories that begin with a dot “.”) are treated. See [dotfiles](https://expressjs.com/en/4x/api.html#dotfiles) below. | String | ```plaintext undefined ``` |
| ```plaintext etag ``` | Enable or disable etag generation NOTE: ```plaintext express.static ``` always sends weak ETags. | Boolean | ```plaintext true ``` |
| ```plaintext extensions ``` | Sets file extension fallbacks: If a file is not found, search for files with the specified extensions and serve the first one found. Example: ```plaintext ['html', 'htm'] ``` . | Mixed | ```plaintext false ``` |
| ```plaintext fallthrough ``` | Let client errors fall-through as unhandled requests, otherwise forward a client error. See [fallthrough](https://expressjs.com/en/4x/api.html#fallthrough) below. | Boolean | ```plaintext true ``` |
| ```plaintext immutable ``` | Enable or disable the ```plaintext immutable ``` directive in the ```plaintext Cache-Control ``` response header. If enabled, the ```plaintext maxAge ``` option should also be specified to enable caching. The ```plaintext immutable ``` directive will prevent supported clients from making conditional requests during the life of the ```plaintext maxAge ``` option to check if the file has changed. | Boolean | ```plaintext false ``` |
| ```plaintext index ``` | Sends the specified directory index file. Set to ```plaintext false ``` to disable directory indexing. | Mixed | “index.html” |
| ```plaintext lastModified ``` | Set the ```plaintext Last-Modified ``` header to the last modified date of the file on the OS. | Boolean | ```plaintext true ``` |
| ```plaintext maxAge ``` | Set the max-age property of the Cache-Control header in milliseconds or a string in [ms format](https://www.npmjs.org/package/ms). | Number | 0 |
| ```plaintext redirect ``` | Redirect to trailing “/” when the pathname is a directory. | Boolean | ```plaintext true ``` |
| ```plaintext setHeaders ``` | Function for setting HTTP headers to serve with the file. See [setHeaders](https://expressjs.com/en/4x/api.html#setHeaders) below. | Function |  |
| ```plaintext acceptRanges ``` | Enable or disable accepting ranged requests. Disabling this will not send the ```plaintext Accept-Ranges ``` header and will ignore the contents of the Range request header. | Boolean | true |
| ```plaintext cacheControl ``` | Enable or disable setting the ```plaintext Cache-Control ``` response header. Disabling this will ignore the immutable and maxAge options. | Boolean | true |

For more information, see [Serving static files in Express](https://expressjs.com/starter/static-files.html). and [Using middleware - Built-in middleware](https://expressjs.com/en/guide/using-middleware.html#middleware.built-in).

##### dotfiles

Possible values for this option are:

*   “allow” - No special treatment for dotfiles.
*   “deny” - Deny a request for a dotfile, respond with 
```plaintext
403
```
, then call 
```plaintext
next()
```
.
*   “ignore” - Act as if the dotfile does not exist, respond with 
```plaintext
404
```
, then call 
```plaintext
next()
```
.
*   ```plaintext
undefined
```
 - Act as ignore, except that files in a directory that begins with a dot are **NOT** ignored.

##### fallthrough

When this option is 
```plaintext
true
```
, client errors such as a bad request or a request to a non-existent file will cause this middleware to simply call 
```plaintext
next()
```
 to invoke the next middleware in the stack. When false, these errors (even 404s), will invoke 
```plaintext
next(err)
```
.

Set this option to 
```plaintext
true
```
 so you can map multiple physical directories to the same web address or for routes to fill in non-existent files.

Use 
```plaintext
false
```
 if you have mounted this middleware at a path designed to be strictly a single file system directory, which allows for short-circuiting 404s for less overhead. This middleware will also reply to all methods.

##### setHeaders

For this option, specify a function to set custom response headers. Alterations to the headers must occur synchronously.

The signature of the function is:

```
fn(res, path, stat)
```

Arguments:

*   ```plaintext
res
```
, the [response object](https://expressjs.com/en/4x/api.html#res).
*   ```plaintext
path
```
, the file path that is being sent.
*   ```plaintext
stat
```
, the 
```plaintext
stat
```
 object of the file that is being sent.

#### Example of express.static

Here is an example of using the 
```plaintext
express.static
```
 middleware function with an elaborate options object:

```
var options = {
  dotfiles: 'ignore',
  etag: false,
  extensions: ['htm', 'html'],
  index: false,
  maxAge: '1d',
  redirect: false,
  setHeaders: function (res, path, stat) {
    res.set('x-timestamp', Date.now())
  }
}

app.use(express.static('public', options))
```

### express.text([options])

This middleware is available in Express v4.17.0 onwards.

This is a built-in middleware function in Express. It parses incoming request payloads into a string and is based on [body-parser](https://expressjs.com/resources/middleware/body-parser.html).

Returns middleware that parses all bodies as a string and only looks at requests where the 
```plaintext
Content-Type
```
 header matches the 
```plaintext
type
```
 option. This parser accepts any Unicode encoding of the body and supports automatic inflation of 
```plaintext
gzip
```
 and 
```plaintext
deflate
```
 encodings.

A new 
```plaintext
body
```
 string containing the parsed data is populated on the 
```plaintext
request
```
 object after the middleware (i.e. 
```plaintext
req.body
```
), or an empty object (
```plaintext
{}
```
) if there was no body to parse, the 
```plaintext
Content-Type
```
 was not matched, or an error occurred.

As 
```plaintext
req.body
```
’s shape is based on user-controlled input, all properties and values in this object are untrusted and should be validated before trusting. For example, 
```plaintext
req.body.trim()
```
 may fail in multiple ways, for example stacking multiple parsers 
```plaintext
req.body
```
 may be from a different parser. Testing that 
```plaintext
req.body
```
 is a string before calling string methods is recommended.

The following table describes the properties of the optional 
```plaintext
options
```
 object.

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| ```plaintext defaultCharset ``` | Specify the default character set for the text content if the charset is not specified in the ```plaintext Content-Type ``` header of the request. | String | ```plaintext "utf-8" ``` |
| ```plaintext inflate ``` | Enables or disables handling deflated (compressed) bodies; when disabled, deflated bodies are rejected. | Boolean | ```plaintext true ``` |
| ```plaintext limit ``` | Controls the maximum request body size. If this is a number, then the value specifies the number of bytes; if it is a string, the value is passed to the [bytes](https://www.npmjs.com/package/bytes) library for parsing. | Mixed | ```plaintext "100kb" ``` |
| ```plaintext type ``` | This is used to determine what media type the middleware will parse. This option can be a string, array of strings, or a function. If not a function, ```plaintext type ``` option is passed directly to the [type-is](https://www.npmjs.org/package/type-is#readme) library and this can be an extension name (like ```plaintext txt ``` ), a mime type (like ```plaintext text/plain ``` ), or a mime type with a wildcard (like ```plaintext */* ``` or ```plaintext text/* ``` ). If a function, the ```plaintext type ``` option is called as ```plaintext fn(req) ``` and the request is parsed if it returns a truthy value. | Mixed | ```plaintext "text/plain" ``` |
| ```plaintext verify ``` | This option, if supplied, is called as ```plaintext verify(req, res, buf, encoding) ``` , where ```plaintext buf ``` is a ```plaintext Buffer ``` of the raw request body and ```plaintext encoding ``` is the encoding of the request. The parsing can be aborted by throwing an error. | Function | ```plaintext undefined ``` |

### express.urlencoded([options])

This middleware is available in Express v4.16.0 onwards.

This is a built-in middleware function in Express. It parses incoming requests with urlencoded payloads and is based on [body-parser](https://expressjs.com/resources/middleware/body-parser.html).

Returns middleware that only parses urlencoded bodies and only looks at requests where the 
```plaintext
Content-Type
```
 header matches the 
```plaintext
type
```
 option. This parser accepts only UTF-8 encoding of the body and supports automatic inflation of 
```plaintext
gzip
```
 and 
```plaintext
deflate
```
 encodings.

A new 
```plaintext
body
```
 object containing the parsed data is populated on the 
```plaintext
request
```
 object after the middleware (i.e. 
```plaintext
req.body
```
), or an empty object (
```plaintext
{}
```
) if there was no body to parse, the 
```plaintext
Content-Type
```
 was not matched, or an error occurred. This object will contain key-value pairs, where the value can be a string or array (when 
```plaintext
extended
```
 is 
```plaintext
false
```
), or any type (when 
```plaintext
extended
```
 is 
```plaintext
true
```
).

As 
```plaintext
req.body
```
’s shape is based on user-controlled input, all properties and values in this object are untrusted and should be validated before trusting. For example, 
```plaintext
req.body.foo.toString()
```
 may fail in multiple ways, for example 
```plaintext
foo
```
 may not be there or may not be a string, and 
```plaintext
toString
```
 may not be a function and instead a string or other user-input.

The following table describes the properties of the optional 
```plaintext
options
```
 object.

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| ```plaintext extended ``` | This option allows to choose between parsing the URL-encoded data with the ```plaintext querystring ``` library (when ```plaintext false ``` ) or the ```plaintext qs ``` library (when ```plaintext true ``` ). The “extended” syntax allows for rich objects and arrays to be encoded into the URL-encoded format, allowing for a JSON-like experience with URL-encoded. For more information, please [see the qs library](https://www.npmjs.org/package/qs#readme). | Boolean | ```plaintext true ``` |
| ```plaintext inflate ``` | Enables or disables handling deflated (compressed) bodies; when disabled, deflated bodies are rejected. | Boolean | ```plaintext true ``` |
| ```plaintext limit ``` | Controls the maximum request body size. If this is a number, then the value specifies the number of bytes; if it is a string, the value is passed to the [bytes](https://www.npmjs.com/package/bytes) library for parsing. | Mixed | ```plaintext "100kb" ``` |
| ```plaintext parameterLimit ``` | This option controls the maximum number of parameters that are allowed in the URL-encoded data. If a request contains more parameters than this value, an error will be raised. | Number | ```plaintext 1000 ``` |
| ```plaintext type ``` | This is used to determine what media type the middleware will parse. This option can be a string, array of strings, or a function. If not a function, ```plaintext type ``` option is passed directly to the [type-is](https://www.npmjs.org/package/type-is#readme) library and this can be an extension name (like ```plaintext urlencoded ``` ), a mime type (like ```plaintext application/x-www-form-urlencoded ``` ), or a mime type with a wildcard (like ```plaintext */x-www-form-urlencoded ``` ). If a function, the ```plaintext type ``` option is called as ```plaintext fn(req) ``` and the request is parsed if it returns a truthy value. | Mixed | ```plaintext "application/x-www-form-urlencoded" ``` |
| ```plaintext verify ``` | This option, if supplied, is called as ```plaintext verify(req, res, buf, encoding) ``` , where ```plaintext buf ``` is a ```plaintext Buffer ``` of the raw request body and ```plaintext encoding ``` is the encoding of the request. The parsing can be aborted by throwing an error. | Function | ```plaintext undefined ``` |
| ```plaintext depth ``` | Configure the maximum depth of the ```plaintext qs ``` library when ```plaintext extended ``` is ```plaintext true ``` . This allows you to limit the amount of keys that are parsed and can be useful to prevent certain types of abuse. Defaults to ```plaintext 32 ``` . It is recommended to keep this value as low as possible. | Number | ```plaintext 32 ``` |

The 
```plaintext
depth
```
 option was added in Express v4.20.0. If you are using an earlier version, this option will not be available.

[](https://expressjs.com/en/4x/api.html)

Application
-----------

The 
```plaintext
app
```
 object conventionally denotes the Express application. Create it by calling the top-level 
```plaintext
express()
```
 function exported by the Express module:

```
var express = require('express')
var app = express()

app.get('/', function (req, res) {
  res.send('hello world')
})

app.listen(3000)
```

The 
```plaintext
app
```
 object has methods for

*   Routing HTTP requests; see for example, [app.METHOD](https://expressjs.com/en/4x/api.html#app.METHOD) and [app.param](https://expressjs.com/en/4x/api.html#app.param).
*   Configuring middleware; see [app.route](https://expressjs.com/en/4x/api.html#app.route).
*   Rendering HTML views; see [app.render](https://expressjs.com/en/4x/api.html#app.render).
*   Registering a template engine; see [app.engine](https://expressjs.com/en/4x/api.html#app.engine).

It also has settings (properties) that affect how the application behaves; for more information, see [Application settings](https://expressjs.com/en/4x/api.html#app.settings.table).

The Express application object can be referred from the [request object](https://expressjs.com/en/4x/api.html#req) and the [response object](https://expressjs.com/en/4x/api.html#res) as 
```plaintext
req.app
```
, and 
```plaintext
res.app
```
, respectively.

### Properties

### app.locals

The 
```plaintext
app.locals
```
 object has properties that are local variables within the application, and will be available in templates rendered with [res.render](https://expressjs.com/en/4x/api.html#res.render).

The 
```plaintext
locals
```
 object is used by view engines to render a response. The object keys may be particularly sensitive and should not contain user-controlled input, as it may affect the operation of the view engine or provide a path to cross-site scripting. Consult the documentation for the used view engine for additional considerations.

```
console.dir(app.locals.title)
// => 'My App'

console.dir(app.locals.email)
// => '[email protected]'
```

Once set, the value of 
```plaintext
app.locals
```
 properties persist throughout the life of the application, in contrast with [res.locals](https://expressjs.com/en/4x/api.html#res.locals) properties that are valid only for the lifetime of the request.

You can access local variables in templates rendered within the application. This is useful for providing helper functions to templates, as well as application-level data. Local variables are available in middleware via 
```plaintext
req.app.locals
```
 (see [req.app](https://expressjs.com/en/4x/api.html#req.app))

```
app.locals.title = 'My App'
app.locals.strftime = require('strftime')
app.locals.email = '[email protected]'
```

### app.mountpath

The 
```plaintext
app.mountpath
```
 property contains one or more path patterns on which a sub-app was mounted.

A sub-app is an instance of 
```plaintext
express
```
 that may be used for handling the request to a route.

```
var express = require('express')

var app = express() // the main app
var admin = express() // the sub app

admin.get('/', function (req, res) {
  console.log(admin.mountpath) // /admin
  res.send('Admin Homepage')
})

app.use('/admin', admin) // mount the sub app
```

It is similar to the [baseUrl](https://expressjs.com/en/4x/api.html#req.baseUrl) property of the 
```plaintext
req
```
 object, except 
```plaintext
req.baseUrl
```
 returns the matched URL path, instead of the matched patterns.

If a sub-app is mounted on multiple path patterns, 
```plaintext
app.mountpath
```
 returns the list of patterns it is mounted on, as shown in the following example.

```
var admin = express()

admin.get('/', function (req, res) {
  console.dir(admin.mountpath) // [ '/adm*n', '/manager' ]
  res.send('Admin Homepage')
})

var secret = express()
secret.get('/', function (req, res) {
  console.log(secret.mountpath) // /secr*t
  res.send('Admin Secret')
})

admin.use('/secr*t', secret) // load the 'secret' router on '/secr*t', on the 'admin' sub app
app.use(['/adm*n', '/manager'], admin) // load the 'admin' router on '/adm*n' and '/manager', on the parent app
```

### Events

### app.on('mount', callback(parent))

The 
```plaintext
mount
```
 event is fired on a sub-app, when it is mounted on a parent app. The parent app is passed to the callback function.

**NOTE**

Sub-apps will:

*   Not inherit the value of settings that have a default value. You must set the value in the sub-app.
*   Inherit the value of settings with no default value.

For details, see [Application settings](https://expressjs.com/en/4x/api.html#app.settings.table).

```
var admin = express()

admin.on('mount', function (parent) {
  console.log('Admin Mounted')
  console.log(parent) // refers to the parent app
})

admin.get('/', function (req, res) {
  res.send('Admin Homepage')
})

app.use('/admin', admin)
```

### Methods

### app.all(path, callback [, callback ...])

This method is like the standard [app.METHOD()](https://expressjs.com/en/4x/api.html#app.METHOD) methods, except it matches all HTTP verbs.

#### Arguments

| Argument | Description | Default |
| --- | --- | --- |
| `path` | The path for which the middleware function is invoked; can be any of: * A string representing a path. * A path pattern. * A regular expression pattern to match paths. * An array of combinations of any of the above. For examples, see [Path examples](https://expressjs.com/en/4x/api.html#path-examples). | '/' (root path) |
| `callback` | Callback functions; can be: * A middleware function. * A series of middleware functions (separated by commas). * An array of middleware functions. * A combination of all of the above. You can provide multiple callback functions that behave just like middleware, except that these callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api.html#router) and [app](https://expressjs.com/en/4x/api.html#application) implement the middleware interface, you can use them as you would any other middleware function. For examples, see [Middleware callback function examples](https://expressjs.com/en/4x/api.html#middleware-callback-function-examples). | None |

#### Examples

The following callback is executed for requests to 
```plaintext
/secret
```
 whether using GET, POST, PUT, DELETE, or any other HTTP request method:

```
app.all('/secret', function (req, res, next) {
  console.log('Accessing the secret section ...')
  next() // pass control to the next handler
})
```

The 
```plaintext
app.all()
```
 method is useful for mapping “global” logic for specific path prefixes or arbitrary matches. For example, if you put the following at the top of all other route definitions, it requires that all routes from that point on require authentication, and automatically load a user. Keep in mind that these callbacks do not have to act as end-points: 
```plaintext
loadUser
```
 can perform a task, then call 
```plaintext
next()
```
 to continue matching subsequent routes.

```
app.all('*', requireAuthentication, loadUser)
```

Or the equivalent:

```
app.all('*', requireAuthentication)
app.all('*', loadUser)
```

Another example is white-listed “global” functionality. The example is similar to the ones above, but it only restricts paths that start with “/api”:

```
app.all('/api/*', requireAuthentication)
```

### app.delete(path, callback [, callback ...])

Routes HTTP DELETE requests to the specified path with the specified callback functions. For more information, see the [routing guide](https://expressjs.com/en/guide/routing.html).

#### Arguments

| Argument | Description | Default |
| --- | --- | --- |
| `path` | The path for which the middleware function is invoked; can be any of: * A string representing a path. * A path pattern. * A regular expression pattern to match paths. * An array of combinations of any of the above. For examples, see [Path examples](https://expressjs.com/en/4x/api.html#path-examples). | '/' (root path) |
| `callback` | Callback functions; can be: * A middleware function. * A series of middleware functions (separated by commas). * An array of middleware functions. * A combination of all of the above. You can provide multiple callback functions that behave just like middleware, except that these callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api.html#router) and [app](https://expressjs.com/en/4x/api.html#application) implement the middleware interface, you can use them as you would any other middleware function. For examples, see [Middleware callback function examples](https://expressjs.com/en/4x/api.html#middleware-callback-function-examples). | None |

#### Example

```
app.delete('/', function (req, res) {
  res.send('DELETE request to homepage')
})
```

### app.disable(name)

Sets the Boolean setting 
```plaintext
name
```
 to 
```plaintext
false
```
, where 
```plaintext
name
```
 is one of the properties from the [app settings table](https://expressjs.com/en/4x/api.html#app.settings.table). Calling 
```plaintext
app.set('foo', false)
```
 for a Boolean property is the same as calling 
```plaintext
app.disable('foo')
```
.

For example:

```
app.disable('trust proxy')
app.get('trust proxy')
// => false
```

### app.disabled(name)

Returns 
```plaintext
true
```
 if the Boolean setting 
```plaintext
name
```
 is disabled (
```plaintext
false
```
), where 
```plaintext
name
```
 is one of the properties from the [app settings table](https://expressjs.com/en/4x/api.html#app.settings.table).

```
app.disabled('trust proxy')
// => true

app.enable('trust proxy')
app.disabled('trust proxy')
// => false
```

### app.enable(name)

Sets the Boolean setting 
```plaintext
name
```
 to 
```plaintext
true
```
, where 
```plaintext
name
```
 is one of the properties from the [app settings table](https://expressjs.com/en/4x/api.html#app.settings.table). Calling 
```plaintext
app.set('foo', true)
```
 for a Boolean property is the same as calling 
```plaintext
app.enable('foo')
```
.

```
app.enable('trust proxy')
app.get('trust proxy')
// => true
```

### app.enabled(name)

Returns 
```plaintext
true
```
 if the setting 
```plaintext
name
```
 is enabled (
```plaintext
true
```
), where 
```plaintext
name
```
 is one of the properties from the [app settings table](https://expressjs.com/en/4x/api.html#app.settings.table).

```
app.enabled('trust proxy')
// => false

app.enable('trust proxy')
app.enabled('trust proxy')
// => true
```

### app.engine(ext, callback)

Registers the given template engine 
```plaintext
callback
```
 as 
```plaintext
ext
```
.

By default, Express will 
```plaintext
require()
```
 the engine based on the file extension. For example, if you try to render a “foo.pug” file, Express invokes the following internally, and caches the 
```plaintext
require()
```
 on subsequent calls to increase performance.

```
app.engine('pug', require('pug').__express)
```

Use this method for engines that do not provide 
```plaintext
.__express
```
 out of the box, or if you wish to “map” a different extension to the template engine.

For example, to map the EJS template engine to “.html” files:

```
app.engine('html', require('ejs').renderFile)
```

In this case, EJS provides a 
```plaintext
.renderFile()
```
 method with the same signature that Express expects: 
```plaintext
(path, options, callback)
```
, though note that it aliases this method as 
```plaintext
ejs.__express
```
 internally so if you’re using “.ejs” extensions you don’t need to do anything.

Some template engines do not follow this convention. The [consolidate.js](https://github.com/tj/consolidate.js) library maps Node template engines to follow this convention, so they work seamlessly with Express.

```
var engines = require('consolidate')
app.engine('haml', engines.haml)
app.engine('html', engines.hogan)
```

### app.get(name)

Returns the value of 
```plaintext
name
```
 app setting, where 
```plaintext
name
```
 is one of the strings in the [app settings table](https://expressjs.com/en/4x/api.html#app.settings.table). For example:

```
app.get('title')
// => undefined

app.set('title', 'My Site')
app.get('title')
// => "My Site"
```

### app.get(path, callback [, callback ...])

Routes HTTP GET requests to the specified path with the specified callback functions.

#### Arguments

| Argument | Description | Default |
| --- | --- | --- |
| `path` | The path for which the middleware function is invoked; can be any of: * A string representing a path. * A path pattern. * A regular expression pattern to match paths. * An array of combinations of any of the above. For examples, see [Path examples](https://expressjs.com/en/4x/api.html#path-examples). | '/' (root path) |
| `callback` | Callback functions; can be: * A middleware function. * A series of middleware functions (separated by commas). * An array of middleware functions. * A combination of all of the above. You can provide multiple callback functions that behave just like middleware, except that these callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api.html#router) and [app](https://expressjs.com/en/4x/api.html#application) implement the middleware interface, you can use them as you would any other middleware function. For examples, see [Middleware callback function examples](https://expressjs.com/en/4x/api.html#middleware-callback-function-examples). | None |

For more information, see the [routing guide](https://expressjs.com/en/guide/routing.html).

#### Example

```
app.get('/', function (req, res) {
  res.send('GET request to homepage')
})
```

### app.listen(path, [callback])

Starts a UNIX socket and listens for connections on the given path. This method is identical to Node’s [http.Server.listen()](https://nodejs.org/api/http.html#http_server_listen).

```
var express = require('express')
var app = express()
app.listen('/tmp/sock')
```

### app.listen([port[, host[, backlog]]][, callback])

Binds and listens for connections on the specified host and port. This method is identical to Node’s [http.Server.listen()](https://nodejs.org/api/http.html#http_server_listen).

If port is omitted or is 0, the operating system will assign an arbitrary unused port, which is useful for cases like automated tasks (tests, etc.).

```
var express = require('express')
var app = express()
app.listen(3000)
```

The 
```plaintext
app
```
 returned by 
```plaintext
express()
```
 is in fact a JavaScript 
```plaintext
Function
```
, designed to be passed to Node’s HTTP servers as a callback to handle requests. This makes it easy to provide both HTTP and HTTPS versions of your app with the same code base, as the app does not inherit from these (it is simply a callback):

```
var express = require('express')
var https = require('https')
var http = require('http')
var app = express()

http.createServer(app).listen(80)
https.createServer(options, app).listen(443)
```

The 
```plaintext
app.listen()
```
 method returns an [http.Server](https://nodejs.org/api/http.html#http_class_http_server) object and (for HTTP) is a convenience method for the following:

```
app.listen = function () {
  var server = http.createServer(this)
  return server.listen.apply(server, arguments)
}
```

Note

All the forms of Node’s [http.Server.listen()](https://nodejs.org/api/http.html#http_server_listen) method are in fact actually supported.

### app.METHOD(path, callback [, callback ...])

Routes an HTTP request, where METHOD is the HTTP method of the request, such as GET, PUT, POST, and so on, in lowercase. Thus, the actual methods are 
```plaintext
app.get()
```
, 
```plaintext
app.post()
```
, 
```plaintext
app.put()
```
, and so on. See [Routing methods](https://expressjs.com/en/4x/api.html#routing-methods) below for the complete list.

#### Arguments

| Argument | Description | Default |
| --- | --- | --- |
| `path` | The path for which the middleware function is invoked; can be any of: * A string representing a path. * A path pattern. * A regular expression pattern to match paths. * An array of combinations of any of the above. For examples, see [Path examples](https://expressjs.com/en/4x/api.html#path-examples). | '/' (root path) |
| `callback` | Callback functions; can be: * A middleware function. * A series of middleware functions (separated by commas). * An array of middleware functions. * A combination of all of the above. You can provide multiple callback functions that behave just like middleware, except that these callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api.html#router) and [app](https://expressjs.com/en/4x/api.html#application) implement the middleware interface, you can use them as you would any other middleware function. For examples, see [Middleware callback function examples](https://expressjs.com/en/4x/api.html#middleware-callback-function-examples). | None |

#### Routing methods

Express supports the following routing methods corresponding to the HTTP methods of the same names:

*   `checkout`
*   `copy`
*   `delete`
*   `get`
*   `head`
*   `lock`
*   `merge`
*   `mkactivity`

*   `mkcol`
*   `move`
*   `m-search`
*   `notify`
*   `options`
*   `patch`
*   `post`

*   `purge`
*   `put`
*   `report`
*   `search`
*   `subscribe`
*   `trace`
*   `unlock`
*   `unsubscribe`

The API documentation has explicit entries only for the most popular HTTP methods 
```plaintext
app.get()
```
, 
```plaintext
app.post()
```
, 
```plaintext
app.put()
```
, and 
```plaintext
app.delete()
```
. However, the other methods listed above work in exactly the same way.

To route methods that translate to invalid JavaScript variable names, use the bracket notation. For example, 
```plaintext
app['m-search']('/', function ...
```
.

The 
```plaintext
app.get()
```
 function is automatically called for the HTTP 
```plaintext
HEAD
```
 method in addition to the 
```plaintext
GET
```
 method if 
```plaintext
app.head()
```
 was not called for the path before 
```plaintext
app.get()
```
.

The method, 
```plaintext
app.all()
```
, is not derived from any HTTP method and loads middleware at the specified path for _all_ HTTP request methods. For more information, see [app.all](https://expressjs.com/en/4x/api.html#app.all).

For more information on routing, see the [routing guide](https://expressjs.com/en/guide/routing.html).

### app.param([name], callback)

Add callback triggers to [route parameters](https://expressjs.com/en/guide/routing.html#route-parameters), where 
```plaintext
name
```
 is the name of the parameter or an array of them, and 
```plaintext
callback
```
 is the callback function. The parameters of the callback function are the request object, the response object, the next middleware, the value of the parameter and the name of the parameter, in that order.

If 
```plaintext
name
```
 is an array, the 
```plaintext
callback
```
 trigger is registered for each parameter declared in it, in the order in which they are declared. Furthermore, for each declared parameter except the last one, a call to 
```plaintext
next
```
 inside the callback will call the callback for the next declared parameter. For the last parameter, a call to 
```plaintext
next
```
 will call the next middleware in place for the route currently being processed, just like it would if 
```plaintext
name
```
 were just a string.

For example, when 
```plaintext
:user
```
 is present in a route path, you may map user loading logic to automatically provide 
```plaintext
req.user
```
 to the route, or perform validations on the parameter input.

```
app.param('user', function (req, res, next, id) {
  // try to get the user details from the User model and attach it to the request object
  User.find(id, function (err, user) {
    if (err) {
      next(err)
    } else if (user) {
      req.user = user
      next()
    } else {
      next(new Error('failed to load user'))
    }
  })
})
```

Param callback functions are local to the router on which they are defined. They are not inherited by mounted apps or routers, nor are they triggered for route parameters inherited from parent routers. Hence, param callbacks defined on 
```plaintext
app
```
 will be triggered only by route parameters defined on 
```plaintext
app
```
 routes.

All param callbacks will be called before any handler of any route in which the param occurs, and they will each be called only once in a request-response cycle, even if the parameter is matched in multiple routes, as shown in the following examples.

```
app.param('id', function (req, res, next, id) {
  console.log('CALLED ONLY ONCE')
  next()
})

app.get('/user/:id', function (req, res, next) {
  console.log('although this matches')
  next()
})

app.get('/user/:id', function (req, res) {
  console.log('and this matches too')
  res.end()
})
```

On 
```plaintext
GET /user/42
```
, the following is printed:

```
CALLED ONLY ONCE
although this matches
and this matches too
```

```
app.param(['id', 'page'], function (req, res, next, value) {
  console.log('CALLED ONLY ONCE with', value)
  next()
})

app.get('/user/:id/:page', function (req, res, next) {
  console.log('although this matches')
  next()
})

app.get('/user/:id/:page', function (req, res) {
  console.log('and this matches too')
  res.end()
})
```

On 
```plaintext
GET /user/42/3
```
, the following is printed:

```
CALLED ONLY ONCE with 42
CALLED ONLY ONCE with 3
although this matches
and this matches too
```

The following section describes 
```plaintext
app.param(callback)
```
, which is deprecated as of v4.11.0.

The behavior of the 
```plaintext
app.param(name, callback)
```
 method can be altered entirely by passing only a function to 
```plaintext
app.param()
```
. This function is a custom implementation of how 
```plaintext
app.param(name, callback)
```
 should behave - it accepts two parameters and must return a middleware.

The first parameter of this function is the name of the URL parameter that should be captured, the second parameter can be any JavaScript object which might be used for returning the middleware implementation.

The middleware returned by the function decides the behavior of what happens when a URL parameter is captured.

In this example, the 
```plaintext
app.param(name, callback)
```
 signature is modified to 
```plaintext
app.param(name, accessId)
```
. Instead of accepting a name and a callback, 
```plaintext
app.param()
```
 will now accept a name and a number.

```
var express = require('express')
var app = express()

// customizing the behavior of app.param()
app.param(function (param, option) {
  return function (req, res, next, val) {
    if (val === option) {
      next()
    } else {
      next('route')
    }
  }
})

// using the customized app.param()
app.param('id', 1337)

// route to trigger the capture
app.get('/user/:id', function (req, res) {
  res.send('OK')
})

app.listen(3000, function () {
  console.log('Ready')
})
```

In this example, the 
```plaintext
app.param(name, callback)
```
 signature remains the same, but instead of a middleware callback, a custom data type checking function has been defined to validate the data type of the user id.

```
app.param(function (param, validator) {
  return function (req, res, next, val) {
    if (validator(val)) {
      next()
    } else {
      next('route')
    }
  }
})

app.param('id', function (candidate) {
  return !isNaN(parseFloat(candidate)) && isFinite(candidate)
})
```

The ‘
```plaintext
.
```
’ character can’t be used to capture a character in your capturing regexp. For example you can’t use 
```plaintext
'/user-.+/'
```
 to capture 
```plaintext
'users-gami'
```
, use 
```plaintext
[\\s\\S]
```
 or 
```plaintext
[\\w\\W]
```
 instead (as in 
```plaintext
'/user-[\\s\\S]+/'
```
.

Examples:

```
// captures '1-a_6' but not '543-azser-sder'
router.get('/[0-9]+-[[\\w]]*', function (req, res, next) { next() })

// captures '1-a_6' and '543-az(ser"-sder' but not '5-a s'
router.get('/[0-9]+-[[\\S]]*', function (req, res, next) { next() })

// captures all (equivalent to '.*')
router.get('[[\\s\\S]]*', function (req, res, next) { next() })
```

### app.path()

Returns the canonical path of the app, a string.

```
var app = express()
var blog = express()
var blogAdmin = express()

app.use('/blog', blog)
blog.use('/admin', blogAdmin)

console.dir(app.path()) // ''
console.dir(blog.path()) // '/blog'
console.dir(blogAdmin.path()) // '/blog/admin'
```

The behavior of this method can become very complicated in complex cases of mounted apps: it is usually better to use [req.baseUrl](https://expressjs.com/en/4x/api.html#req.baseUrl) to get the canonical path of the app.

### app.post(path, callback [, callback ...])

Routes HTTP POST requests to the specified path with the specified callback functions. For more information, see the [routing guide](https://expressjs.com/en/guide/routing.html).

#### Arguments

| Argument | Description | Default |
| --- | --- | --- |
| `path` | The path for which the middleware function is invoked; can be any of: * A string representing a path. * A path pattern. * A regular expression pattern to match paths. * An array of combinations of any of the above. For examples, see [Path examples](https://expressjs.com/en/4x/api.html#path-examples). | '/' (root path) |
| `callback` | Callback functions; can be: * A middleware function. * A series of middleware functions (separated by commas). * An array of middleware functions. * A combination of all of the above. You can provide multiple callback functions that behave just like middleware, except that these callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api.html#router) and [app](https://expressjs.com/en/4x/api.html#application) implement the middleware interface, you can use them as you would any other middleware function. For examples, see [Middleware callback function examples](https://expressjs.com/en/4x/api.html#middleware-callback-function-examples). | None |

#### Example

```
app.post('/', function (req, res) {
  res.send('POST request to homepage')
})
```

### app.put(path, callback [, callback ...])

Routes HTTP PUT requests to the specified path with the specified callback functions.

#### Arguments

| Argument | Description | Default |
| --- | --- | --- |
| `path` | The path for which the middleware function is invoked; can be any of: * A string representing a path. * A path pattern. * A regular expression pattern to match paths. * An array of combinations of any of the above. For examples, see [Path examples](https://expressjs.com/en/4x/api.html#path-examples). | '/' (root path) |
| `callback` | Callback functions; can be: * A middleware function. * A series of middleware functions (separated by commas). * An array of middleware functions. * A combination of all of the above. You can provide multiple callback functions that behave just like middleware, except that these callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api.html#router) and [app](https://expressjs.com/en/4x/api.html#application) implement the middleware interface, you can use them as you would any other middleware function. For examples, see [Middleware callback function examples](https://expressjs.com/en/4x/api.html#middleware-callback-function-examples). | None |

#### Example

```
app.put('/', function (req, res) {
  res.send('PUT request to homepage')
})
```

### app.render(view, [locals], callback)

Returns the rendered HTML of a view via the 
```plaintext
callback
```
 function. It accepts an optional parameter that is an object containing local variables for the view. It is like [res.render()](https://expressjs.com/en/4x/api.html#res.render), except it cannot send the rendered view to the client on its own.

Think of 
```plaintext
app.render()
```
 as a utility function for generating rendered view strings. Internally 
```plaintext
res.render()
```
 uses 
```plaintext
app.render()
```
 to render views.

The 
```plaintext
view
```
 argument performs file system operations like reading a file from disk and evaluating Node.js modules, and as so for security reasons should not contain input from the end-user.

The 
```plaintext
locals
```
 object is used by view engines to render a response. The object keys may be particularly sensitive and should not contain user-controlled input, as it may affect the operation of the view engine or provide a path to cross-site scripting. Consult the documentation for the used view engine for additional considerations.

The local variable 
```plaintext
cache
```
 is reserved for enabling view cache. Set it to 
```plaintext
true
```
, if you want to cache view during development; view caching is enabled in production by default.

```
app.render('email', function (err, html) {
  // ...
})

app.render('email', { name: 'Tobi' }, function (err, html) {
  // ...
})
```

### app.route(path)

Returns an instance of a single route, which you can then use to handle HTTP verbs with optional middleware. Use 
```plaintext
app.route()
```
 to avoid duplicate route names (and thus typo errors).

```
var app = express()

app.route('/events')
  .all(function (req, res, next) {
    // runs for all HTTP verbs first
    // think of it as route specific middleware!
  })
  .get(function (req, res, next) {
    res.json({})
  })
  .post(function (req, res, next) {
    // maybe add a new event...
  })
```

### app.set(name, value)

Assigns setting 
```plaintext
name
```
 to 
```plaintext
value
```
. You may store any value that you want, but certain names can be used to configure the behavior of the server. These special names are listed in the [app settings table](https://expressjs.com/en/4x/api.html#app.settings.table).

Calling 
```plaintext
app.set('foo', true)
```
 for a Boolean property is the same as calling 
```plaintext
app.enable('foo')
```
. Similarly, calling 
```plaintext
app.set('foo', false)
```
 for a Boolean property is the same as calling 
```plaintext
app.disable('foo')
```
.

Retrieve the value of a setting with [```plaintext app.get() ```](https://expressjs.com/en/4x/api.html#app.get).

```
app.set('title', 'My Site')
app.get('title') // "My Site"
```

#### Application Settings

The following table lists application settings.

Note that sub-apps will:

*   Not inherit the value of settings that have a default value. You must set the value in the sub-app.
*   Inherit the value of settings with no default value; these are explicitly noted in the table below.

Exceptions: Sub-apps will inherit the value of 
```plaintext
trust proxy
```
 even though it has a default value (for backward-compatibility); Sub-apps will not inherit the value of 
```plaintext
view cache
```
 in production (when 
```plaintext
NODE_ENV
```
 is “production”).

| Property | Type | Description | Default |
| --- | --- | --- | --- |
| ```plaintext case sensitive routing ``` | Boolean | Enable case sensitivity. When enabled, "/Foo" and "/foo" are different routes. When disabled, "/Foo" and "/foo" are treated the same. **NOTE**: Sub-apps will inherit the value of this setting. | N/A (undefined) |
| ```plaintext env ``` | String | Environment mode. Be sure to set to “production” in a production environment; see [Production best practices: performance and reliability](https://expressjs.com/en/advanced/best-practice-performance.html#env). | ```plaintext process.env.NODE_ENV ``` ( ```plaintext NODE_ENV ``` environment variable) or “development” if ```plaintext NODE_ENV ``` is not set. |
| ```plaintext etag ``` | Varied | Set the ETag response header. For possible values, see the [```plaintext etag ``` options table](https://expressjs.com/en/4x/api.html#etag.options.table). [More about the HTTP ETag header](http://en.wikipedia.org/wiki/HTTP_ETag). | ```plaintext weak ``` |
| ```plaintext jsonp callback name ``` | String | Specifies the default JSONP callback name. | “callback” |
| ```plaintext json escape ``` | Boolean | Enable escaping JSON responses from the ```plaintext res.json ``` , ```plaintext res.jsonp ``` , and ```plaintext res.send ``` APIs. This will escape the characters ```plaintext < ``` , ```plaintext > ``` , and ```plaintext & ``` as Unicode escape sequences in JSON. The purpose of this it to assist with [mitigating certain types of persistent XSS attacks](https://blog.mozilla.org/security/2017/07/18/web-service-audits-firefox-accounts/) when clients sniff responses for HTML. **NOTE**: Sub-apps will inherit the value of this setting. | N/A (undefined) |
| ```plaintext json replacer ``` | Varied | The ['replacer' argument used by `JSON.stringify`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#The_replacer_parameter). **NOTE**: Sub-apps will inherit the value of this setting. | N/A (undefined) |
| ```plaintext json spaces ``` | Varied | The ['space' argument used by `JSON.stringify`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#The_space_argument). This is typically set to the number of spaces to use to indent prettified JSON. **NOTE**: Sub-apps will inherit the value of this setting. | N/A (undefined) |
| ```plaintext query parser ``` | Varied | Disable query parsing by setting the value to ```plaintext false ``` , or set the query parser to use either “simple” or “extended” or a custom query string parsing function. The simple query parser is based on Node’s native query parser, [querystring](http://nodejs.org/api/querystring.html). The extended query parser is based on [qs](https://www.npmjs.org/package/qs). A custom query string parsing function will receive the complete query string, and must return an object of query keys and their values. | "extended" |
| ```plaintext strict routing ``` | Boolean | Enable strict routing. When enabled, the router treats "/foo" and "/foo/" as different. Otherwise, the router treats "/foo" and "/foo/" as the same. **NOTE**: Sub-apps will inherit the value of this setting. | N/A (undefined) |
| ```plaintext subdomain offset ``` | Number | The number of dot-separated parts of the host to remove to access subdomain. | 2 |
| ```plaintext trust proxy ``` | Varied | Indicates the app is behind a front-facing proxy, and to use the ```plaintext X-Forwarded-* ``` headers to determine the connection and the IP address of the client. NOTE: ```plaintext X-Forwarded-* ``` headers are easily spoofed and the detected IP addresses are unreliable. When enabled, Express attempts to determine the IP address of the client connected through the front-facing proxy, or series of proxies. The `req.ips` property, then contains an array of IP addresses the client is connected through. To enable it, use the values described in the [trust proxy options table](https://expressjs.com/en/4x/api.html#trust.proxy.options.table). The `trust proxy` setting is implemented using the [proxy-addr](https://www.npmjs.org/package/proxy-addr) package. For more information, see its documentation. **NOTE**: Sub-apps _will_ inherit the value of this setting, even though it has a default value. | ```plaintext false ``` (disabled) |
| ```plaintext views ``` | String or Array | A directory or an array of directories for the application's views. If an array, the views are looked up in the order they occur in the array. | ```plaintext process.cwd() + '/views' ``` |
| ```plaintext view cache ``` | Boolean | Enables view template compilation caching. **NOTE**: Sub-apps will not inherit the value of this setting in production (when `NODE_ENV` is "production"). | ```plaintext true ``` in production, otherwise undefined. |
| ```plaintext view engine ``` | String | The default engine extension to use when omitted. **NOTE**: Sub-apps will inherit the value of this setting. | N/A (undefined) |
| ```plaintext x-powered-by ``` | Boolean | Enables the "X-Powered-By: Express" HTTP header. | ```plaintext true ``` |

##### Options for `trust proxy` setting

Read [Express behind proxies](https://expressjs.com/en/guide/behind-proxies.html) for more information.

| Type | Value |
| --- | --- |
| Boolean | If ```plaintext true ``` , the client’s IP address is understood as the left-most entry in the ```plaintext X-Forwarded-* ``` header. If ```plaintext false ``` , the app is understood as directly facing the Internet and the client’s IP address is derived from ```plaintext req.connection.remoteAddress ``` . This is the default setting. |
| String String containing comma-separated values Array of strings | An IP address, subnet, or an array of IP addresses, and subnets to trust. Pre-configured subnet names are: * loopback - ```plaintext 127.0.0.1/8 ``` , ```plaintext ::1/128 ``` * linklocal - ```plaintext 169.254.0.0/16 ``` , ```plaintext fe80::/10 ``` * uniquelocal - ```plaintext 10.0.0.0/8 ``` , ```plaintext 172.16.0.0/12 ``` , ```plaintext 192.168.0.0/16 ``` , ```plaintext fc00::/7 ``` Set IP addresses in any of the following ways: Specify a single subnet: ``` app.set('trust proxy', 'loopback') ``` Specify a subnet and an address: ``` app.set('trust proxy', 'loopback, 123.123.123.123') ``` Specify multiple subnets as CSV: ``` app.set('trust proxy', 'loopback, linklocal, uniquelocal') ``` Specify multiple subnets as an array: ``` app.set('trust proxy', ['loopback', 'linklocal', 'uniquelocal']) ``` When specified, the IP addresses or the subnets are excluded from the address determination process, and the untrusted IP address nearest to the application server is determined as the client’s IP address. |
| Number | Trust the _n_ th hop from the front-facing proxy server as the client. |
| Function | Custom trust implementation. Use this only if you know what you are doing. ``` app.set('trust proxy', function (ip) { if (ip === '127.0.0.1' || ip === '123.123.123.123') return true // trusted IPs else return false }) ``` |

##### Options for `etag` setting

**NOTE**: These settings apply only to dynamic files, not static files. The [express.static](https://expressjs.com/en/4x/api.html#express.static) middleware ignores these settings.

The ETag functionality is implemented using the [etag](https://www.npmjs.org/package/etag) package. For more information, see its documentation.

| Type | Value |
| --- | --- |
| Boolean | ```plaintext true ``` enables weak ETag. This is the default setting. ```plaintext false ``` disables ETag altogether. |
| String | If "strong", enables strong ETag. If "weak", enables weak ETag. |
| Function | Custom ETag function implementation. Use this only if you know what you are doing. ``` app.set('etag', function (body, encoding) { return generateHash(body, encoding) // consider the function is defined }) ``` |

### app.use([path,] callback [, callback...])

Mounts the specified [middleware](https://expressjs.com/en/guide/using-middleware.html) function or functions at the specified path: the middleware function is executed when the base of the requested path matches 
```plaintext
path
```
.

#### Arguments

| Argument | Description | Default |
| --- | --- | --- |
| `path` | The path for which the middleware function is invoked; can be any of: * A string representing a path. * A path pattern. * A regular expression pattern to match paths. * An array of combinations of any of the above. For examples, see [Path examples](https://expressjs.com/en/4x/api.html#path-examples). | '/' (root path) |
| `callback` | Callback functions; can be: * A middleware function. * A series of middleware functions (separated by commas). * An array of middleware functions. * A combination of all of the above. You can provide multiple callback functions that behave just like middleware, except that these callbacks can invoke `next('route')` to bypass the remaining route callback(s). You can use this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if there is no reason to proceed with the current route. Since [router](https://expressjs.com/en/4x/api.html#router) and [app](https://expressjs.com/en/4x/api.html#application) implement the middleware interface, you can use them as you would any other middleware function. For examples, see [Middleware callback function examples](https://expressjs.com/en/4x/api.html#middleware-callback-function-examples). | None |

#### Description

A route will match any path that follows its path immediately with a “
```plaintext
/
```
”. For example: 
```plaintext
app.use('/apple', ...)
```
 will match “/apple”, “/apple/images”, “/apple/images/news”, and so on.

Since 
```plaintext
path
```
 defaults to “/”, middleware mounted without a path will be executed for every request to the app. For example, this middleware function will be executed for _every_ request to the app:

```
app.use(function (req, res, next) {
  console.log('Time: %d', Date.now())
  next()
})
```

**NOTE**

Sub-apps will:

*   Not inherit the value of settings that have a default value. You must set the value in the sub-app.
*   Inherit the value of settings with no default value.

For details, see [Application settings](https://expressjs.com/en/4x/api.html#app.settings.table).

Middleware functions are executed sequentially, therefore the order of middleware inclusion is important.

```
// this middleware will not allow the request to go beyond it
app.use(function (req, res, next) {
  res.send('Hello World')
})

// requests will never reach this route
app.get('/', function (req, res) {
  res.send('Welcome')
})
```

**Error-handling middleware**

Error-handling middleware always takes _four_ arguments. You must provide four arguments to identify it as an error-handling middleware function. Even if you don’t need to use the 
```plaintext
next
```
 object, you must specify it to maintain the signature. Otherwise, the 
```plaintext
next
```
 object will be interpreted as regular middleware and will fail to handle errors. For details about error-handling middleware, see: [Error handling](https://expressjs.com/en/guide/error-handling.html).

Define error-handling middleware functions in the same way as other middleware functions, except with four arguments instead of three, specifically with the signature 
```plaintext
(err, req, res, next)
```
):

```
app.use(function (err, req, res, next) {
  console.error(err.stack)
  res.status(500).send('Something broke!')
})
```

#### Path examples

The following table provides some simple examples of valid 
```plaintext
path
```
 values for mounting middleware.

| Type | Example |
| --- | --- |
| Path | Matches the exact path ```plaintext /abcd ``` and any sub-paths starting with ```plaintext /abcd/ ``` (for example, ```plaintext /abcd/foo ``` ): ``` app.use('/abcd', function (req, res, next) { next() }) ``` |
| Path Pattern | This will match paths starting with ```plaintext /abcd ``` and ```plaintext /abd ``` : ``` app.use('/abc?d', function (req, res, next) { next() }) ``` This will match paths starting with ```plaintext /abcd ``` , ```plaintext /abbcd ``` , ```plaintext /abbbbbcd ``` , and so on: ``` app.use('/ab+cd', function (req, res, next) { next() }) ``` This will match paths starting with ```plaintext /abcd ``` , ```plaintext /abxcd ``` , ```plaintext /abFOOcd ``` , ```plaintext /abbArcd ``` , and so on: ``` app.use('/ab*cd', function (req, res, next) { next() }) ``` This will match paths starting with ```plaintext /ad ``` and ```plaintext /abcd ``` : ``` app.use('/a(bc)?d', function (req, res, next) { next() }) ``` |
| Regular Expression | This will match paths starting with ```plaintext /abc ``` and ```plaintext /xyz ``` : ``` app.use(/\/abc|\/xyz/, function (req, res, next) { next() }) ``` |
| Array | This will match paths starting with ```plaintext /abcd ``` , ```plaintext /xyza ``` , ```plaintext /lmn ``` , and ```plaintext /pqr ``` : ``` app.use(['/abcd', '/xyza', /\/lmn|\/pqr/], function (req, res, next) { next() }) ``` |

#### Middleware callback function examples

The following table provides some simple examples of middleware functions that can be used as the 
```plaintext
callback
```
 argument to 
```plaintext
app.use()
```
, 
```plaintext
app.METHOD()
```
, and 
```plaintext
app.all()
```
.

| Usage | Example |
| --- | --- |
| Single Middleware | You can define and mount a middleware function locally. ``` app.use(function (req, res, next) { next() }) ``` A router is valid middleware. ``` var router = express.Router() router.get('/', function (req, res, next) { next() }) app.use(router) ``` An Express app is valid middleware. ``` var subApp = express() subApp.get('/', function (req, res, next) { next() }) app.use(subApp) ``` |
| Series of Middleware | You can specify more than one middleware function at the same mount path. ``` var r1 = express.Router() r1.get('/', function (req, res, next) { next() }) var r2 = express.Router() r2.get('/', function (req, res, next) { next() }) app.use(r1, r2) ``` |
| Array | Use an array to group middleware logically. ``` var r1 = express.Router() r1.get('/', function (req, res, next) { next() }) var r2 = express.Router() r2.get('/', function (req, res, next) { next() }) app.use([r1, r2]) ``` |
| Combination | You can combine all the above ways of mounting middleware. ``` function mw1 (req, res, next) { next() } function mw2 (req, res, next) { next() } var r1 = express.Router() r1.get('/', function (req, res, next) { next() }) var r2 = express.Router() r2.get('/', function (req, res, next) { next() }) var subApp = express() subApp.get('/', function (req, res, next) { next() }) app.use(mw1, [mw2, r1, r2], subApp) ``` |

</div>

Following are some examples of using the [express.static](https://expressjs.com/en/guide/using-middleware.html#middleware.built-in) middleware in an Express app.

Serve static content for the app from the “public” directory in the application directory:

```
// GET /style.css etc
app.use(express.static(path.join(__dirname, 'public')))
```

Mount the middleware at “/static” to serve static content only when their request path is prefixed with “/static”:

```
// GET /static/style.css etc.
app.use('/static', express.static(path.join(__dirname, 'public')))
```

Disable logging for static content requests by loading the logger middleware after the static middleware:

```
app.use(express.static(path.join(__dirname, 'public')))
app.use(logger())
```

Serve static files from multiple directories, but give precedence to “./public” over the others:

```
app.use(express.static(path.join(__dirname, 'public')))
app.use(express.static(path.join(__dirname, 'files')))
app.use(express.static(path.join(__dirname, 'uploads')))
```

[](https://expressjs.com/en/4x/api.html)

Request
-------

The 
```plaintext
req
```
 object represents the HTTP request and has properties for the request query string, parameters, body, HTTP headers, and so on. In this documentation and by convention, the object is always referred to as 
```plaintext
req
```
 (and the HTTP response is 
```plaintext
res
```
) but its actual name is determined by the parameters to the callback function in which you’re working.

For example:

```
app.get('/user/:id', function (req, res) {
  res.send('user ' + req.params.id)
})
```

But you could just as well have:

```
app.get('/user/:id', function (request, response) {
  response.send('user ' + request.params.id)
})
```

The 
```plaintext
req
```
 object is an enhanced version of Node’s own request object and supports all [built-in fields and methods](https://nodejs.org/api/http.html#http_class_http_incomingmessage).

### Properties

In Express 4, 
```plaintext
req.files
```
 is no longer available on the 
```plaintext
req
```
 object by default. To access uploaded files on the 
```plaintext
req.files
```
 object, use multipart-handling middleware like [busboy](https://www.npmjs.com/package/busboy), [multer](https://www.npmjs.com/package/multer), [formidable](https://www.npmjs.com/package/formidable), [multiparty](https://www.npmjs.com/package/multiparty), [connect-multiparty](https://www.npmjs.com/package/connect-multiparty), or [pez](https://www.npmjs.com/package/pez).

### req.app

This property holds a reference to the instance of the Express application that is using the middleware.

If you follow the pattern in which you create a module that just exports a middleware function and 
```plaintext
require()
```
 it in your main file, then the middleware can access the Express instance via 
```plaintext
req.app
```

For example:

```
// index.js
app.get('/viewdirectory', require('./mymiddleware.js'))
```

```
// mymiddleware.js
module.exports = function (req, res) {
  res.send('The views directory is ' + req.app.get('views'))
}
```

### req.baseUrl

The URL path on which a router instance was mounted.

The 
```plaintext
req.baseUrl
```
 property is similar to the [mountpath](https://expressjs.com/en/4x/api.html#app.mountpath) property of the 
```plaintext
app
```
 object, except 
```plaintext
app.mountpath
```
 returns the matched path pattern(s).

For example:

```
var greet = express.Router()

greet.get('/jp', function (req, res) {
  console.log(req.baseUrl) // /greet
  res.send('Konnichiwa!')
})

app.use('/greet', greet) // load the router on '/greet'
```

Even if you use a path pattern or a set of path patterns to load the router, the 
```plaintext
baseUrl
```
 property returns the matched string, not the pattern(s). In the following example, the 
```plaintext
greet
```
 router is loaded on two path patterns.

```
app.use(['/gre+t', '/hel{2}o'], greet) // load the router on '/gre+t' and '/hel{2}o'
```

When a request is made to 
```plaintext
/greet/jp
```
, 
```plaintext
req.baseUrl
```
 is “/greet”. When a request is made to 
```plaintext
/hello/jp
```
, 
```plaintext
req.baseUrl
```
 is “/hello”.

### req.body

Contains key-value pairs of data submitted in the request body. By default, it is 
```plaintext
undefined
```
, and is populated when you use body-parsing middleware such as [```plaintext express.json() ```](https://expressjs.com/en/4x/api.html#express.json) or [```plaintext express.urlencoded() ```](https://expressjs.com/en/4x/api.html#express.urlencoded).

As 
```plaintext
req.body
```
’s shape is based on user-controlled input, all properties and values in this object are untrusted and should be validated before trusting. For example, 
```plaintext
req.body.foo.toString()
```
 may fail in multiple ways, for example 
```plaintext
foo
```
 may not be there or may not be a string, and 
```plaintext
toString
```
 may not be a function and instead a string or other user-input.

The following example shows how to use body-parsing middleware to populate 
```plaintext
req.body
```
.

```
var express = require('express')

var app = express()

app.use(express.json()) // for parsing application/json
app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded

app.post('/profile', function (req, res, next) {
  console.log(req.body)
  res.json(req.body)
})
```

### req.cookies

When using [cookie-parser](https://www.npmjs.com/package/cookie-parser) middleware, this property is an object that contains cookies sent by the request. If the request contains no cookies, it defaults to 
```plaintext
{}
```
.

```
// Cookie: name=tj
console.dir(req.cookies.name)
// => 'tj'
```

If the cookie has been signed, you have to use [req.signedCookies](https://expressjs.com/en/4x/api.html#req.signedCookies).

For more information, issues, or concerns, see [cookie-parser](https://github.com/expressjs/cookie-parser).

### req.fresh

When the response is still “fresh” in the client’s cache 
```plaintext
true
```
 is returned, otherwise 
```plaintext
false
```
 is returned to indicate that the client cache is now stale and the full response should be sent.

When a client sends the 
```plaintext
Cache-Control: no-cache
```
 request header to indicate an end-to-end reload request, this module will return 
```plaintext
false
```
 to make handling these requests transparent.

Further details for how cache validation works can be found in the [HTTP/1.1 Caching Specification](https://tools.ietf.org/html/rfc7234).

```
console.dir(req.fresh)
// => true
```

### req.hostname

Contains the hostname derived from the 
```plaintext
Host
```
 HTTP header.

When the [```plaintext trust proxy ``` setting](https://expressjs.com/4x/api.html#trust.proxy.options.table) does not evaluate to 
```plaintext
false
```
, this property will instead get the value from the 
```plaintext
X-Forwarded-Host
```
 header field. This header can be set by the client or by the proxy.

If there is more than one 
```plaintext
X-Forwarded-Host
```
 header in the request, the value of the first header is used. This includes a single header with comma-separated values, in which the first value is used.

Prior to Express v4.17.0, the 
```plaintext
X-Forwarded-Host
```
 could not contain multiple values or be present more than once.

```
// Host: "example.com:3000"
console.dir(req.hostname)
// => 'example.com'
```

### req.ip

Contains the remote IP address of the request.

When the [```plaintext trust proxy ``` setting](https://expressjs.com/4x/api.html#trust.proxy.options.table) does not evaluate to 
```plaintext
false
```
, the value of this property is derived from the left-most entry in the 
```plaintext
X-Forwarded-For
```
 header. This header can be set by the client or by the proxy.

```
console.dir(req.ip)
// => '127.0.0.1'
```

### req.ips

When the [```plaintext trust proxy ``` setting](https://expressjs.com/4x/api.html#trust.proxy.options.table) does not evaluate to 
```plaintext
false
```
, this property contains an array of IP addresses specified in the 
```plaintext
X-Forwarded-For
```
 request header. Otherwise, it contains an empty array. This header can be set by the client or by the proxy.

For example, if 
```plaintext
X-Forwarded-For
```
 is 
```plaintext
client, proxy1, proxy2
```
, 
```plaintext
req.ips
```
 would be 
```plaintext
["client", "proxy1", "proxy2"]
```
, where 
```plaintext
proxy2
```
 is the furthest downstream.

### req.method

Contains a string corresponding to the HTTP method of the request: 
```plaintext
GET
```
, 
```plaintext
POST
```
, 
```plaintext
PUT
```
, and so on.

### req.originalUrl

```plaintext
req.url
```
 is not a native Express property, it is inherited from Node’s [http module](https://nodejs.org/api/http.html#http_message_url).

This property is much like 
```plaintext
req.url
```
; however, it retains the original request URL, allowing you to rewrite 
```plaintext
req.url
```
 freely for internal routing purposes. For example, the “mounting” feature of [app.use()](https://expressjs.com/en/4x/api.html#app.use) will rewrite 
```plaintext
req.url
```
 to strip the mount point.

```
// GET /search?q=something
console.dir(req.originalUrl)
// => '/search?q=something'
```

```plaintext
req.originalUrl
```
 is available both in middleware and router objects, and is a combination of 
```plaintext
req.baseUrl
```
 and 
```plaintext
req.url
```
. Consider following example:

```
app.use('/admin', function (req, res, next) { // GET 'http://www.example.com/admin/new?sort=desc'
  console.dir(req.originalUrl) // '/admin/new?sort=desc'
  console.dir(req.baseUrl) // '/admin'
  console.dir(req.path) // '/new'
  next()
})
```

### req.params

This property is an object containing properties mapped to the [named route “parameters”](https://expressjs.com/en/guide/routing.html#route-parameters). For example, if you have the route 
```plaintext
/user/:name
```
, then the “name” property is available as 
```plaintext
req.params.name
```
. This object defaults to 
```plaintext
{}
```
.

```
// GET /user/tj
console.dir(req.params.name)
// => 'tj'
```

When you use a regular expression for the route definition, capture groups are provided as integer keys using 
```plaintext
req.params[n]
```
, where 
```plaintext
n
```
 is the n th capture group. This rule is applied to unnamed wild card matches with string routes such as 
```plaintext
/file/*
```
:

```
// GET /file/javascripts/jquery.js
console.dir(req.params[0])
// => 'javascripts/jquery.js'
```

Named capturing groups in regular expressions behave like named route parameters. For example the group from 
```plaintext
/^\/file\/(?<path>.*)$/
```
 expression is available as 
```plaintext
req.params.path
```
.

If you need to make changes to a key in 
```plaintext
req.params
```
, use the [app.param](https://expressjs.com/en/4x/api.html#app.param) handler. Changes are applicable only to [parameters](https://expressjs.com/en/guide/routing.html#route-parameters) already defined in the route path.

Any changes made to the 
```plaintext
req.params
```
 object in a middleware or route handler will be reset.

Note

Express automatically decodes the values in 
```plaintext
req.params
```
 (using 
```plaintext
decodeURIComponent
```
).

### req.path

Contains the path part of the request URL.

```
// example.com/users?sort=desc
console.dir(req.path)
// => '/users'
```

When called from a middleware, the mount point is not included in 
```plaintext
req.path
```
. See [app.use()](https://expressjs.com/4x/api.html#app.use) for more details.

### req.protocol

Contains the request protocol string: either 
```plaintext
http
```
 or (for TLS requests) 
```plaintext
https
```
.

When the [```plaintext trust proxy ``` setting](https://expressjs.com/en/4x/api.html#trust.proxy.options.table) does not evaluate to 
```plaintext
false
```
, this property will use the value of the 
```plaintext
X-Forwarded-Proto
```
 header field if present. This header can be set by the client or by the proxy.

```
console.dir(req.protocol)
// => 'http'
```

### req.query

This property is an object containing a property for each query string parameter in the route. When [query parser](https://expressjs.com/en/4x/api.html#app.settings.table) is set to disabled, it is an empty object 
```plaintext
{}
```
, otherwise it is the result of the configured query parser.

As 
```plaintext
req.query
```
’s shape is based on user-controlled input, all properties and values in this object are untrusted and should be validated before trusting. For example, 
```plaintext
req.query.foo.toString()
```
 may fail in multiple ways, for example 
```plaintext
foo
```
 may not be there or may not be a string, and 
```plaintext
toString
```
 may not be a function and instead a string or other user-input.

The value of this property can be configured with the [query parser application setting](https://expressjs.com/en/4x/api.html#app.settings.table) to work how your application needs it. A very popular query string parser is the [```plaintext qs ``` module](https://www.npmjs.org/package/qs), and this is used by default. The 
```plaintext
qs
```
 module is very configurable with many settings, and it may be desirable to use different settings than the default to populate 
```plaintext
req.query
```
:

```
var qs = require('qs')
app.set('query parser', function (str) {
  return qs.parse(str, { /* custom options */ })
})
```

Check out the [query parser application setting](https://expressjs.com/en/4x/api.html#app.settings.table) documentation for other customization options.

### req.res

This property holds a reference to the [response object](https://expressjs.com/en/4x/api.html#res) that relates to this request object.

### req.route

Contains the currently-matched route, a string. For example:

```
app.get('/user/:id?', function userIdHandler (req, res) {
  console.log(req.route)
  res.send('GET')
})
```

Example output from the previous snippet:

```
{ path: '/user/:id?',
  stack:
   [ { handle: [Function: userIdHandler],
       name: 'userIdHandler',
       params: undefined,
       path: undefined,
       keys: [],
       regexp: /^\/?$/i,
       method: 'get' } ],
  methods: { get: true } }
```

### req.secure

A Boolean property that is true if a TLS connection is established. Equivalent to:

```
console.dir(req.protocol === 'https')
// => true
```

### req.signedCookies

When using [cookie-parser](https://www.npmjs.com/package/cookie-parser) middleware, this property contains signed cookies sent by the request, unsigned and ready for use. Signed cookies reside in a different object to show developer intent; otherwise, a malicious attack could be placed on 
```plaintext
req.cookie
```
 values (which are easy to spoof). Note that signing a cookie does not make it “hidden” or encrypted; but simply prevents tampering (because the secret used to sign is private).

If no signed cookies are sent, the property defaults to 
```plaintext
{}
```
.

```
// Cookie: user=tobi.CP7AWaXDfAKIRfH49dQzKJx7sKzzSoPq7/AcBBRVwlI3
console.dir(req.signedCookies.user)
// => 'tobi'
```

For more information, issues, or concerns, see [cookie-parser](https://github.com/expressjs/cookie-parser).

### req.stale

Indicates whether the request is “stale,” and is the opposite of 
```plaintext
req.fresh
```
. For more information, see [req.fresh](https://expressjs.com/en/4x/api.html#req.fresh).

```
console.dir(req.stale)
// => true
```

### req.subdomains

An array of subdomains in the domain name of the request.

```
// Host: "tobi.ferrets.example.com"
console.dir(req.subdomains)
// => ['ferrets', 'tobi']
```

The application property 
```plaintext
subdomain offset
```
, which defaults to 2, is used for determining the beginning of the subdomain segments. To change this behavior, change its value using [app.set](https://expressjs.com/en/4x/api.html#app.set).

### req.xhr

A Boolean property that is 
```plaintext
true
```
 if the request’s 
```plaintext
X-Requested-With
```
 header field is “XMLHttpRequest”, indicating that the request was issued by a client library such as jQuery.

```
console.dir(req.xhr)
// => true
```

### Methods

### req.accepts(types)

Checks if the specified content types are acceptable, based on the request’s 
```plaintext
Accept
```
 HTTP header field. The method returns the best match, or if none of the specified content types is acceptable, returns 
```plaintext
false
```
 (in which case, the application should respond with 
```plaintext
406 "Not Acceptable"
```
).

The 
```plaintext
type
```
 value may be a single MIME type string (such as “application/json”), an extension name such as “json”, a comma-delimited list, or an array. For a list or array, the method returns the _best_ match (if any).

```
// Accept: text/html
req.accepts('html')
// => "html"

// Accept: text/*, application/json
req.accepts('html')
// => "html"
req.accepts('text/html')
// => "text/html"
req.accepts(['json', 'text'])
// => "json"
req.accepts('application/json')
// => "application/json"

// Accept: text/*, application/json
req.accepts('image/png')
req.accepts('png')
// => false

// Accept: text/*;q=.5, application/json
req.accepts(['html', 'json'])
// => "json"
```

For more information, or if you have issues or concerns, see [accepts](https://github.com/expressjs/accepts).

### req.acceptsCharsets(charset [, ...])

Returns the first accepted charset of the specified character sets, based on the request’s 
```plaintext
Accept-Charset
```
 HTTP header field. If none of the specified charsets is accepted, returns 
```plaintext
false
```
.

For more information, or if you have issues or concerns, see [accepts](https://github.com/expressjs/accepts).

### req.acceptsEncodings(encoding [, ...])

Returns the first accepted encoding of the specified encodings, based on the request’s 
```plaintext
Accept-Encoding
```
 HTTP header field. If none of the specified encodings is accepted, returns 
```plaintext
false
```
.

For more information, or if you have issues or concerns, see [accepts](https://github.com/expressjs/accepts).

### req.acceptsLanguages([lang, ...])

Returns the first accepted language of the specified languages, based on the request’s 
```plaintext
Accept-Language
```
 HTTP header field. If none of the specified languages is accepted, returns 
```plaintext
false
```
.

If no 
```plaintext
lang
```
 argument is given, then 
```plaintext
req.acceptsLanguages()
```
 returns all languages from the HTTP 
```plaintext
Accept-Language
```
 header as an 
```plaintext
Array
```
.

For more information, or if you have issues or concerns, see [accepts](https://github.com/expressjs/accepts).

Express (4.x) source: [request.js line 179](https://github.com/expressjs/express/blob/4.x/lib/request.js#L179)

Accepts (1.3) source: [index.js line 195](https://github.com/jshttp/accepts/blob/f69c19e459bd501e59fb0b1a40b7471bb578113a/index.js#L195)

### req.get(field)

Returns the specified HTTP request header field (case-insensitive match). The 
```plaintext
Referrer
```
 and 
```plaintext
Referer
```
 fields are interchangeable.

```
req.get('Content-Type')
// => "text/plain"

req.get('content-type')
// => "text/plain"

req.get('Something')
// => undefined
```

Aliased as 
```plaintext
req.header(field)
```
.

### req.is(type)

Returns the matching content type if the incoming request’s “Content-Type” HTTP header field matches the MIME type specified by the 
```plaintext
type
```
 parameter. If the request has no body, returns 
```plaintext
null
```
. Returns 
```plaintext
false
```
 otherwise.

```
// With Content-Type: text/html; charset=utf-8
req.is('html')
// => 'html'
req.is('text/html')
// => 'text/html'
req.is('text/*')
// => 'text/*'

// When Content-Type is application/json
req.is('json')
// => 'json'
req.is('application/json')
// => 'application/json'
req.is('application/*')
// => 'application/*'

// Using arrays
// When Content-Type is application/json
req.is(['json', 'html'])
// => 'json'

// Using multiple arguments
// When Content-Type is application/json
req.is('json', 'html')
// => 'json'

req.is('html')
// => false
req.is(['xml', 'yaml'])
// => false
req.is('xml', 'yaml')
// => false
```

For more information, or if you have issues or concerns, see [type-is](https://github.com/expressjs/type-is).

### req.param(name [, defaultValue])

Deprecated. Use either 
```plaintext
req.params
```
, 
```plaintext
req.body
```
 or 
```plaintext
req.query
```
, as applicable.

Returns the value of param 
```plaintext
name
```
 when present.

```
// ?name=tobi
req.param('name')
// => "tobi"

// POST name=tobi
req.param('name')
// => "tobi"

// /user/tobi for /user/:name
req.param('name')
// => "tobi"
```

Lookup is performed in the following order:

*   ```plaintext
req.params
```
*   ```plaintext
req.body
```
*   ```plaintext
req.query
```

Optionally, you can specify 
```plaintext
defaultValue
```
 to set a default value if the parameter is not found in any of the request objects.

Direct access to 
```plaintext
req.body
```
, 
```plaintext
req.params
```
, and 
```plaintext
req.query
```
 should be favoured for clarity - unless you truly accept input from each object.

Body-parsing middleware must be loaded for 
```plaintext
req.param()
```
 to work predictably. Refer [req.body](https://expressjs.com/en/4x/api.html#req.body) for details.

### req.range(size[, options])

```plaintext
Range
```
 header parser.

The 
```plaintext
size
```
 parameter is the maximum size of the resource.

The 
```plaintext
options
```
 parameter is an object that can have the following properties.

| Property | Type | Description |
| --- | --- | --- |
| ```plaintext combine ``` | Boolean | Specify if overlapping & adjacent ranges should be combined, defaults to ```plaintext false ``` . When ```plaintext true ``` , ranges will be combined and returned as if they were specified that way in the header. |

An array of ranges will be returned or negative numbers indicating an error parsing.

*   ```plaintext
-2
```
 signals a malformed header string
*   ```plaintext
-1
```
 signals an unsatisfiable range

```
// parse header from request
var range = req.range(1000)

// the type of the range
if (range.type === 'bytes') {
  // the ranges
  range.forEach(function (r) {
    // do something with r.start and r.end
  })
}
```

[](https://expressjs.com/en/4x/api.html)

Response
--------

The 
```plaintext
res
```
 object represents the HTTP response that an Express app sends when it gets an HTTP request.

In this documentation and by convention, the object is always referred to as 
```plaintext
res
```
 (and the HTTP request is 
```plaintext
req
```
) but its actual name is determined by the parameters to the callback function in which you’re working.

For example:

```
app.get('/user/:id', function (req, res) {
  res.send('user ' + req.params.id)
})
```

But you could just as well have:

```
app.get('/user/:id', function (request, response) {
  response.send('user ' + request.params.id)
})
```

The 
```plaintext
res
```
 object is an enhanced version of Node’s own response object and supports all [built-in fields and methods](https://nodejs.org/api/http.html#http_class_http_serverresponse).

### Properties

### res.app

This property holds a reference to the instance of the Express application that is using the middleware.

```plaintext
res.app
```
 is identical to the [req.app](https://expressjs.com/en/4x/api.html#req.app) property in the request object.

### res.headersSent

Boolean property that indicates if the app sent HTTP headers for the response.

```
app.get('/', function (req, res) {
  console.dir(res.headersSent) // false
  res.send('OK')
  console.dir(res.headersSent) // true
})
```

### res.locals

Use this property to set variables accessible in templates rendered with [res.render](https://expressjs.com/en/4x/api.html#res.render). The variables set on 
```plaintext
res.locals
```
 are available within a single request-response cycle, and will not be shared between requests.

The 
```plaintext
locals
```
 object is used by view engines to render a response. The object keys may be particularly sensitive and should not contain user-controlled input, as it may affect the operation of the view engine or provide a path to cross-site scripting. Consult the documentation for the used view engine for additional considerations.

In order to keep local variables for use in template rendering between requests, use [app.locals](https://expressjs.com/en/4x/api.html#app.locals) instead.

This property is useful for exposing request-level information such as the request path name, authenticated user, user settings, and so on to templates rendered within the application.

```
app.use(function (req, res, next) {
  // Make `user` and `authenticated` available in templates
  res.locals.user = req.user
  res.locals.authenticated = !req.user.anonymous
  next()
})
```

### Methods

### res.append(field [, value])

Note

```plaintext
res.append()
```
 is supported by Express v4.11.0+

Appends the specified 
```plaintext
value
```
 to the HTTP response header 
```plaintext
field
```
. If the header is not already set, it creates the header with the specified value. The 
```plaintext
value
```
 parameter can be a string or an array.

Note

calling 
```plaintext
res.set()
```
 after 
```plaintext
res.append()
```
 will reset the previously-set header value.

```
res.append('Link', ['<http://localhost/>', '<http://localhost:3000/>'])
res.append('Set-Cookie', 'foo=bar; Path=/; HttpOnly')
res.append('Warning', '199 Miscellaneous warning')
```

### res.attachment([filename])

Sets the HTTP response 
```plaintext
Content-Disposition
```
 header field to “attachment”. If a 
```plaintext
filename
```
 is given, then it sets the Content-Type based on the extension name via 
```plaintext
res.type()
```
, and sets the 
```plaintext
Content-Disposition
```
 “filename=” parameter.

```
res.attachment()
// Content-Disposition: attachment

res.attachment('path/to/logo.png')
// Content-Disposition: attachment; filename="logo.png"
// Content-Type: image/png
```

### res.cookie(name, value [, options])

Sets cookie 
```plaintext
name
```
 to 
```plaintext
value
```
. The 
```plaintext
value
```
 parameter may be a string or object converted to JSON.

The 
```plaintext
options
```
 parameter is an object that can have the following properties.

| Property | Type | Description |
| --- | --- | --- |
| ```plaintext domain ``` | String | Domain name for the cookie. Defaults to the domain name of the app. |
| ```plaintext encode ``` | Function | A synchronous function used for cookie value encoding. Defaults to ```plaintext encodeURIComponent ``` . |
| ```plaintext expires ``` | Date | Expiry date of the cookie in GMT. If not specified or set to 0, creates a session cookie. |
| ```plaintext httpOnly ``` | Boolean | Flags the cookie to be accessible only by the web server. |
| ```plaintext maxAge ``` | Number | Convenient option for setting the expiry time relative to the current time in milliseconds. |
| ```plaintext path ``` | String | Path for the cookie. Defaults to “/”. |
| ```plaintext partitioned ``` | Boolean | Indicates that the cookie should be stored using partitioned storage. See [Cookies Having Independent Partitioned State (CHIPS)](https://developer.mozilla.org/en-US/docs/Web/Privacy/Partitioned_cookies) for more details. |
| ```plaintext priority ``` | String | Value of the “Priority” **Set-Cookie** attribute. |
| ```plaintext secure ``` | Boolean | Marks the cookie to be used with HTTPS only. |
| ```plaintext signed ``` | Boolean | Indicates if the cookie should be signed. |
| ```plaintext sameSite ``` | Boolean or String | Value of the “SameSite” **Set-Cookie** attribute. More information at [https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00#section-4.1.1](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00#section-4.1.1). |

All 
```plaintext
res.cookie()
```
 does is set the HTTP 
```plaintext
Set-Cookie
```
 header with the options provided. Any option not specified defaults to the value stated in [RFC 6265](http://tools.ietf.org/html/rfc6265).

For example:

```
res.cookie('name', 'tobi', { domain: '.example.com', path: '/admin', secure: true })
res.cookie('rememberme', '1', { expires: new Date(Date.now() + 900000), httpOnly: true })
```

You can set multiple cookies in a single response by calling 
```plaintext
res.cookie
```
 multiple times, for example:

```
res
  .status(201)
  .cookie('access_token', 'Bearer ' + token, {
    expires: new Date(Date.now() + 8 * 3600000) // cookie will be removed after 8 hours
  })
  .cookie('test', 'test')
  .redirect(301, '/admin')
```

The 
```plaintext
encode
```
 option allows you to choose the function used for cookie value encoding. Does not support asynchronous functions.

Example use case: You need to set a domain-wide cookie for another site in your organization. This other site (not under your administrative control) does not use URI-encoded cookie values.

```
// Default encoding
res.cookie('some_cross_domain_cookie', 'http://mysubdomain.example.com', { domain: 'example.com' })
// Result: 'some_cross_domain_cookie=http%3A%2F%2Fmysubdomain.example.com; Domain=example.com; Path=/'

// Custom encoding
res.cookie('some_cross_domain_cookie', 'http://mysubdomain.example.com', { domain: 'example.com', encode: String })
// Result: 'some_cross_domain_cookie=http://mysubdomain.example.com; Domain=example.com; Path=/;'
```

The 
```plaintext
maxAge
```
 option is a convenience option for setting “expires” relative to the current time in milliseconds. The following is equivalent to the second example above.

```
res.cookie('rememberme', '1', { maxAge: 900000, httpOnly: true })
```

You can pass an object as the 
```plaintext
value
```
 parameter; it is then serialized as JSON and parsed by 
```plaintext
bodyParser()
```
 middleware.

```
res.cookie('cart', { items: [1, 2, 3] })
res.cookie('cart', { items: [1, 2, 3] }, { maxAge: 900000 })
```

When using [cookie-parser](https://www.npmjs.com/package/cookie-parser) middleware, this method also supports signed cookies. Simply include the 
```plaintext
signed
```
 option set to 
```plaintext
true
```
. Then 
```plaintext
res.cookie()
```
 will use the secret passed to 
```plaintext
cookieParser(secret)
```
 to sign the value.

```
res.cookie('name', 'tobi', { signed: true })
```

Later you may access this value through the [req.signedCookie](https://expressjs.com/en/4x/api.html#req.signedCookies) object.

### res.clearCookie(name [, options])

Clears the cookie with the specified 
```plaintext
name
```
 by sending a 
```plaintext
Set-Cookie
```
 header that sets its expiration date in the past. This instructs the client that the cookie has expired and is no longer valid. For more information about available 
```plaintext
options
```
, see [res.cookie()](https://expressjs.com/en/4x/api.html#res.cookie).

If the 
```plaintext
maxAge
```
 or 
```plaintext
expires
```
 options are set, the cookie may not be cleared depending on the time values provided, as Express does not ignore these options. It is therefore recommended to omit these options when calling this method. Passing these two options has been deprecated since Express v4.20.0.

Web browsers and other compliant clients will only clear the cookie if the given 
```plaintext
options
```
 is identical to those given to [res.cookie()](https://expressjs.com/en/4x/api.html#res.cookie), excluding 
```plaintext
expires
```
 and 
```plaintext
maxAge
```
.

```
res.cookie('name', 'tobi', { path: '/admin' })
res.clearCookie('name', { path: '/admin' })
```

### res.download(path [, filename] [, options] [, fn])

Transfers the file at 
```plaintext
path
```
 as an “attachment”. Typically, browsers will prompt the user for download. By default, the 
```plaintext
Content-Disposition
```
 header “filename=” parameter is derived from the 
```plaintext
path
```
 argument, but can be overridden with the 
```plaintext
filename
```
 parameter. If 
```plaintext
path
```
 is relative, then it will be based on the current working directory of the process or the 
```plaintext
root
```
 option, if provided.

This API provides access to data on the running file system. Ensure that either (a) the way in which the 
```plaintext
path
```
 argument was constructed is secure if it contains user input or (b) set the 
```plaintext
root
```
 option to the absolute path of a directory to contain access within.

When the 
```plaintext
root
```
 option is provided, Express will validate that the relative path provided as 
```plaintext
path
```
 will resolve within the given 
```plaintext
root
```
 option.

The following table provides details on the 
```plaintext
options
```
 parameter.

The optional 
```plaintext
options
```
 argument is supported by Express v4.16.0 onwards.

| Property | Description | Default | Availability |
| --- | --- | --- | --- |
| ```plaintext maxAge ``` | Sets the max-age property of the ```plaintext Cache-Control ``` header in milliseconds or a string in [ms format](https://www.npmjs.org/package/ms) | 0 | 4.16+ |
| ```plaintext root ``` | Root directory for relative filenames. |  | 4.18+ |
| ```plaintext lastModified ``` | Sets the ```plaintext Last-Modified ``` header to the last modified date of the file on the OS. Set ```plaintext false ``` to disable it. | Enabled | 4.16+ |
| ```plaintext headers ``` | Object containing HTTP headers to serve with the file. The header ```plaintext Content-Disposition ``` will be overridden by the ```plaintext filename ``` argument. |  | 4.16+ |
| ```plaintext dotfiles ``` | Option for serving dotfiles. Possible values are “allow”, “deny”, “ignore”. | “ignore” | 4.16+ |
| ```plaintext acceptRanges ``` | Enable or disable accepting ranged requests. | ```plaintext true ``` | 4.16+ |
| ```plaintext cacheControl ``` | Enable or disable setting ```plaintext Cache-Control ``` response header. | ```plaintext true ``` | 4.16+ |
| ```plaintext immutable ``` | Enable or disable the ```plaintext immutable ``` directive in the ```plaintext Cache-Control ``` response header. If enabled, the ```plaintext maxAge ``` option should also be specified to enable caching. The ```plaintext immutable ``` directive will prevent supported clients from making conditional requests during the life of the ```plaintext maxAge ``` option to check if the file has changed. | ```plaintext false ``` | 4.16+ |

The method invokes the callback function 
```plaintext
fn(err)
```
 when the transfer is complete or when an error occurs. If the callback function is specified and an error occurs, the callback function must explicitly handle the response process either by ending the request-response cycle, or by passing control to the next route.

```
res.download('/report-12345.pdf')

res.download('/report-12345.pdf', 'report.pdf')

res.download('/report-12345.pdf', 'report.pdf', function (err) {
  if (err) {
    // Handle error, but keep in mind the response may be partially-sent
    // so check res.headersSent
  } else {
    // decrement a download credit, etc.
  }
})
```

### res.end([data[, encoding]][, callback])

Ends the response process. This method actually comes from Node core, specifically the [response.end() method of http.ServerResponse](https://nodejs.org/api/http.html#responseenddata-encoding-callback).

Use to quickly end the response without any data. If you need to respond with data, instead use methods such as [res.send()](https://expressjs.com/en/4x/api.html#res.send) and [res.json()](https://expressjs.com/en/4x/api.html#res.json).

```
res.end()
res.status(404).end()
```

### res.format(object)

Performs content-negotiation on the 
```plaintext
Accept
```
 HTTP header on the request object, when present. It uses [req.accepts()](https://expressjs.com/en/4x/api.html#req.accepts) to select a handler for the request, based on the acceptable types ordered by their quality values. If the header is not specified, the first callback is invoked. When no match is found, the server responds with 406 “Not Acceptable”, or invokes the 
```plaintext
default
```
 callback.

The 
```plaintext
Content-Type
```
 response header is set when a callback is selected. However, you may alter this within the callback using methods such as 
```plaintext
res.set()
```
 or 
```plaintext
res.type()
```
.

The following example would respond with 
```plaintext
{ "message": "hey" }
```
 when the 
```plaintext
Accept
```
 header field is set to “application/json” or “*/json” (however if it is “*/*”, then the response will be “hey”).

```
res.format({
  'text/plain': function () {
    res.send('hey')
  },

  'text/html': function () {
    res.send('<p>hey</p>')
  },

  'application/json': function () {
    res.send({ message: 'hey' })
  },

  default: function () {
    // log the request and respond with 406
    res.status(406).send('Not Acceptable')
  }
})
```

In addition to canonicalized MIME types, you may also use extension names mapped to these types for a slightly less verbose implementation:

```
res.format({
  text: function () {
    res.send('hey')
  },

  html: function () {
    res.send('<p>hey</p>')
  },

  json: function () {
    res.send({ message: 'hey' })
  }
})
```

### res.get(field)

Returns the HTTP response header specified by 
```plaintext
field
```
. The match is case-insensitive.

```
res.get('Content-Type')
// => "text/plain"
```

### res.json([body])

Sends a JSON response. This method sends a response (with the correct content-type) that is the parameter converted to a JSON string using [JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

The parameter can be any JSON type, including object, array, string, Boolean, number, or null, and you can also use it to convert other values to JSON.

```
res.json(null)
res.json({ user: 'tobi' })
res.status(500).json({ error: 'message' })
```

### res.jsonp([body])

Sends a JSON response with JSONP support. This method is identical to 
```plaintext
res.json()
```
, except that it opts-in to JSONP callback support.

```
res.jsonp(null)
// => callback(null)

res.jsonp({ user: 'tobi' })
// => callback({ "user": "tobi" })

res.status(500).jsonp({ error: 'message' })
// => callback({ "error": "message" })
```

By default, the JSONP callback name is simply 
```plaintext
callback
```
. Override this with the [jsonp callback name](https://expressjs.com/en/4x/api.html#app.settings.table) setting.

The following are some examples of JSONP responses using the same code:

```
// ?callback=foo
res.jsonp({ user: 'tobi' })
// => foo({ "user": "tobi" })

app.set('jsonp callback name', 'cb')

// ?cb=foo
res.status(500).jsonp({ error: 'message' })
// => foo({ "error": "message" })
```

### res.links(links)

Joins the 
```plaintext
links
```
 provided as properties of the parameter to populate the response’s 
```plaintext
Link
```
 HTTP header field.

For example, the following call:

```
res.links({
  next: 'http://api.example.com/users?page=2',
  last: 'http://api.example.com/users?page=5'
})
```

Yields the following results:

```
Link: <http://api.example.com/users?page=2>; rel="next",
      <http://api.example.com/users?page=5>; rel="last"
```

### res.location(path)

Sets the response 
```plaintext
Location
```
 HTTP header to the specified 
```plaintext
path
```
 parameter.

```
res.location('/foo/bar')
res.location('http://example.com')
res.location('back')
```

Note

```plaintext
'back'
```
 was deprecated in 4.21.0, use 
```plaintext
req.get('Referrer') || '/'
```
 as an argument instead.

A 
```plaintext
path
```
 value of “back” has a special meaning, it refers to the URL specified in the 
```plaintext
Referer
```
 header of the request. If the 
```plaintext
Referer
```
 header was not specified, it refers to “/”.

See also [Security best practices: Prevent open redirect vulnerabilities](http://expressjs.com/en/advanced/best-practice-security.html#prevent-open-redirects).

After encoding the URL, if not encoded already, Express passes the specified URL to the browser in the 
```plaintext
Location
```
 header, without any validation.

Browsers take the responsibility of deriving the intended URL from the current URL or the referring URL, and the URL specified in the 
```plaintext
Location
```
 header; and redirect the user accordingly.

### res.redirect([status,] path)

Redirects to the URL derived from the specified 
```plaintext
path
```
, with specified 
```plaintext
status
```
, a positive integer that corresponds to an [HTTP status code](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes) . If not specified, 
```plaintext
status
```
 defaults to “302 “Found”.

```
res.redirect('/foo/bar')
res.redirect('http://example.com')
res.redirect(301, 'http://example.com')
res.redirect('../login')
```

Redirects can be a fully-qualified URL for redirecting to a different site:

```
res.redirect('http://google.com')
```

Redirects can be relative to the root of the host name. For example, if the application is on 
```plaintext
http://example.com/admin/post/new
```
, the following would redirect to the URL 
```plaintext
http://example.com/admin
```
:

```
res.redirect('/admin')
```

Redirects can be relative to the current URL. For example, from 
```plaintext
http://example.com/blog/admin/
```
 (notice the trailing slash), the following would redirect to the URL 
```plaintext
http://example.com/blog/admin/post/new
```
.

```
res.redirect('post/new')
```

Redirecting to 
```plaintext
post/new
```
 from 
```plaintext
http://example.com/blog/admin
```
 (no trailing slash), will redirect to 
```plaintext
http://example.com/blog/post/new
```
.

If you found the above behavior confusing, think of path segments as directories (with trailing slashes) and files, it will start to make sense.

Path-relative redirects are also possible. If you were on 
```plaintext
http://example.com/admin/post/new
```
, the following would redirect to 
```plaintext
http://example.com/admin/post
```
:

```
res.redirect('..')
```

A 
```plaintext
back
```
 redirection redirects the request back to the [referer](http://en.wikipedia.org/wiki/HTTP_referer), defaulting to 
```plaintext
/
```
 when the referer is missing.

```
res.redirect('back')
```

Note

```plaintext
back
```
 redirect was deprecated in 4.21.0, use 
```plaintext
req.get('Referrer') || '/'
```
 as an argument instead.

See also [Security best practices: Prevent open redirect vulnerabilities](http://expressjs.com/en/advanced/best-practice-security.html#prevent-open-redirects).

### res.render(view [, locals] [, callback])

Renders a 
```plaintext
view
```
 and sends the rendered HTML string to the client. Optional parameters:

*   ```plaintext
locals
```
, an object whose properties define local variables for the view.
*   ```plaintext
callback
```
, a callback function. If provided, the method returns both the possible error and rendered string, but does not perform an automated response. When an error occurs, the method invokes 
```plaintext
next(err)
```
 internally.

The 
```plaintext
view
```
 argument is a string that is the file path of the view file to render. This can be an absolute path, or a path relative to the 
```plaintext
views
```
 setting. If the path does not contain a file extension, then the 
```plaintext
view engine
```
 setting determines the file extension. If the path does contain a file extension, then Express will load the module for the specified template engine (via 
```plaintext
require()
```
) and render it using the loaded module’s 
```plaintext
__express
```
 function.

For more information, see [Using template engines with Express](https://expressjs.com/en/guide/using-template-engines.html).

The 
```plaintext
view
```
 argument performs file system operations like reading a file from disk and evaluating Node.js modules, and as so for security reasons should not contain input from the end-user.

The 
```plaintext
locals
```
 object is used by view engines to render a response. The object keys may be particularly sensitive and should not contain user-controlled input, as it may affect the operation of the view engine or provide a path to cross-site scripting. Consult the documentation for the used view engine for additional considerations.

The local variable 
```plaintext
cache
```
 enables view caching. Set it to 
```plaintext
true
```
, to cache the view during development; view caching is enabled in production by default.

```
// send the rendered view to the client
res.render('index')

// if a callback is specified, the rendered HTML string has to be sent explicitly
res.render('index', function (err, html) {
  res.send(html)
})

// pass a local variable to the view
res.render('user', { name: 'Tobi' }, function (err, html) {
  // ...
})
```

### res.req

 This property holds a reference to the [request object](https://expressjs.com/en/4x/api.html#req) that relates to this response object. 
### res.send([body])

Sends the HTTP response.

The 
```plaintext
body
```
 parameter can be a 
```plaintext
Buffer
```
 object, a 
```plaintext
String
```
, an object, 
```plaintext
Boolean
```
, or an 
```plaintext
Array
```
. For example:

```
res.send(Buffer.from('whoop'))
res.send({ some: 'json' })
res.send('<p>some html</p>')
res.status(404).send('Sorry, we cannot find that!')
res.status(500).send({ error: 'something blew up' })
```

This method performs many useful tasks for simple non-streaming responses: For example, it automatically assigns the 
```plaintext
Content-Length
```
 HTTP response header field (unless previously defined) and provides automatic HEAD and HTTP cache freshness support.

When the parameter is a 
```plaintext
Buffer
```
 object, the method sets the 
```plaintext
Content-Type
```
 response header field to “application/octet-stream”, unless previously defined as shown below:

```
res.set('Content-Type', 'text/html')
res.send(Buffer.from('<p>some html</p>'))
```

When the parameter is a 
```plaintext
String
```
, the method sets the 
```plaintext
Content-Type
```
 to “text/html”:

```
res.send('<p>some html</p>')
```

When the parameter is an 
```plaintext
Array
```
 or 
```plaintext
Object
```
, Express responds with the JSON representation:

```
res.send({ user: 'tobi' })
res.send([1, 2, 3])
```

### res.sendFile(path [, options] [, fn])

```plaintext
res.sendFile()
```
 is supported by Express v4.8.0 onwards.

Transfers the file at the given 
```plaintext
path
```
. Sets the 
```plaintext
Content-Type
```
 response HTTP header field based on the filename’s extension. Unless the 
```plaintext
root
```
 option is set in the options object, 
```plaintext
path
```
 must be an absolute path to the file.

This API provides access to data on the running file system. Ensure that either (a) the way in which the 
```plaintext
path
```
 argument was constructed into an absolute path is secure if it contains user input or (b) set the 
```plaintext
root
```
 option to the absolute path of a directory to contain access within.

When the 
```plaintext
root
```
 option is provided, the 
```plaintext
path
```
 argument is allowed to be a relative path, including containing 
```plaintext
..
```
. Express will validate that the relative path provided as 
```plaintext
path
```
 will resolve within the given 
```plaintext
root
```
 option.

The following table provides details on the 
```plaintext
options
```
 parameter.

| Property | Description | Default | Availability |
| --- | --- | --- | --- |
| ```plaintext maxAge ``` | Sets the max-age property of the ```plaintext Cache-Control ``` header in milliseconds or a string in [ms format](https://www.npmjs.org/package/ms) | 0 |  |
| ```plaintext root ``` | Root directory for relative filenames. |  |  |
| ```plaintext lastModified ``` | Sets the ```plaintext Last-Modified ``` header to the last modified date of the file on the OS. Set ```plaintext false ``` to disable it. | Enabled | 4.9.0+ |
| ```plaintext headers ``` | Object containing HTTP headers to serve with the file. |  |  |
| ```plaintext dotfiles ``` | Option for serving dotfiles. Possible values are “allow”, “deny”, “ignore”. | “ignore” |  |
| ```plaintext acceptRanges ``` | Enable or disable accepting ranged requests. | ```plaintext true ``` | 4.14+ |
| ```plaintext cacheControl ``` | Enable or disable setting ```plaintext Cache-Control ``` response header. | ```plaintext true ``` | 4.14+ |
| ```plaintext immutable ``` | Enable or disable the ```plaintext immutable ``` directive in the ```plaintext Cache-Control ``` response header. If enabled, the ```plaintext maxAge ``` option should also be specified to enable caching. The ```plaintext immutable ``` directive will prevent supported clients from making conditional requests during the life of the ```plaintext maxAge ``` option to check if the file has changed. | ```plaintext false ``` | 4.16+ |

The method invokes the callback function 
```plaintext
fn(err)
```
 when the transfer is complete or when an error occurs. If the callback function is specified and an error occurs, the callback function must explicitly handle the response process either by ending the request-response cycle, or by passing control to the next route.

Here is an example of using 
```plaintext
res.sendFile
```
 with all its arguments.

```
app.get('/file/:name', function (req, res, next) {
  var options = {
    root: path.join(__dirname, 'public'),
    dotfiles: 'deny',
    headers: {
      'x-timestamp': Date.now(),
      'x-sent': true
    }
  }

  var fileName = req.params.name
  res.sendFile(fileName, options, function (err) {
    if (err) {
      next(err)
    } else {
      console.log('Sent:', fileName)
    }
  })
})
```

The following example illustrates using 
```plaintext
res.sendFile
```
 to provide fine-grained support for serving files:

```
app.get('/user/:uid/photos/:file', function (req, res) {
  var uid = req.params.uid
  var file = req.params.file

  req.user.mayViewFilesFrom(uid, function (yes) {
    if (yes) {
      res.sendFile('/uploads/' + uid + '/' + file)
    } else {
      res.status(403).send("Sorry! You can't see that.")
    }
  })
})
```

For more information, or if you have issues or concerns, see [send](https://github.com/pillarjs/send).

### res.sendStatus(statusCode)

Sets the response HTTP status code to 
```plaintext
statusCode
```
 and sends the registered status message as the text response body. If an unknown status code is specified, the response body will just be the code number.

```
res.sendStatus(404)
```

Some versions of Node.js will throw when 
```plaintext
res.statusCode
```
 is set to an invalid HTTP status code (outside of the range 
```plaintext
100
```
 to 
```plaintext
599
```
). Consult the HTTP server documentation for the Node.js version being used.

[More about HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

### res.set(field [, value])

Sets the response’s HTTP header 
```plaintext
field
```
 to 
```plaintext
value
```
. To set multiple fields at once, pass an object as the parameter.

```
res.set('Content-Type', 'text/plain')

res.set({
  'Content-Type': 'text/plain',
  'Content-Length': '123',
  ETag: '12345'
})
```

Aliased as 
```plaintext
res.header(field [, value])
```
.

### res.status(code)

Sets the HTTP status for the response. It is a chainable alias of Node’s [response.statusCode](http://nodejs.org/api/http.html#http_response_statuscode).

```
res.status(403).end()
res.status(400).send('Bad Request')
res.status(404).sendFile('/absolute/path/to/404.png')
```

### res.type(type)

Sets the 
```plaintext
Content-Type
```
 HTTP header to the MIME type as determined by the specified 
```plaintext
type
```
. If 
```plaintext
type
```
 contains the “/” character, then it sets the 
```plaintext
Content-Type
```
 to the exact value of 
```plaintext
type
```
, otherwise it is assumed to be a file extension and the MIME type is looked up in a mapping using the 
```plaintext
express.static.mime.lookup()
```
 method.

```
res.type('.html')
// => 'text/html'
res.type('html')
// => 'text/html'
res.type('json')
// => 'application/json'
res.type('application/json')
// => 'application/json'
res.type('png')
// => 'image/png'
```

Aliased as 
```plaintext
res.contentType(type)
```
.

### res.vary(field)

Adds the field to the 
```plaintext
Vary
```
 response header, if it is not there already.

```
res.vary('User-Agent').render('docs')
```

[](https://expressjs.com/en/4x/api.html)

Router
------

A 
```plaintext
router
```
 object is an instance of middleware and routes. You can think of it as a “mini-application,” capable only of performing middleware and routing functions. Every Express application has a built-in app router.

A router behaves like middleware itself, so you can use it as an argument to [app.use()](https://expressjs.com/en/4x/api.html#app.use) or as the argument to another router’s [use()](https://expressjs.com/en/4x/api.html#router.use) method.

The top-level 
```plaintext
express
```
 object has a [Router()](https://expressjs.com/en/4x/api.html#express.router) method that creates a new 
```plaintext
router
```
 object.

Once you’ve created a router object, you can add middleware and HTTP method routes (such as 
```plaintext
get
```
, 
```plaintext
put
```
, 
```plaintext
post
```
, and so on) to it just like an application. For example:

```
// invoked for any requests passed to this router
router.use(function (req, res, next) {
  // .. some logic here .. like any other middleware
  next()
})

// will handle any request that ends in /events
// depends on where the router is "use()'d"
router.get('/events', function (req, res, next) {
  // ..
})
```

You can then use a router for a particular root URL in this way separating your routes into files or even mini-apps.

```
// only requests to /calendar/* will be sent to our "router"
app.use('/calendar', router)
```

Keep in mind that any middleware applied to a router will run for all requests on that router’s path, even those that aren’t part of the router.

### Methods

### router.all(path, [callback, ...] callback)

This method is just like the 
```plaintext
router.METHOD()
```
 methods, except that it matches all HTTP methods (verbs).

This method is extremely useful for mapping “global” logic for specific path prefixes or arbitrary matches. For example, if you placed the following route at the top of all other route definitions, it would require that all routes from that point on would require authentication, and automatically load a user. Keep in mind that these callbacks do not have to act as end points; 
```plaintext
loadUser
```
 can perform a task, then call 
```plaintext
next()
```
 to continue matching subsequent routes.

```
router.all('*', requireAuthentication, loadUser)
```

Or the equivalent:

```
router.all('*', requireAuthentication)
router.all('*', loadUser)
```

Another example of this is white-listed “global” functionality. Here the example is much like before, but it only restricts paths prefixed with “/api”:

```
router.all('/api/*', requireAuthentication)
```

### router.METHOD(path, [callback, ...] callback)

The 
```plaintext
router.METHOD()
```
 methods provide the routing functionality in Express, where METHOD is one of the HTTP methods, such as GET, PUT, POST, and so on, in lowercase. Thus, the actual methods are 
```plaintext
router.get()
```
, 
```plaintext
router.post()
```
, 
```plaintext
router.put()
```
, and so on.

The 
```plaintext
router.get()
```
 function is automatically called for the HTTP 
```plaintext
HEAD
```
 method in addition to the 
```plaintext
GET
```
 method if 
```plaintext
router.head()
```
 was not called for the path before 
```plaintext
router.get()
```
.

You can provide multiple callbacks, and all are treated equally, and behave just like middleware, except that these callbacks may invoke 
```plaintext
next('route')
```
 to bypass the remaining route callback(s). You can use this mechanism to perform pre-conditions on a route then pass control to subsequent routes when there is no reason to proceed with the route matched.

The following snippet illustrates the most simple route definition possible. Express translates the path strings to regular expressions, used internally to match incoming requests. Query strings are _not_ considered when performing these matches, for example “GET /” would match the following route, as would “GET /?name=tobi”.

```
router.get('/', function (req, res) {
  res.send('hello world')
})
```

You can also use regular expressions—useful if you have very specific constraints, for example the following would match “GET /commits/71dbb9c” as well as “GET /commits/71dbb9c..4c084f9”.

```
router.get(/^\/commits\/(\w+)(?:\.\.(\w+))?$/, function (req, res) {
  var from = req.params[0]
  var to = req.params[1] || 'HEAD'
  res.send('commit range ' + from + '..' + to)
})
```

### router.param(name, callback)

Adds callback triggers to route parameters, where 
```plaintext
name
```
 is the name of the parameter and 
```plaintext
callback
```
 is the callback function. Although 
```plaintext
name
```
 is technically optional, using this method without it is deprecated starting with Express v4.11.0 (see below).

The parameters of the callback function are:

*   ```plaintext
req
```
, the request object.
*   ```plaintext
res
```
, the response object.
*   ```plaintext
next
```
, indicating the next middleware function.
*   The value of the 
```plaintext
name
```
 parameter.
*   The name of the parameter.

Unlike 
```plaintext
app.param()
```
, 
```plaintext
router.param()
```
 does not accept an array of route parameters.

For example, when 
```plaintext
:user
```
 is present in a route path, you may map user loading logic to automatically provide 
```plaintext
req.user
```
 to the route, or perform validations on the parameter input.

```
router.param('user', function (req, res, next, id) {
  // try to get the user details from the User model and attach it to the request object
  User.find(id, function (err, user) {
    if (err) {
      next(err)
    } else if (user) {
      req.user = user
      next()
    } else {
      next(new Error('failed to load user'))
    }
  })
})
```

Param callback functions are local to the router on which they are defined. They are not inherited by mounted apps or routers, nor are they triggered for route parameters inherited from parent routers. Hence, param callbacks defined on 
```plaintext
router
```
 will be triggered only by route parameters defined on 
```plaintext
router
```
 routes.

A param callback will be called only once in a request-response cycle, even if the parameter is matched in multiple routes, as shown in the following examples.

```
router.param('id', function (req, res, next, id) {
  console.log('CALLED ONLY ONCE')
  next()
})

router.get('/user/:id', function (req, res, next) {
  console.log('although this matches')
  next()
})

router.get('/user/:id', function (req, res) {
  console.log('and this matches too')
  res.end()
})
```

On 
```plaintext
GET /user/42
```
, the following is printed:

```
CALLED ONLY ONCE
although this matches
and this matches too
```

The following section describes 
```plaintext
router.param(callback)
```
, which is deprecated as of v4.11.0.

The behavior of the 
```plaintext
router.param(name, callback)
```
 method can be altered entirely by passing only a function to 
```plaintext
router.param()
```
. This function is a custom implementation of how 
```plaintext
router.param(name, callback)
```
 should behave - it accepts two parameters and must return a middleware.

The first parameter of this function is the name of the URL parameter that should be captured, the second parameter can be any JavaScript object which might be used for returning the middleware implementation.

The middleware returned by the function decides the behavior of what happens when a URL parameter is captured.

In this example, the 
```plaintext
router.param(name, callback)
```
 signature is modified to 
```plaintext
router.param(name, accessId)
```
. Instead of accepting a name and a callback, 
```plaintext
router.param()
```
 will now accept a name and a number.

```
var express = require('express')
var app = express()
var router = express.Router()

// customizing the behavior of router.param()
router.param(function (param, option) {
  return function (req, res, next, val) {
    if (val === option) {
      next()
    } else {
      res.sendStatus(403)
    }
  }
})

// using the customized router.param()
router.param('id', '1337')

// route to trigger the capture
router.get('/user/:id', function (req, res) {
  res.send('OK')
})

app.use(router)

app.listen(3000, function () {
  console.log('Ready')
})
```

In this example, the 
```plaintext
router.param(name, callback)
```
 signature remains the same, but instead of a middleware callback, a custom data type checking function has been defined to validate the data type of the user id.

```
router.param(function (param, validator) {
  return function (req, res, next, val) {
    if (validator(val)) {
      next()
    } else {
      res.sendStatus(403)
    }
  }
})

router.param('id', function (candidate) {
  return !isNaN(parseFloat(candidate)) && isFinite(candidate)
})
```

### router.route(path)

Returns an instance of a single route which you can then use to handle HTTP verbs with optional middleware. Use 
```plaintext
router.route()
```
 to avoid duplicate route naming and thus typing errors.

Building on the 
```plaintext
router.param()
```
 example above, the following code shows how to use 
```plaintext
router.route()
```
 to specify various HTTP method handlers.

```
var router = express.Router()

router.param('user_id', function (req, res, next, id) {
  // sample user, would actually fetch from DB, etc...
  req.user = {
    id: id,
    name: 'TJ'
  }
  next()
})

router.route('/users/:user_id')
  .all(function (req, res, next) {
    // runs for all HTTP verbs first
    // think of it as route specific middleware!
    next()
  })
  .get(function (req, res, next) {
    res.json(req.user)
  })
  .put(function (req, res, next) {
    // just an example of maybe updating the user
    req.user.name = req.params.name
    // save user ... etc
    res.json(req.user)
  })
  .post(function (req, res, next) {
    next(new Error('not implemented'))
  })
  .delete(function (req, res, next) {
    next(new Error('not implemented'))
  })
```

This approach re-uses the single 
```plaintext
/users/:user_id
```
 path and adds handlers for various HTTP methods.

Note

When you use 
```plaintext
router.route()
```
, middleware ordering is based on when the _route_ is created, not when method handlers are added to the route. For this purpose, you can consider method handlers to belong to the route to which they were added.

### router.use([path], [function, ...] function)

Uses the specified middleware function or functions, with optional mount path 
```plaintext
path
```
, that defaults to “/”.

This method is similar to [app.use()](https://expressjs.com/en/4x/api.html#app.use). A simple example and use case is described below. See [app.use()](https://expressjs.com/en/4x/api.html#app.use) for more information.

Middleware is like a plumbing pipe: requests start at the first middleware function defined and work their way “down” the middleware stack processing for each path they match.

```
var express = require('express')
var app = express()
var router = express.Router()

// simple logger for this router's requests
// all requests to this router will first hit this middleware
router.use(function (req, res, next) {
  console.log('%s %s %s', req.method, req.url, req.path)
  next()
})

// this will only be invoked if the path starts with /bar from the mount point
router.use('/bar', function (req, res, next) {
  // ... maybe some additional /bar logging ...
  next()
})

// always invoked
router.use(function (req, res, next) {
  res.send('Hello World')
})

app.use('/foo', router)

app.listen(3000)
```

The “mount” path is stripped and is _not_ visible to the middleware function. The main effect of this feature is that a mounted middleware function may operate without code changes regardless of its “prefix” pathname.

The order in which you define middleware with 
```plaintext
router.use()
```
 is very important. They are invoked sequentially, thus the order defines middleware precedence. For example, usually a logger is the very first middleware you would use, so that every request gets logged.

```
var logger = require('morgan')
var path = require('path')

router.use(logger())
router.use(express.static(path.join(__dirname, 'public')))
router.use(function (req, res) {
  res.send('Hello')
})
```

Now suppose you wanted to ignore logging requests for static files, but to continue logging routes and middleware defined after 
```plaintext
logger()
```
. You would simply move the call to 
```plaintext
express.static()
```
 to the top, before adding the logger middleware:

```
router.use(express.static(path.join(__dirname, 'public')))
router.use(logger())
router.use(function (req, res) {
  res.send('Hello')
})
```

Another example is serving files from multiple directories, giving precedence to “./public” over the others:

```
router.use(express.static(path.join(__dirname, 'public')))
router.use(express.static(path.join(__dirname, 'files')))
router.use(express.static(path.join(__dirname, 'uploads')))
```

The 
```plaintext
router.use()
```
 method also supports named parameters so that your mount points for other routers can benefit from preloading using named parameters.

**NOTE**: Although these middleware functions are added via a particular router, _when_ they run is defined by the path they are attached to (not the router). Therefore, middleware added via one router may run for other routers if its routes match. For example, this code shows two different routers mounted on the same path:

```
var authRouter = express.Router()
var openRouter = express.Router()

authRouter.use(require('./authenticate').basic(usersdb))

authRouter.get('/:user_id/edit', function (req, res, next) {
  // ... Edit user UI ...
})
openRouter.get('/', function (req, res, next) {
  // ... List users ...
})
openRouter.get('/:user_id', function (req, res, next) {
  // ... View user ...
})

app.use('/users', authRouter)
app.use('/users', openRouter)
```

Even though the authentication middleware was added via the 
```plaintext
authRouter
```
 it will run on the routes defined by the 
```plaintext
openRouter
```
 as well since both routers were mounted on 
```plaintext
/users
```
. To avoid this behavior, use different paths for each router.

[Edit this page](https://github.com/expressjs/expressjs.com/tree/gh-pages/_includes/api/en/4x)

[](https://expressjs.com/en/4x/api.html#)

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
