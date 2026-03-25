# Source: https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server

Title: Migration from Apollo Server | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server

Markdown Content:
Migration from Apollo Server | Yoga
===============
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#nextra-skip-nav)

[Yoga](https://the-guild.dev/graphql/yoga-server)

[Yoga](https://the-guild.dev/graphql/yoga-server)

*   Products
*   Developer
*   Company
*   [Tutorial](https://the-guild.dev/graphql/yoga-server/tutorial)

v5

[Yoga 5 Docs (latest)](https://the-guild.dev/graphql/yoga-server/docs)[Yoga 4 Docs](https://the-guild.dev/graphql/yoga-server/v4)[Yoga 3 Docs](https://the-guild.dev/graphql/yoga-server/v3)[Yoga 2 Docs](https://the-guild.dev/graphql/yoga-server/v2)

⌘K

[Contact us](https://the-guild.dev/contact)[Docs](https://the-guild.dev/graphql/yoga-server/docs)

⌘K

*   Documentation

    *   [Quick start](https://the-guild.dev/graphql/yoga-server/docs)
    *   Features

        *   [GraphQL Schema](https://the-guild.dev/graphql/yoga-server/docs/features/schema)
        *   [GraphiQL](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql)
        *   [GraphQL Context](https://the-guild.dev/graphql/yoga-server/docs/features/context)
        *   [Error Masking](https://the-guild.dev/graphql/yoga-server/docs/features/error-masking)
        *   [Execution Cancellation](https://the-guild.dev/graphql/yoga-server/docs/features/execution-cancellation)
        *   [Introspection](https://the-guild.dev/graphql/yoga-server/docs/features/introspection)
        *   [Subscriptions](https://the-guild.dev/graphql/yoga-server/docs/features/subscriptions)
        *   [File Uploads](https://the-guild.dev/graphql/yoga-server/docs/features/file-uploads)
        *   [Defer and Stream](https://the-guild.dev/graphql/yoga-server/docs/features/defer-stream)
        *   [Batching](https://the-guild.dev/graphql/yoga-server/docs/features/request-batching)
        *   [CORS](https://the-guild.dev/graphql/yoga-server/docs/features/cors)
        *   [CSRF Prevention](https://the-guild.dev/graphql/yoga-server/docs/features/csrf-prevention)
        *   [Parsing and Validation Caching](https://the-guild.dev/graphql/yoga-server/docs/features/parsing-and-validation-caching)
        *   [Response Caching](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching)
        *   [Persisted Operations](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations)
        *   [Automatic Persisted Queries](https://the-guild.dev/graphql/yoga-server/docs/features/automatic-persisted-queries)
        *   [Logging and Debugging](https://the-guild.dev/graphql/yoga-server/docs/features/logging-and-debugging)
        *   [Health Check](https://the-guild.dev/graphql/yoga-server/docs/features/health-check)
        *   [REST API](https://the-guild.dev/graphql/yoga-server/docs/features/sofa-api)
        *   [Cookies](https://the-guild.dev/graphql/yoga-server/docs/features/cookies)
        *   [Apollo Federation](https://the-guild.dev/graphql/yoga-server/docs/features/apollo-federation)
        *   [Testing](https://the-guild.dev/graphql/yoga-server/docs/features/testing)
        *   [JWT](https://the-guild.dev/graphql/yoga-server/docs/features/jwt)
        *   [Landing Page](https://the-guild.dev/graphql/yoga-server/docs/features/landing-page)
        *   [Request Customization](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization)
        *   [Explicit Resource Management](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management)
        *   [Custom Plugins](https://the-guild.dev/graphql/yoga-server/docs/features/envelop-plugins)
        *   [Monitoring](https://the-guild.dev/graphql/yoga-server/docs/features/monitoring)

    *   [Preparing for Production](https://the-guild.dev/graphql/yoga-server/docs/prepare-for-production)
    *   Integrations

        *   [AWS Lambda](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-aws-lambda)
        *   [Cloudflare Workers](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers)
        *   [Google Cloud Platform](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-gcp)
        *   [Azure Functions](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-azure-functions)
        *   [Deno](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-deno)
        *   [Express](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-express)
        *   [Fastify](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-fastify)
        *   [Koa](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-koa)
        *   [NestJS](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-nestjs)
        *   [Next.js](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-nextjs)
        *   [SvelteKit](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-sveltekit)
        *   [Hapi](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-hapi)
        *   [Bun](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-bun)
        *   [µWebSockets.js](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-uwebsockets)
        *   [Other Environments](https://the-guild.dev/graphql/yoga-server/docs/integrations/z-other-environments)

    *   Migration

        *   [Apollo Server](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server)
            *   [Installation](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#installation)
            *   [Example initial usage of GraphQL Yoga](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#example-initial-usage-of-graphql-yoga)
            *   [Migration from standalone `apollo-server`](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#migration-from-standalone-apollo-server)
            *   [Migration from `apollo-server-*`](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#migration-from-apollo-server-)
            *   [Batched Queries/Requests](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#batched-queriesrequests)

        *   [Express GraphQL](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-express-graphql)
        *   [Yoga v1](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v1)
        *   [Yoga v2](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v2)
        *   [Yoga v3](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3)
        *   [Migration from Yoga V4](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v4)

    *   [Comparison](https://the-guild.dev/graphql/yoga-server/docs/comparison)

*   [Tutorial](https://the-guild.dev/graphql/yoga-server/tutorial)

System

*   [Quick start](https://the-guild.dev/graphql/yoga-server/docs)
*   Features

    *   [GraphQL Schema](https://the-guild.dev/graphql/yoga-server/docs/features/schema)
    *   [GraphiQL](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql)
    *   [GraphQL Context](https://the-guild.dev/graphql/yoga-server/docs/features/context)
    *   [Error Masking](https://the-guild.dev/graphql/yoga-server/docs/features/error-masking)
    *   [Execution Cancellation](https://the-guild.dev/graphql/yoga-server/docs/features/execution-cancellation)
    *   [Introspection](https://the-guild.dev/graphql/yoga-server/docs/features/introspection)
    *   [Subscriptions](https://the-guild.dev/graphql/yoga-server/docs/features/subscriptions)
    *   [File Uploads](https://the-guild.dev/graphql/yoga-server/docs/features/file-uploads)
    *   [Defer and Stream](https://the-guild.dev/graphql/yoga-server/docs/features/defer-stream)
    *   [Batching](https://the-guild.dev/graphql/yoga-server/docs/features/request-batching)
    *   [CORS](https://the-guild.dev/graphql/yoga-server/docs/features/cors)
    *   [CSRF Prevention](https://the-guild.dev/graphql/yoga-server/docs/features/csrf-prevention)
    *   [Parsing and Validation Caching](https://the-guild.dev/graphql/yoga-server/docs/features/parsing-and-validation-caching)
    *   [Response Caching](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching)
    *   [Persisted Operations](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations)
    *   [Automatic Persisted Queries](https://the-guild.dev/graphql/yoga-server/docs/features/automatic-persisted-queries)
    *   [Logging and Debugging](https://the-guild.dev/graphql/yoga-server/docs/features/logging-and-debugging)
    *   [Health Check](https://the-guild.dev/graphql/yoga-server/docs/features/health-check)
    *   [REST API](https://the-guild.dev/graphql/yoga-server/docs/features/sofa-api)
    *   [Cookies](https://the-guild.dev/graphql/yoga-server/docs/features/cookies)
    *   [Apollo Federation](https://the-guild.dev/graphql/yoga-server/docs/features/apollo-federation)
    *   [Testing](https://the-guild.dev/graphql/yoga-server/docs/features/testing)
    *   [JWT](https://the-guild.dev/graphql/yoga-server/docs/features/jwt)
    *   [Landing Page](https://the-guild.dev/graphql/yoga-server/docs/features/landing-page)
    *   [Request Customization](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization)
    *   [Explicit Resource Management](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management)
    *   [Custom Plugins](https://the-guild.dev/graphql/yoga-server/docs/features/envelop-plugins)
    *   [Monitoring](https://the-guild.dev/graphql/yoga-server/docs/features/monitoring)

*   [Preparing for Production](https://the-guild.dev/graphql/yoga-server/docs/prepare-for-production)
*   Integrations

    *   [AWS Lambda](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-aws-lambda)
    *   [Cloudflare Workers](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers)
    *   [Google Cloud Platform](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-gcp)
    *   [Azure Functions](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-azure-functions)
    *   [Deno](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-deno)
    *   [Express](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-express)
    *   [Fastify](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-fastify)
    *   [Koa](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-koa)
    *   [NestJS](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-nestjs)
    *   [Next.js](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-nextjs)
    *   [SvelteKit](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-sveltekit)
    *   [Hapi](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-hapi)
    *   [Bun](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-bun)
    *   [µWebSockets.js](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-uwebsockets)
    *   [Other Environments](https://the-guild.dev/graphql/yoga-server/docs/integrations/z-other-environments)

*   Migration

    *   [Apollo Server](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server)
    *   [Express GraphQL](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-express-graphql)
    *   [Yoga v1](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v1)
    *   [Yoga v2](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v2)
    *   [Yoga v3](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3)
    *   [Migration from Yoga V4](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v4)

*   [Comparison](https://the-guild.dev/graphql/yoga-server/docs/comparison)

System

On This Page

*   [Installation](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#installation)
*   [Install equivalent Envelop plugins of the Apollo Server](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#install-equivalent-envelop-plugins-of-the-apollo-server)
*   [Example initial usage of GraphQL Yoga](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#example-initial-usage-of-graphql-yoga)
*   [Migration from standalone `apollo-server`](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#migration-from-standalone-apollo-server)
*   [Migration from `apollo-server-*`](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#migration-from-apollo-server-)
*   [Batched Queries/Requests](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#batched-queriesrequests)

[Question? Give us feedback](https://github.com/graphql-hive/graphql-yoga/issues/new?title=Feedback%20for%20%E2%80%9CMigration%20from%20Apollo%20Server%E2%80%9D&labels=kind/docs)[Edit this page on GitHub](https://github.com/graphql-hive/graphql-yoga/tree/main/website/src/content/docs/migration/migration-from-apollo-server.mdx)Scroll to top

[Documentation](https://the-guild.dev/graphql/yoga-server/docs "Documentation")Migration Apollo Server

Migration from Apollo Server
============================

Installation[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#installation)
------------------------------------------------------------------------------------------------------------------

You can start with installing `graphql-yoga` package.

npm pnpm yarn bun

`npm i graphql-yoga`

`pnpm add graphql-yoga`

`yarn add graphql-yoga`

`bun add graphql-yoga`

### Install equivalent Envelop plugins of the Apollo Server[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#install-equivalent-envelop-plugins-of-the-apollo-server)

Some features that are included within apollo-server by default must be installed as envelop plugins ([Learn more about envelop plugins here](https://the-guild.dev/graphql/yoga-server/docs/features/envelop-plugins)).

*   Apollo Federation
    *   If you are using Apollo Federation, [install `@envelop/use-apollo-federation`](https://www.envelop.dev/plugins/use-apollo-federation)

*   Apollo Server Errors
    *   If you are using Apollo Server errors, [install `@envelop/use-apollo-server-errors`](https://www.envelop.dev/plugins/use-apollo-server-errors)

*   Apollo Tracing
    *   If you are using Apollo Tracing, [install `@envelop/use-apollo-tracing`](https://www.envelop.dev/plugins/use-apollo-tracing)

*   Response Cache
    *   If you are using Response Cache, [you should set up `@graphql-yoga/plugin-response-cache`](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching) for the same functionality

[Check out more plugins on Envelop Plugin Hub](https://www.envelop.dev/plugins)

Example initial usage of GraphQL Yoga[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#example-initial-usage-of-graphql-yoga)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

For example if you are using Apollo Server Errors;

`apollo-server-errors-example.ts`

```
import { schema } from './schema'
- import { ApolloServer } from 'apollo-server'
+ import { createYoga } from 'graphql-yoga'
+ import { useApolloServerErrors } from '@envelop/apollo-server-errors'
 
- const server = new ApolloServer({
+ const yoga = createYoga({
  // You can also pass `typeDefs` and `resolvers` here directly if you previously use `ApolloServer` constructor to build your `GraphQLSchema`
  // schema: createSchema({ typeDefs, resolvers }),
  schema,
+  plugins: [useApolloServerErrors()],
})
 
+ const server = createServer(yoga)
 
server.listen(4000)
```

Migration from standalone `apollo-server`[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#migration-from-standalone-apollo-server)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You don’t need anything special. You can just use GraphQL Yoga as in the example above.

Migration from `apollo-server-*`[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#migration-from-apollo-server-)
-------------------------------------------------------------------------------------------------------------------------------------------------------

Check the integration section to choose the server framework you are using with Apollo Server.

For example, if you are using **Express**, you should remove the standalone HTTP server part(`createServer(yoga)`&`server.listen(4000)`) from the code above and replace `server.applyMiddleware({ app })` with the route as in [Express Integration section](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-express)

```
- server.applyMiddleware({ app })
+ app.use('/graphql', yoga)
```

Batched Queries/Requests[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server#batched-queriesrequests)
-----------------------------------------------------------------------------------------------------------------------------------------

Batched queries is a practice first supported and made popular by the Apollo ecosystem. The idea of batched query operations is to reduce the number of network requests by grouping them together. This is achieved by slightly delaying the HTTP request in order to gather all the query operations that are executed shortly after each other.

GraphQL Yoga does not support batched queries for the following reasons:

**_All batched queries are as slow as the longest running individual query._**

Because the GraphQL server does not start sending a response to the client until all the queries are completed, a slow query will prevent a faster query result to be already processed/shown to the end user.

**_Batched queries can ba achieved by composing multiple GraphQL fragments/operation into a single one._**

Instead of having two operations:

```
query A {
  viewer {
    id
    name
  }
}
```

```
query B($postId: ID!) {
  post(id: $postId) {
    id
    title
  }
}
```

These operations can be combined into a single operation:

```
query AB($postId: ID!) {
  viewer {
    id
    name
  }
  post(id: $postId) {
    id
    title
  }
}
```

Furthermore, if you want a partial of the GraphQL operation to arrive at the client as soon as possible, you can use the `@defer` directive.

```
query AB($postId: ID!) {
  ... on Query @defer(label: "A") {
    viewer {
      id
      name
    }
  }
  ... on Query @defer(label: "A") {
    post(id: $postId) {
      id
      title
    }
  }
}
```

You can learn more on how to get the best out of this in our [“Unleash the power of Fragments with GraphQL Codegen” article](https://the-guild.dev/blog/unleash-the-power-of-fragments-with-graphql-codegen).

Last updated on March 6, 2026

[Other Environments](https://the-guild.dev/graphql/yoga-server/docs/integrations/z-other-environments "Other Environments")[Express GraphQL](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-express-graphql "Express GraphQL")

[Yoga](https://the-guild.dev/)
A fully-featured, simple to set up, performant and extendable server

### Products

*   [Hive](https://the-guild.dev/graphql/hive "Open Source GraphQL Federation Platform (Schema Registry, Gateway, Analytics)")
*   [Hive Gateway](https://the-guild.dev/graphql/hive/gateway "GraphQL Gateway (Router) for federated GraphQL with Subscriptions support and built-in security features")
*   [Yoga](https://the-guild.dev/graphql/yoga-server "A fully-featured, simple to set up, performant and extendable server")
*   [Mesh](https://the-guild.dev/graphql/mesh "A fully-featured GraphQL federation framework")
*   [Codegen](https://the-guild.dev/graphql/codegen "Generation of typed queries, mutations, subscriptions and typed GraphQL resolvers")
*   [Inspector](https://the-guild.dev/graphql/inspector "Schema management tool")
*   [Envelop](https://the-guild.dev/graphql/envelop "Develop and share plugins that are usable with any GraphQL server framework or schema")
*   [SOFA](https://the-guild.dev/graphql/sofa-api "Generate RESTful APIs from your GraphQL server")
*   [Scalars](https://the-guild.dev/graphql/scalars "Common custom GraphQL Scalars for precise type-safe GraphQL schemas")
*   [GraphQL ESLint](https://the-guild.dev/graphql/eslint "Customizable ESLint parser, plugin, and rule set for GraphQL")

### Developer

*   [Documentation](https://the-guild.dev/graphql/yoga-server/docs "Read the docs")
*   [Hive Status](https://status.graphql-hive.com/ "Check Hive status")
*   [Hive Updates](https://the-guild.dev/graphql/hive/product-updates "Read most recent developments from Hive")
*   [Blog](https://the-guild.dev/graphql/hive/blog "Read our blog")

### Company

*   [About](https://the-guild.dev/about-us "Learn more about us")
*   [Brand Assets](https://the-guild.dev/logos "Brand Assets")
*   [Newsletter](https://the-guild.dev/newsletter "Newsletter")

[OSS Friends](https://the-guild.dev/graphql/hive/oss-friends)[Pricing](https://the-guild.dev/graphql/hive/pricing)[Contact Us](https://the-guild.dev/contact)

[](https://github.com/the-guild-org "Check our GitHub account")[](https://twitter.com/TheGuildDev "Visit our Twitter")[](https://linkedin.com/company/the-guild-software "Visit our LinkedIn")[](https://discord.com/invite/xud7bH9 "Reach us on Discord")[](https://youtube.com/watch?v=d_GBgH-L5c4&list=PLhCf3AUOg4PgQoY_A6xWDQ70yaNtPYtZd "Watch Our Videos")

© 2026 The Guild
