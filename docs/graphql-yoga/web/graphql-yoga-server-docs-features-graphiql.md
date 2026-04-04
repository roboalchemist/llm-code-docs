# Source: https://the-guild.dev/graphql/yoga-server/docs/features/graphiql

Title: GraphiQL | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/features/graphiql

Markdown Content:
GraphiQL | Yoga
===============
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#nextra-skip-nav)

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
            *   [Default Document String](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#default-document-string)
            *   [Disable GraphiQL](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#disable-graphiql)
            *   [Dynamic Options per Request](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#dynamic-options-per-request)
            *   [Offline Usage](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#offline-usage)
            *   [Usage with Content Security Policy](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#usage-with-content-security-policy)
            *   [Apollo Sandbox (as alternative)](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#apollo-sandbox-as-alternative)

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

On This Page

*   [Default Document String](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#default-document-string)
*   [Disable GraphiQL](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#disable-graphiql)
*   [Dynamic Options per Request](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#dynamic-options-per-request)
*   [Offline Usage](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#offline-usage)
*   [Usage with Content Security Policy](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#usage-with-content-security-policy)
*   [Apollo Sandbox (as alternative)](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#apollo-sandbox-as-alternative)

[Question? Give us feedback](https://github.com/graphql-hive/graphql-yoga/issues/new?title=Feedback%20for%20%E2%80%9CGraphiQL%E2%80%9D&labels=kind/docs)[Edit this page on GitHub](https://github.com/graphql-hive/graphql-yoga/tree/main/website/src/content/docs/features/graphiql.mdx)Scroll to top

[Documentation](https://the-guild.dev/graphql/yoga-server/docs "Documentation")[Features](https://the-guild.dev/graphql/yoga-server/docs/features/schema "Features")GraphiQL

GraphiQL
========

[GraphiQL](https://github.com/graphql/graphiql) is an in-browser IDE for writing, validating, and testing GraphQL queries.

By default, GraphiQL is enabled only when in development and served under the `/graphql` route for `GET` requests with a `accept: text/html` header. You can configure or completely disable GraphiQL with the `graphiql` option.

Default Document String[](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#default-document-string)
-------------------------------------------------------------------------------------------------------------------

You can set the default document string for GraphiQL by setting the `defaultQuery` option.

Set the default Document String

```
import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
 
// Provide your schema
const yoga = createYoga({
  graphiql: {
    defaultQuery: /* GraphQL */ `
      query {
        hello
      }
    `
  }
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Disable GraphiQL[](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#disable-graphiql)
-----------------------------------------------------------------------------------------------------

You can disable GraphiQL simply by setting `graphiql: false`.

💡

Be aware that disabling GraphiQL does not really make your GraphQL server more secure. As long as the introspection and/or the “did you mean x” suggestion feature of GraphQL are enabled.

You can further decrease your attack surface by disabling GraphQL introspection.

[Learn more about disabling introspection](https://the-guild.dev/graphql/yoga-server/docs/features/introspection)

Disable GraphiQL

```
import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
 
// Provide your schema
const yoga = createYoga({ graphiql: false })
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Dynamic Options per Request[](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#dynamic-options-per-request)
---------------------------------------------------------------------------------------------------------------------------

You can also dynamically set GraphiQL options based on the incoming request. This allows rendering GraphiQL conditionally e.g. based on a header presence or value.

Dynamic options based on the incoming request

```
import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
 
// Provide your schema
const yoga = createYoga({
  graphiql(request) {
    if (request.headers.get('graphiql-enabled')) {
      return true
    }
    return false
  }
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Within the function passed to `graphiql` you also have access to the `serverContext`. E.g. on Node.js it contains the `http.Request` and `http.Response` objects.

```
import { createServer } from 'node:http'
import { createYoga } from 'graphql-yoga'
 
// Provide your schema
const yoga = createYoga({
  graphiql(request, { req, res }) {
    // access something attached to the request object
    // e.g. a user object added by an auth middleware.
    if (req.user.role === 'admin') {
      return true
    }
    return false
  }
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

Offline Usage[](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#offline-usage)
-----------------------------------------------------------------------------------------------

By default, GraphiQL code is served from a CDN because if we added GraphiQL code inside Yoga, it would end up with huge bundle size and exceed the payload limit for some environments for example (CF Workers, AWS etc). If you want to use GraphiQL from a local version, you need to install it manually.

npm pnpm yarn bun

`npm i @graphql-yoga/render-graphiql`

`pnpm add @graphql-yoga/render-graphiql`

`yarn add @graphql-yoga/render-graphiql`

`bun add @graphql-yoga/render-graphiql`

And you need to pass imported `renderGraphiQL` to `createYoga` like below:

Render GraphiQL offline

```
import { createYoga } from 'graphql-yoga'
import { renderGraphiQL } from '@graphql-yoga/render-graphiql'
 
const yoga = createYoga({ renderGraphiQL })
```

Usage with Content Security Policy[](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#usage-with-content-security-policy)
-----------------------------------------------------------------------------------------------------------------------------------------

In production, chances are you have enabled [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (CSP) to prevent attacks.

Yoga by itself doesn’t require any special CSP configuration, but if you plan to use GraphiQL, you will need to add some sources to your CSP configuration:

*   `script-src`:
    *   `unpkg.com`: used to load the graphql module.
    *   `unsafe-inline`: GraphiQL is bundled with Webpack which rely on script tag injections.

*   `style-src`:
    *   `unpkg.com`: GraphiQL styles are loaded directly from its module bundle, next to its scripts.

*   `img-src`:
    *   `raw.githubusercontent.com`: The Guild logo is loaded from github

Apollo Sandbox (as alternative)[](https://the-guild.dev/graphql/yoga-server/docs/features/graphiql#apollo-sandbox-as-alternative)
---------------------------------------------------------------------------------------------------------------------------------

If you want to use [Apollo Sandbox](https://www.apollographql.com/docs/apollo-sandbox) in favor of GraphiQL. You can install this package and use it;

npm pnpm yarn bun

`npm i @graphql-yoga/render-apollo-sandbox`

`pnpm add @graphql-yoga/render-apollo-sandbox`

`yarn add @graphql-yoga/render-apollo-sandbox`

`bun add @graphql-yoga/render-apollo-sandbox`

Use Apollo Sandbox

```
import { createYoga } from 'graphql-yoga'
import { renderApolloSandbox } from '@graphql-yoga/render-apollo-sandbox'
 
// Pass Apollo Sandbox renderer instead of GraphiQL
const yoga = createYoga({
  renderGraphiQL: renderApolloSandbox({
    /**
     * Options here
     */
  })
})
```

About the options, see here: [Apollo Sandbox Options](https://www.apollographql.com/docs/apollo-sandbox#options)

Last updated on March 6, 2026

[GraphQL Schema](https://the-guild.dev/graphql/yoga-server/docs/features/schema "GraphQL Schema")[GraphQL Context](https://the-guild.dev/graphql/yoga-server/docs/features/context "GraphQL Context")

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
