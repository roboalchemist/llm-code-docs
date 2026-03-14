# Source: https://expressjs.com/en/guide/routing.html

Title: Express routing

URL Source: https://expressjs.com/en/guide/routing.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Express routing
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

*   [**English**](https://expressjs.com/en/guide/routing.html)
*   [Français](https://expressjs.com/fr/guide/routing.html)
*   [Deutsch](https://expressjs.com/de/guide/routing.html)
*   [Español](https://expressjs.com/es/guide/routing.html)
*   [Italiano](https://expressjs.com/it/guide/routing.html)
*   [日本語](https://expressjs.com/ja/guide/routing.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/guide/routing.html)
*   [繁體中文](https://expressjs.com/zh-tw/guide/routing.html)
*   [한국어](https://expressjs.com/ko/guide/routing.html)
*   [Português](https://expressjs.com/pt-br/guide/routing.html)

Routing
=======

_Routing_ refers to how an application’s endpoints (URIs) respond to client requests. For an introduction to routing, see [Basic routing](https://expressjs.com/en/starter/basic-routing.html).

You define routing using methods of the Express 
```plaintext
app
```
 object that correspond to HTTP methods; for example, 
```plaintext
app.get()
```
 to handle GET requests and 
```plaintext
app.post
```
 to handle POST requests. For a full list, see [app.METHOD](https://expressjs.com/en/5x/api.html#app.METHOD). You can also use [app.all()](https://expressjs.com/en/5x/api.html#app.all) to handle all HTTP methods and [app.use()](https://expressjs.com/en/5x/api.html#app.use) to specify middleware as the callback function (See [Using middleware](https://expressjs.com/en/guide/using-middleware.html) for details).

These routing methods specify a callback function (sometimes called “handler functions”) called when the application receives a request to the specified route (endpoint) and HTTP method. In other words, the application “listens” for requests that match the specified route(s) and method(s), and when it detects a match, it calls the specified callback function.

In fact, the routing methods can have more than one callback function as arguments. With multiple callback functions, it is important to provide 
```plaintext
next
```
 as an argument to the callback function and then call 
```plaintext
next()
```
 within the body of the function to hand off control to the next callback.

The following code is an example of a very basic route.

```
const express = require('express')
const app = express()

// respond with "hello world" when a GET request is made to the homepage
app.get('/', (req, res) => {
  res.send('hello world')
})
```

Route methods
-------------

A route method is derived from one of the HTTP methods, and is attached to an instance of the 
```plaintext
express
```
 class.

The following code is an example of routes that are defined for the 
```plaintext
GET
```
 and the 
```plaintext
POST
```
 methods to the root of the app.

```
// GET method route
app.get('/', (req, res) => {
  res.send('GET request to the homepage')
})

// POST method route
app.post('/', (req, res) => {
  res.send('POST request to the homepage')
})
```

Express supports methods that correspond to all HTTP request methods: 
```plaintext
get
```
, 
```plaintext
post
```
, and so on. For a full list, see [app.METHOD](https://expressjs.com/en/5x/api.html#app.METHOD).

There is a special routing method, 
```plaintext
app.all()
```
, used to load middleware functions at a path for _all_ HTTP request methods. For example, the following handler is executed for requests to the route 
```plaintext
"/secret"
```
 whether using 
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
, 
```plaintext
DELETE
```
, or any other HTTP request method supported in the [http module](https://nodejs.org/api/http.html#http_http_methods).

```
app.all('/secret', (req, res, next) => {
  console.log('Accessing the secret section ...')
  next() // pass control to the next handler
})
```

Route paths
-----------

Route paths, in combination with a request method, define the endpoints at which requests can be made. Route paths can be strings, string patterns, or regular expressions.

Caution

In express 5, the characters 
```plaintext
?
```
, 
```plaintext
+
```
, 
```plaintext
*
```
, 
```plaintext
[]
```
, and 
```plaintext
()
```
 are handled differently than in version 4, please review the [migration guide](https://expressjs.com/en/guide/migrating-5.html#path-syntax) for more information.

Caution

In express 4, regular expression characters such as 
```plaintext
$
```
 need to be escaped with a 
```plaintext
\
```
.

Note

Express uses [path-to-regexp](https://www.npmjs.com/package/path-to-regexp) for matching the route paths; see the path-to-regexp documentation for all the possibilities in defining route paths. [Express Playground Router](https://bjohansebas.github.io/playground-router/) is a handy tool for testing basic Express routes, although it does not support pattern matching.

Warning

Query strings are not part of the route path.

### Route paths based on strings

This route path will match requests to the root route, 
```plaintext
/
```
.

```
app.get('/', (req, res) => {
  res.send('root')
})
```

This route path will match requests to 
```plaintext
/about
```
.

```
app.get('/about', (req, res) => {
  res.send('about')
})
```

This route path will match requests to 
```plaintext
/random.text
```
.

```
app.get('/random.text', (req, res) => {
  res.send('random.text')
})
```

### Route paths based on string patterns

Caution

The string patterns in Express 5 no longer work. Please refer to the [migration guide](https://expressjs.com/en/guide/migrating-5.html#path-syntax) for more information.

This route path will match 
```plaintext
acd
```
 and 
```plaintext
abcd
```
.

```
app.get('/ab?cd', (req, res) => {
  res.send('ab?cd')
})
```

This route path will match 
```plaintext
abcd
```
, 
```plaintext
abbcd
```
, 
```plaintext
abbbcd
```
, and so on.

```
app.get('/ab+cd', (req, res) => {
  res.send('ab+cd')
})
```

This route path will match 
```plaintext
abcd
```
, 
```plaintext
abxcd
```
, 
```plaintext
abRANDOMcd
```
, 
```plaintext
ab123cd
```
, and so on.

```
app.get('/ab*cd', (req, res) => {
  res.send('ab*cd')
})
```

This route path will match 
```plaintext
/abe
```
 and 
```plaintext
/abcde
```
.

```
app.get('/ab(cd)?e', (req, res) => {
  res.send('ab(cd)?e')
})
```

### Route paths based on regular expressions

This route path will match anything with an “a” in it.

```
app.get(/a/, (req, res) => {
  res.send('/a/')
})
```

This route path will match 
```plaintext
butterfly
```
 and 
```plaintext
dragonfly
```
, but not 
```plaintext
butterflyman
```
, 
```plaintext
dragonflyman
```
, and so on.

```
app.get(/.*fly$/, (req, res) => {
  res.send('/.*fly$/')
})
```

Route parameters
----------------

Route parameters are named URL segments that are used to capture the values specified at their position in the URL. The captured values are populated in the 
```plaintext
req.params
```
 object, with the name of the route parameter specified in the path as their respective keys.

```
Route path: /users/:userId/books/:bookId
Request URL: http://localhost:3000/users/34/books/8989
req.params: { "userId": "34", "bookId": "8989" }
```

To define routes with route parameters, simply specify the route parameters in the path of the route as shown below.

```
app.get('/users/:userId/books/:bookId', (req, res) => {
  res.send(req.params)
})
```

The name of route parameters must be made up of “word characters” ([A-Za-z0-9_]).

Since the hyphen (
```plaintext
-
```
) and the dot (
```plaintext
.
```
) are interpreted literally, they can be used along with route parameters for useful purposes.

```
Route path: /flights/:from-:to
Request URL: http://localhost:3000/flights/LAX-SFO
req.params: { "from": "LAX", "to": "SFO" }
```

```
Route path: /plantae/:genus.:species
Request URL: http://localhost:3000/plantae/Prunus.persica
req.params: { "genus": "Prunus", "species": "persica" }
```

Caution

In express 5, Regexp characters are not supported in route paths, for more information please refer to the [migration guide](https://expressjs.com/en/guide/migrating-5.html#path-syntax).

To have more control over the exact string that can be matched by a route parameter, you can append a regular expression in parentheses (
```plaintext
()
```
):

```
Route path: /user/:userId(\d+)
Request URL: http://localhost:3000/user/42
req.params: {"userId": "42"}
```

Warning

Because the regular expression is usually part of a literal string, be sure to escape any 
```plaintext
\
```
 characters with an additional backslash, for example 
```plaintext
\\d+
```
.

Warning

In Express 4.x, [the ```plaintext * ``` character in regular expressions is not interpreted in the usual way](https://github.com/expressjs/express/issues/2495). As a workaround, use 
```plaintext
{0,}
```
 instead of 
```plaintext
*
```
. This will likely be fixed in Express 5.

Route handlers
--------------

You can provide multiple callback functions that behave like [middleware](https://expressjs.com/en/guide/using-middleware.html) to handle a request. The only exception is that these callbacks might invoke 
```plaintext
next('route')
```
 to bypass the remaining route callbacks. You can use this mechanism to impose pre-conditions on a route, then pass control to subsequent routes if there’s no reason to proceed with the current route.

```
app.get('/user/:id', (req, res, next) => {
  if (req.params.id === '0') {
    return next('route')
  }
  res.send(`User ${req.params.id}`)
})

app.get('/user/:id', (req, res) => {
  res.send('Special handler for user ID 0')
})
```

In this example:

*   ```plaintext
GET /user/5
```
 → handled by first route → sends “User 5”
*   ```plaintext
GET /user/0
```
 → first route calls 
```plaintext
next('route')
```
, skipping to the next matching 
```plaintext
/user/:id
```
 route

Route handlers can be in the form of a function, an array of functions, or combinations of both, as shown in the following examples.

A single callback function can handle a route. For example:

```
app.get('/example/a', (req, res) => {
  res.send('Hello from A!')
})
```

More than one callback function can handle a route (make sure you specify the 
```plaintext
next
```
 object). For example:

```
app.get('/example/b', (req, res, next) => {
  console.log('the response will be sent by the next function ...')
  next()
}, (req, res) => {
  res.send('Hello from B!')
})
```

An array of callback functions can handle a route. For example:

```
const cb0 = function (req, res, next) {
  console.log('CB0')
  next()
}

const cb1 = function (req, res, next) {
  console.log('CB1')
  next()
}

const cb2 = function (req, res) {
  res.send('Hello from C!')
}

app.get('/example/c', [cb0, cb1, cb2])
```

A combination of independent functions and arrays of functions can handle a route. For example:

```
const cb0 = function (req, res, next) {
  console.log('CB0')
  next()
}

const cb1 = function (req, res, next) {
  console.log('CB1')
  next()
}

app.get('/example/d', [cb0, cb1], (req, res, next) => {
  console.log('the response will be sent by the next function ...')
  next()
}, (req, res) => {
  res.send('Hello from D!')
})
```

Response methods
----------------

The methods on the response object (
```plaintext
res
```
) in the following table can send a response to the client, and terminate the request-response cycle. If none of these methods are called from a route handler, the client request will be left hanging.

| Method | Description |
| --- | --- |
| [res.download()](https://expressjs.com/en/5x/api.html#res.download) | Prompt a file to be downloaded. |
| [res.end()](https://expressjs.com/en/5x/api.html#res.end) | End the response process. |
| [res.json()](https://expressjs.com/en/5x/api.html#res.json) | Send a JSON response. |
| [res.jsonp()](https://expressjs.com/en/5x/api.html#res.jsonp) | Send a JSON response with JSONP support. |
| [res.redirect()](https://expressjs.com/en/5x/api.html#res.redirect) | Redirect a request. |
| [res.render()](https://expressjs.com/en/5x/api.html#res.render) | Render a view template. |
| [res.send()](https://expressjs.com/en/5x/api.html#res.send) | Send a response of various types. |
| [res.sendFile()](https://expressjs.com/en/5x/api.html#res.sendFile) | Send a file as an octet stream. |
| [res.sendStatus()](https://expressjs.com/en/5x/api.html#res.sendStatus) | Set the response status code and send its string representation as the response body. |

app.route()
-----------

You can create chainable route handlers for a route path by using 
```plaintext
app.route()
```
. Because the path is specified at a single location, creating modular routes is helpful, as is reducing redundancy and typos. For more information about routes, see: [Router() documentation](https://expressjs.com/en/5x/api.html#router).

Here is an example of chained route handlers that are defined by using 
```plaintext
app.route()
```
.

```
app.route('/book')
  .get((req, res) => {
    res.send('Get a random book')
  })
  .post((req, res) => {
    res.send('Add a book')
  })
  .put((req, res) => {
    res.send('Update the book')
  })
```

express.Router
--------------

Use the 
```plaintext
express.Router
```
 class to create modular, mountable route handlers. A 
```plaintext
Router
```
 instance is a complete middleware and routing system; for this reason, it is often referred to as a “mini-app”.

The following example creates a router as a module, loads a middleware function in it, defines some routes, and mounts the router module on a path in the main app.

Create a router file named 
```plaintext
birds.js
```
 in the app directory, with the following content:

```
const express = require('express')
const router = express.Router()

// middleware that is specific to this router
const timeLog = (req, res, next) => {
  console.log('Time: ', Date.now())
  next()
}
router.use(timeLog)

// define the home page route
router.get('/', (req, res) => {
  res.send('Birds home page')
})
// define the about route
router.get('/about', (req, res) => {
  res.send('About birds')
})

module.exports = router
```

Then, load the router module in the app:

```
const birds = require('./birds')

// ...

app.use('/birds', birds)
```

The app will now be able to handle requests to 
```plaintext
/birds
```
 and 
```plaintext
/birds/about
```
, as well as call the 
```plaintext
timeLog
```
 middleware function that is specific to the route.

But if the parent route 
```plaintext
/birds
```
 has path parameters, it will not be accessible by default from the sub-routes. To make it accessible, you will need to pass the 
```plaintext
mergeParams
```
 option to the Router constructor [reference](https://expressjs.com/en/5x/api.html#app.use).

```
const router = express.Router({ mergeParams: true })
```

[Next: Writing middleware for use in Express apps](https://expressjs.com/en/guide/writing-middleware.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/guide/routing.md)

[](https://expressjs.com/en/guide/routing.html#)

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
