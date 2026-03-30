# Source: https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3

Title: Migration from Yoga V3 | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3

Markdown Content:
Migration from Yoga V3 | Yoga
===============
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#nextra-skip-nav)

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
            *   [Install the new NPM package](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#install-the-new-npm-package)
            *   [Drop unused graphiql options `defaultVariableEditorOpen` and `headerEditorEnabled`](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#drop-unused-graphiql-options-defaultvariableeditoropen-and-headereditorenabled)
            *   [Subscriptions use GraphQL over SSE “distinct connections mode”](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#subscriptions-use-graphql-over-sse-distinct-connections-mode)
            *   [Subscriptions only use SSE (text/event-stream) as transport method](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#subscriptions-only-use-sse-textevent-stream-as-transport-method)
            *   [Parse and validation cache are now under a single option `parserAndValidationCache`](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#parse-and-validation-cache-are-now-under-a-single-option-parserandvalidationcache)

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

*   [Install the new NPM package](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#install-the-new-npm-package)
*   [Drop unused graphiql options `defaultVariableEditorOpen` and `headerEditorEnabled`](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#drop-unused-graphiql-options-defaultvariableeditoropen-and-headereditorenabled)
*   [Subscriptions use GraphQL over SSE “distinct connections mode”](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#subscriptions-use-graphql-over-sse-distinct-connections-mode)
*   [Subscriptions only use SSE (text/event-stream) as transport method](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#subscriptions-only-use-sse-textevent-stream-as-transport-method)
*   [Parse and validation cache are now under a single option `parserAndValidationCache`](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#parse-and-validation-cache-are-now-under-a-single-option-parserandvalidationcache)

[Question? Give us feedback](https://github.com/graphql-hive/graphql-yoga/issues/new?title=Feedback%20for%20%E2%80%9CMigration%20from%20Yoga%20V3%E2%80%9D&labels=kind/docs)[Edit this page on GitHub](https://github.com/graphql-hive/graphql-yoga/tree/main/website/src/content/docs/migration/migration-from-yoga-v3.mdx)Scroll to top

[Documentation](https://the-guild.dev/graphql/yoga-server/docs "Documentation")[Migration](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-apollo-server "Migration")Yoga v3

Migration from Yoga V3
======================

Install the new NPM package[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#install-the-new-npm-package)
------------------------------------------------------------------------------------------------------------------------------------------

npm pnpm yarn bun

`npm i graphql-yoga`

`pnpm add graphql-yoga`

`yarn add graphql-yoga`

`bun add graphql-yoga`

Drop unused graphiql options `defaultVariableEditorOpen` and `headerEditorEnabled`[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#drop-unused-graphiql-options-defaultvariableeditoropen-and-headereditorenabled)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These two graphiql options were not used and are now removed completely.

```
import { createYoga } from 'graphql-yoga'
import { schema } from './schema'
 
const yoga = createYoga({
  schema,
  graphiql: {
-    defaultVariableEditorOpen: false,
-    headerEditorEnabled: false
  }
})
```

Subscriptions use GraphQL over SSE “distinct connections mode”[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#subscriptions-use-graphql-over-sse-distinct-connections-mode)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Yoga previously used a custom, and simple, subscriptions transport over SSE. Now it implements the [GraphQL over SSE “distinct connections mode”](https://github.com/enisdenjo/graphql-sse/blob/master/PROTOCOL.md#distinct-connections-mode) instead.

Nothing has changed on the server; but, on the client-side, we recommend you use [`graphql-sse`](https://the-guild.dev/graphql/sse). The [recipes section](https://the-guild.dev/graphql/sse/recipes) will help you get going with any client out there!

Subscriptions only use SSE (text/event-stream) as transport method[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#subscriptions-only-use-sse-textevent-stream-as-transport-method)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously Yoga supported `multipart/mixed` just like `text/event-stream`. However, this was not a standard and it was not supported by any client. So, we decided to drop it and only support `text/event-stream` as the transport method.

Parse and validation cache are now under a single option `parserAndValidationCache`[](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v3#parse-and-validation-cache-are-now-under-a-single-option-parserandvalidationcache)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously Yoga used two separate envelop plugins for parsing and caching. Now, it leverages a custom built plugin focused on Yoga. It therefore yields better performance, feels more native and of course reduces bundle size.

```
import {
  DocumentNode,
-  GraphQLError,
+  validate,
} from 'graphql'
import { createYoga } from 'graphql-yoga'
import { schema } from './my-schema'
import {
  documentCacheStore,
  errorCacheStore,
  validationCacheStore,
} from './my-cache'
 
interface CacheStore<T> {
  get(key: string): T | undefined
  set(key: string, value: T): void
}
 
const yoga = createYoga({
  schema,
- parserCache: {
+ parserAndValidationCache: {
    documentCache: documentCacheStore as CacheStore<DocumentNode>,
    errorCache: errorCacheStore as CacheStore<Error>,
+   validationCache: validationCacheStore as CacheStore<typeof validate>,
  },
- validationCache: validationCacheStore as CacheStore<readonly GraphQLError[]>
})
```

Last updated on March 6, 2026

[Yoga v2](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v2 "Yoga v2")[Migration from Yoga V4](https://the-guild.dev/graphql/yoga-server/docs/migration/migration-from-yoga-v4 "Migration from Yoga V4")

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
