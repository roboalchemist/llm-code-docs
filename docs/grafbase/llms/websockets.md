# Source: https://grafbase.com/docs/gateway/configuration/websockets.md

## Websocket subscriptions

Grafbase Gateway supports GraphQL subscriptions over websockets, in addition to SSE and multipart streams. The same protocol is used for communication between the client and the gateway, and between the gateway and the subgraph implementing the subscription: [graphql-transport-ws](https://github.com/graphql/graphql-over-http/blob/main/rfcs/GraphQLOverWebSocket.md). The protocol was developed and popularized by the [graphql-ws](https://github.com/enisdenjo/graphql-ws/blob/master/PROTOCOL.md) library. It is being standardized as part of the GraphQL over HTTP specification, and in our experience, it is by far the most common.

If you need the gateway to support other websocket protocols, please [let us know](/contact)!

The gateway exposes websocket subscriptions on the `/ws` endpoint, with the `ws://` or `wss://` scheme. The gateway will automatically upgrade the connection to a websocket connection if the client sends a `Connection: Upgrade` header. Please note that the the `Sec-WebSocket-Protocol` is required (and its value must currently be `graphql-transport-ws`), or the gateway will reject the request with a 400 Bad Request status code.

## Configuration

```toml
[websockets]
forward_connection_init_payload = false
```

- `forward_connection_init_payload`: When set to `true`, the gateway will forward the [ConnectionInit payload](https://github.com/graphql/graphql-over-http/blob/main/rfcs/GraphQLOverWebSocket.md#connectioninit) to the subgraph. This is useful when the subgraph requires additional information from the client, for example access tokens, during the connection initialization phase. The default value is `true`.