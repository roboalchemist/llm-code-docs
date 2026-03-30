# Source: https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management

Title: Explicit Resource Management | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management

Markdown Content:
Explicit Resource Management | Yoga
===============
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#nextra-skip-nav)

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
            *   [Dispose GraphQL Yoga](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#dispose-graphql-yoga)
            *   [Plugin Disposal](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#plugin-disposal)
            *   [Background jobs](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#background-jobs)

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

*   [Dispose GraphQL Yoga](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#dispose-graphql-yoga)
*   [Dispose on Node.js](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#dispose-on-nodejs)
*   [Plugin Disposal](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#plugin-disposal)
*   [Background jobs](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#background-jobs)

[Question? Give us feedback](https://github.com/graphql-hive/graphql-yoga/issues/new?title=Feedback%20for%20%E2%80%9CExplicit%20Resource%20Management%E2%80%9D&labels=kind/docs)[Edit this page on GitHub](https://github.com/graphql-hive/graphql-yoga/tree/main/website/src/content/docs/features/explicit-resource-management.mdx)Scroll to top

[Documentation](https://the-guild.dev/graphql/yoga-server/docs "Documentation")[Features](https://the-guild.dev/graphql/yoga-server/docs/features/schema "Features")Explicit Resource Management

Explicit Resource Management
============================

While implementing your GraphQL server with GraphQL Yoga, you need to control over the lifecycle of your resources. This is especially important when you are dealing with resources that need to be cleaned up when they are no longer needed, or clean up the operations in a queue when the server is shutting down.

Dispose GraphQL Yoga[](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#dispose-graphql-yoga)
---------------------------------------------------------------------------------------------------------------------------------

GraphQL Yoga supports [Explicit Resource Management](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management) approach that allows you to dispose of resources when they are no longer needed. This can be done in two ways shown below;

`await using` syntax`dispose` method

We use the `await using` syntax to create a new instance of `yoga` and dispose of it when the block is exited. Notice that we are using a block to limit the scope of `yoga` within `{ }`. So resources will be disposed of when the block is exited.

```
console.log('Yoga is starting')
{
  await using yoga = createYoga({
    schema: createSchema({
      typeDefs: /* GraphQL */ `
        type Query {
          hello: String
        }
      `,
      resolvers: {
        Query: {
          hello: () => 'world'
        }
      }
    })
  })
}
console.log('Yoga is disposed')
```

We create a new instance of `yoga` and

dispose of it using the `dispose` method.

```
console.log('Yoga is starting')
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String
      }
    `,
    resolvers: {
      Query: {
        hello: () => 'world'
      }
    }
  })
})
await yoga.dispose()
console.log('Yoga is disposed')
```

In the first example, we use the `await using` syntax to create a new instance of `yoga` and dispose of it when the block is exited. In the second example,

### Dispose on Node.js[](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#dispose-on-nodejs)

When running GraphQL Yoga on Node.js, you can use process event listeners or server’s `close` event to trigger GraphQL Yoga’s disposal. Or you can configure GraphQL Yoga to handle this automatically by listening `process` exit signals.

Explicit disposal Automatic disposal on process exit

We can dispose of the GraphQL Yoga instance when the server is closed like below.

```
import { createServer } from 'http'
import { createSchema, createYoga } from 'graphql-yoga'
 
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        hello: String
      }
    `,
    resolvers: {
      Query: { hello: () => 'world' }
    }
  })
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
server.once('close', async () => {
  await yoga.dispose()
  console.info('Server is disposed so is Yoga')
})
```

`disposeOnProcessTerminate` option will register an event listener for `process` termination in Node.js

```
import { createServer } from 'http'
import { createSchema, createYoga } from 'graphql-yoga'
 
createServer(
  createYoga({
    schema: createSchema({
      typeDefs: /* GraphQL */ `
        type Query {
          hello: String
        }
      `,
      resolvers: { Query: { hello: () => 'world' } }
    }),
    disposeOnProcessTerminate: true
  })
).listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Plugin Disposal[](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#plugin-disposal)
-----------------------------------------------------------------------------------------------------------------------

If you have plugins that need some internal resources to be disposed of, you can use the `onDispose` hook to dispose of them. This hook will be invoked when the GraphQL Yoga instance is disposed like above.

```
let dbConnection: Connection
const plugin = {
  onPluginInit: async () => {
    dbConnection = await createConnection()
  },
  onDispose: async () => {
    // Dispose of resources
    await dbConnection.close()
  }
}
```

Or you can flush a queue of operations when the server is shutting down.

```
const backgroundJobs: Promise<void>[] = []
 
const plugin = {
  onRequestParse() {
    backgroundJobs.push(
      sendAnalytics({
        /* ... */
      })
    )
  },
  onDispose: async () => {
    // Flush the queue of background jobs
    await Promise.all(backgroundJobs)
  }
}
```

But for this kind of purposes, `waitUntil` can be a better choice.

Background jobs[](https://the-guild.dev/graphql/yoga-server/docs/features/explicit-resource-management#background-jobs)
-----------------------------------------------------------------------------------------------------------------------

If you have background jobs that need to be completed before the environment is shut down. `waitUntil` is better choice than `onDispose`. In this case, those jobs will keep running in the background but in case of disposal, they will be awaited. `waitUntil` works so similar to [Cloudflare Workers’ `waitUntil` function](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/#parameters).

But GraphQL Yoga handles `waitUntil` even if it is not provided by the environment.

```
const yoga = createSchema({
  typeDefs: /* GraphQL */ `
    type Query {
      greetings(name: String!): String
    }
  `,
  resolvers: {
    Query: {
      hello: (_, args, context) => {
        // This does not block the response
        context.waitUntil(
          fetch('http://my-analytics.com/analytics', {
            method: 'POST',
            body: JSON.stringify({
              name: args.name,
              userAgent: context.request.headers.get('User-Agent')
            })
          })
        )
        return `Hello, ${args.name}`
      }
    }
  }
})
 
const res = await yoga.fetch('http://localhost:4000/graphql', {
  query: /* GraphQL */ `
    query {
      greetings(name: "John")
    }
  `
})
 
console.log(await res.json()) // { data: { greetings: "Hello, John" } }
 
await yoga.dispose()
// The fetch request for `analytics` will be awaited here
```

Last updated on March 6, 2026

[Request Customization](https://the-guild.dev/graphql/yoga-server/docs/features/request-customization "Request Customization")[Custom Plugins](https://the-guild.dev/graphql/yoga-server/docs/features/envelop-plugins "Custom Plugins")

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

Questions? Chat with us.We are online

Chat with The Guild
