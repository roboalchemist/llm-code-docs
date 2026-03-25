# Source: https://mswjs.io/docs/api/http-response

Title: HttpResponse

URL Source: https://mswjs.io/docs/api/http-response

Markdown Content:
HttpResponse - Mock Service Worker
===============

You are viewing the docs for **MSW 2.0**. To access the 1.x docs [click here](https://v1.mswjs.io/).

[![Image 1](https://mswjs.io/_astro/msw.ChZQPzKa.svg)](https://mswjs.io/ "Mock Service Worker")

 Search 

/

*   [Docs](https://mswjs.io/docs)
*   [Ecosystem](https://mswjs.io/ecosystem)
*   [Blog](https://mswjs.io/blog)
*   [Sponsor](https://github.com/sponsors/mswjs)
*   
    *   [Docs](https://mswjs.io/docs)
    *   [Ecosystem](https://mswjs.io/ecosystem)
    *   [Blog](https://mswjs.io/blog)

*   [Introduction](https://mswjs.io/docs/)
*   [Quick start](https://mswjs.io/docs/quick-start)
*   [Philosophy](https://mswjs.io/docs/philosophy)
*   [Comparison](https://mswjs.io/docs/comparison)
*   [Default behaviors](https://mswjs.io/docs/defaults)
*   [Limitations](https://mswjs.io/docs/limitations)
*   
[Migrations](https://mswjs.io/docs/migrations)
    *   [1.x → 2.x](https://mswjs.io/docs/migrations/1.x-to-2.x)

*   [Debugging runbook](https://mswjs.io/docs/runbook)
*   [FAQ](https://mswjs.io/docs/faq)
*    Mocking HTTP 
    *   [Introduction](https://mswjs.io/docs/http/)
    *   
[Intercepting requests](https://mswjs.io/docs/http/intercepting-requests/)
        *   [Path parameters](https://mswjs.io/docs/http/intercepting-requests/path-parameters)
        *   [Query parameters](https://mswjs.io/docs/http/intercepting-requests/query-parameters)
        *   [Request body](https://mswjs.io/docs/http/intercepting-requests/body)
        *   [Request cookies](https://mswjs.io/docs/http/intercepting-requests/cookies)

    *   [Handling requests](https://mswjs.io/docs/http/handling-requests)
    *   
[Mocking responses](https://mswjs.io/docs/http/mocking-responses/)
        *   [Error responses](https://mswjs.io/docs/http/mocking-responses/error-responses)
        *   [Network errors](https://mswjs.io/docs/http/mocking-responses/network-errors)
        *   [Binary responses](https://mswjs.io/docs/http/mocking-responses/binary)
        *   [Cookies](https://mswjs.io/docs/http/mocking-responses/cookies)
        *   [Redirects](https://mswjs.io/docs/http/mocking-responses/redirects)
        *   [Polling](https://mswjs.io/docs/http/mocking-responses/polling)
        *   [Streaming](https://mswjs.io/docs/http/mocking-responses/streaming)
        *   [Response timing](https://mswjs.io/docs/http/mocking-responses/response-timing)
        *   [File uploads](https://mswjs.io/docs/http/mocking-responses/file-uploads)
        *   [Proxying requests](https://mswjs.io/docs/http/mocking-responses/proxying-requests)
        *   [Response patching](https://mswjs.io/docs/http/mocking-responses/response-patching)

*    Mocking SSE 
    *   [Introduction](https://mswjs.io/docs/sse/)
    *   [Intercepting sources](https://mswjs.io/docs/sse/intercepting-sources/)
    *   
[Server events](https://mswjs.io/docs/sse/server-events/)
        *   [Message events](https://mswjs.io/docs/sse/server-events/message-events)
        *   [Custom events](https://mswjs.io/docs/sse/server-events/custom-events)
        *   [Retry](https://mswjs.io/docs/sse/server-events/retry)
        *   [Erroring the connection](https://mswjs.io/docs/sse/server-events/erroring-the-connection)
        *   [Closing the connection](https://mswjs.io/docs/sse/server-events/closing-the-connection)
        *   [Establishing server connection](https://mswjs.io/docs/sse/server-events/establishing-server-connection)

*    Mocking GraphQL 
    *   [Introduction](https://mswjs.io/docs/graphql/)
    *   
[Intercepting operations](https://mswjs.io/docs/graphql/intercepting-operations/)
        *   [Queries](https://mswjs.io/docs/graphql/intercepting-operations/queries)
        *   [Mutations](https://mswjs.io/docs/graphql/intercepting-operations/mutations)
        *   [Operations](https://mswjs.io/docs/graphql/intercepting-operations/operations)
        *   [Variables](https://mswjs.io/docs/graphql/intercepting-operations/variables)

    *   
[Mocking responses](https://mswjs.io/docs/graphql/mocking-responses/)
        *   [Errors](https://mswjs.io/docs/graphql/mocking-responses/errors)
        *   [Query batching](https://mswjs.io/docs/graphql/mocking-responses/query-batching)

    *   [Schema-first mocking](https://mswjs.io/docs/graphql/schema-first-mocking)

*    Mocking WebSocket 
    *   [Introduction](https://mswjs.io/docs/websocket/)
    *   
[Client events](https://mswjs.io/docs/websocket/client-events/)
        *   [Sending data](https://mswjs.io/docs/websocket/client-events/sending-data)
        *   [Broadcasting data](https://mswjs.io/docs/websocket/client-events/broadcasting-data)
        *   [Client-to-server forwarding](https://mswjs.io/docs/websocket/client-events/client-to-server-forwarding)
        *   [Closing client connection](https://mswjs.io/docs/websocket/client-events/closing-client-connection)
        *   [Erroring the connection](https://mswjs.io/docs/websocket/client-events/erroring-the-connection)

    *   
[Server events](https://mswjs.io/docs/websocket/server-events/)
        *   [Establishing server connection](https://mswjs.io/docs/websocket/server-events/establishing-server-connection)
        *   [Sending data](https://mswjs.io/docs/websocket/server-events/sending-data)
        *   [Server-to-client forwarding](https://mswjs.io/docs/websocket/server-events/server-to-client-forwarding)
        *   [Closing server connection](https://mswjs.io/docs/websocket/server-events/closing-server-connection)

    *   [Type safety](https://mswjs.io/docs/websocket/type-safety)
    *   [Event logs](https://mswjs.io/docs/websocket/event-logs)
    *   [Bindings](https://mswjs.io/docs/websocket/bindings)

*    Integrations 
    *   [Browser integration](https://mswjs.io/docs/integrations/browser)
    *   [Node.js integration](https://mswjs.io/docs/integrations/node)
    *   [React Native integration](https://mswjs.io/docs/integrations/react-native)

*    API 
    *   
[setupWorker](https://mswjs.io/docs/api/setup-worker/)
        *   [start()](https://mswjs.io/docs/api/setup-worker/start)
        *   [stop()](https://mswjs.io/docs/api/setup-worker/stop)
        *   [use()](https://mswjs.io/docs/api/setup-worker/use)
        *   [resetHandlers()](https://mswjs.io/docs/api/setup-worker/reset-handlers)
        *   [restoreHandlers()](https://mswjs.io/docs/api/setup-worker/restore-handlers)
        *   [listHandlers()](https://mswjs.io/docs/api/setup-worker/list-handlers)

    *   
[setupServer](https://mswjs.io/docs/api/setup-server/)
        *   [listen()](https://mswjs.io/docs/api/setup-server/listen)
        *   [close()](https://mswjs.io/docs/api/setup-server/close)
        *   [use()](https://mswjs.io/docs/api/setup-server/use)
        *   [boundary()](https://mswjs.io/docs/api/setup-server/boundary)
        *   [resetHandlers()](https://mswjs.io/docs/api/setup-server/reset-handlers)
        *   [restoreHandlers()](https://mswjs.io/docs/api/setup-server/restore-handlers)
        *   [listHandlers()](https://mswjs.io/docs/api/setup-server/list-handlers)

    *   [http](https://mswjs.io/docs/api/http)
    *   [graphql](https://mswjs.io/docs/api/graphql)
    *   [ws](https://mswjs.io/docs/api/ws)
    *   [sse](https://mswjs.io/docs/api/sse)
    *   [delay](https://mswjs.io/docs/api/delay)
    *   [HttpResponse](https://mswjs.io/docs/api/http-response)
    *   [bypass](https://mswjs.io/docs/api/bypass)
    *   [passthrough](https://mswjs.io/docs/api/passthrough)
    *   [RequestHandler](https://mswjs.io/docs/api/request-handler)
    *   [getResponse](https://mswjs.io/docs/api/get-response)
    *   [Life-cycle events](https://mswjs.io/docs/api/life-cycle-events)
    *   [isCommonAssetRequest](https://mswjs.io/docs/api/is-common-asset-request)

*    CLI 
    *   [init](https://mswjs.io/docs/cli/init)

*    Best practices 
    *   [Introduction](https://mswjs.io/docs/best-practices/)
    *   [Structuring handlers](https://mswjs.io/docs/best-practices/structuring-handlers)
    *   [Network behavior overrides](https://mswjs.io/docs/best-practices/network-behavior-overrides)
    *   [Avoid request assertions](https://mswjs.io/docs/best-practices/avoid-request-assertions)
    *   [Custom request predicate](https://mswjs.io/docs/best-practices/custom-request-predicate)
    *   [Dynamic mock scenarios](https://mswjs.io/docs/best-practices/dynamic-mock-scenarios)
    *   [Managing the worker](https://mswjs.io/docs/best-practices/managing-the-worker)
    *   [Using with TypeScript](https://mswjs.io/docs/best-practices/typescript)

*    Recipes 
    *   [Custom worker script location](https://mswjs.io/docs/recipes/custom-worker-script-location)
    *   [Global response delay](https://mswjs.io/docs/recipes/global-response-delay)
    *   [Higher-order resolver](https://mswjs.io/docs/recipes/higher-order-resolver)
    *   [Keeping mocks in sync](https://mswjs.io/docs/recipes/keeping-mocks-in-sync)
    *   [Merging Service Workers](https://mswjs.io/docs/recipes/merging-service-workers)
    *   [Using base URL](https://mswjs.io/docs/recipes/using-base-url)
    *   [Using CDN](https://mswjs.io/docs/recipes/using-cdn)
    *   [Using custom "homepage" property](https://mswjs.io/docs/recipes/using-custom-homepage)
    *   [Using local HTTPS](https://mswjs.io/docs/recipes/using-local-https)
    *   [Vitest Browser Mode](https://mswjs.io/docs/recipes/vitest-browser-mode)
    *   [XMLHttpRequest progress events](https://mswjs.io/docs/recipes/xmlhttprequest-progress-events)

*   [Introduction](https://mswjs.io/docs/)
*   [Quick start](https://mswjs.io/docs/quick-start)
*   [Philosophy](https://mswjs.io/docs/philosophy)
*   [Comparison](https://mswjs.io/docs/comparison)
*   [Default behaviors](https://mswjs.io/docs/defaults)
*   [Limitations](https://mswjs.io/docs/limitations)
*   
[Migrations](https://mswjs.io/docs/migrations)
    *   [1.x → 2.x](https://mswjs.io/docs/migrations/1.x-to-2.x)

*   [Debugging runbook](https://mswjs.io/docs/runbook)
*   [FAQ](https://mswjs.io/docs/faq)
*    Mocking HTTP 
    *   [Introduction](https://mswjs.io/docs/http/)
    *   
[Intercepting requests](https://mswjs.io/docs/http/intercepting-requests/)
        *   [Path parameters](https://mswjs.io/docs/http/intercepting-requests/path-parameters)
        *   [Query parameters](https://mswjs.io/docs/http/intercepting-requests/query-parameters)
        *   [Request body](https://mswjs.io/docs/http/intercepting-requests/body)
        *   [Request cookies](https://mswjs.io/docs/http/intercepting-requests/cookies)

    *   [Handling requests](https://mswjs.io/docs/http/handling-requests)
    *   
[Mocking responses](https://mswjs.io/docs/http/mocking-responses/)
        *   [Error responses](https://mswjs.io/docs/http/mocking-responses/error-responses)
        *   [Network errors](https://mswjs.io/docs/http/mocking-responses/network-errors)
        *   [Binary responses](https://mswjs.io/docs/http/mocking-responses/binary)
        *   [Cookies](https://mswjs.io/docs/http/mocking-responses/cookies)
        *   [Redirects](https://mswjs.io/docs/http/mocking-responses/redirects)
        *   [Polling](https://mswjs.io/docs/http/mocking-responses/polling)
        *   [Streaming](https://mswjs.io/docs/http/mocking-responses/streaming)
        *   [Response timing](https://mswjs.io/docs/http/mocking-responses/response-timing)
        *   [File uploads](https://mswjs.io/docs/http/mocking-responses/file-uploads)
        *   [Proxying requests](https://mswjs.io/docs/http/mocking-responses/proxying-requests)
        *   [Response patching](https://mswjs.io/docs/http/mocking-responses/response-patching)

*    Mocking SSE 
    *   [Introduction](https://mswjs.io/docs/sse/)
    *   [Intercepting sources](https://mswjs.io/docs/sse/intercepting-sources/)
    *   
[Server events](https://mswjs.io/docs/sse/server-events/)
        *   [Message events](https://mswjs.io/docs/sse/server-events/message-events)
        *   [Custom events](https://mswjs.io/docs/sse/server-events/custom-events)
        *   [Retry](https://mswjs.io/docs/sse/server-events/retry)
        *   [Erroring the connection](https://mswjs.io/docs/sse/server-events/erroring-the-connection)
        *   [Closing the connection](https://mswjs.io/docs/sse/server-events/closing-the-connection)
        *   [Establishing server connection](https://mswjs.io/docs/sse/server-events/establishing-server-connection)

*    Mocking GraphQL 
    *   [Introduction](https://mswjs.io/docs/graphql/)
    *   
[Intercepting operations](https://mswjs.io/docs/graphql/intercepting-operations/)
        *   [Queries](https://mswjs.io/docs/graphql/intercepting-operations/queries)
        *   [Mutations](https://mswjs.io/docs/graphql/intercepting-operations/mutations)
        *   [Operations](https://mswjs.io/docs/graphql/intercepting-operations/operations)
        *   [Variables](https://mswjs.io/docs/graphql/intercepting-operations/variables)

    *   
[Mocking responses](https://mswjs.io/docs/graphql/mocking-responses/)
        *   [Errors](https://mswjs.io/docs/graphql/mocking-responses/errors)
        *   [Query batching](https://mswjs.io/docs/graphql/mocking-responses/query-batching)

    *   [Schema-first mocking](https://mswjs.io/docs/graphql/schema-first-mocking)

*    Mocking WebSocket 
    *   [Introduction](https://mswjs.io/docs/websocket/)
    *   
[Client events](https://mswjs.io/docs/websocket/client-events/)
        *   [Sending data](https://mswjs.io/docs/websocket/client-events/sending-data)
        *   [Broadcasting data](https://mswjs.io/docs/websocket/client-events/broadcasting-data)
        *   [Client-to-server forwarding](https://mswjs.io/docs/websocket/client-events/client-to-server-forwarding)
        *   [Closing client connection](https://mswjs.io/docs/websocket/client-events/closing-client-connection)
        *   [Erroring the connection](https://mswjs.io/docs/websocket/client-events/erroring-the-connection)

    *   
[Server events](https://mswjs.io/docs/websocket/server-events/)
        *   [Establishing server connection](https://mswjs.io/docs/websocket/server-events/establishing-server-connection)
        *   [Sending data](https://mswjs.io/docs/websocket/server-events/sending-data)
        *   [Server-to-client forwarding](https://mswjs.io/docs/websocket/server-events/server-to-client-forwarding)
        *   [Closing server connection](https://mswjs.io/docs/websocket/server-events/closing-server-connection)

    *   [Type safety](https://mswjs.io/docs/websocket/type-safety)
    *   [Event logs](https://mswjs.io/docs/websocket/event-logs)
    *   [Bindings](https://mswjs.io/docs/websocket/bindings)

*    Integrations 
    *   [Browser integration](https://mswjs.io/docs/integrations/browser)
    *   [Node.js integration](https://mswjs.io/docs/integrations/node)
    *   [React Native integration](https://mswjs.io/docs/integrations/react-native)

*    API 
    *   
[setupWorker](https://mswjs.io/docs/api/setup-worker/)
        *   [start()](https://mswjs.io/docs/api/setup-worker/start)
        *   [stop()](https://mswjs.io/docs/api/setup-worker/stop)
        *   [use()](https://mswjs.io/docs/api/setup-worker/use)
        *   [resetHandlers()](https://mswjs.io/docs/api/setup-worker/reset-handlers)
        *   [restoreHandlers()](https://mswjs.io/docs/api/setup-worker/restore-handlers)
        *   [listHandlers()](https://mswjs.io/docs/api/setup-worker/list-handlers)

    *   
[setupServer](https://mswjs.io/docs/api/setup-server/)
        *   [listen()](https://mswjs.io/docs/api/setup-server/listen)
        *   [close()](https://mswjs.io/docs/api/setup-server/close)
        *   [use()](https://mswjs.io/docs/api/setup-server/use)
        *   [boundary()](https://mswjs.io/docs/api/setup-server/boundary)
        *   [resetHandlers()](https://mswjs.io/docs/api/setup-server/reset-handlers)
        *   [restoreHandlers()](https://mswjs.io/docs/api/setup-server/restore-handlers)
        *   [listHandlers()](https://mswjs.io/docs/api/setup-server/list-handlers)

    *   [http](https://mswjs.io/docs/api/http)
    *   [graphql](https://mswjs.io/docs/api/graphql)
    *   [ws](https://mswjs.io/docs/api/ws)
    *   [sse](https://mswjs.io/docs/api/sse)
    *   [delay](https://mswjs.io/docs/api/delay)
    *   [HttpResponse](https://mswjs.io/docs/api/http-response)
    *   [bypass](https://mswjs.io/docs/api/bypass)
    *   [passthrough](https://mswjs.io/docs/api/passthrough)
    *   [RequestHandler](https://mswjs.io/docs/api/request-handler)
    *   [getResponse](https://mswjs.io/docs/api/get-response)
    *   [Life-cycle events](https://mswjs.io/docs/api/life-cycle-events)
    *   [isCommonAssetRequest](https://mswjs.io/docs/api/is-common-asset-request)

*    CLI 
    *   [init](https://mswjs.io/docs/cli/init)

*    Best practices 
    *   [Introduction](https://mswjs.io/docs/best-practices/)
    *   [Structuring handlers](https://mswjs.io/docs/best-practices/structuring-handlers)
    *   [Network behavior overrides](https://mswjs.io/docs/best-practices/network-behavior-overrides)
    *   [Avoid request assertions](https://mswjs.io/docs/best-practices/avoid-request-assertions)
    *   [Custom request predicate](https://mswjs.io/docs/best-practices/custom-request-predicate)
    *   [Dynamic mock scenarios](https://mswjs.io/docs/best-practices/dynamic-mock-scenarios)
    *   [Managing the worker](https://mswjs.io/docs/best-practices/managing-the-worker)
    *   [Using with TypeScript](https://mswjs.io/docs/best-practices/typescript)

*    Recipes 
    *   [Custom worker script location](https://mswjs.io/docs/recipes/custom-worker-script-location)
    *   [Global response delay](https://mswjs.io/docs/recipes/global-response-delay)
    *   [Higher-order resolver](https://mswjs.io/docs/recipes/higher-order-resolver)
    *   [Keeping mocks in sync](https://mswjs.io/docs/recipes/keeping-mocks-in-sync)
    *   [Merging Service Workers](https://mswjs.io/docs/recipes/merging-service-workers)
    *   [Using base URL](https://mswjs.io/docs/recipes/using-base-url)
    *   [Using CDN](https://mswjs.io/docs/recipes/using-cdn)
    *   [Using custom "homepage" property](https://mswjs.io/docs/recipes/using-custom-homepage)
    *   [Using local HTTPS](https://mswjs.io/docs/recipes/using-local-https)
    *   [Vitest Browser Mode](https://mswjs.io/docs/recipes/vitest-browser-mode)
    *   [XMLHttpRequest progress events](https://mswjs.io/docs/recipes/xmlhttprequest-progress-events)

HttpResponse
============

[**Still Using Cursor?**Type a Task. Augment writes the code**Install Now**](https://server.ethicalads.io/proxy/click/10133/019ceab4-f1ad-71b1-8c4a-293a929b4796/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)

**Please consider disabling AdBlocker for this site.** Thank you for supporting the project.

The `HttpResponse` class is a drop-in replacement for the Fetch API Response designed to allow for more convenient response declaration and support otherwise unavailable features, like mocking response cookies.

[Why not native `Response`?](https://mswjs.io/docs/api/http-response#why-not-native-response)
---------------------------------------------------------------------------------------------

You can absolutely use the native Fetch API `Response` instances in your response resolvers. MSW is built on top of the standard request and response primitives, so you can use them any time instead.

However, the `HttpResponse` class enables certain features, like mocking response cookies, which are not available when using the standard `Response` class. For the sake of consistency, we highly recommend using the `HttpResponse` class on a daily basis. We acknowledge that it is a library-specific API and we are dedicated to make it teach you about the web fundamentals through respecting the default `Response` constructor signature and methods as well as minimizing the amount of library-specific features this class ships.

> Historically, the choice was between implicitly patching the global `Response` and `Headers` classes to establish a proxy setter whenever a `Set-Cookie` header is set, since it cannot be read afterward. We’ve decided not to meddle with the globals because we respect the integrity of your application and the environment it runs in, and want to prove that API mocking can be built on best practices and standard APIs instead.

[Call signature](https://mswjs.io/docs/api/http-response#call-signature)
------------------------------------------------------------------------

The `HttpResponse` class has the identical constructor signature to the Fetch API [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) class. This includes the static response methods like `Response.json()` and `Response.error()` too.

```
class HttpResponse {
  constructor(
    body:
      | Blob
      | ArrayBuffer
      | TypedArray
      | DateView
      | FormData
      | ReadableStream
      | URLSearchParams
      | string
      | null
      | undefined
    options?: {
      status?: number
      statusText?: string
      headers?: HeadersInit
    }
  )
}
```

[HttpResponse.ts Source code for the `HttpResponse` class.](https://github.com/mswjs/msw/tree/main/src/core/HttpResponse.ts)
[Standard methods](https://mswjs.io/docs/api/http-response#standard-methods)
----------------------------------------------------------------------------

### [`new HttpResponse(body, init)`](https://mswjs.io/docs/api/http-response#new-httpresponsebody-init)

Constructs a new `Response` instance with the given response body and options.

`const response = new HttpResponse('Hello world!')`

Similar to the regular `Response` constructor, you can provide `HttpResponse` with response options to customize the response instance:

```
// This is synonymous to "new Response()".
new HttpResponse('Not found', {
  status: 404,
  headers: {
    'Content-Type': 'text/plain',
  },
})
```

> Please see the [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response/Response) API to learn more about constructing responses.

### [`HttpResponse.json(body, init)`](https://mswjs.io/docs/api/http-response#httpresponsejsonbody-init)

A static method that creates a new response with the JSON body.

```
http.get('/resource', () => {
  // This is synonymous to "Response.json(body)".
  return HttpResponse.json({
    id: 'abc-123',
    title: 'Modern Testing Practices',
  })
})
```

As with other shorthand methods under the `HttpResponse` class, you can provide the `init` argument to describe your mocked response properties:

```
http.get('/resource', () => {
  return HttpResponse.json(
    {
      errorMessage: 'Missing session',
    },
    { status: 401 },
  )
})
```

### [`HttpResponse.error()`](https://mswjs.io/docs/api/http-response#httpresponseerror)

A static method that creates a new network error response instance.

```
http.get('/resource', () => {
  // This is synonymous to "Response.error()".
  return HttpResponse.error()
})
```

> Note that neither `HttpResponse.error()` nor `Response.error()` allow customizing the network error response. MSW chooses to abide by that behavior, especially since the custom network error messages are handled inconsistently across different request clients (some expose the error, others do not).

[Custom methods](https://mswjs.io/docs/api/http-response#custom-methods)
------------------------------------------------------------------------

The `HttpResponse` class also comes with a set of custom static methods to simplify response declaration. These methods do not have alternatives in the Fetch API specification and are entirely library-specific.

### [`HttpResponse.text(body, init)`](https://mswjs.io/docs/api/http-response#httpresponsetextbody-init)

Creates a `Response` instance with the `Content-Type: text/plain` header and given response body.

`HttpResponse.text('Hello world!')`

### [`HttpResponse.html(body, init)`](https://mswjs.io/docs/api/http-response#httpresponsehtmlbody-init)

Creates a `Response` instance with the `Content-Type: text/html` header and given response body.

`HttpResponse.html(`<p class="greeting">Hello world!</p>`)`

### [`HttpResponse.xml(body, init)`](https://mswjs.io/docs/api/http-response#httpresponsexmlbody-init)

Creates a `Response` instance with the `Content-Type: application/xml` header and given response body.

```
HttpResponse.xml(`
<post>
  <id>abc-123</id>
  <title>Modern Testing Practices</title>
</post>
`)
```

### [`HttpResponse.formData(body, init)`](https://mswjs.io/docs/api/http-response#httpresponseformdatabody-init)

Creates a `Response` instance with the `Content-Type: multipart/form-data` header and given response body.

```
const form = new FormData()
form.append('id', 'abc-123')
form.append('title', 'Modern Testing Practices')
 
HttpResponse.formData(form)
```

### [`HttpResponse.arrayBuffer(body, init)`](https://mswjs.io/docs/api/http-response#httpresponsearraybufferbody-init)

Creates a new `Response` instance with the given `ArrayBuffer` body. Automatically sets the `Content-Length` response header based on the buffer’s byte length. Does not set any additional headers like `Content-Type`.

```
HttpResponse.arrayBuffer(buffer, {
  headers: {
    'Content-Type': 'application/octet-stream',
  },
})
```

[Related materials](https://mswjs.io/docs/api/http-response#related-materials)
------------------------------------------------------------------------------

[Mocking responses Learn about response resolvers and the different ways to respond to a request.](https://mswjs.io/docs/http/mocking-responses/)

Last updated on  November 10, 2025

[Edit this page on GitHub](https://github.com/mswjs/mswjs.io/edit/main/websites/mswjs.io/src/content/docs/api/http-response.mdx)
Was this helpful?

1.   🤩
2.   😐
3.   😩

#### Contents

*   [Why not native Response?](https://mswjs.io/docs/api/http-response#why-not-native-response)
*   [Call signature](https://mswjs.io/docs/api/http-response#call-signature)
*   [Standard methods](https://mswjs.io/docs/api/http-response#standard-methods)
    *   [new HttpResponse(body, init)](https://mswjs.io/docs/api/http-response#new-httpresponsebody-init)
    *   [HttpResponse.json(body, init)](https://mswjs.io/docs/api/http-response#httpresponsejsonbody-init)
    *   [HttpResponse.error()](https://mswjs.io/docs/api/http-response#httpresponseerror)

*   [Custom methods](https://mswjs.io/docs/api/http-response#custom-methods)
    *   [HttpResponse.text(body, init)](https://mswjs.io/docs/api/http-response#httpresponsetextbody-init)
    *   [HttpResponse.html(body, init)](https://mswjs.io/docs/api/http-response#httpresponsehtmlbody-init)
    *   [HttpResponse.xml(body, init)](https://mswjs.io/docs/api/http-response#httpresponsexmlbody-init)
    *   [HttpResponse.formData(body, init)](https://mswjs.io/docs/api/http-response#httpresponseformdatabody-init)
    *   [HttpResponse.arrayBuffer(body, init)](https://mswjs.io/docs/api/http-response#httpresponsearraybufferbody-init)

*   [Related materials](https://mswjs.io/docs/api/http-response#related-materials)

#### Community

*   [GitHub](https://github.com/mswjs/msw)
*   [Discord](https://kettanaito.com/discord)
*   [Blog](https://mswjs.io/blog)

#### Partners

*   [](https://www.chromatic.com/?ref=mswjs)
*   [](https://workleap.com/?ref=mswjs)

© 2026 Mock Service Worker

Created with  by [kettanaito](https://twitter.com/kettanaito)

*   [](https://github.com/mswjs)
*   [](https://twitter.com/ApiMocking)
*   [](https://youtube.com/c/MockServiceWorker)
*   [](https://kettanaito.com/discord)
*   [](https://opencollective.com/mswjs)

#### Library

*   [Documentation](https://mswjs.io/docs)
*   [Branding](https://mswjs.io/branding)
*   [Blog](https://mswjs.io/blog)

#### Resources

*   [Quick start](https://mswjs.io/docs/quick-start)
*   [Best practices](https://mswjs.io/docs/best-practices)
*   [Examples](https://github.com/mswjs/examples)

#### Community

*   [GitHub](https://github.com/mswjs/msw)
*   [Twitter](https://twitter.com/ApiMocking)
*   [Discord](https://kettanaito.com/discord)
