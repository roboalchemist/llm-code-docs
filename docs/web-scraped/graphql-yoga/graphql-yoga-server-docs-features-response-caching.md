# Source: https://the-guild.dev/graphql/yoga-server/docs/features/response-caching

Title: Response Caching | Yoga

URL Source: https://the-guild.dev/graphql/yoga-server/docs/features/response-caching

Markdown Content:
[Skip to Content](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#nextra-skip-nav)

On This Page

Response Caching
----------------

Response caching is a technique for reducing server load by caching GraphQL query operation results. For incoming GraphQL Query operations with the same variable values, the same response is returned from a cache instead of executed again.

Quick Start[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#quick-start)
---------------------------------------------------------------------------------------------------

The response cache is a separate package that needs to be installed.

`npm i @graphql-yoga/plugin-response-cache`

`pnpm add @graphql-yoga/plugin-response-cache`

`yarn add @graphql-yoga/plugin-response-cache`

`bun add @graphql-yoga/plugin-response-cache`

The following sample setup show as slow field resolver (`Query.slow`).

Response cache example

```
import { createServer } from 'node:http'
import { setTimeout as setTimeout$ } from 'node:timers/promises'
import { createSchema, createYoga } from 'graphql-yoga'
import { useResponseCache } from '@graphql-yoga/plugin-response-cache'
 
const yoga = createYoga({
  schema: createSchema({
    typeDefs: /* GraphQL */ `
      type Query {
        slow: String
      }
    `,
    resolvers: {
      Query: {
        slow: async () => {
          await setTimeout$(5000)
          return 'I am slow.'
        }
      }
    }
  }),
  plugins: [
    useResponseCache({
      // global cache
      session: () => null
    })
  ]
})
 
const server = createServer(yoga)
server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql')
})
```

After starting the server we can execute a GraphQL Query operation, that selects the `Query.slow` field.

Execute slow GraphQL Query Operation with cUrl

```
curl -X POST -H 'Content-Type: application/json' http://localhost:4000/graphql \
  -d '{"query":"{slow}"}' -w '\nTotal time : %{time_total}'
```

The output will look similar to the following:

Initial Request time

```
{"data":{"slow":"I am slow."}}
Total time:5.026632
```

After executing the same curl statement a second time, the duration is significantly lower.

Cached Request time

```
{"data":{"slow":"I am slow."}}
Total time:0.007571%
```

Session based caching[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#session-based-caching)
-----------------------------------------------------------------------------------------------------------------------

If your GraphQL API returns specific data depending on the viewer’s session, you can use the `session` option to cache the response per session. Usually, the session is determined by an HTTP header, e.g. an user id within the encoded access token.

The `session` function receives a `request` parameter that is a [`Request` object](https://developer.mozilla.org/en-US/docs/Web/API/Request).

Response Cache configuration based on header

```
useResponseCache({
  // cache based on the authentication header
  session: request => request.headers.get('authentication')
})
```

You can also get the session value from the [GraphQL Context](https://the-guild.dev/graphql/yoga-server/docs/features/context) object. For example, you can use the JWT token from the context provided by [JWT Plugin](https://the-guild.dev/graphql/yoga-server/docs/features/jwt).

Response Cache configuration based on context

```
useResponseCache({
  // cache based on the authentication header
  session: ({ context }) => context.jwt.token
})
```

### Enforce session based caching[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#enforce-session-based-caching)

In some cases, a type or a field should only be cached if their is a session. For this, you can use the `scope` to indicate that the cache should only be used if a session is present.

Response Cache configuration with scope

```
useResponseCache({
  // cache based on the authentication header
  session: request => request.headers.get('authentication')
 
  // You can use configuration object to define the scope
  scopePerSchemaCoordinate: {
    'Query.me': 'PRIVATE', // on a field
    User: 'PRIVATE', // or a type
  }
})
```

It is also possible to use the `@cacheControl` directive to define the scope.

Response Cache configuration with scope using @cacheControl directive

```
import { cacheControlDirective } from '@graphql-yoga/plugin-response-cache'
 
const typeDefs = /* GraphQL */ `
  # the directive needs to be defined in the schema
  ${cacheControlDirective}
 
  type Query {
    # cache operations selecting Query.lazy for 10 seconds
    me: User @cacheControl(scope: PRIVATE)
  }
 
  type User @cacheControl(scope: PRIVATE) {
    #...
  }
`
```

Any query containing a type or a field with the scope `PRIVATE` will only be cached if a session is present.

Time to Live (TTL)[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#time-to-live-ttl)
---------------------------------------------------------------------------------------------------------------

It is possible to give cached operations a time to live. Either globally, based on [schema coordinates](https://github.com/graphql/graphql-wg/blob/main/rfcs/SchemaCoordinates.md) or object types.

If a query operation result contains multiple objects of the same or different types, the lowest TTL is picked.

### Using plugin configuration[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#using-plugin-configuration)

Response Cache configuration with TTL

```
useResponseCache({
  session: () => null,
  // by default cache all operations for 2 seconds
  ttl: 2_000,
  ttlPerType: {
    // only cache query operations containing User for 500ms
    User: 500
  },
  ttlPerSchemaCoordinate: {
    // cache operations selecting Query.lazy for 10 seconds
    'Query.lazy': 10_000
  }
})
```

### Using Schema directive `@cacheControl`[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#using-schema-directive-cachecontrol)

For a schema first approach, the `@cacheControl` directive can be used to define the TTL.

Notice that the global default TTL can only be define in the plugin options `ttl` and not via the directive.

```
import { cacheControlDirective } from '@graphql-yoga/plugin-response-cache'
 
const typeDefs = /* GraphQL */ `
  # the directive needs to be defined in the schema
  ${cacheControlDirective}
 
  type Query {
    # cache operations selecting Query.lazy for 10 seconds
    lazy: Something @cacheControl(maxAge: 10)
  }
 
  # only cache query operations containing User for 1 second
  type User @cacheControl(maxAge: 1) {
    #...
  }
`
```

Invalidations via Mutation[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#invalidations-via-mutation)
---------------------------------------------------------------------------------------------------------------------------------

When executing a mutation operation the cached query results that contain type entities within the Mutation result will be automatically be invalidated.

GraphQL mutation operation

```
mutation UpdateUser {
  updateUser(id: 1, newName: "John") {
    __typename
    id
    name
  }
}
```

GraphQL operation execution result

```
{
  "data": {
    "updateLaunch": {
      "__typename": "User",
      "id": "1",
      "name": "John"
    }
  }
}
```

For the given GraphQL operation and execution result, all cached query results that contain the type `User` with the id `1` will be invalidated.

This behavior can be disabled by setting the `invalidateViaMutation` option to `false`.

Disabling mutation invalidation

```
useResponseCache({
  session: request => null,
  invalidateViaMutation: false
})
```

Manual Invalidation[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#manual-invalidation)
-------------------------------------------------------------------------------------------------------------------

You can invalidate a type or specific instances of a type using the cache invalidation API.

In order to use the API, you need to manually instantiate the cache and pass it to the `useResponseCache` plugin.

Manual cache construction

```
import { createInMemoryCache, useResponseCache } from '@graphql-yoga/plugin-response-cache'
 
const cache = createInMemoryCache()
 
useResponseCache({
  session: () => null,
  cache
})
```

Then in your business logic you can call the `invalidate` method on the cache instance.

Invalidate all GraphQL query results that reference a specific type:

Invalidating a type

`cache.invalidate([{ typename: 'User' }])`

Invalidate all GraphQL query results that reference a specific entity of a type:

Invalidate a specific entity of a type

`cache.invalidate([{ typename: 'User', id: '1' }])`

Invalidate all GraphQL query results multiple entities in a single call.

Invalidate multiple entities

```
cache.invalidate([
  { typename: 'Post', id: '1' },
  { typename: 'User', id: '2' }
])
```

External Cache[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#external-cache)
---------------------------------------------------------------------------------------------------------

By default, the response cache stores all the cached query results in memory.

If you want a cache that is shared between multiple server instances you can use one of many `envelop` plugins that provide a cache implementation for a specific cache provider.

### Redis Cache[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#redis-cache)

`npm i @envelop/response-cache-redis`

`pnpm add @envelop/response-cache-redis`

`yarn add @envelop/response-cache-redis`

`bun add @envelop/response-cache-redis`

Create a custom Redis Cache

```
import { Redis } from 'ioredis'
import { createRedisCache } from '@envelop/response-cache-redis'
import { useResponseCache } from '@graphql-yoga/plugin-response-cache'
 
const redis = new Redis({
  host: 'my-redis-db.example.com',
  port: '30652',
  password: '1234567890'
})
 
const redis = new Redis('redis://:1234567890@my-redis-db.example.com:30652')
 
const cache = createRedisCache({ redis })
 
useResponseCache({
  session: () => null,
  cache
})
```

### Cloudflare KV Cache[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#cloudflare-kv-cache)

The Cloudflare KV cache only works when running the graphql server on Cloudflare Workers.

`npm i @envelop/response-cache-cloudflare-kv`

`pnpm add @envelop/response-cache-cloudflare-kv`

`yarn add @envelop/response-cache-cloudflare-kv`

`bun add @envelop/response-cache-cloudflare-kv`

Use Graphql Yoga with Cloudflare KV Cache in Cloudflare Workers

```
import { createSchema, createYoga, YogaInitialContext } from 'graphql-yoga'
import { useResponseCache } from '@envelop/response-cache'
import { createKvCache } from '@envelop/response-cache-cloudflare-kv'
import { resolvers } from './graphql-schema/resolvers.generated'
import { typeDefs } from './graphql-schema/typeDefs.generated'
 
export type Env = {
  GRAPHQL_RESPONSE_CACHE: KVNamespace
}
export type GraphQLContext = YogaInitialContext & Env & ExecutionContext
 
const graphqlServer = createYoga<GraphQLContext>({
  schema: createSchema({ typeDefs, resolvers }),
  plugins: [
    useResponseCache({
      cache: createKvCache({
        KV: env.GRAPHQL_RESPONSE_CACHE,
        ctx,
        keyPrefix: 'graphql' // optional
        cacheReadTTL: 1000 * 60, // 1 minute
      }),
      session: () => null,
      includeExtensionMetadata: true,
      ttl: 1000 * 60 // 1 minute
    })
  ]
})
 
export default {
  fetch: graphqlServer,
}
```

HTTP Caching via `ETag` and `If-None-Match` headers[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#http-caching-via-etag-and-if-none-match-headers)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Response Caching plugin sends `ETag` headers to the client, and respects `If-None-Match` headers in the HTTP request.

If the client sends an `If-None-Match` header with the same value as the `ETag` header, the server will respond with a `304 Not Modified` status code without any content, which allows you to reduce the server load.

Most of the browsers and some HTTP clients support this behavior, so you can use it to improve the performance of your frontend application.

[Learn more about `ETag` and `If-None-Match` headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag).

### Example with `curl`[](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#example-with-curl)

First we send a request to the GraphQL server, and we can see that the response contains the headers

Get ETag and Last-Modified headers

```
curl -H 'Content-Type: application/json' \
  "http://localhost:4000/graphql?query={me{id name}}" -v
```

Then the server will respond a data something the following with the `ETag` and `Last-Modified` headers:

*   `ETag` is the key that is used to identify the cached response.
*   `Last-Modified` is used to determine if the cached response is still valid.

Response with ETag and Last-Modified headers

```
> GET /graphql?query={me{id,name}} HTTP/1.1
> Host: localhost:4000
> User-Agent: curl/7.68.0
> Accept: application/json
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< access-control-allow-origin: *
< content-length: 130
< content-type: application/json; charset=utf-8
< etag: 2c0ebfe7b2b0273029f2fa23a99d213b56f4838756b3ef7b323c04de1e836be3
< last-modified: Wed Feb 15 2023 15:23:55 GMT+0300 (GMT+03:00)
< Date: Wed, 15 Feb 2023 12:23:55 GMT
< Connection: keep-alive
< Keep-Alive: timeout=5
<
 
{"data":{"me":{"id":"1","name":"Bob"}}}
```

In the next calls, we can use the `ETag` header as the `If-None-Match` header together with `Last-Modified` header as `If-Modified-Since` to check if the cached response is still valid.

Use the headers to check if the cached response is still valid

```
curl -H "Accept: application/json" \
  -H "If-None-Match: 2c0ebfe7b2b0273029f2fa23a99d213b56f4838756b3ef7b323c04de1e836be3" \
  -H "If-Modified-Since: Wed Feb 15 2023 15:23:55 GMT" \
  "http://localhost:4000/graphql?query=\{me\{id,name\}\}" -v
```

Then the server will return `304: Not Modified` status code with no content.
