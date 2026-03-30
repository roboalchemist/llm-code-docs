# Source: https://expressjs.com/en/guide/error-handling.html

Title: Express error handling

URL Source: https://expressjs.com/en/guide/error-handling.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Express error handling
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

*   [**English**](https://expressjs.com/en/guide/error-handling.html)
*   [Français](https://expressjs.com/fr/guide/error-handling.html)
*   [Deutsch](https://expressjs.com/de/guide/error-handling.html)
*   [Español](https://expressjs.com/es/guide/error-handling.html)
*   [Italiano](https://expressjs.com/it/guide/error-handling.html)
*   [日本語](https://expressjs.com/ja/guide/error-handling.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/guide/error-handling.html)
*   [繁體中文](https://expressjs.com/zh-tw/guide/error-handling.html)
*   [한국어](https://expressjs.com/ko/guide/error-handling.html)
*   [Português](https://expressjs.com/pt-br/guide/error-handling.html)

Error Handling
==============

_Error Handling_ refers to how Express catches and processes errors that occur both synchronously and asynchronously. Express comes with a default error handler so you don’t need to write your own to get started.

Catching Errors
---------------

It’s important to ensure that Express catches all errors that occur while running route handlers and middleware.

Errors that occur in synchronous code inside route handlers and middleware require no extra work. If synchronous code throws an error, then Express will catch and process it. For example:

```
app.get('/', (req, res) => {
  throw new Error('BROKEN') // Express will catch this on its own.
})
```

For errors returned from asynchronous functions invoked by route handlers and middleware, you must pass them to the 
```plaintext
next()
```
 function, where Express will catch and process them. For example:

```
app.get('/', (req, res, next) => {
  fs.readFile('/file-does-not-exist', (err, data) => {
    if (err) {
      next(err) // Pass errors to Express.
    } else {
      res.send(data)
    }
  })
})
```

Starting with Express 5, route handlers and middleware that return a Promise will call 
```plaintext
next(value)
```
 automatically when they reject or throw an error. For example:

```
app.get('/user/:id', async (req, res, next) => {
  const user = await getUserById(req.params.id)
  res.send(user)
})
```

If 
```plaintext
getUserById
```
 throws an error or rejects, 
```plaintext
next
```
 will be called with either the thrown error or the rejected value. If no rejected value is provided, 
```plaintext
next
```
 will be called with a default Error object provided by the Express router.

If you pass anything to the 
```plaintext
next()
```
 function (except the string 
```plaintext
'route'
```
), Express regards the current request as being an error and will skip any remaining non-error handling routing and middleware functions.

If the callback in a sequence provides no data, only errors, you can simplify this code as follows:

```
app.get('/', [
  function (req, res, next) {
    fs.writeFile('/inaccessible-path', 'data', next)
  },
  function (req, res) {
    res.send('OK')
  }
])
```

In the above example, 
```plaintext
next
```
 is provided as the callback for 
```plaintext
fs.writeFile
```
, which is called with or without errors. If there is no error, the second handler is executed, otherwise Express catches and processes the error.

You must catch errors that occur in asynchronous code invoked by route handlers or middleware and pass them to Express for processing. For example:

```
app.get('/', (req, res, next) => {
  setTimeout(() => {
    try {
      throw new Error('BROKEN')
    } catch (err) {
      next(err)
    }
  }, 100)
})
```

The above example uses a 
```plaintext
try...catch
```
 block to catch errors in the asynchronous code and pass them to Express. If the 
```plaintext
try...catch
```
 block were omitted, Express would not catch the error since it is not part of the synchronous handler code.

Use promises to avoid the overhead of the 
```plaintext
try...catch
```
 block or when using functions that return promises. For example:

```
app.get('/', (req, res, next) => {
  Promise.resolve().then(() => {
    throw new Error('BROKEN')
  }).catch(next) // Errors will be passed to Express.
})
```

Since promises automatically catch both synchronous errors and rejected promises, you can simply provide 
```plaintext
next
```
 as the final catch handler and Express will catch errors, because the catch handler is given the error as the first argument.

You could also use a chain of handlers to rely on synchronous error catching, by reducing the asynchronous code to something trivial. For example:

```
app.get('/', [
  function (req, res, next) {
    fs.readFile('/maybe-valid-file', 'utf-8', (err, data) => {
      res.locals.data = data
      next(err)
    })
  },
  function (req, res) {
    res.locals.data = res.locals.data.split(',')[1]
    res.send(res.locals.data)
  }
])
```

The above example has a couple of trivial statements from the 
```plaintext
readFile
```
 call. If 
```plaintext
readFile
```
 causes an error, then it passes the error to Express, otherwise you quickly return to the world of synchronous error handling in the next handler in the chain. Then, the example above tries to process the data. If this fails, then the synchronous error handler will catch it. If you had done this processing inside the 
```plaintext
readFile
```
 callback, then the application might exit and the Express error handlers would not run.

Whichever method you use, if you want Express error handlers to be called in and the application to survive, you must ensure that Express receives the error.

The default error handler
-------------------------

Express comes with a built-in error handler that takes care of any errors that might be encountered in the app. This default error-handling middleware function is added at the end of the middleware function stack.

If you pass an error to 
```plaintext
next()
```
 and you do not handle it in a custom error handler, it will be handled by the built-in error handler; the error will be written to the client with the stack trace. The stack trace is not included in the production environment.

Set the environment variable 
```plaintext
NODE_ENV
```
 to 
```plaintext
production
```
, to run the app in production mode.

When an error is written, the following information is added to the response:

*   The 
```plaintext
res.statusCode
```
 is set from 
```plaintext
err.status
```
 (or 
```plaintext
err.statusCode
```
). If this value is outside the 4xx or 5xx range, it will be set to 500.
*   The 
```plaintext
res.statusMessage
```
 is set according to the status code.
*   The body will be the HTML of the status code message when in production environment, otherwise will be 
```plaintext
err.stack
```
.
*   Any headers specified in an 
```plaintext
err.headers
```
 object.

If you call 
```plaintext
next()
```
 with an error after you have started writing the response (for example, if you encounter an error while streaming the response to the client), the Express default error handler closes the connection and fails the request.

So when you add a custom error handler, you must delegate to the default Express error handler, when the headers have already been sent to the client:

```
function errorHandler (err, req, res, next) {
  if (res.headersSent) {
    return next(err)
  }
  res.status(500)
  res.render('error', { error: err })
}
```

Note that the default error handler can get triggered if you call 
```plaintext
next()
```
 with an error in your code more than once, even if custom error handling middleware is in place.

Other error handling middleware can be found at [Express middleware](https://expressjs.com/en/resources/middleware.html).

Writing error handlers
----------------------

Define error-handling middleware functions in the same way as other middleware functions, except error-handling functions have four arguments instead of three: 
```plaintext
(err, req, res, next)
```
. For example:

```
app.use((err, req, res, next) => {
  console.error(err.stack)
  res.status(500).send('Something broke!')
})
```

You define error-handling middleware last, after other 
```plaintext
app.use()
```
 and routes calls; for example:

```
const bodyParser = require('body-parser')
const methodOverride = require('method-override')

app.use(bodyParser.urlencoded({
  extended: true
}))
app.use(bodyParser.json())
app.use(methodOverride())
app.use((err, req, res, next) => {
  // logic
})
```

Responses from within a middleware function can be in any format, such as an HTML error page, a simple message, or a JSON string.

For organizational (and higher-level framework) purposes, you can define several error-handling middleware functions, much as you would with regular middleware functions. For example, to define an error-handler for requests made by using 
```plaintext
XHR
```
 and those without:

```
const bodyParser = require('body-parser')
const methodOverride = require('method-override')

app.use(bodyParser.urlencoded({
  extended: true
}))
app.use(bodyParser.json())
app.use(methodOverride())
app.use(logErrors)
app.use(clientErrorHandler)
app.use(errorHandler)
```

In this example, the generic 
```plaintext
logErrors
```
 might write request and error information to 
```plaintext
stderr
```
, for example:

```
function logErrors (err, req, res, next) {
  console.error(err.stack)
  next(err)
}
```

Also in this example, 
```plaintext
clientErrorHandler
```
 is defined as follows; in this case, the error is explicitly passed along to the next one.

Notice that when _not_ calling “next” in an error-handling function, you are responsible for writing (and ending) the response. Otherwise, those requests will “hang” and will not be eligible for garbage collection.

```
function clientErrorHandler (err, req, res, next) {
  if (req.xhr) {
    res.status(500).send({ error: 'Something failed!' })
  } else {
    next(err)
  }
}
```

Implement the “catch-all” 
```plaintext
errorHandler
```
 function as follows (for example):

```
function errorHandler (err, req, res, next) {
  res.status(500)
  res.render('error', { error: err })
}
```

If you have a route handler with multiple callback functions, you can use the 
```plaintext
route
```
 parameter to skip to the next route handler. For example:

```
app.get('/a_route_behind_paywall',
  (req, res, next) => {
    if (!req.user.hasPaid) {
      // continue handling this request
      next('route')
    } else {
      next()
    }
  }, (req, res, next) => {
    PaidContent.find((err, doc) => {
      if (err) return next(err)
      res.json(doc)
    })
  })
```

In this example, the 
```plaintext
getPaidContent
```
 handler will be skipped but any remaining handlers in 
```plaintext
app
```
 for 
```plaintext
/a_route_behind_paywall
```
 would continue to be executed.

Calls to 
```plaintext
next()
```
 and 
```plaintext
next(err)
```
 indicate that the current handler is complete and in what state. 
```plaintext
next(err)
```
 will skip all remaining handlers in the chain except for those that are set up to handle errors as described above.

[Previous: Using template engines with Express](https://expressjs.com/en/guide/using-template-engines.html)[Next: Debugging Express](https://expressjs.com/en/guide/debugging.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/guide/error-handling.md)

[](https://expressjs.com/en/guide/error-handling.html#)

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
