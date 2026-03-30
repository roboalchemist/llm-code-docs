# Source: https://mswjs.io/docs/migrations/1.x-to-2.x

Title: 1.x → 2.x

URL Source: https://mswjs.io/docs/migrations/1.x-to-2.x

Markdown Content:
[About the release](https://mswjs.io/docs/migrations/1.x-to-2.x#about-the-release)
----------------------------------------------------------------------------------

Version 2.0 brings the biggest API change to the library since its inception. Alongside the new API, it includes various features, such as `ReadableStream` support, ESM-compatibility, and countless bug fixes. This guide will help you migrate your application to version 2.0. **We highly recommend you read it from start to finish.**

> Make sure to read the official announcement for this release if you’ve missed it!

[Introducing MSW 2.0 Official announcement post.](https://mswjs.io/blog/introducing-msw-2.0)
[Codemods](https://mswjs.io/docs/migrations/1.x-to-2.x#codemods)
----------------------------------------------------------------

Our friends at Codemod.com have prepared a fantastic **collection of codemods** that can help you migrate to MSW 2.0.

*   [**Codemods to migrate**](https://go.codemod.com/msw-codemods)

[Installation](https://mswjs.io/docs/migrations/1.x-to-2.x#installation)
------------------------------------------------------------------------

`npm install msw@latest`

[Breaking changes](https://mswjs.io/docs/migrations/1.x-to-2.x#breaking-changes)
--------------------------------------------------------------------------------

### [Environment](https://mswjs.io/docs/migrations/1.x-to-2.x#environment)

#### [Node.js version](https://mswjs.io/docs/migrations/1.x-to-2.x#nodejs-version)

**This release sets the minimal supported Node.js version to 18.0.0.**

#### [TypeScript version](https://mswjs.io/docs/migrations/1.x-to-2.x#typescript-version)

**This release sets the minimal supported TypeScript version to 4.7**. If you are using an older TypeScript version, please migrate to version 4.7 or later to use MSW. Please consider that at the moment of writing this TypeScript 4.6 is almost two years old.

### [Imports](https://mswjs.io/docs/migrations/1.x-to-2.x#imports)

#### [Worker imports](https://mswjs.io/docs/migrations/1.x-to-2.x#worker-imports)

Everything related to the browser-side integration is now exported from the `msw/browser` entrypoint. This includes both the `setupWorker` function and the relevant type definitions.

**Before:**

`import { setupWorker } from 'msw'`

**After:**

`import { setupWorker } from 'msw/browser'`

### [Response resolver arguments](https://mswjs.io/docs/migrations/1.x-to-2.x#response-resolver-arguments)

Response resolver function no longer accepts `req`, `res`, and `ctx` arguments. Instead, it accepts a single argument which is an object containing information about the intercepted request.

**Before:**

`rest.get('/resource', (req, res, ctx) => {})`

**After:**

`http.get('/resource', (info) => {})`

Depending on the handler namespace used (`http` or `graphql`), the `info` object contains different properties. You can learn about how to access request information now in the [Request changes](https://mswjs.io/docs/migrations/1.x-to-2.x#request-changes).

Learn more about the updated call signature of the request handler namespaces:

[http API reference for the `http` namespace.](https://mswjs.io/docs/api/http)[graphql API reference for the `graphql` namespace.](https://mswjs.io/docs/api/graphql)
### [Request changes](https://mswjs.io/docs/migrations/1.x-to-2.x#request-changes)

#### [Request URL](https://mswjs.io/docs/migrations/1.x-to-2.x#request-url)

Since the intercepted request is now described as a Fetch API `Request` instance, its `request.url` property is no longer a `URL` instance but a plain `string.`

**Before:**

```
rest.get('/resource', (req) => {
  const productId = req.url.searchParams.get('id')
})
```

**After:**

If you wish to operate with it as a `URL` instance, you should create it first from the `request.url` string.

```
import { http } from 'msw'
 
http.get('/resource', ({ request }) => {
  const url = new URL(request.url)
  const productId = url.searchParams.get('id')
})
```

#### [Request params](https://mswjs.io/docs/migrations/1.x-to-2.x#request-params)

Path parameters are no longer exposed under `req.params`.

**Before:**

```
rest.get('/post/:id', (req) => {
  const { id } = req.params
})
```

**After:**

To access path parameters, use the `params` object on the response resolver.

```
import { http } from 'msw'
 
http.get('/post/:id', ({ params }) => {
  const { id } = params
})
```

#### [Request cookies](https://mswjs.io/docs/migrations/1.x-to-2.x#request-cookies)

Request cookies are no longer exposed under `req.cookies.`

**Before:**

```
rest.get('/resource', (req) => {
  const { token } = req.cookies
})
```

**After:**

To access request cookies, use the `cookies` object on the response resolver.

```
import { http } from 'msw'
 
http.get('/resource', ({ cookies }) => {
  const { token } = cookies
})
```

#### [Request body](https://mswjs.io/docs/migrations/1.x-to-2.x#request-body)

You can no longer read the intercepted request body via the `req.body` property. In fact, according to the Fetch API specification, `request.body` will now return a `ReadableStream` if the body is set.

**Before:**

```
rest.post('/resource', (req) => {
  // The library would assume a JSON request body
  // based on the request's "Content-Type" header.
  const { id } = req.body
})
```

**After:**

MSW will **no longer assume the request body type**. Instead, you should read the request body as you wish using the standard `Request` methods like `.text()`, `.json()`, `.arrayBuffer()`, etc.

```
import { http } from 'msw'
 
http.post('/user', async ({ request }) => {
  // Read the request body as JSON.
  const user = await request.json()
  const { id } = user
})
```

### [Response declaration](https://mswjs.io/docs/migrations/1.x-to-2.x#response-declaration)

Mocked responses are no longer declared using the `res()` composition function. We are departing from the composition approach in favor of adhering to the web standards.

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.json({ id: 'abc-123' }))
})
```

**After:**

To declare a mocked response, create a Fetch API `Response` instance and return it from the response resolver.

```
import { http } from 'msw'
 
http.get('/resource', () => {
  return new Response(JSON.stringify({ id: 'abc-123' }), {
    headers: {
      'Content-Type': 'application/json',
    },
  })
})
```

To provide a less verbose interface and also support such features as mocking response cookies, the library now provides a custom `HttpResponse` class that you can use as a drop-in replacement for the native `Response` class.

```
import { http, HttpResponse } from 'msw'
 
export const handlers = [
  http.get('/resource', () => {
    return HttpResponse.json({ id: 'abc-123' })
  }),
]
```

Learn more about the new `HttpResponse` API:

[HttpResponse API reference for the `HttpResponse` class.](https://mswjs.io/docs/api/http-response)
### [`req.passthrough()`](https://mswjs.io/docs/migrations/1.x-to-2.x#reqpassthrough)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return req.passthrough()
})
```

**After:**

```
import { http, passthrough } from 'msw'
 
export const handlers = [
  http.get('/resource', () => {
    return passthrough()
  }),
]
```

### [`res.once()`](https://mswjs.io/docs/migrations/1.x-to-2.x#resonce)

Since the `res()` composition API is gone, so is the `res.once()` one-time request handler declaration.

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res.once(ctx.text('Hello world!'))
})
```

**After:**

To declare a one-time request handler, provide an object as the third argument to it, and set the `once` property of that object to `true`.

```
import { http, HttpResponse } from 'msw'
 
http.get(
  '/resource',
  () => {
    return new HttpResponse('Hello world!')
  },
  { once: true },
)
```

### [`res.networkError()`](https://mswjs.io/docs/migrations/1.x-to-2.x#resnetworkerror)

To mock a network error, call the `HttpResponse.error()` static method and return it from the response resolver.

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res.networkError('Custom error message')
})
```

**After:**

```
import { http, HttpResponse } from 'msw'
 
http.get('/resource', () => {
  return HttpResponse.error()
})
```

> Note that the [`Response.error()`](https://developer.mozilla.org/en-US/docs/Web/API/Response/error_static) doesn’t accept a custom error message. Previously, MSW did its best to coerce the custom error message you provided to the underlying request client but it never worked reliably because it’s up to the request client to handle or disregard the network error message.

### [Context utilities](https://mswjs.io/docs/migrations/1.x-to-2.x#context-utilities)

With this release we are deprecating the `ctx` utilities object. Instead, use the `HttpResponse` class to declare mocked response properties, like status, headers, or body.

#### [`ctx.status()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxstatus)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.status(201))
})
```

**After:**

```
import { http, HttpResponse } from 'msw'
 
http.get('/resource', () => {
  return new HttpResponse(null, {
    status: 201,
  })
})
```

#### [`ctx.set()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxset)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.set('X-Custom-Header', 'foo'))
})
```

**After:**

```
import { http, HttpResponse } from 'msw'
 
http.get('/resource', () => {
  return new HttpResponse(null, {
    headers: {
      'X-Custom-Header': 'foo',
    },
  })
})
```

> Learn about the standard [`Headers` API](https://developer.mozilla.org/en-US/docs/Web/API/Headers).

#### [`ctx.cookie()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxcookie)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.cookie('token', 'abc-123'))
})
```

**After:**

```
import { http, HttpResponse } from 'msw'
 
http.get('/resource', () => {
  return new HttpResponse(null, {
    headers: {
      'Set-Cookie': 'token=abc-123',
    },
  })
})
```

The library is able to detect whenever you are mocking response cookies via the `HttpResponse` class. If you wish to mock response cookies, you must use that class, since response cookies cannot be read on the native `Response` class after they are set.

#### [`ctx.body()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxbody)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.body('Hello world'), ctx.set('Content-Type', 'text/plain'))
})
```

**After:**

```
import { http, HttpResponse } from 'msw'
 
http.get('/resource', (req, res, ctx) => {
  return new HttpResponse('Hello world')
})
```

#### [`ctx.text()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxtext)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.text('Hello world!'))
})
```

**After:**

```
import { http, HttpResponse } from 'msw'
 
http.get('/resource', () => {
  return new HttpResponse('Hello world!')
})
```

#### [`ctx.json()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxjson)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.json({ id: 'abc-123' }))
})
```

**After:**

```
import { http, HttpResponse } from 'msw'
 
http.get('/resource', () => {
  return HttpResponse.json({ id: 'abc-123' })
})
```

> Note that you don’t have to explicitly specify the `Content-Type` response header when using static `HttpResponse` methods like `HttpResponse.text()`, `HttpResponse.json()`, and others.

#### [`ctx.xml()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxxml)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.xml('<foo>bar</foo>'))
})
```

**After:**

```
import { http, HttpResponse } from 'msw'
 
http.get('/resource', () => {
  return HttpResponse.xml('<foo>bar</foo>')
})
```

#### [`ctx.data()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxdata)

**Before:**

```
graphql.query('GetUser', (req, res, ctx) => {
  return res(
    ctx.data({
      user: {
        firstName: 'John',
      },
    }),
  )
})
```

**After:**

The `graphql` handler namespace no longer gets a special treatment. Instead, you should declare standard JSON responses directly.

To make the mocked response definition for GraphQL operations more comfortable, use the `HttpResponse.json()` static method:

```
import { graphql, HttpResponse } from 'msw'
 
graphql.query('GetUser', () => {
  return HttpResponse.json({
    data: {
      user: {
        firstName: 'John',
      },
    },
  })
})
```

> Using `HttpResponse`, you have to explicitly include the root-level `data` property on the response.

#### [`ctx.errors()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxerrors)

**Before:**

```
graphql.mutation('Login', (req, res, ctx) => {
  const { username } = req.variables
 
  return res(
    ctx.errors([
      {
        message: `Failed to login:  user "${username}" does not exist`,
      },
    ]),
  )
})
```

**After:**

```
import { graphql, HttpResponse } from 'msw'
 
graphql.mutation('Login', ({ variables }) => {
  const { username } = variables
 
  return HttpResponse.json({
    errors: [
      {
        message: `Failed to login:  user "${username}" does not exist`,
      },
    ],
  })
})
```

> Using `HttpResponse`, you have to explicitly include the `errors` root-level property on the response.

#### [`ctx.extensions()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxextensions)

**Before:**

```
graphql.query('GetUser', (req, res, ctx) => {
  return res(
    ctx.data({
      user: {
        firstName: 'John',
      },
    }),
    ctx.extensions({
      requestId: 'abc-123',
    }),
  )
})
```

**After:**

```
import { graphql, HttpResponse } from 'msw'
 
graphql.query('GetUser', () => {
  return HttpResponse.json({
    data: {
      user: {
        firstName: 'John',
      },
    },
    extensions: {
      requestId: 'abc-123',
    },
  })
})
```

#### [`ctx.delay()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxdelay)

**Before:**

```
rest.get('/resource', (req, res, ctx) => {
  return res(ctx.delay(500), ctx.text('Hello world'))
})
```

**After:**

The library now exports the `delay()` function that returns a timeout `Promise`. You can await it anywhere in your response resolvers to emulate server-side delay.

```
import { http, HttpResponse, delay } from 'msw'
 
http.get('/resource', async () => {
  await delay(500)
  return HttpResponse.text('Hello world')
})
```

The call signature of the `delay()` function remains identical to the previous `ctx.delay()`.

[delay API reference for the `delay` function.](https://mswjs.io/docs/api/delay)
#### [`ctx.fetch()`](https://mswjs.io/docs/migrations/1.x-to-2.x#ctxfetch)

**Before:**

```
rest.get('/resource', async (req, res, ctx) => {
  const originalResponse = await ctx.fetch(req)
  const originalJson = await originalResponse.json()
 
  return res(
    ctx.json({
      ...originalJson,
      mocked: true,
    }),
  )
})
```

**After:**

To perform an additional request within the handler, use the new `bypass` function exported from `msw`. This function wraps any given `Request` instance, marking it as the one MSW should ignore when intercepting requests.

```
import { http, HttpResponse, bypass } from 'msw'
 
http.get('/resource', async ({ request }) => {
  const originalResponse = await fetch(bypass(request))
  const originalJson = await originalResponse.json()
 
  return HttpResponse.json({
    ...originalJson,
    mocked: true,
  })
})
```

[bypass API reference for the `bypass` function.](https://mswjs.io/docs/api/bypass)
#### [`printHandlers()`](https://mswjs.io/docs/migrations/1.x-to-2.x#printhandlers)

The `.printHandlers()` method on `worker`/`server` has been removed in favor of the new `.listHandlers()` method.

**Before:**

`worker.printHandlers()`

**After:**

The new `.listHandlers()` method returns a read-only array of currently active request handlers.

```
worker.listHandlers().forEach((handler) => {
  console.log(handler.info.header)
})
```

### [onUnhandledRequest](https://mswjs.io/docs/migrations/1.x-to-2.x#onunhandledrequest)

The `request` argument of the `onUnhandledRequest` has changed from being an abstract request object to be a Fetch API `Request` instance. Take that into account when accessing its properties, like `request.url`.

**Before:**

```
server.listen({
  onUnhandledRequest(request, print) {
    const url = request.url
 
    if (url.pathname.includes('/assets/')) {
      return
    }
 
    print.warning()
  },
})
```

**After:**

The `request` argument is an instance of `Request`, which makes its `url` property a `string`.

```
server.listen({
  onUnhandledRequest(request, print) {
    // Create a new URL instance manually.
    const url = new URL(request.url)
 
    if (url.pathname.includes('/assets/')) {
      return
    }
 
    print.warning()
  },
})
```

### [Life-cycle events](https://mswjs.io/docs/migrations/1.x-to-2.x#life-cycle-events)

This release brings changes to the [Life-cycle events](https://mswjs.io/docs/api/life-cycle-events) listeners’ call signature.

**Before:**

`server.events.on('request:start', (request, requestId) => {})`

**After:**

Every life-cycle event listener now accepts _a single argument_ being an object.

`server.events.on('request:start', ({ request, requestId }) => {})`

[New API](https://mswjs.io/docs/migrations/1.x-to-2.x#new-api)
--------------------------------------------------------------

In addition to the breaking changes, this release introduces a list of new APIs. Most of them are focused on providing compatibility with the deprecated functionality.

*   [`HttpResponse`](https://mswjs.io/docs/api/http-response)
*   [`http`](https://mswjs.io/docs/api/http)
*   [`delay()`](https://mswjs.io/docs/api/delay)
*   [`passthrough()`](https://mswjs.io/docs/api/passthrough)
*   [`bypass()`](https://mswjs.io/docs/api/bypass)

[Frequent issues](https://mswjs.io/docs/migrations/1.x-to-2.x#frequent-issues)
------------------------------------------------------------------------------

### [`Request`/`Response`/`TextEncoder` is not defined (Jest)](https://mswjs.io/docs/migrations/1.x-to-2.x#requestresponsetextencoder-is-not-defined-jest)

This issue is caused by your environment not having the Node.js globals for one reason or another. This commonly happens when using `jest-environment-jsdom` because it intentionally replaces built-in APIs with polyfills, breaking their Node.js compatibility.

To fix this, use the [`jest-fixed-jsdom`](https://github.com/mswjs/jest-fixed-jsdom) environment instead of `jest-environment-jsdom`.

`npm i jest-fixed-jsdom`

```
// jest.config.js
module.exports = {
  testEnvironment: 'jest-fixed-jsdom',
}
```

This custom environment is a superset of `jest-environment-jsdom` with the built-in Node.js modules added back. That being said, there are a lot of things that Jest/JSDOM breaks in your test environment that are problematic to fix. **This setup is a workaround**.

If you find this setup cumbersome, consider migrating to a modern testing framework, like [Vitest](https://vitest.dev/), which has none of the Node.js globals issues and provides native ESM support out of the box.

### [Cannot find module ‘msw/node’ (JSDOM)](https://mswjs.io/docs/migrations/1.x-to-2.x#cannot-find-module-mswnode-jsdom)

This error is thrown by your test runner because JSDOM uses the `browser` export condition by default. This means that when you import any third-party packages, like MSW, JSDOM forces its `browser` export to be used as the entrypoint. This is incorrect and dangerous because _JSDOM still runs in Node.js_ and cannot guarantee full browser compatibility by design.

To fix this, set the `testEnvironmentOptions.customExportConditions` option in your `jest.config.js` to `['']`:

```
// jest.config.js
module.exports = {
  testEnvironmentOptions: {
    customExportConditions: [''],
  },
}
```

This will force JSDOM to use the default export condition when importing `msw/node`, resulting in correct imports.

### [`multipart/form-data is not supported` Error in Node.js](https://mswjs.io/docs/migrations/1.x-to-2.x#multipartform-data-is-not-supported-error-in-nodejs)

Earlier versions of Node.js, like v18.8.0, didn’t have official support for `request.formData()`. Please upgrade to the latest Node.js 18.x where such a support has been added.
