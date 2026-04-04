# Source: https://mswjs.io/docs/api/ws

Title: ws

URL Source: https://mswjs.io/docs/api/ws

Markdown Content:
ws - Mock Service Worker
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

ws
==

Intercept WebSocket connections.

**Please consider disabling AdBlocker for this site.** Thank you for supporting the project.

The `ws` namespace helps you create event handlers to intercept WebSocket connections.

[Call signature](https://mswjs.io/docs/api/ws#call-signature)
-------------------------------------------------------------

The `ws` namespace exposes a method called `link()`. The `link()` method creates a WebSocket link preconfigured to handle WebSocket connections matching the specified URL.

`ws.link(url: string | URL | RegExp)`

[ws.ts Source code for the `ws` namespace.](https://github.com/mswjs/msw/tree/main/src/core/ws.ts)
[Event handler](https://mswjs.io/docs/api/ws#event-handler)
-----------------------------------------------------------

The object returned from the `ws.link()` call is referred to as a _WebSocket link_. The link has the following properties and methods:

### [`.addEventListener(event, listener)`](https://mswjs.io/docs/api/ws#addeventlistenerevent-listener)

Adds a [connection listener](https://mswjs.io/docs/api/ws#connection-listener) for the outgoing WebSocket client connections.

### [`.clients`](https://mswjs.io/docs/api/ws#clients)

*   `Set<WebSocketClientConnection>`

The set of all active WebSocket clients.

### [`.broadcast(data)`](https://mswjs.io/docs/api/ws#broadcastdata)

*   `data: string | Blob | ArrayBuffer`

Sends the given data to all active WebSocket clients.

```
const api = ws.link('wss://*')
api.broadcast('hello, everyone')
```

### [`.broadcastExcept(clients, data)`](https://mswjs.io/docs/api/ws#broadcastexceptclients-data)

*   `clients: WebSocketClientConnection | Array<WebSocketClientConnection>`
*   `data: string | Blob | ArrayBuffer`

Sends the given data to all active WebSocket clients except the given `clients`.

```
const api = ws.link('wss://*')
 
api.addEventListener('connection', ({ client }) => {
  api.broadcastExcept(client, 'all except this')
})
```

You can also provide an array of WebSocket client connections as the argument to `clients`:

```
const ignoredClients = Array.from(api.clients).filter((client) => {
  return client.url.includes('abc')
})
 
api.broadcastExcept(ignoredClients, 'hello')
```

[Connection listener](https://mswjs.io/docs/api/ws#connection-listener)
-----------------------------------------------------------------------

| Argument | Type | Description |
| --- | --- | --- |
| `client` | [`WebSocketClientConnection`](https://mswjs.io/docs/api/ws#websocketclientconnection) | Outgoing WebSocket client connection object. |
| `server` | [`WebSocketServerConnection`](https://mswjs.io/docs/api/ws#websocketserverconnection) | Actual WebSocket server connection object. |
| `params` | `Record<string, string>` | Path parameters extracted from the connection `url`. |
| `info` | [`WebSocketConnectionInfo`](https://mswjs.io/docs/api/ws#websocketconnectioninfo) | Extra information about this WebSocket connection. |

The connection listener is called on every outgoing WebSocket client connection.

```
import { ws } from 'msw'
import { setupWorker } from 'msw/browser'
 
const api = ws.link('wss://chat.example.com')
 
const worker = setupWorker(
  api.addEventListener('connection', () => {
    console.log('client connected!')
  }),
)
 
await worker.start()
 
const socket = new WebSocket('wss://chat.example.com')
socket.onopen = () => {
  console.log('connection established!')
}
```

In this example, the WebSocket connection to `wss://chat.example.com` emits the `"connection"` event on the `api` event handler because the endpoint matches the one provided to the `ws.link()` call. Since the connection is successful, the `"open"` event is also dispatched on the `socket` instance.

[`WebSocketClientConnection`](https://mswjs.io/docs/api/ws#websocketclientconnection)
-------------------------------------------------------------------------------------

The `WebSocketClientConnection` object represents an intercepted WebSocket client connection from the _server’s_ perspective. This means that the `message` event on the client stands for a message _sent_ by the client and received by the “server”.

### [`.addEventListener(event, listener, options)`](https://mswjs.io/docs/api/ws#addeventlistenerevent-listener-options)

Adds a listener to the given client event. These are the supported client events:

| Event name | Description |
| --- | --- |
| `message` | Dispatched when this client _sends_ a message. |
| `error` | Dispatched when this client connection has been closed with an error. |
| `close` | Dispatched when this client is closed (e.g. by your application). |

### [`.removeEventListener(event, listener, options)`](https://mswjs.io/docs/api/ws#removeeventlistenerevent-listener-options)

Removes the listener for the given client event.

### [`.send(data)`](https://mswjs.io/docs/api/ws#senddata)

*   `data: string | Blob | ArrayBuffer`

Sends data to the WebSocket client. This is equivalent to the client receiving that data from the server.

```
api.addEventListener('connection', ({ client }) => {
  client.send('hello')
  client.send(new Blob(['hello']))
  client.send(new TextEncoder().encode('hello'))
})
```

### [`.close(code, reason)`](https://mswjs.io/docs/api/ws#closecode-reason)

*   `code: number | undefined`, default: `1000`
*   `reason: string | undefined`

Closes the active WebSocket client connection.

```
api.addEventListener('connection', ({ client }) => {
  client.close()
})
```

Unlike the `WebSocket.prototype.close()` method, the `client.close()` method accepts non-configurable close codes. This allows you to emulate client close scenarios based on server-side errors.

```
api.addEventListener('connection', ({ client }) => {
  client.addEventListener('message', (event) => {
    client.close(1003, 'Invalid data')
  })
})
```

You can also implement custom close code and reason:

```
api.addEventListener('connection', ({ client }) => {
  client.close(4000, 'Custom close reason')
})
```

[`WebSocketServerConnection`](https://mswjs.io/docs/api/ws#websocketserverconnection)
-------------------------------------------------------------------------------------

The `WebSocketServerConnection` object represents the actual WebSocket server connection.

### [`.connect()`](https://mswjs.io/docs/api/ws#connect)

Establishes connection to the actual WebSocket server.

```
api.addEventListener('connection', ({ server }) => {
  server.connect()
})
```

### [`.addEventListener(event, listener, options)`](https://mswjs.io/docs/api/ws#addeventlistenerevent-listener-options-1)

Adds a listener to the original server WebSocket connection. The supported events are:

| Event name | Description |
| --- | --- |
| `open` | Dispatched when the connection to the original server has been opened. |
| `message` | Dispatched when the original server _sends_ a message. |
| `error` | Dispatched when the original server connection has been closed with an error. |
| `close` | Dispatched when the original server connection has been closed. |

### [`.removeEventListener(event, listener, options)`](https://mswjs.io/docs/api/ws#removeeventlistenerevent-listener-options-1)

Removes the listener for the given server event.

### [`.send(data)`](https://mswjs.io/docs/api/ws#senddata-1)

*   `data: string | Blob | ArrayBuffer`

Sends data to the actual WebSocket server. This is equivalent to the client sending this data to the server.

```
api.addEventListener('connection', ({ server }) => {
  server.connect()
 
  server.addEventListener('message', (event) => {
    if (event.data === 'hello from server') {
      server.send('hello from client')
    }
  })
})
```

### [`.close(code, reason)`](https://mswjs.io/docs/api/ws#closecode-reason-1)

Closes the underlying original WebSocket server connection. Provides a custom close `code` and `reason`.

```
api.addEventListener('connection', ({ server }) => {
  server.connect()
  server.close()
})
```

[`WebSocketConnectionInfo`](https://mswjs.io/docs/api/ws#websocketconnectioninfo)
---------------------------------------------------------------------------------

The `info` argument on the `connection` event listener contains additional WebSocket connection information.

| Property name | Type | Description |
| --- | --- | --- |
| `protocols` | `string | string[] | undefined` | The list of protocols used when establishing this WebSocket connection. |

```
api.addEventListener('connection', ({ info }) => {
  if (info.protocols?.includes('chat')) {
    // Handle the chat protocol connection.
  }
})
```

Last updated on  November 10, 2025

[Edit this page on GitHub](https://github.com/mswjs/mswjs.io/edit/main/websites/mswjs.io/src/content/docs/api/ws.mdx)
Was this helpful?

1.   🤩
2.   😐
3.   😩

#### Contents

*   [Call signature](https://mswjs.io/docs/api/ws#call-signature)
*   [Event handler](https://mswjs.io/docs/api/ws#event-handler)
    *   [.addEventListener(event, listener)](https://mswjs.io/docs/api/ws#addeventlistenerevent-listener)
    *   [.clients](https://mswjs.io/docs/api/ws#clients)
    *   [.broadcast(data)](https://mswjs.io/docs/api/ws#broadcastdata)
    *   [.broadcastExcept(clients, data)](https://mswjs.io/docs/api/ws#broadcastexceptclients-data)

*   [Connection listener](https://mswjs.io/docs/api/ws#connection-listener)
*   [WebSocketClientConnection](https://mswjs.io/docs/api/ws#websocketclientconnection)
    *   [.addEventListener(event, listener, options)](https://mswjs.io/docs/api/ws#addeventlistenerevent-listener-options)
    *   [.removeEventListener(event, listener, options)](https://mswjs.io/docs/api/ws#removeeventlistenerevent-listener-options)
    *   [.send(data)](https://mswjs.io/docs/api/ws#senddata)
    *   [.close(code, reason)](https://mswjs.io/docs/api/ws#closecode-reason)

*   [WebSocketServerConnection](https://mswjs.io/docs/api/ws#websocketserverconnection)
    *   [.connect()](https://mswjs.io/docs/api/ws#connect)
    *   [.addEventListener(event, listener, options)](https://mswjs.io/docs/api/ws#addeventlistenerevent-listener-options-1)
    *   [.removeEventListener(event, listener, options)](https://mswjs.io/docs/api/ws#removeeventlistenerevent-listener-options-1)
    *   [.send(data)](https://mswjs.io/docs/api/ws#senddata-1)
    *   [.close(code, reason)](https://mswjs.io/docs/api/ws#closecode-reason-1)

*   [WebSocketConnectionInfo](https://mswjs.io/docs/api/ws#websocketconnectioninfo)

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
