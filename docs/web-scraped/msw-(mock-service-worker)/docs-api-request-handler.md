# Source: https://mswjs.io/docs/api/request-handler

Title: RequestHandler

URL Source: https://mswjs.io/docs/api/request-handler

Markdown Content:
RequestHandler - Mock Service Worker
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

RequestHandler
==============

The base class for request handler implementation.

[**Still Using Cursor?**Ask AI to Build a Feature. Augment creates a working PR.**Install Now**](https://server.ethicalads.io/proxy/click/10132/019ceab5-52fb-7300-86b1-55154fa55978/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)

**Please consider disabling AdBlocker for this site.** Thank you for supporting the project.

This class is meant for creating custom request handlers. Please prefer using the standard [`http`](https://mswjs.io/docs/api/http) and [`graphql`](https://mswjs.io/docs/api/graphql) namespaces before creating a custom request handler.

[Call signature](https://mswjs.io/docs/api/request-handler#call-signature)
--------------------------------------------------------------------------

```
import { RequestHandler } from 'msw'
 
export class CustomRequestHandler extends RequestHandler {
  constructor() {
    super(args)
  }
}
```

The `RequestHandler` class constructor expects a single `args` object with the following properties:

| Argument name | Type | Description |
| --- | --- | --- |
| `info` | `object` | Request handler [information](https://mswjs.io/docs/api/request-handler#info) object. |
| `resolver` | `Function` | [Response resolver](https://mswjs.io/docs/http/intercepting-requests/#response-resolver) function to handle matching requests. |
| `options` | `object` | _Optional_. Request handler [options](https://mswjs.io/docs/api/request-handler#request-handler-options). |

[Request handler options](https://mswjs.io/docs/api/request-handler#request-handler-options)
--------------------------------------------------------------------------------------------

### [`once`](https://mswjs.io/docs/api/request-handler#once)

*   _Optional_. `Boolean`.

When set to `true`, marks this request handler as inactive after the first …

[Properties](https://mswjs.io/docs/api/request-handler#properties)
------------------------------------------------------------------

### [`info`](https://mswjs.io/docs/api/request-handler#info)

*   `object`.

Information object about this request handler.

| Property name | Type | Description |
| --- | --- | --- |
| `header` | `string` | Public string representation of this request handler. |
| `callFrame` | `string` | The top-most frame of this request handler’s call. Useful for debugging. |

The `info` object on the request handler instance will also merge whatever object you provide as the `info` argument to the `RequestHandler` constructor.

```
class MyHandler extends RequestHandler {
  constructor(method, path, resolver) {
    super({
      info: {
        // Public representation of this request handler.
        // This string will be used when logging the handler
        // using the ".log()" method.
        header: `${method} ${path}`,
        // Additional info properties forwarded from the
        // constructor arguments of this custom handler.
        method,
        path,
      },
      resolver,
    })
  }
}
 
const handler = new MyHandler('GET', '/user')
console.log(handler.info.method) // "GET"
console.log(handler.info.path) // "/user"
```

The `info` object is meant for representing public information about the request handler. Do not use this object for internal handler context. Instead, declare whichever additional properties you need as private properties on the custom request handler class.

[Methods](https://mswjs.io/docs/api/request-handler#methods)
------------------------------------------------------------

### [`parse(args)`](https://mswjs.io/docs/api/request-handler#parseargs)

Parses the intercepted request to extract additional information for further request handler phases.

| Argument name | Type | Description |
| --- | --- | --- |
| `request` | `Request` | Intercepted request instance. |
| `context` | `object` | Request resolution context. |

### [`extendResolverArgs(args)`](https://mswjs.io/docs/api/request-handler#extendresolverargsargs)

Extends the response resolver argument object. Whichever object is returned from the `extendResolverArgs()` method gets shallow-merged with the default response resolver argument object.

| Argument name | Type | Description |
| --- | --- | --- |
| `request` | `Request` | Intercepted request instance. |
| `parsedResult` | `object` | The object returned from the `parse()` method. |
| `context` | `object` | Request resolution context. |

### [`predicate(args)`](https://mswjs.io/docs/api/request-handler#predicateargs)

Decides whether the intercepted request should be handled by this request handler. The `predicate()` method is expected to return a boolean.

| Argument name | Type | Description |
| --- | --- | --- |
| `request` | `Request` | Intercepted request instance. |
| `parsedResult` | `object` | The object returned from the `parse()` method. |
| `context` | `object` | Request resolution context. |

### [`log(args)`](https://mswjs.io/docs/api/request-handler#logargs)

Prints a browser console message whenever this request handler has handled the intercepted request.

| Argument name | Type | Description |
| --- | --- | --- |
| `request` | `Request` | Intercepted request instance. |
| `response` | `Response` | Response instance returned from the `resolver` function. |
| `parsedResult` | `object` | The object returned from the `parse()` method. |

[Request phases](https://mswjs.io/docs/api/request-handler#request-phases)
--------------------------------------------------------------------------

Whenever MSW intercepts a request, it will pass it to the request handler. The request handler will then process the request in phases listed in the following order:

### [Phase 1: Parsing](https://mswjs.io/docs/api/request-handler#phase-1-parsing)

First, the intercepted request instance will be parsed using the `parse()` method of the request handler. The parsing phase is designed to extract additional information from the request that is otherwise unavailable in the Fetch API `Request` instance.

Let’s create a custom `SearchParamsHandler` that will only handle requests whose search parameters will match the expected object.

```
// SearchParamsHandler.js
import { RequestHandler } from 'msw'
 
export class SearchParamsHandler extends RequestHandler {
  constructor(expectedParams, resolver) {
    super({
      info: { header: JSON.stringify(expectedParams) },
      resolver,
    })
    this.expectedParams = expectedParams
  }
 
  parse({ request }) {
    // Extract search parameters from the intercepted request URL.
    const searchParams = new URL(request.url).searchParams
 
    // Expose the search parameters for the other handler's methods.
    return {
      searchParams,
    }
  }
}
```

### [Phase 2: Predicate](https://mswjs.io/docs/api/request-handler#phase-2-predicate)

The next phase determines if the intercepted request should be handled by this request handler. The intercepted request instance and the parsing result returned from the `parse()` method are passed to the `predicate()` method of the request handler. The predicate method must return a boolean indicating whether this handler is meant to handle the intercepted request.

For example, let’s iterate on the custom `SearchParamsHandler` request handler to only match the intercepted requests whose search parameters match the provided `expectedParams` object.

```
// SearchParamsHandler.js
import { RequestHandler } from 'msw'
 
export class SearchParamsHandler extends RequestHandler {
  constructor(expectedParams, resolver) {
    super({
      info: { header: JSON.stringify(expectedParams) },
      resolver,
    })
    this.expectedParams = expectedParams
  }
 
  parse({ request }) {
    const searchParams = new URL(request.url).searchParams
 
    return {
      searchParams,
    }
  }
 
  predicate({ request, parsedResult }) {
    const { searchParams } = parsedResult
 
    // Iterate over the expected search parameters and
    // make sure that the actual request matches them.
    for (const [expectedParamName, expectedParamValue] of Object.entries(
      this.expectedParams,
    )) {
      if (searchParams.get(expectedParamName) !== expectedParamValue) {
        return false
      }
    }
 
    return true
  }
}
```

### [Phrase 3: Resolution](https://mswjs.io/docs/api/request-handler#phrase-3-resolution)

If the request handler returned `true` in the predicate phase, the resolution phase begins. The parent `RequestHandler` class handles the request resolution by executing the provided `resolver` function with the `request` instance and whichever additional information returned from the `extendResolverArgs()` method. The response returned from the resolver function is propagated to MSW and it applies it to the request.

Here’s an example of using the `extendResolverArgs()` method to extract `URLSearchParams` from the intercepted request’s URL and expose them as additional data on the response resolver argument.

```
// SearchParamsHandler.js
import { RequestHandler } from 'msw'
 
export class SearchParamsHandler extends RequestHandler {
  constructor(expectedParams, resolver) {
    super({
      info: { header: JSON.stringify(expectedParams) },
      resolver,
    })
  }
 
  parse({ request }) {
    const searchParams = new URL(request.url).searchParams
 
    return {
      searchParams,
    }
  }
 
  predicate({ request, parsedResult }) {
    /* Search params predicate here */
  }
 
  extendResolverArgs({ request, parsedResult }) {
    return {
      searchParams: parsedResult.searchParams,
    }
  }
}
```

```
// handlers.js
import { HttpResponse } from 'msw'
import { SearchParamsHandler } from './SearchParamsHandler'
 
export const handlers = [
  new SearchParamsHandler({ id: 'abc-123' }, ({ request, searchParams }) => {
    // The custom request handler exposes the reference to
    // the "URLSearchParams" instance of the intercepted request
    // so we can operate with it directly in the resolver.
    const id = searchParams.get('id')
    return HttpResponse.json({ id })
  }),
]
```

Last updated on  November 10, 2025

[Edit this page on GitHub](https://github.com/mswjs/mswjs.io/edit/main/websites/mswjs.io/src/content/docs/api/request-handler.mdx)
Was this helpful?

1.   🤩
2.   😐
3.   😩

#### Contents

*   [Call signature](https://mswjs.io/docs/api/request-handler#call-signature)
*   [Request handler options](https://mswjs.io/docs/api/request-handler#request-handler-options)
    *   [once](https://mswjs.io/docs/api/request-handler#once)

*   [Properties](https://mswjs.io/docs/api/request-handler#properties)
    *   [info](https://mswjs.io/docs/api/request-handler#info)

*   [Methods](https://mswjs.io/docs/api/request-handler#methods)
    *   [parse(args)](https://mswjs.io/docs/api/request-handler#parseargs)
    *   [extendResolverArgs(args)](https://mswjs.io/docs/api/request-handler#extendresolverargsargs)
    *   [predicate(args)](https://mswjs.io/docs/api/request-handler#predicateargs)
    *   [log(args)](https://mswjs.io/docs/api/request-handler#logargs)

*   [Request phases](https://mswjs.io/docs/api/request-handler#request-phases)
    *   [Phase 1: Parsing](https://mswjs.io/docs/api/request-handler#phase-1-parsing)
    *   [Phase 2: Predicate](https://mswjs.io/docs/api/request-handler#phase-2-predicate)
    *   [Phrase 3: Resolution](https://mswjs.io/docs/api/request-handler#phrase-3-resolution)

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
