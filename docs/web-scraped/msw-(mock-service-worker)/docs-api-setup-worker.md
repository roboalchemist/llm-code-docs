# Source: https://mswjs.io/docs/api/setup-worker/

Title: setupWorker

URL Source: https://mswjs.io/docs/api/setup-worker/

Markdown Content:
setupWorker - Mock Service Worker
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

setupWorker
===========

Configure the interception of requests in a browser.

**Please consider disabling AdBlocker for this site.** Thank you for supporting the project.

The `setupWorker()` function prepares the client-worker communication channel to enable API mocking in the browser.

[Call signature](https://mswjs.io/docs/api/setup-worker/#call-signature)
------------------------------------------------------------------------

The `setupWorker()` function expects an optional list of [Request handlers](https://mswjs.io/docs/http/intercepting-requests) spread as its arguments and returns a [Worker instance](https://mswjs.io/docs/api/setup-worker/#worker-instance).

When called without any arguments, the function will return you a worker instance that has no network description (i.e. no request handlers). Use the methods like [`worker.use()`](https://mswjs.io/docs/api/setup-worker/use) and [`worker.resetHandlers()`](https://mswjs.io/docs/api/setup-worker/reset-handlers) to add and remove _runtime_ request handlers to the worker instance.

```
import { setupWorker } from 'msw/browser'
 
const worker = setupWorker()
// worker.start()
// worker.use(...handlers)
```

However, if you provide request handlers as the spread argument to the `setupWorker()` function, those handlers will be considered _initial_ and will always persist on the worker instance even when resetting the handlers (learn how to opt-out from this [here](https://mswjs.io/docs/api/setup-worker/reset-handlers)).

```
import { http, HttpResponse } from 'msw'
import { setupWorker } from 'msw/browser'
 
const worker = setupWorker(
  http.get('/resource', () => HttpResponse.json({ id: 'abc-123' })),
)
```

[Worker instance](https://mswjs.io/docs/api/setup-worker/#worker-instance)
--------------------------------------------------------------------------

The `setupWorker()` function returns you a _worker instance_ that is an object you can use to control API mocking in the current browser environment. Below, you can see the list of methods available on the worker instance.

### [Methods](https://mswjs.io/docs/api/setup-worker/#methods)

*   [`start(options)`](https://mswjs.io/docs/api/setup-worker/start)
*   [`stop()`](https://mswjs.io/docs/api/setup-worker/stop)
*   [`use(...handlers)`](https://mswjs.io/docs/api/setup-worker/use)
*   [`resetHandlers(...handlers)`](https://mswjs.io/docs/api/setup-worker/reset-handlers)
*   [`restoreHandlers()`](https://mswjs.io/docs/api/setup-worker/restore-handlers)
*   [`listHandlers()`](https://mswjs.io/docs/api/setup-worker/list-handlers)
    *   The `.printHandlers()` method on `worker`/`server` has been removed in favor of the new `.listHandlers()` method.

Last updated on  November 10, 2025

[Edit this page on GitHub](https://github.com/mswjs/mswjs.io/edit/main/websites/mswjs.io/src/content/docs/api/setup-worker/index.mdx)
Was this helpful?

1.   🤩
2.   😐
3.   😩

#### Contents

*   [Call signature](https://mswjs.io/docs/api/setup-worker/#call-signature)
*   [Worker instance](https://mswjs.io/docs/api/setup-worker/#worker-instance)
    *   [Methods](https://mswjs.io/docs/api/setup-worker/#methods)

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
