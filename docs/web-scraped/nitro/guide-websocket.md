# Source: https://nitro.build/guide/websocket

-   [](/guide "Getting Started")

    ::: 
    []
    :::

    [Getting Started]
-   [](/deploy "Overview")

    ::: 
    []
    :::

    [Overview]
-   [](/config "Config")

    ::: 
    []
    :::

    [Config]

-   [[][Getting Started]](/guide)
-   [[][Server Utils]](/guide/utils)
-   [[][Tasks]](/guide/tasks)
-   [[][Server Routes]](/guide/routing)
-   [[][WebSocket]](/guide/websocket)
-   [[][KV Storage]](/guide/storage)
-   [[][SQL Database]](/guide/database)
-   [[][Cache]](/guide/cache)
-   [[][Fetch]](/guide/fetch)
-   [[][Assets]](/guide/assets)
-   [[][Plugins]](/guide/plugins)
-   [[][Configuration]](/guide/configuration)
-   [[][TypeScript]](/guide/typescript)
-   [[][Nightly Channel]](/guide/nightly)

<div>

# WebSocket 

Nitro natively supports a cross platform WebSocket API

</div>

<div>

Nitro natively supports runtime agnostic [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) API using [CrossWS](https://crossws.unjs.io/) and [H3 WebSocket](https://v1.h3.dev/guide/websocket).

[[]](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)[][] Read more in [WebSocket in MDN].

[[]](https://crossws.unjs.io/)[][] Read more in [CrossWS].

## [[[]]Opt-in to the experimental feature](#opt-in-to-the-experimental-feature) 

[] WebSockets support is currently experimental. See [nitrojs/nitro#2171](https://github.com/nitrojs/nitro/issues/2171) for platform support status.

In order to enable websocket support you need to enable the experimental `websocket` feature flag.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(
})
```

[]

``` 
export default defineNuxtConfig(
  }
})
```

## [[[]]Usage](#usage) 

Create a websocket handler in `server/routes/_ws.ts`.

[] You can use any route like `server/routes/chatroom.ts` to register upgrade handler on `/chatroom`.

[][server/routes/\_ws.ts]

[]

``` 
export default defineWebSocketHandler(,

  message(peer, message) 
  },

  close(peer, event) ,

  error(peer, error) ,
});
```

[] Nitro allows you defining multiple websocket handlers using same routing of event handlers.

Use a client to connect to server. Example: (`server/routes/websocket.ts`)

[][index.ts]

[]

``` 
export default defineEventHandler(() => );
```

Now you can try it on `/websocket` route!

[] Check out our [chat demo](https://nuxt-chat.pi0.io/) using Nitro Websocket API.

## [[[]]Server-Sent Events (SSE)](#server-sent-events-sse) 

As an alternative to WebSockets, you can use [Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

### [[[]]Example](#example) 

Create an SSE handler in `server/routes/sse.ts`.

[][server/routes/sse.ts]

[]

``` 
export default defineEventHandler(async (event) => `)
  }, 1000)

  eventStream.onClosed(async () => )

  return eventStream.send()
})
```

Then connect to this SSE endpoint from the client

[]

``` 
const eventSource = new EventSource('http://localhost:3000/sse')

eventSource.onmessage = (event) => 
```

[[]](https://v1.h3.dev/guide/websocket#server-sent-events-sse)[][] Read more in [SSE guide in H3].

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/3.websocket.md)

[](/guide/routing)

[]

Server Routes

Nitro supports filesystem routing to automatically map files to h3 routes.

[](/guide/storage)

[]

KV Storage

Nitro provides a built-in storage layer that can abstract filesystem or database or any other data source.

[On this page][[]]

[On this page][[]]

-   [[Opt-in to the experimental feature]](#opt-in-to-the-experimental-feature)
-   [[Usage]](#usage)
-   [[Server-Sent Events (SSE)]](#server-sent-events-sse)
    -   [[Example]](#example)