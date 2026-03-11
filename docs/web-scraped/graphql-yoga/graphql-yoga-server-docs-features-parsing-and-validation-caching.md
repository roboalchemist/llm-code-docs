# Source: https://the-guild.dev/graphql/yoga-server/docs/features/parsing-and-validation-caching

Title: Parsing and Validation Caching | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/features/parsing-and-validation-caching

Markdown Content:
Parsing and Validation Caching | Yoga
===============
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/features/parsing-and-validation-caching#nextra-skip-nav)

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

[Question? Give us feedback](https://github.com/graphql-hive/graphql-yoga/issues/new?title=Feedback%20for%20%E2%80%9CParsing%20and%20Validation%20Caching%E2%80%9D&labels=kind/docs)[Edit this page on GitHub](https://github.com/graphql-hive/graphql-yoga/tree/main/website/src/content/docs/features/parsing-and-validation-caching.mdx)Scroll to top

[Documentation](https://the-guild.dev/graphql/yoga-server/docs "Documentation")[Features](https://the-guild.dev/graphql/yoga-server/docs/features/schema "Features")Parsing and Validation Caching

Parsing and Validation Caching
==============================

By default, Yoga will maintain a parsing and validation cache. If requests contain documents that have been executed before, they will not be parsed and validated again.

Using the parser cache can improve performance up to ~60%, and using the validation cache up to ~50% (based on benchmarks).

This behavior is built-in and can be optionally disabled using the `parserAndValidationCache` options:

Disable validation and parser caching

```
import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
import { schema } from './my-schema'
 
const yoga = createYoga({
  schema,
  parserAndValidationCache: false // disable parse and validate caching
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Furthermore, you can provide your own cache store to both of these plugins by implementing the following interface:

Custom cache store

```
import { createServer } from 'node:http'
import { DocumentNode, validate } from 'graphql'
import { createYoga } from 'graphql-yoga'
import { documentCacheStore, errorCacheStore, validationCacheStore } from './my-cache'
import { schema } from './my-schema'
 
interface CacheStore<T> {
  get(key: string): T | undefined
  set(key: string, value: T): void
}
 
const yoga = createYoga({
  schema,
  parserAndValidationCache: {
    documentCache: documentCacheStore as CacheStore<DocumentNode>,
    errorCache: errorCacheStore as CacheStore<Error>,
    validationCache: validationCacheStore as CacheStore<typeof validate>
  }
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Yoga uses a custom parser and validation cache plugin that’s built-in.

Last updated on March 6, 2026

[CSRF Prevention](https://the-guild.dev/graphql/yoga-server/docs/features/csrf-prevention "CSRF Prevention")[Response Caching](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching "Response Caching")

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
