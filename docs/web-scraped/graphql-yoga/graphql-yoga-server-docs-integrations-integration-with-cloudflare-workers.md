# Source: https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers

Title: Integration with Cloudflare Workers | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers

Markdown Content:
Integration with Cloudflare Workers | Yoga
===============
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#nextra-skip-nav)

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
            *   [Installation](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#installation)
            *   [Example with regular `fetch` event listener](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#example-with-regular-fetch-event-listener)
            *   [Example with Modules Approach](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#example-with-modules-approach)
            *   [Enabling Subscriptions](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#enabling-subscriptions)
            *   [Debug Logging](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#debug-logging)

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

*   [Installation](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#installation)
*   [Example with regular `fetch` event listener](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#example-with-regular-fetch-event-listener)
*   [Example with Modules Approach](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#example-with-modules-approach)
*   [Access to environmental values (KV Namespaces etc.)](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#access-to-environmental-values-kv-namespaces-etc)
*   [Enabling Subscriptions](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#enabling-subscriptions)
*   [Compatibility for Server Sent Events](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#compatibility-for-server-sent-events)
*   [Debug Logging](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#debug-logging)

[Question? Give us feedback](https://github.com/graphql-hive/graphql-yoga/issues/new?title=Feedback%20for%20%E2%80%9CIntegration%20with%20Cloudflare%20Workers%E2%80%9D&labels=kind/docs)[Edit this page on GitHub](https://github.com/graphql-hive/graphql-yoga/tree/main/website/src/content/docs/integrations/integration-with-cloudflare-workers.mdx)Scroll to top

[Documentation](https://the-guild.dev/graphql/yoga-server/docs "Documentation")[Integrations](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-aws-lambda "Integrations")Cloudflare Workers

Integration with Cloudflare Workers
===================================

GraphQL Yoga provides you a cross-platform GraphQL Server. So you can easily integrate it into any platform besides Node.js.

[Cloudflare Workers](https://developers.cloudflare.com/workers) provides a serverless execution environment that allows you to create entirely new applications or augment existing ones without configuring or maintaining infrastructure.

You will want to use the package `graphql-yoga` which has an agnostic HTTP handler using [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)’s [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) objects when building GraphQL powered Cloudflare Workers.

> Watch [Episode #48 of `graphql.wtf`](https://graphql.wtf/episodes/48-graphql-yoga-cloudflare-workers-kv) for a quick introduction to using GraphQL Yoga with Cloudflare Workers, and KV:

Installation[](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#installation)
----------------------------------------------------------------------------------------------------------------------------

npm pnpm yarn bun

`npm i graphql-yoga graphql`

`pnpm add graphql-yoga graphql`

`yarn add graphql-yoga graphql`

`bun add graphql-yoga graphql`

Example with regular `fetch` event listener[](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#example-with-regular-fetch-event-listener)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

listener.mjs

```
import { createSchema, createYoga } from 'graphql-yoga'
 
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `,
    resolvers: {
      Query: {
        hello: () => 'Hello World!'
      }
    }
  })
})
 
self.addEventListener('fetch', yoga)
```

> You can also check a full example on our GitHub repository [here](https://github.com/graphql-hive/graphql-yoga/tree/main/examples/service-worker)

Example with Modules Approach[](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#example-with-modules-approach)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

modules.mjs

```
import { createSchema, createYoga } from 'graphql-yoga'
 
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `,
    resolvers: {
      Query: {
        hello: () => 'Hello World!'
      }
    }
  })
})
export default { fetch: yoga.fetch }
```

### Access to environmental values (KV Namespaces etc.)[](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#access-to-environmental-values-kv-namespaces-etc)

You can access your KV namespaces etc through the context.

```
import { createSchema, createYoga } from 'graphql-yoga'
 
interface Env {
  MY_NAMESPACE: KVNamespace
}
 
const yoga = createYoga<Env>({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        todo(id: ID!): String
        todos: [String]
      }
      type Mutation {
        createTodo(id: ID!, text: String!): String
        deleteTodo(id: ID!): String
      }
    `,
    resolvers: {
      Query: {
        todo: (_, { id }, { MY_NAMESPACE }) => MY_NAMESPACE.get(id),
        todos: (_, __, { MY_NAMESPACE }) => MY_NAMESPACE.list()
      },
      Mutation: {
        // MY_NAMESPACE is available as a GraphQL context
        createTodo(_, { id, text }, context) {
          return context.MY_NAMESPACE.put(id, text)
        },
        deleteTodo(_, { id }, context) {
          return context.MY_NAMESPACE.delete(id)
        }
      }
    }
  })
})
 
export default { fetch: yoga.fetch }
```

If you need `ExecutionContext` as well inside your resolvers, you can extend the context type like below;

```
import { createYoga } from 'graphql-yoga'
 
interface Env {
  MY_NAMESPACE: KVNamespace
}
 
const yoga = createYoga<Env & ExecutionContext>({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String!
      }
    `,
    resolvers: {
      Query: {
        hello: () => 'Hello World!'
      }
    }
  })
})
 
export default { fetch: yoga.fetch }
```

> You can also check a full example on our GitHub repository [here](https://github.com/graphql-hive/graphql-yoga/tree/main/examples/cloudflare-modules)

Enabling Subscriptions[](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#enabling-subscriptions)
------------------------------------------------------------------------------------------------------------------------------------------------

For a library enabling topic-based subscriptions using GraphQL Yoga, `graphql-ws`, see [graphql-workers-subscriptions](https://github.com/bubblydoo/graphql-workers-subscriptions). This library uses Durable Objects and D1 to manage the subscriptions state.

### Compatibility for Server Sent Events[](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#compatibility-for-server-sent-events)

In order to enable Server Sent Events based subscriptions with Cloudflare Workers, make sure you have set the compatibility date in your wrangler configuration file to a date after 2022-11-30 (if that’s not possible, add compatibility flag `streams_enable_constructors`).

`compatibility_date = "2022-11-30"`

Debug Logging[](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-cloudflare-workers#debug-logging)
------------------------------------------------------------------------------------------------------------------------------

You should expose `DEBUG` variable in your environment to enable more verbose logging from GraphQL Yoga application.

Last updated on March 6, 2026

[AWS Lambda](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-aws-lambda "AWS Lambda")[Google Cloud Platform](https://the-guild.dev/graphql/yoga-server/docs/integrations/integration-with-gcp "Google Cloud Platform")

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
