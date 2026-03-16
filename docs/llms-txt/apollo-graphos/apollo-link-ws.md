# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-ws.md

# WebSocketLink

**We no longer recommend using `WebSocketLink` or the `subscriptions-transport-ws` library**, because the library is not actively maintained. To execute subscriptions, We instead recommend using the newer `graphql-ws` library with the accompanying [`GraphQLWsLink`](https://www.apollographql.com/docs/react/api/link/apollo-link-subscriptions).

Whichever library you use, make sure you use the *same* library in your server and any clients you support. For more information, see [Choosing a subscription library](https://www.apollographql.com/docs/react/data/subscriptions/#choosing-a-subscription-library).

`WebSocketLink` is a terminating link that executes GraphQL operations over WebSocket connections using the `subscriptions-transport-ws` library. It's primarily used for GraphQL subscriptions but can also handle queries and mutations.

TypeScript

```
 import { WebSocketLink } from "@apollo/client/link/ws";
 import { SubscriptionClient } from "subscriptions-transport-ws";

 const wsLink = new WebSocketLink(
   new SubscriptionClient("ws://localhost:4000/subscriptions", {
     reconnect: true,
   })
 );
```

## Constructor signature

```ts
constructor(
  paramsOrClient: WebSocketLink.Configuration | SubscriptionClient
): WebSocketLink
```

## Installation

`WebSocketLink` requires the [`subscriptions-transport-ws`](https://github.com/apollographql/subscriptions-transport-ws) library. Install it in your project:

```shell
npm install subscriptions-transport-ws
```

## Types

### [`WebSocketLink.Configuration`](https://www.apollographql.com/docs/react/api/link/apollo-link-ws.md#websocketlink.configuration)

Configuration options for creating a `WebSocketLink` instance.

Properties

Name / Type

Description

###### [`options`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-ws.md#configuration-options)

`ClientOptions`

Configuration options passed to the underlying `SubscriptionClient`.

These options configure the WebSocket connection behavior, including reconnection settings, connection parameters, and event handlers.

For a complete list of available options, see the [supported `subscriptions-transport-ws` options](https://github.com/apollographql/subscriptions-transport-ws/blob/master/src/client.ts#L61-L71).

###### [`uri`](https://www.apollographql.com/docs/react/api/link/apollo-link-ws.md#configuration-uri)

`string`

The WebSocket endpoint URI to connect to.

This should be a valid WebSocket URI (starting with `ws://` or `wss://`) that points to your GraphQL subscription endpoint.

"ws\://localhost:4000/subscriptions"

###### [`webSocketImpl`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-ws.md#configuration-websocketimpl)

`any`

A custom WebSocket implementation to use for the connection.

This is useful in environments that don't have native WebSocket support. You can provide a WebSocket polyfill or implementation that conforms to the W3C WebSocket API.

TypeScript

```
 import WebSocket from "ws";

 const wsLink = new WebSocketLink({
   uri: "ws://localhost:4000/subscriptions",
   webSocketImpl: WebSocket,
 });
```
