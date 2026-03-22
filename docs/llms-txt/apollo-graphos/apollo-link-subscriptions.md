# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-subscriptions.md

# GraphQLWsLink

The `GraphQLWsLink` is a terminating link sends GraphQL operations over a WebSocket connection using the [`graphql-ws`](https://www.npmjs.com/package/graphql-ws) library. It's used most commonly with GraphQL [subscriptions](https://apollographql.com/docs/react/data/subscriptions/),

**note**

This link works with the `graphql-ws` library. If your server uses the deprecated `subscriptions-transport-ws` library, use the deprecated [`WebSocketLink`](https://apollographql.com/docs/react/api/link/apollo-link-ws) link instead.

`GraphQLWsLink` requires the [`graphql-ws`](https://www.npmjs.com/package/graphql-ws) library. Install it in your project like so:

```shell
npm install graphql-ws
```

TypeScript

```
 import { GraphQLWsLink } from "@apollo/client/link/subscriptions";
 import { createClient } from "graphql-ws";

 const link = new GraphQLWsLink(
   createClient({
     url: "ws://localhost:3000/subscriptions",
   })
 );
```

## Constructor signature

```js
constructor(
  client: Client
): GraphQLWsLink
```

### Options

The `GraphQLWsLink` constructor takes a single argument: a `Client` instance from the `graphql-ws` library. To create this instance, call the library's [`createClient`](https://the-guild.dev/graphql/ws/docs/client/functions/createClient) function. This function requires a `url` option, which is the URL to your WebSocket server. WebSocket URLs typically start with `ws://` or `wss://`.

See the [`ClientOptions`](https://the-guild.dev/graphql/ws/docs/client/interfaces/ClientOptions) documentation for more details on the supported options provided to the `createClient` function.

#### Retrying failed connections

See the [`graphql-ws` recipes](https://the-guild.dev/graphql/ws/recipes) for strategies on retrying failed connections from the client. We generally recommend this approach over retrying failed connections from the link chain or your components because it provides more detailed information on why the connection failed.

Alternatively, you can handle retries more generically within the link chain by using [`RetryLink`](https://www.apollographql.com/docs/react/api/link/apollo-link-retry). This link resends the operation to the terminating link upon failure.

## Usage

See [Subscriptions](https://www.apollographql.com/docs/react/data/subscriptions/) for more information on using subscription operations in Apollo Client.
