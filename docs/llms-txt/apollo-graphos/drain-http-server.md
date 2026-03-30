# Source: https://www.apollographql.com/docs/apollo-server/api/plugin/drain-http-server.md

# API Reference: Drain HTTP Server Plugin

## Using the plugin

> In the examples below, we use top-level [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top_level_await) calls to start our server asynchronously. Check out our [Getting Started](https://www.apollographql.com/docs/apollo-server/getting-started#step-2-install-dependencies) guide to see how we configured our project to support this.

This article documents the options for the `ApolloServerPluginDrainHttpServer` plugin, which you can import from `@apollo/server/plugin/drainHttpServer`.

This plugin is designed for use with `expressMiddleware` and other [framework integrations](https://www.apollographql.com/docs/apollo-server/integrations/integration-index) built on top of [Node `http.Server`s](https://nodejs.org/api/http.html#http_class_http_server). **We highly recommend** using this plugin to ensure your server shuts down gracefully.

> You do not need to use this plugin with the `startStandaloneServer` function; it automatically handles server draining.

When you use this plugin, Apollo Server will drain your HTTP server when you call the `stop()` method (which is also called for you when the `SIGTERM` and `SIGINT` signals are received, unless disabled with the [`stopOnTerminationSignals` constructor option](https://www.apollographql.com/docs/apollo-server/api/apollo-server/#stoponterminationsignals)).

Specifically, it will:

* Stop listening for new connections
* Close idle connections (i.e., connections with no current HTTP request)
* Close active connections whenever they become idle
* Wait for all connections to be closed
* After a grace period, if any connections remain active, forcefully close them.

This plugin is exported from the `@apollo/server` package. Here's a basic example of how to use it with Express:

```ts title=index.ts
import { ApolloServer } from '@apollo/server';
import { ApolloServerPluginDrainHttpServer } from '@apollo/server/plugin/drainHttpServer';
import { expressMiddleware } from '@as-integrations/express5';
import express from 'express';
import http from 'http';
import cors from 'cors';
import { typeDefs, resolvers } from './schema';

interface MyContext {
  token?: String;
}

const app = express();
// Our httpServer handles incoming requests to our Express app.
// Below, we tell Apollo Server to "drain" this httpServer,
// enabling our servers to shut down gracefully.
const httpServer = http.createServer(app);

const server = new ApolloServer<MyContext>({
  typeDefs,
  resolvers,
  plugins: [ApolloServerPluginDrainHttpServer({ httpServer })],
});
await server.start();

app.use(
  '/graphql',
  cors<cors.CorsRequest>(),
  express.json(),
  expressMiddleware(server, {
    context: async ({ req }) => ({ token: req.headers.token }),
  }),
);

await new Promise<void>((resolve) =>
  httpServer.listen({ port: 4000 }, resolve),
);

console.log(`🚀 Server ready at http://localhost:4000/graphql`);
```

## Options

Name /Type
Description

###### `httpServer`

[`http.Server`](https://nodejs.org/api/http.html#http_class_http_server)

The server to drain; required.

###### `stopGracePeriodMillis`

`number`

How long to wait before forcefully closing non-idle connections. Defaults to `10_000` (ten seconds).
