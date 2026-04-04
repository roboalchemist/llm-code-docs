# Source: https://docs.redwoodjs.com/docs/graphql

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [GraphQL](/docs/graphql/index)
-   [About]

[Version: 8.8]

On this page

<div>

# GraphQL

</div>

GraphQL is a fundamental part of Redwood. Having said that, you can get going without knowing anything about it, and can actually get quite far without ever having to read [the docs](https://graphql.org/learn/). But to master Redwood, you\'ll need to have more than just a vague notion of what GraphQL is. You\'ll have to really grok it.

## GraphQL 101[​](#graphql-101 "Direct link to GraphQL 101") 

GraphQL is a query language that enhances the exchange of data between clients (in Redwood\'s case, a React app) and servers (a Redwood API).

Unlike a REST API, a GraphQL Client performs operations that allow gathering a rich dataset in a single request. There\'s three types of GraphQL operations, but here we\'ll only focus on two: Queries (to read data) and Mutations (to create, update, or delete data).

The following GraphQL query:

``` 
query GetProject 
    tags 
  }
}
```

returns the following JSON response:

``` 
,
      "tags": []
    }
  },
  "errors": null
}
```

Notice that the response\'s structure mirrors the query\'s. In this way, GraphQL makes fetching data descriptive and predictable.

Again, unlike a REST API, a GraphQL API is built on a schema that specifies exactly which queries and mutations can be performed. For the `GetProject` query above, here\'s the schema backing it:

``` 
type Project 

# ... User and Tag type definitions

type Query 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

More information on GraphQL types can be found in the [official GraphQL documentation](https://graphql.org/learn/schema/).

Finally, the GraphQL schema is associated with a resolvers map that helps resolve each requested field. For example, here\'s what the resolver for the owner field on the Project type may look like:

``` 
export const Project = ) =>  }).user()
  },
  // ...
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

You can read more about resolvers in the dedicated [Understanding Default Resolvers](#understanding-default-resolvers) section below.

To summarize, when a GraphQL query reaches a GraphQL API, here\'s what happens:

``` 
+--------------------+                  +--------------------+
|                    | 1.send operation |                    |
|                    |                  |   GraphQL Server   |
|   GraphQL Client   +----------------->|    |               |
|                    |                  |    |  2.resolve    |
|                    |                  |    |     data      |
+--------------------+                  |    v               |
          ^                             | +----------------+ |
          |                             | |                | |
          |                             | |    Resolvers   | |
          |                             | |                | |
          |                             | +--------+-------+ |
          |  3. respond JSON with data  |          |         |
          +-----------------------------+ <--------+         |
                                        |                    |
                                        +--------------------+
```

In contrast to most GraphQL implementations, Redwood provides a \"deconstructed\" way of creating a GraphQL API:

-   You define your SDLs (schema) in `*.sdl.js` files, which define what queries and mutations are available, and what fields can be returned
-   For each query or mutation, you write a service function with the same name. This is the resolver
-   Redwood then takes all your SDLs and Services (resolvers), combines them into a GraphQL server, and expose it as an endpoint

## RedwoodJS and GraphQL[​](#redwoodjs-and-graphql "Direct link to RedwoodJS and GraphQL") 

Besides taking care of the annoying stuff for you (namely, mapping your resolvers, which gets annoying fast if you do it yourself!), there\'s not many gotchas with GraphQL in Redwood. The only Redwood-specific thing you should really be aware of is [resolver args](#redwoods-resolver-args).

Since there\'s two parts to GraphQL in Redwood, the client and the server, we\'ve divided this doc up that way.

On the `web` side, Redwood uses [Apollo Client](https://www.apollographql.com/docs/react/) by default though you can swap it out for something else if you want.

The `api` side offers a GraphQL server built on [GraphQL Yoga](https://www.graphql-yoga.com) and the [Envelop plugin system](https://www.envelop.dev/docs) from [The Guild](https://the-guild.dev).

### 

Redwood\'s api side is \"serverless first\", meaning it\'s architected as functions which can be deployed on either serverless or traditional infrastructure, and Redwood\'s GraphQL endpoint is effectively \"just another function\" (with a whole lot more going on under the hood, but that part is handled for you, out of the box). One of the tenets of the Redwood philosophy is \"Redwood believes that, as much as possible, you should be able to operate in a serverless mindset and deploy to a generic computational grid."

### GraphQL Yoga and the Generic Computation Grid[​](#graphql-yoga-and-the-generic-computation-grid "Direct link to GraphQL Yoga and the Generic Computation Grid") 

To be able to deploy to a "generic computation grid" means that, as a developer, you should be able to deploy using the provider or technology of your choosing. You should be able to deploy to Netlify, Vercel, Fly, Render, AWS Serverless, or elsewhere with ease and no vendor or platform lock in. You should be in control of the framework, what the response looks like, and how your clients consume it.

The same should be true of your GraphQL Server. [GraphQL Yoga](https://www.graphql-yoga.com) from [The Guild](https://the-guild.dev) makes that possible.

> The fully-featured GraphQL Server with focus on easy setup, performance and great developer experience.

RedwoodJS leverages Yoga\'s Envelop plugins to implement custom internal plugins to help with [authentication](#authentication), [logging](#logging), [directive handling](#directives), and more.

### Security Best Practices[​](#security-best-practices "Direct link to Security Best Practices") 

RedwoodJS implements GraphQL Armor from [Escape Technologies](https://escape.tech) to make your endpoint more secure by default by implementing common GraphQL [security best practices](#security).

GraphQL Armor, developed by Escape in partnership with The Guild, is a middleware for JS servers that adds a security layer to the RedwoodJS GraphQL endpoint.

### Trusted Documents[​](#trusted-documents "Direct link to Trusted Documents") 

In addition, RedwoodJS can be setup to enforce [persisted operations](https://the-guild.dev/graphql/yoga-server/docs/features/persisted-operations) \-- alternatively called [Trusted Documents](https://benjie.dev/graphql/trusted-documents).

See [Configure Trusted Documents](/docs/graphql/trusted-documents#configure-trusted-documents) for more information and usage instructions.

### Conclusion[​](#conclusion "Direct link to Conclusion") 

All this gets us closer to Redwood\'s goal of being able to deploy to a \"generic computation grid\". And that's exciting!

## Client-side[​](#client-side "Direct link to Client-side") 

### RedwoodApolloProvider[​](#redwoodapolloprovider "Direct link to RedwoodApolloProvider") 

By default, Redwood Apps come ready-to-query with the `RedwoodApolloProvider`. As you can tell from the name, this Provider wraps [ApolloProvider](https://www.apollographql.com/docs/react/api/react/hooks/#the-apolloprovider-component). Omitting a few things, this is what you\'ll normally see in Redwood Apps:

web/src/App.js

``` 
import  from '@redwoodjs/web/apollo'

// ...

const App = () => (
  <RedwoodApolloProvider>
    <Routes />
  </RedwoodApolloProvider>
)

// ...
```

You can use Apollo\'s `useQuery` and `useMutation` hooks by importing them from `@redwoodjs/web`, though if you\'re using `useQuery`, we recommend that you use a [Cell](/docs/cells):

web/src/components/MutateButton.js

``` 
import  from '@redwoodjs/web'

const MUTATION = gql`
  # your mutation...
`

const MutateButton = () => )}>
      Click to mutate
    </button>
  )
}
```

Note that you\'re free to use any of Apollo\'s other hooks, you\'ll just have to import them from `@apollo/client` instead. In particular, these two hooks might come in handy:

Hook

Description

[useLazyQuery](https://www.apollographql.com/docs/react/api/react/hooks/#uselazyquery)

Execute queries in response to events other than component rendering

[useApolloClient](https://www.apollographql.com/docs/react/api/react/hooks/#useapolloclient)

Access your instance of `ApolloClient`

### Customizing the Apollo Client and Cache[​](#customizing-the-apollo-client-and-cache "Direct link to Customizing the Apollo Client and Cache") 

By default, `RedwoodApolloProvider` configures an `ApolloClient` instance with 1) a default instance of `InMemoryCache` to cache responses from the GraphQL API and 2) an `authMiddleware` to sign API requests for use with [Redwood\'s built-in auth](/docs/authentication). Beyond the `cache` and `link` params, which are used to set up that functionality, you can specify additional params to be passed to `ApolloClient` using the `graphQLClientConfig` prop. The full list of available configuration options for the client are [documented here on Apollo\'s site](https://www.apollographql.com/docs/react/api/core/ApolloClient/#options).

Depending on your use case, you may want to configure `InMemoryCache`. For example, you may need to specify a type policy to change the key by which a model is cached or to enable pagination on a query. [This article from Apollo](https://www.apollographql.com/docs/react/caching/cache-configuration/) explains in further detail why and how you might want to do this.

To configure the cache when it\'s created, use the `cacheConfig` property on `graphQLClientConfig`. Any value you pass is passed directly to `InMemoryCache` when it\'s created.

For example, if you have a query named `search` that supports [Apollo\'s offset pagination](https://www.apollographql.com/docs/react/pagination/core-api/), you could enable it by specifying:

``` 
<RedwoodApolloProvider graphQLClientConfig=
        }
      }
    }
  }
}}>
```

### Swapping out the RedwoodApolloProvider[​](#swapping-out-the-redwoodapolloprovider "Direct link to Swapping out the RedwoodApolloProvider") 

As long as you\'re willing to do a bit of configuring yourself, you can swap out `RedwoodApolloProvider` with your GraphQL Client of choice. You\'ll just have to get to know a bit of the make up of the [RedwoodApolloProvider](https://github.com/redwoodjs/redwood/blob/main/packages/web/src/apollo/index.tsx#L71-L84); it\'s actually composed of a few more Providers and hooks:

-   `FetchConfigProvider`
-   `useFetchConfig`
-   `GraphQLHooksProvider`

For an example of configuring your own GraphQL Client, see the [redwoodjs-react-query-provider](https://www.npmjs.com/package/redwoodjs-react-query-provider). If you were thinking about using [react-query](https://react-query.tanstack.com/), you can also just go ahead and install it!

Note that if you don\'t import `RedwoodApolloProvider`, it won\'t be included in your bundle, dropping your bundle size quite a lot!

## Server-side[​](#server-side "Direct link to Server-side") 

### Understanding Default Resolvers[​](#understanding-default-resolvers "Direct link to Understanding Default Resolvers") 

According to the spec, for every field in your sdl, there has to be a resolver in your Services. But you\'ll usually see fewer resolvers in your Services than you technically should. And that\'s because if you don\'t define a resolver, GraphQL Yoga server will.

The key question the Yoga server asks is: \"Does the parent argument (in Redwood apps, the `parent` argument is named `root`---see [Redwood\'s Resolver Args](#redwoods-resolver-args)) have a property with this resolver\'s exact name?\" Most of the time, especially with Prisma Client\'s ergonomic returns, the answer is yes.

Let\'s walk through an example. Say our sdl looks like this:

api/src/graphql/user.sdl.js

``` 
export const schema = gql`
  type User 

  type Query 
`
```

So we have a User model in our `schema.prisma` that looks like this:

``` 
model User 
```

If you create your Services for this model using Redwood\'s generator (`yarn rw g service user`), your Services will look like this:

api/src/services/user/user.js

``` 
import  from 'src/lib/db'

export const users = () => 
```

Which begs the question: where are the resolvers for the User fields---`id`, `email`, and `name`? All we have is the resolver for the Query field, `users`.

As we just mentioned, GraphQL Yoga defines them for you. And since the `root` argument for `id`, `email`, and `name` has a property with each resolvers\' exact name (i.e. `root.id`, `root.email`, `root.name`), it\'ll return the property\'s value (instead of returning `undefined`, which is what Yoga would do if that weren\'t the case).

But, if you wanted to be explicit about it, this is what it would look like:

api/src/services/user/user.js

``` 
import  from 'src/lib/db'

export const users = () => 

export const Users = ) => root.id,
  email: (_args, ) => root.email,
  name: (_args, ) => root.name,
}
```

The terminological way of saying this is, to create a resolver for a field on a type, in the Service, export an object with the same name as the type that has a property with the same name as the field.

Sometimes you want to do this since you can do things like add completely custom fields this way:

``` 
export const Users = ) => root.id,
  email: (_args, ) => root.email,
  name: (_args, ) => root.name,
  age: (_args, ) =>
    new Date().getFullYear() - root.birthDate.getFullYear(),
}
```

### Redwood\'s Resolver Args[​](#redwoods-resolver-args "Direct link to Redwood's Resolver Args") 

[According to the spec](https://graphql.org/learn/execution/#root-fields-resolvers), resolvers take four arguments: `args`, `obj`, `context`, and `info`. In Redwood, resolvers do take these four arguments, but what they\'re named and how they\'re passed to resolvers is slightly different:

-   `args` is passed as the first argument
-   `obj` is named `root` (all the rest keep their names)
-   `root`, `context`, and `info` are wrapped into an object, `gqlArgs`; this object is passed as the second argument

Here\'s an example to make things clear:

``` 
export const Post =  }).user(),
}
```

Of the four, you\'ll see `args` and `root` being used a lot.

Argument

Description

`args`

The arguments provided to the field in the GraphQL query

`root`

The previous return in the resolver chain

`context`

Holds important contextual information, like the currently logged in user

`info`

Holds field-specific information relevant to the current query as well as the schema details

> **There\'s so many terms!**
>
> Half the battle here is really just coming to terms. To keep your head from spinning, keep in mind that everybody tends to rename `obj` to something else: Redwood calls it `root`, GraphQL Yoga calls it `parent`. `obj` isn\'t exactly the most descriptive name in the world.

### Context[​](#context "Direct link to Context") 

In Redwood, the `context` object that\'s passed to resolvers is actually available to all your Services, whether or not they\'re serving as resolvers. Just import it from `@redwoodjs/graphql-server`:

``` 
import  from '@redwoodjs/graphql-server'
```

#### How to Modify the Context[​](#how-to-modify-the-context "Direct link to How to Modify the Context") 

Because the context is read-only in your services, if you need to modify it, then you need to do so in the `createGraphQLHandler`.

To populate or enrich the context on a per-request basis with additional attributes, set the `context` attribute `createGraphQLHandler` to a custom ContextFunction that modifies the context.

For example, if we want to populate a new, custom `ipAddress` attribute on the context with the information from the request\'s event, declare the `setIpAddress` ContextFunction as seen here:

api/src/functions/graphql.js

``` 
// ...

const ipAddress = () => 

const setIpAddress = async () => )
}

export const handler = createGraphQLHandler(,
  },
  schema: makeMergedSchema(),
  context: setIpAddress,
  onException: () => ,
})
```

> **Note:** If you use the preview GraphQL Yoga/Envelop `graphql-server` package and a custom ContextFunction to modify the context in the createGraphQL handler, the function is provided ***only the context*** and ***not the event***. However, the `event` information is available as an attribute of the context as `context.event`. Therefore, in the above example, one would fetch the ip address from the event this way: `ipAddress()`.

### The Root Schema[​](#the-root-schema "Direct link to The Root Schema") 

Did you know that you can query `redwood`? Try it in the GraphQL Playground (you can find the GraphQL Playground at [http://localhost:8911/graphql](http://localhost:8911/graphql) when your dev server is running---`yarn rw dev api`):

``` 
query 
}
```

How is this possible? Via Redwood\'s [root schema](https://github.com/redwoodjs/redwood/blob/main/packages/graphql-server/src/rootSchema.ts). The root schema is where things like currentUser are defined:

``` 
scalar BigInt
scalar Date
scalar Time
scalar DateTime
scalar JSON
scalar JSONObject

type Redwood 

type Query 
```

Now that you\'ve seen the sdl, be sure to check out [the resolvers](https://github.com/redwoodjs/redwood/blob/main/packages/graphql-server/src/rootSchema.ts):

``` 
export const resolvers: Resolvers = ,
    }),
  },
}
```

## CORS Configuration[​](#cors-configuration "Direct link to CORS Configuration") 

CORS stands for [Cross Origin Resource Sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing); in a nutshell, by default, browsers aren\'t allowed to access resources outside their own domain.

Let\'s say you\'re hosting each of your Redwood app\'s sides on different domains: the web side on `www.example.com` and the api side (and thus, the GraphQL Server) on `api.example.com`. When the browser tries to fetch data from the `/graphql` function, you\'ll see an error that says the request was blocked due to CORS. Wording may vary, but it\'ll be similar to:

> ⛔️ Access to fetch \... has been blocked by CORS policy: Response to preflight request doesn\'t pass access control check: No \'Access-Control-Allow-Origin\' header is present on the requested resource.

To fix this, you need to \"configure CORS\" by adding:

``` 
'Access-Control-Allow-Origin': 'https://example.com'
'Access-Control-Allow-Credentials': true
```

to the GraphQL response headers which you can do this by setting the `cors` option in `api/src/functions/graphql.s`:

``` 
export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  cors: ,
  onException: () => ,
})
```

For more in-depth discussion and configuration of CORS when it comes to using a cookie-based auth system (like [dbAuth](/docs/authentication#self-hosted-auth-installation-and-setup)), see the [CORS documentation](/docs/cors).

## Health Checks[​](#health-checks "Direct link to Health Checks") 

You can use health checks to determine if a server is available and ready to start serving traffic. For example, services like [Pingdom](https://www.pingdom.com) use health checks to determine server uptime and will notify you if it becomes unavailable.

Redwood\'s GraphQL server provides a health check endpoint at `/graphql/health` as part of its GraphQL handler. If the server is healthy and can accept requests, the response will contain the following headers:

``` 
content-type: application/json
server: GraphQL Yoga
x-yoga-id: yoga
```

and will return a `HTTP/1.1 200 OK` status with the body:

``` 

```

Note the `x-yoga-id` header. The header\'s value defaults to `yoga` when `healthCheckId` isn\'t set in `createGraphQLHandler`. But you can customize it when configuring your GraphQL handler:

api/src/functions/graphql.ts

``` 
// ...

export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  onException: () => ,
})
```

If the health check fails, then the GraphQL server is unavailable and you should investigate what could be causing the downtime.

#### Perform a Health Check[​](#perform-a-health-check "Direct link to Perform a Health Check") 

To perform a health check, make a HTTP GET request to the `/graphql/health` endpoint.

For local development, with the proxy using `curl` from the command line:

``` 
curl "http://localhost:8910/.redwood/functions/graphql/health" -i
```

or by directly invoking the graphql function:

``` 
curl "http://localhost:8911/graphql/health" -i
```

you should get the response:

``` 

```

For production, make a request wherever your `/graphql` function exists.

> These examples use `curl` but you can perform a health check via any HTTP GET request.

#### Perform a Readiness Check[​](#perform-a-readiness-check "Direct link to Perform a Readiness Check") 

A readiness check confirms that your GraphQL server can accept requests and serve **your server\'s** traffic.

It forwards a request to the health check with a header that must match your `healthCheckId` in order to succeed. If the `healthCheckId` doesn\'t match or the request fails, then your GraphQL server isn\'t \"ready\".

To perform a readiness check, make a HTTP GET request to the `/graphql/readiness` endpoint with the appropriate `healthCheckId` header. For local development, you can make a request to the proxy:

``` 
curl "http://localhost:8910/.redwood/functions/graphql/readiness" \
  -H 'x-yoga-id: yoga' \
  -i
```

or directly invoke the graphql function:

``` 
curl "http://localhost:8911/graphql/readiness" \
  -H 'x-yoga-id: yoga' \
  -i
```

Either way, you should get a `200 OK` HTTP status if ready, or a `503 Service Unavailable` if not.

For production, make a request wherever your `/graphql` function exists.

> These examples use `curl` but you can perform a readiness check via any HTTP GET request with the proper headers.

## Verifying GraphQL Schema[​](#verifying-graphql-schema "Direct link to Verifying GraphQL Schema") 

In order to keep your GraphQL endpoint and services secure, you must specify one of `@requireAuth`, `@skipAuth` or a custom directive on **every** query and mutation defined in your SDL.

Redwood will verify that your schema complies with these runs when:

-   building (or building just the api)
-   launching the dev server.

If any fail this check, you will see:

-   each query of mutation listed in the command\'s error log
-   a fatal error `⚠️ GraphQL server crashed` if launching the server

### Build-time Verification[​](#build-time-verification "Direct link to Build-time Verification") 

When building via the `yarn rw build` command and the SDL fails verification, you will see output that lists each query or mutation missing the directive:

``` 
✔ Generating Prisma Client...
✖ Verifying graphql schema...
→ - deletePost Mutation
Building API...
Cleaning Web...
Building Web...
Prerendering Web...

You must specify one of @requireAuth, @skipAuth or a custom directive for
- contacts Query
- posts Query
- post Query
- createContact Mutation
- createPost Mutation
- updatePost Mutation
- deletePost Mutation
```

### Dev Server Verification[​](#dev-server-verification "Direct link to Dev Server Verification") 

When launching the dev server via the `yarn rw dev` command, you will see output that lists each query or mutation missing the directive:

``` 
gen | Generating TypeScript definitions and GraphQL schemas...
gen | 37 files generated
api | Building... Took 444 ms
api | Starting API Server... Took 2 ms
api | Listening on http://localhost:8911/
api | Importing Server Functions...
web | ...
api | FATAL [2021-09-24 18:41:49.700 +0000]:
api | ⚠️ GraphQL server crashed
api \
  | api | Error: You must specify one of @requireAuth, @skipAuth or a custom directive for
api | - contacts Query
api | - posts Query
api | - post Query
api | - createContact Mutation
api | - createPost Mutation
api | - updatePost Mutation
api | - deletePost Mutation
```

To fix these errors, simple declare with `@requireAuth` to enforce authentication or `@skipAuth` to keep the operation public on each as appropriate for your app\'s permissions needs.

## Default Scalars[​](#default-scalars "Direct link to Default Scalars") 

Redwood includes a selection of scalar types by default.

Currently we allow you to control whether or not the `File` scalar is included automatically or not. By default we include the `File` scalar which maps to the standard `File` type. To disable this scalar you should add config to two places:

1.  In your `redwood.toml` file like so:

    ::: 
    ::: codeBlockContent_QJqH
    ``` 
    [graphql]
      includeScalars.File = false
    ```
    :::
    :::

2.  In your `functions/graphql.ts` like so:

    ::: 
    ::: codeBlockContent_QJqH
    ``` 
    export const handler = createGraphQLHandler( },
      directives,
      sdls,
      services,
      onException: () => ,
      includeScalars: ,
    })
    ```
    :::
    :::

With those two config values added your schema will no longer contain the `File` scalar by default and you are free to add your own or continue without one.

## Custom Scalars[​](#custom-scalars "Direct link to Custom Scalars") 

GraphQL scalar types give data meaning and validate that their values makes sense. Out of the box, GraphQL comes with `Int`, `Float`, `String`, `Boolean` and `ID`. While those can cover a wide variety of use cases, you may need more specific scalar types to better describe and validate your application\'s data.

For example, if there\'s a `Person` type in your schema that has a field like `ageInYears`, if it\'s actually supposed to represent a person\'s age, technically it should only be a positive integer---never a negative one. Something like the [`PositiveInt` scalar](https://www.graphql-scalars.dev/docs/scalars/positive-int) provides that meaning and validation.

### Scalars vs Service vs Directives[​](#scalars-vs-service-vs-directives "Direct link to Scalars vs Service vs Directives") 

How are custom scalars different from Service Validations or Validator Directives?

[Service validations](/docs/services#service-validations) run when resolving the service. Because they run at the start of your Service function and throw if conditions aren\'t met, they\'re great for validating whenever you use a Service---anywhere, anytime. For example, they\'ll validate via GraphQL, Serverless Functions, webhooks, etc. Custom scalars, however, only validate via GraphQL and not anywhere else.

Service validations also perform more fine-grained checks than scalars which are more geared toward validating that data is of a specific **type**.

[Validator Directives](#directives) control user **access** to data and also whether or not a user is authorized to perform certain queries and/or mutations.

### How To Add a Custom Scalar[​](#how-to-add-a-custom-scalar "Direct link to How To Add a Custom Scalar") 

Let\'s say that you have a `Product` type that has three fields: a name, a description, and the type of currency. The built-in `String` scalar should suffice for the first two, but for the third, you\'d be better off with a more-specific `String` scalar that only accepts [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency codes, like `USD`, `EUR`, `CAD`, etc. Luckily there\'s already a [`Currency` scalar type](https://github.com/Urigo/graphql-scalars/blob/master/src/scalars/Currency.ts) that does exactly that! All you have to do is add it to your GraphQL schema.

To add a custom scalar to your GraphQL schema:

1.  Add the scalar definition to one of your sdl files, such as `api/src/graphql/scalars.sdl.ts`

> Note that you may have to create this file. Moreover, it\'s just a convention---custom scalar type definitions can be in any of your sdl files.

api/src/graphql/scalars.sdl.ts

``` 
export const schema = gql`
  scalar Currency
`
```

\

2.  Import the scalar\'s definition and resolver and pass them to your GraphQLHandler via the `schemaOptions` property:

api/src/functions/graphql.ts

``` 
import  from 'graphql-scalars'

// ...

export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  schemaOptions: ,
  },
  onException: () => ,
})
```

\

3.  Use the scalar in your types

``` 
export const schema = gql`
  type Product 

  type Query 

  input CreateProductInput 

  input UpdateProductInput 

  type Mutation 
`
```

## Directives[​](#directives "Direct link to Directives") 

Directives supercharge your GraphQL services. They add configuration to fields, types or operations that act like \"middleware\" that lets you run reusable code during GraphQL execution to perform tasks like [authentication](#authentication), formatting, and more.

You\'ll recognize a directive by its preceded by the `@` character, e.g. `@myDirective`, and by being declared alongside a field:

``` 
type Bar 
```

or a Query or Mutation:

``` 
type Query 

type Mutation 
```

See the [Directives](/docs/directives) section for complete information on RedwoodJS Directives.

## Fragments[​](#fragments "Direct link to Fragments") 

See [fragments](/docs/graphql/fragments)

## Unions[​](#unions "Direct link to Unions") 

Unions are abstract GraphQL types that enable a schema field to return one of multiple object types.

`union FavoriteTree = Redwood | Ginkgo | Oak`

A field can have a union as its return type.

``` 
type Query 
```

All of a union\'s included types must be object types and do not need to share any fields.

To query a union, you can take advantage on [inline fragments](https://graphql.org/learn/queries/#inline-fragments) to include subfields of multiple possible types.

``` 
query GetFavoriteTrees 
    ... on Ginkgo 
    ... on Oak 
  }
}
```

Redwood will automatically detect your union types in your `sdl` files and resolve *which* of your union\'s types is being returned. If the returned object does not match any of the valid types, the associated operation will produce a GraphQL error.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

In order to use Union types web-side with your Apollo GraphQL client, you will need to [generate possible types from fragments and union types](/docs/graphql/fragments#possible-types-for-unions).

## useCache[​](#usecache "Direct link to useCache") 

Apollo Client stores the results of your GraphQL queries in a local, normalized, in-memory cache. This enables the client to respond almost immediately to queries for already-cached data, without even sending a network request.

useCache is a custom hook that returns the cache object and some useful methods to interact with the cache:

-   [evict](#evict)
-   [extract](#extract)
-   [identify](#identify)
-   [modify](#modify)
-   [resetStore](#resetstore)
-   [clearStore](#clearstore)

``` 
import  from '@redwoodjs/web/apollo'
```

### cache[​](#cache "Direct link to cache") 

Returns the normalized, in-memory cache.

``` 
import  from '@redwoodjs/web/apollo'

const  = useCache()
```

### evict[​](#evict "Direct link to evict") 

Either removes a normalized object from the cache or removes a specific field from a normalized object in the cache.

``` 
import  from '@redwoodjs/web/apollo'

const Fruit = (: ) =>  = useCache()
  const  = useRegisteredFragment<Fruit>(id)

  evict(fruit)
}
```

### extract[​](#extract "Direct link to extract") 

Returns a serialized representation of the cache\'s current contents

``` 
import  from '@redwoodjs/web/apollo'

const Fruit = (: ) =>  = useCache()

  // Logs the cache's current contents
  console.log(extract())
```

### identify[​](#identify "Direct link to identify") 

``` 
import  from '@redwoodjs/web/apollo'

const Fruit = (: ) =>  = useCache()
  const  = useRegisteredFragment<Fruit>(id)

  // Returns "Fruit:ownpc6co8a1w5bhfmavecko9"
  console.log(identify(fruit))
}
```

### modify[​](#modify "Direct link to modify") 

Modifies one or more field values of a cached object. Must provide a modifier function for each field to modify. A modifier function takes a cached field\'s current value and returns the value that should replace it.

Returns true if the cache was modified successfully and false otherwise.

``` 
import  from '@redwoodjs/web/apollo'

const Fruit = (: ) =>  = useCache()
  const  = useRegisteredFragment<Fruit>(id)

  // Modify the name of a given fruit entity to be uppercase

  <button onClick=})}>
    Uppercase 
  </button>

  // ...
}
```

### clearStore[​](#clearstore "Direct link to clearStore") 

To reset the cache without refetching active queries, use the clearStore method.

``` 
import  from '@redwoodjs/web/apollo'

const Fruit = (: ) =>  = useCache()

  clearStore()
}
```

### resetStore[​](#resetstore "Direct link to resetStore") 

Reset the cache entirely, such as when a user logs out.

``` 
import  from '@redwoodjs/web/apollo'

const Fruit = (: ) =>  = useCache()

  resetStore()
}
```

## GraphQL Handler Setup[​](#graphql-handler-setup "Direct link to GraphQL Handler Setup") 

Redwood\'s `GraphQLHandlerOptions` allows you to configure your GraphQL handler schema, context, authentication, security and more.

``` 
export interface GraphQLHandlerOptions '
   */
  services: ServicesGlobImports

  /**
   * @description SDLs (schema definitions) passed from the glob import:
   * import sdls from 'src/graphql\/**\/*.'
   */
  sdls: SdlGlobImports

  /**
   * @description Directives passed from the glob import:
   * import directives from 'src/directives/**\/*.'
   */
  directives?: DirectiveGlobImports

  /**
   * @description A list of options passed to [makeExecutableSchema]
   * (https://www.graphql-tools.com/docs/generate-schema/#makeexecutableschemaoptions).
   */
  schemaOptions?: Partial<IExecutableSchemaDefinition>

  /**
   * @description CORS configuration
   */
  cors?: CorsConfig

  /**
   *  @description Customize GraphQL Armor plugin configuration
   *
   * @see https://escape-technologies.github.io/graphql-armor/docs/configuration/examples
   */
  armorConfig?: ArmorConfig

  /**
   * @description Customize the default error message used to mask errors.
   *
   * By default, the masked error message is "Something went wrong"
   *
   * @see https://github.com/dotansimha/envelop/blob/main/packages/core/docs/use-masked-errors.md
   */
  defaultError?: string

  /**
   * @description Only allows the specified operation types (e.g. subscription, query or mutation).
   *
   * By default, only allow query and mutation (ie, do not allow subscriptions).
   *
   * An array of GraphQL's OperationTypeNode enums:
   * - OperationTypeNode.SUBSCRIPTION
   * - OperationTypeNode.QUERY
   * - OperationTypeNode.MUTATION
   *
   * @see https://github.com/dotansimha/envelop/tree/main/packages/plugins/filter-operation-type
   */
  allowedOperations?: AllowedOperations

  /**
   * @description Custom Envelop plugins
   */
  extraPlugins?: Plugin[]

  /**
   * @description Auth-provider specific token decoder
   */
  authDecoder?: Decoder

  /**
   * @description Customize the GraphiQL Endpoint that appears in the location bar of the GraphQL Playground
   *
   * Defaults to '/graphql' as this value must match the name of the `graphql` function on the api-side.
   */
  graphiQLEndpoint?: string
  /**
   * @description Function that returns custom headers (as string) for GraphiQL.
   *
   * Headers must set auth-provider, Authorization and (if using dbAuth) the encrypted cookie.
   */
  generateGraphiQLHeader?: GenerateGraphiQLHeader
}
```

### Directive Setup[​](#directive-setup "Direct link to Directive Setup") 

Redwood makes it easy to code, organize, and map your directives into the GraphQL schema.

You simply add them to the `directives` directory and the `createGraphQLHandler` will do all the work.

api/src/functions/graphql.ts

``` 
import  from '@redwoodjs/graphql-server'

import directives from 'src/directives/**/*.' // 👈 directives live here
import sdls from 'src/graphql/**/*.sdl.'
import services from 'src/services/**/*.'

import  from 'src/lib/db'
import  from 'src/lib/logger'

export const handler = createGraphQLHandler( },
  armorConfig, //  👈 custom GraphQL Security configuration
  directives, //  👈 directives are added to the schema here
  sdls,
  services,
  onException: () => ,
})
```

> Note: Check-out the [in-depth look at Redwood Directives](/docs/directives) that explains how to generate directives so you may use them to validate access and transform the response.

### Logging Setup[​](#logging-setup "Direct link to Logging Setup") 

For a details on setting up GraphQL Logging, see [Logging](#logging).

### Security Setup[​](#security-setup "Direct link to Security Setup") 

For a details on setting up GraphQL Security, see [Security](#security).

## Logging[​](#logging "Direct link to Logging") 

Logging is essential in production apps to be alerted about critical errors and to be able to respond effectively to support issues. In staging and development environments, logging helps you debug queries, resolvers and cell requests.

We want to make logging simple when using RedwoodJS and therefore have configured the api-side GraphQL handler to log common information about your queries and mutations. Log statements also be optionally enriched with [operation names](https://graphql.org/learn/queries/#operation-name), user agents, request ids, and performance timings to give you more visibility into your GraphQL api.

By configuring the GraphQL handler to use your api side [RedwoodJS logger](/docs/logger), any errors and other log statements about the [GraphQL execution](https://graphql.org/learn/execution/) will be logged to the [destination](/docs/logger#destination-aka-where-to-log) you\'ve set up: to standard output, file, or transport stream.

You configure the logger using the `loggerConfig` that accepts a [`logger`](/docs/logger) and a set of [GraphQL Logger Options](#graphql-logger-options).

### Configure the GraphQL Logger[​](#configure-the-graphql-logger "Direct link to Configure the GraphQL Logger") 

A typical GraphQLHandler `graphql.ts` is as follows:

api/src/functions/graphql.ts

``` 
// ...

import  from 'src/lib/logger'

// ...
export const handler = createGraphQLHandler( },
  // ...
})
```

#### Log Common Information[​](#log-common-information "Direct link to Log Common Information") 

The `loggerConfig` takes several options that logs meaningful information along the graphQL execution lifecycle.

Option

Description

data

Include response data sent to client.

operationName

Include operation name. The operation name is a meaningful and explicit name for your operation. It is only required in multi-operation documents, but its use is encouraged because it is very helpful for debugging and server-side logging. When something goes wrong (you see errors either in your network logs, or in the logs of your GraphQL server) it is easier to identify a query in your codebase by name instead of trying to decipher the contents. Think of this just like a function name in your favorite programming language. See [https://graphql.org/learn/queries/#operation-name](https://graphql.org/learn/queries/#operation-name)

requestId

Include the event\'s requestId, or if none, generate a uuid as an identifier.

query

Include the query. This is the query or mutation (with fields) made in the request.

tracing

Include the tracing and timing information. This will log various performance timings within the GraphQL event lifecycle (parsing, validating, executing, etc).

userAgent

Include the browser (or client\'s) user agent. This can be helpful to know what type of client made the request to resolve issues when encountering errors or unexpected behavior.

Therefore, if you wish to log the GraphQL `query` made, the `data` returned, and the `operationName` used, you would

api/src/functions/graphql.ts

``` 
export const handler = createGraphQLHandler(,
  },
  // ...
})
```

#### Exclude Operations[​](#exclude-operations "Direct link to Exclude Operations") 

You can exclude GraphQL operations by name with `excludeOperations`. This is useful when you want to filter out certain operations from the log output, for example, `IntrospectionQuery` from GraphQL playground:

api/src/functions/graphql.ts

``` 
export const handler = createGraphQLHandler(,
  },
  directives,
  sdls,
  services,
  onException: () => ,
})
```

> **Relevant anatomy of an operation**
>
> In the example below, `"FilteredQuery"` is the operation\'s name. That\'s what you\'d pass to `excludeOperations` if you wanted it filtered out.
>
> ::: 
> ::: codeBlockContent_QJqH
> ``` 
> export const filteredQuery = `
>   query FilteredQuery 
>   }
> ```
> :::
> :::

### Benefits of Logging[​](#benefits-of-logging "Direct link to Benefits of Logging") 

Benefits of logging common GraphQL request information include debugging, profiling, and resolving issue reports.

#### Operation Name Identifies Cells[​](#operation-name-identifies-cells "Direct link to Operation Name Identifies Cells") 

The [operation name](https://graphql.org/learn/queries/#operation-name) is a meaningful and explicit name for your operation. It is only required in multi-operation documents, but its use is encouraged because it is very helpful for debugging and server-side logging.

Because your cell typically has a unique operation name, logging this can help you identify which cell made a request.

api/src/functions/graphql.ts

``` 
// ...
export const handler = createGraphQLHandler( },
// ...
```

#### RequestId for Support Issue Resolution[​](#requestid-for-support-issue-resolution "Direct link to RequestId for Support Issue Resolution") 

Often times, your deployment provider will provide a request identifier to help reconcile and track down problems at an infrastructure level. For example, AWS API Gateway and AWS Lambda (used by Netlify, for example) provides `requestId` on the `event`.

You can include the request identifier setting the `requestId` logger option to `true`.

api/src/functions/graphql.ts

``` 
// ...
export const handler = createGraphQLHandler( },
// ...
```

And then, when working to resolve a support issue with your deployment provider, you can supply this request id to help them track down and investigate the problem more easily.

#### No Need to Log within Services[​](#no-need-to-log-within-services "Direct link to No Need to Log within Services") 

By configuring your GraphQL logger to include `data` and `query` information about each request you can keep your service implementation clean, concise and free of repeated logger statements in every resolver \-- and still log the useful debugging information.

api/src/functions/graphql.ts

``` 
// ...
export const handler = createGraphQLHandler( },
// ...

// api/src/services/posts.js
//...
export const post = async () => ,
  })
}
//...
```

The GraphQL handler will then take care of logging your query and data \-- as long as your logger is setup to log at the `info` [level](/docs/logger#log-level) and above.

> You can also disable the statements in production by just logging at the `warn` [level](/docs/logger#log-level) or above

This means that you can keep your services free of logger statements, but still see what\'s happening!

``` 
api | POST /graphql 200 7.754 ms - 1772
api | DEBUG [2021-09-29 16:04:09.313 +0000] (graphql-server): GraphQL execution started: BlogPostQuery
api |     operationName: "BlogPostQuery"
api |     query: 
api | DEBUG [2021-09-29 16:04:09.321 +0000] (graphql-server): GraphQL execution completed: BlogPostQuery
api |     data: 
api |     }
api |     operationName: "BlogPostQuery"
api |     query: 
api | POST /graphql 200 9.386 ms - 441
```

#### Send to Third-party Transports[​](#send-to-third-party-transports "Direct link to Send to Third-party Transports") 

Stream to third-party log and application monitoring services vital to production logging in serverless environments like [logFlare](https://logflare.app/), [Datadog](https://www.datadoghq.com/) or [LogDNA](https://www.logdna.com/)

#### Supports Log Redaction[​](#supports-log-redaction "Direct link to Supports Log Redaction") 

Everyone has heard of reports that Company X logged emails, or passwords to files or systems that may not have been secured. While RedwoodJS logging won\'t necessarily prevent that, it does provide you with the mechanism to ensure that won\'t happen.

To redact sensitive information, you can supply paths to keys that hold sensitive data using the RedwoodJS logger [redact option](/docs/logger#redaction).

Because this logger is used with the GraphQL handler, it will respect any redaction paths setup.

For example, you have chosen to log `data` return by each request, then you may want to redact sensitive information, like email addresses from your logs.

Here is an example of an application `/api/src/lib/logger.ts` configured to redact email addresses. Take note of the path `data.users[*].email` as this says, in the `data` attribute, redact the `email` from every `user`:

/api/src/lib/logger.ts

``` 
import  from '@redwoodjs/api/logger'

export const logger = createLogger(,
})
```

#### Timing Traces and Metrics[​](#timing-traces-and-metrics "Direct link to Timing Traces and Metrics") 

Often you want to measure and report how long your queries take to execute and respond. You may already be measuring these durations at the database level, but you can also measure the time it takes for your the GraphQL server to parse, validate, and execute the request.

You may turn on logging these metrics via the `tracing` GraphQL configuration option.

api/src/functions/graphql.ts

``` 
// ...
export const handler = createGraphQLHandler( },
// ...
```

Let\'s say we wanted to get some benchmark numbers for the \"find post by id\" resolver

``` 
return await db.post.findUnique(,
})
```

We see that this request took about 500 msecs (note: duration is reported in nanoseconds).

For more details about the information logged and its format, see [Apollo Tracing](https://github.com/apollographql/apollo-tracing).

``` 
pi | INFO [2021-07-09 14:25:52.452 +0000] (graphql-server): GraphQL willSendResponse
api |     tracing: ,
api |           ,
... more paths follow ...
api |         ]
api |       }
api |     }
```

By logging the operation name and extracting the duration for each query, you can easily collect and benchmark query performance.

## Security[​](#security "Direct link to Security") 

Parsing a GraphQL operation document is a very expensive and compute intensive operation that blocks the JavaScript event loop. If an attacker sends a very complex operation document with slight variations over and over again he can easily degrade the performance of the GraphQL server.

RedwoodJS will by default reject a variety malicious operation documents; that is, it\'ll prevent attackers from making malicious queries or mutations.

RedwoodJS is configured out-of-the-box with GraphQL security best practices:

-   Schema Directive-based Authentication including RBAC validation
-   Production Deploys disable Introspection and GraphQL Playground automatically
-   Reject Malicious Operation Documents (Max Aliases, Max Cost, Max Depth, Max Directives, Max Tokens)
-   Prevent Information Leaks (Block Field Suggestions, Mask Errors)

And with the Yoga Envelop Plugin ecosystem available to you, there are options for:

-   CSRF Protection
-   Rate Limiting
-   and more.

### Authentication[​](#authentication "Direct link to Authentication") 

By default, your GraphQL endpoint is open to the world.

That means anyone can request any query and invoke any Mutation. Whatever types and fields are defined in your SDL is data that anyone can access.

Redwood [encourages being secure by default](/docs/directives) by defaulting all queries and mutations to have the `@requireAuth` directive when generating SDL or a service.

When your app builds and your server starts up, Redwood checks that **all** queries and mutations have `@requireAuth`, `@skipAuth` or a custom directive applied.

If not, then your build will fail:

``` 
✖ Verifying graphql schema...
Building API...
Cleaning Web...
Building Web...
Prerendering Web...
You must specify one of @requireAuth, @skipAuth or a custom directive for
- contacts Query
- posts Query
- post Query
- updatePost Mutation
- deletePost Mutation
```

or your server won\'t startup and you should see that \"Schema validation failed\":

``` 
gen | Generating TypeScript definitions and GraphQL schemas...
gen | 47 files generated
api | Building... Took 593 ms
api | [GQL Server Error] - Schema validation failed
api | ----------------------------------------
api | You must specify one of @requireAuth, @skipAuth or a custom directive for
api | - posts Query
api | - createPost Mutation
api | - updatePost Mutation
api | - deletePost Mutation
```

To correct, just add the appropriate directive to your queries and mutations.

If not, then your build will fail and your server won\'t startup.

#### \@requireAuth[​](#requireauth "Direct link to @requireAuth") 

To enforce authentication, simply add the `@requireAuth` directive in your GraphQL schema for any query or field you want protected.

It\'s your responsibility to implement the `requireAuth()` function in your app\'s `api/src/lib/auth.` to check if the user is properly authenticated and/or has the expected role membership.

The `@requireAuth` directive will call the `requireAuth()` function to determine if the user is authenticated or not.

Here we enforce that a user must be logged in to `create`. `update` or `delete` a `Post`.

``` 
type Post 

input CreatePostInput 

input UpdatePostInput 

type Mutation 
```

It\'s your responsibility to implement the `requireAuth()` function in your app\'s `api/src/lib/auth.` to check if the user is properly authenticated and/or has the expected role membership.

The `@requireAuth` directive will call the requireAuth() function to determine if the user is authenticated or not.

api/src/lib/auth.ts

``` 
// ...

export const isAuthenticated = (): boolean => 

// ...

export const requireAuth = (: ) => 

  if (!hasRole()) 
}
```

> **Note**: The `auth.ts` file here is the stub for a new RedwoodJS app. Once you have setup auth with your provider, this will enforce a proper authentication check.

##### Field-level Auth[​](#field-level-auth "Direct link to Field-level Auth") 

You can apply the `@requireAuth` to any field as well (not just queries or mutations):

``` 
type Post 
```

##### Role-based Access Control[​](#role-based-access-control "Direct link to Role-based Access Control") 

The `@requireAuth` directive lets you define roles that are permitted to perform the operation:

``` 
type Mutation 
```

#### \@skipAuth[​](#skipauth "Direct link to @skipAuth") 

If, however, you want your query or mutation to be public, then simply use `@skipAuth`.

In the example, fetching all posts or a single post is allowed for all users, authenticated or not.

``` 
type Post 

type Query 
```

### Introspection and Playground Disabled in Production[​](#introspection-and-playground-disabled-in-production "Direct link to Introspection and Playground Disabled in Production") 

Because it is often useful to ask a GraphQL schema for information about what queries it supports, GraphQL allows us to do so using the [introspection](https://graphql.org/learn/introspection/) system.

The [GraphQL Playground](https://www.graphql-yoga.com/docs/features/graphiql) is a way for you to interact with your schema and try out queries and mutations. It can show you the schema by inspecting it. You can find the GraphQL Playground at [http://localhost:8911/graphql](http://localhost:8911/graphql) when your dev server is running.

> Because both introspection and the playground share possibly sensitive information about your data model, your data, your queries and mutations, best practices for deploying a GraphQL Server call to disable these in production, RedwoodJS **, by default, only enables introspection and the playground when running in development**. That is when `process.env.NODE_ENV === 'development'`.

However, there may be cases where you want to enable introspection as well as the GraphQL Playground. You can enable introspection by setting the `allowIntrospection` option to `true` and enable GraphiQL by setting `allowGraphiQL` to `true`.

Here is an example of `createGraphQLHandler` function with the `allowIntrospection` and `allowGraphiQL` options set to `true`:

``` 
export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  allowIntrospection: true, // 👈 enable introspection in all environments
  allowGraphiQL: true, // 👈 enable GraphiQL Playground in all environments
  onException: () => ,
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

Enabling introspection in production may pose a security risk, as it allows users to access information about your schema, queries, and mutations. Use this option with caution and make sure to secure your GraphQL API properly.

The may be cases where one wants to allow introspection, but not GraphiQL.

Or, you may want to enable GraphiQL, but not allow introspection; for example, to try out known queries, but not to share the entire set of possible operations and types.

### GraphQL Armor Configuration[​](#graphql-armor-configuration "Direct link to GraphQL Armor Configuration") 

[GraphQL Armor](https://escape.tech/graphql-armor/) is a middleware that adds a security layer the RedwoodJS GraphQL endpoint configured with sensible defaults.

You don\'t have to configure anything to enforce protection against alias, cost, depth, directive, tokens abuse in GraphQL operations as well as to block field suggestions or revealing error messages that might leak sensitive information.

But, if you need to enable, disable to modify the default settings, GraphQL Armor is fully configurable in a per-plugin fashion.

Simply define and provide a custom GraphQL Security configuration to your `createGraphQLHandler`:

``` 
export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  armorConfig, //  👈 custom GraphQL Security configuration
  onException: () => ,
})
```

For example, the default max query depth limit is 6. To change that setting to 2 levels, simply provide the configuration to your handler:

``` 
export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  armorConfig:  },
  onException: () => ,
})
```

#### Max Aliases[​](#max-aliases "Direct link to Max Aliases") 

This protection is enabled by default.

Limit the number of aliases in a document. Defaults to 15.

##### Example[​](#example "Direct link to Example") 

Aliases allow you to rename the data that is returned in a query's results. They manipulate the structure of the query result that is fetched from your service, displaying it according to your web component\'s needs.

This contrived example uses 11 alias to rename a Post\'s id and title to various permutations of post, article, and blog to return a different shape in the query result as `articles`:

``` 
 
}
```

##### Configuration and Defaults[​](#configuration-and-defaults "Direct link to Configuration and Defaults") 

Limit the number of aliases in a document. Defaults to 15.

You can change the default value via the `maxAliases` setting when creating your GraphQL handler.

``` 

}
```

#### Cost Limit[​](#cost-limit "Direct link to Cost Limit") 

This protection is enabled by default.

It analyzes incoming GraphQL queries and applies a cost analysis algorithm to prevent resource overload by blocking too expensive requests (DoS attack attempts).

The cost computation is quite simple (and naive) at the moment but there are plans to make it evolve toward a extensive plugin with many features.

Defaults to a overall maxCost limit of 5000.

##### Overview[​](#overview "Direct link to Overview") 

Cost is a factor of the kind of field and depth. Total Cost is a cumulative sum of each field based on its type and its depth in the query.

Scalar fields \-- those that return values like strings or numbers \-- are worth one value; whereas are objects are worth another.

How deep they are nested in the query is a multiplier factor such that:

``` 
COST = FIELD_KIND_COST * (DEPTH * DEPTH_COST_FACTOR)
TOTAL_COST = SUM(COST)
```

If the `TOTAL_COST` exceeds the `maxCost`, an error stops GraphQL execution and rejects the request.

You have control over the field kind and depth costs settings, but the defaults are:

``` 
objectCost: 2, // cost of retrieving an object
scalarCost: 1, // cost of retrieving a scalar
depthCostFactor: 1.5, // multiplicative cost of depth
```

##### Example[​](#example-1 "Direct link to Example") 

In this small example, we have one object field `me` that contains two, nested scalar fields `id` and `me`. There is an operation `profile` (which is neither a scalar nor object and thus ignored as part of the cost calculation).

``` 

  }
}
```

The cost breakdown for cost is:

-   two scalars `id` and `user` worth 1 each
-   they are at level 1 depth with a depth factor of 1.5
-   2 \* ( 1 \* 1.5 ) = 2 \* 1.5 = 3
-   their parent object is `me` worth 2

Therefore the total cost is 2 + 3 = 5.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

The operation definition `query` of `profile` is ignored in the calculation. This is the case even if you name your query `MY_PROFILE` like:

``` 

  }
}
```

##### Configuration and Defaults[​](#configuration-and-defaults-1 "Direct link to Configuration and Defaults") 

Defaults to a overall maxCost limit of 5000.

You can change the default value via the `costLimit` setting when creating your GraphQL handler.

``` 

}
```

#### Max Depth Limit[​](#max-depth-limit "Direct link to Max Depth Limit") 

This protection is enabled by default.

Limit the depth of a document. Defaults to 6 levels.

Attackers often submit expensive, nested queries to abuse query depth that could overload your database or expend costly resources.

Typically, these types of unbounded, complex and expensive GraphQL queries are usually huge deeply nested and take advantage of an understanding of your schema (hence why schema introspection is disabled by default in production) and the data model relationships to create \"cyclical\" queries.

##### Example[​](#example-2 "Direct link to Example") 

An example of a cyclical query here takes advantage of knowing that an author has posts and each post has an author \... that has posts \... that has an another that \... etc.

This cyclical query has a depth of 8.

``` 
// cyclical query example
// depth: 8+
query cyclical 
              }
            }
          }
        }
      }
    }
  }
}
```

##### Configuration and Defaults[​](#configuration-and-defaults-2 "Direct link to Configuration and Defaults") 

Defaults to 6 levels.

You can change the default value via the `maxDepth` setting when creating your GraphQL handler.

``` 

}
```

#### Max Directives[​](#max-directives "Direct link to Max Directives") 

This protections is enabled by default.

Limit the number of directives in a document. Defaults to 50.

##### Example[​](#example-3 "Direct link to Example") 

The following example demonstrates that by using the `@include` and `@skip` GraphQL query directives one can design a large request that requires computation, but in fact returns the expected response \...

``` 

}
```

\... of formatted Posts with just a single id and title.

``` 
,
      ,
      ,
      
    ]
  }
}
```

By limiting the maximum number of directives in the document, malicious queries can be rejected.

##### Configuration and Defaults[​](#configuration-and-defaults-3 "Direct link to Configuration and Defaults") 

You can change the default value via the `maxDirectives` setting when creating your GraphQL handler.

``` 

}
```

#### Max Tokens[​](#max-tokens "Direct link to Max Tokens") 

This protection is enabled by default.

Limit the number of GraphQL tokens in a document.

In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters into a sequence of lexical tokens.

E.g. given the following GraphQL operation.

``` 
 graphql 
 }
```

The tokens are `query`, `` and `}`. Having a total count of 8 tokens.

##### Example[​](#example-4 "Direct link to Example") 

Given the query with 8 tokens:

``` 
 graphql 
 }
```

And a custom configuration to all a maximum of two tokens:

``` 
const armorConfig = ,
}
```

An error is raised:

``` 
'Syntax Error: Token limit of 2 exceeded, found 3.'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

When reporting the number of found tokens, then number found is not the total tokens, but the value when found that exceeded the limit.

Therefore found would be n + 1.

##### Configuration and Defaults[​](#configuration-and-defaults-4 "Direct link to Configuration and Defaults") 

Defaults to 1000.

You can change the default value via the `maxTokens` setting when creating your GraphQL handler.

``` 

}
```

#### Block Field Suggestions[​](#block-field-suggestions "Direct link to Block Field Suggestions") 

This plugin is enabled by default.

It will prevent suggesting fields in case of an erroneous request. Suggestions can lead to the leak of your schema even with disabled introspection, which can be very detrimental in case of a private API.

Example of such a suggestion:

`Cannot query field "sta" on type "Media". Did you mean "stats", "staff", or "status"?`

##### Example[​](#example-5 "Direct link to Example") 

##### Configuration and Defaults[​](#configuration-and-defaults-5 "Direct link to Configuration and Defaults") 

Enabled by default.

You can change the default value via the `blockFieldSuggestions` setting when creating your GraphQL handler.

``` 

}
```

Enabling will hide the field suggestion:

`Cannot query field "sta" on type "Media". [Suggestion hidden]?`

Orm if you want a custom mask:

``` 
,
}
```

`Cannot query field "sta" on type "Media". [REDACTED]?`

### Error Masking[​](#error-masking "Direct link to Error Masking") 

In many GraphQL servers, when an error is thrown, the details of that error are leaked to the outside world. The error and its message are then returned in the response and a client might reveal those errors in logs or even render the message to the user. You could potentially leak sensitive or other information about your app you don\'t want to share---such as database connection failures or even the presence of certain fields.

Redwood is here to help!

Redwood prevents leaking sensitive error-stack information out-of-the-box for unexpected errors. If an error that isn\'t one of [Redwood\'s GraphQL Errors](#redwood-errors) or isn\'t based on a GraphQLError is thrown:

-   The original error and its message will be logged using the defined GraphQL logger, so you\'ll know what went wrong
-   A default message \"Something went wrong\" will replace the error message in the response (Note: you can customize this message)

#### Customizing the Error Message[​](#customizing-the-error-message "Direct link to Customizing the Error Message") 

But what if you still want to share an error message with client? Simply use one of [Redwood\'s GraphQL Errors](#redwood-errors) and your custom message will be shared with your users.

#### Customizing the Default Error Message[​](#customizing-the-default-error-message "Direct link to Customizing the Default Error Message") 

You can customize the default \"Something went wrong\" message used when the error is masked via the `defaultError` setting on the `createGraphQLHandler`:

``` 
export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  defaultError: 'Sorry about that', // 👈 Customize the error message
  onException: () => ,
})
```

#### Redwood Errors[​](#redwood-errors "Direct link to Redwood Errors") 

Redwood Errors are inspired from [Apollo Server Error codes](https://www.apollographql.com/docs/apollo-server/data/errors/#error-codes) for common use cases:

To use a Redwood Error, import each from `@redwoodjs/graphql-server`.

-   `SyntaxError` - An unspecified error occurred
-   `ValidationError` - Invalid input to a service
-   `AuthenticationError` - Failed to authenticate
-   `ForbiddenError` - Unauthorized to access
-   `UserInputError` - Missing input to a service

If you use one of the errors, then the message provided will not be masked and will be shared in the GraphQL response:

``` 
import  from '@redwoodjs/graphql-server'
// ...
throw new UserInputError('An email is required.')
```

then the message provided will not be masked and it will be shred in the GraphQL response.

##### Custom Errors and Uses[​](#custom-errors-and-uses "Direct link to Custom Errors and Uses") 

Need you own custom error and message?

Maybe you\'re integrating with a third-party api and want to handle errors from that service and also want control of how that error is shared with your user client-side.

Simply extend from `RedwoodError` and you\'re all set!

``` 
export class MyCustomError extends RedwoodError 
}
```

For example, in your service, you can create and use it to handle the error and return a friendly message:

``` 
export class WeatherError extends RedwoodError 
}

export const getWeather = async (: WeatherInput)  catch(error) 

    // other error
    throw new WeatherError(`We could not get the weather for $.`)
  }
}
```

#### CSRF Prevention[​](#csrf-prevention "Direct link to CSRF Prevention") 

If you have CORS enabled, almost all requests coming from the browser will have a preflight request - however, some requests are deemed \"simple\" and don\'t make a preflight. One example of such a request is a good ol\' GET request without any headers, this request can be marked as \"simple\" and have preflight CORS checks skipped therefore skipping the CORS check.

This attack can be mitigated by saying: \"all GET requests must have a custom header set\". This would force all clients to manipulate the headers of GET requests, marking them as \"\_not-\_simple\" and therefore always executing a preflight request.

You can achieve this by using the [`@graphql-yoga/plugin-csrf-prevention` GraphQL Yoga plugin](https://the-guild.dev/graphql/yoga-server/docs/features/csrf-prevention).

## Self-Documenting GraphQL API[​](#self-documenting-graphql-api "Direct link to Self-Documenting GraphQL API") 

RedwoodJS helps you document your GraphQL API by generating commented SDL used for GraphiQL and the GraphQL Playground explorer \-- as well as can be turned into API docs using tools like [Docusaurus](#use-in-docusaurus).

If you specify the SDL generator with its `--docs` option, any comments (which the [GraphQL spec](https://spec.graphql.org/October2021/#sec-Descriptions) calls \"descriptions\") will be incorporated into your RedwoodJS app\'s `graphql.schema` file when generating types.

If you comment your Prisma schema models, its fields, or enums, the SDL generator will use those comments as the documentation.

If there is no Prisma comment, then the SDL generator will default a comment that you can then edit.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

If you re-generate the SDL, any custom comments will be overwritten. However, if you make those edits in your Prisma schema, then those will be used.

### Prisma Schema Comments[​](#prisma-schema-comments "Direct link to Prisma Schema Comments") 

Your Prisma schema is documented with triple slash comments (`///`) that precedes:

-   Model names
-   Enum names
-   each Model field name

``` 
/// A blog post.
model Post 

/// A list of allowed colors.
enum Color 
```

### SDL Comments[​](#sdl-comments "Direct link to SDL Comments") 

When used with `--docs` option, [SDL generator](/docs/cli-commands#generate-sdl) adds comments for:

-   Directives
-   Queries
-   Mutations
-   Input Types

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

By default, the `--docs` option to the SDL generator is false and comments are not created.

Comments \[enclosed in `"""` or `"`\]([GraphQL spec](https://spec.graphql.org/October2021/#sec-Descriptions) in your sdl files will be included in the generated GraphQL schema at the root of your project (.redwood/schema.graphql).

``` 
"""
Use to check whether or not a user is authenticated and is associated
with an optional set of roles.
"""
directive @requireAuth(roles: [String]) on FIELD_DEFINITION

"""Use to skip authentication checks and allow public access."""
directive @skipAuth on FIELD_DEFINITION

"""
Autogenerated input type of InputPost.
"""
input CreatePostInput 

"""
Autogenerated input type of UpdatePost.
"""
input UpdatePostInput 

"""
A blog post.
"""
type Post 

"""
About mutations
"""
type Mutation 

"""
About queries
"""
type Query 
```

#### Root Schema[​](#root-schema "Direct link to Root Schema") 

Documentation is also generated for the Redwood Root Schema that defines details about Redwood such as the current user and version information.

``` 
type Query 

"""
The Redwood Root Schema

Defines details about Redwood such as the current user and version information.
"""
type Redwood 

scalar BigInt
scalar Date
scalar DateTime
scalar JSON
scalar JSONObject
scalar Time
```

### Preview in GraphiQL[​](#preview-in-graphiql "Direct link to Preview in GraphiQL") 

The [GraphQL Playground aka GraphiQL](https://www.graphql-yoga.com/docs/features/graphiql) is a way for you to interact with your schema and try out queries and mutations. It can show you the schema by inspecting it. You can find the GraphQL Playground at [http://localhost:8911/graphql](http://localhost:8911/graphql) when your dev server is running.

The documentation generated is present when exploring the schema.

#### Queries[​](#queries "Direct link to Queries") 

![graphiql-queries](/img/graphql-api-docs/graphiql-queries.png)

#### Mutations[​](#mutations "Direct link to Mutations") 

![graphiql-mutations](/img/graphql-api-docs/graphiql-mutations.png)

#### Model Types[​](#model-types "Direct link to Model Types") 

![graphiql-type](/img/graphql-api-docs/graphiql-type.png)

#### Input Types[​](#input-types "Direct link to Input Types") 

![graphiql-input-type](/img/graphql-api-docs/graphiql-input-type.png)

### Use in Docusaurus[​](#use-in-docusaurus "Direct link to Use in Docusaurus") 

If your project uses [Docusaurus](https://docusaurus.io), the generated commented SDL can be used to publish documentation using the [graphql-markdown](https://graphql-markdown.dev/) plugin.

#### Basic Setup[​](#basic-setup "Direct link to Basic Setup") 

The following is some basic setup information, but please consult [Docusaurus](https://docusaurus.io) and the [graphql-markdown](https://graphql-markdown.dev/) for latest instructions.

1.  Install Docusaurus (if you have not done so already)

``` 
npx create-docusaurus@latest docs classic
```

Add `docs` to your `workspaces` in the project\'s `package.json`:

``` 
  "workspaces": ,
```

2.  Ensure a `docs` directory exists at the root of your project

``` 
mkdir docs // if needed
```

3.  Install the GraphQL Generators Plugin

``` 
yarn workspace docs add @graphql-markdown/docusaurus graphql @graphql-tools/graphql-file-loader
```

4.  Ensure a Directory for your GraphQL APi generated documentation resides in with the Docusaurus directory `/docs` structure

``` 
// Change into the "docs" workspace

cd docs

// you should have the "docs" directory and within that a "graphql-api" directory
mkdir docs/graphql-api // if needed
```

5.  Update `docs/docusaurus.config.js` and configure the plugin and navbar

``` 
// docs/docusaurus.config.js
// ...
  plugins: [
    [
      '@graphql-markdown/docusaurus',
      ,
      },
    ],
  ],
// ...
themeConfig:
    /** @type  */
    (,
        items: [
          ,
//...
```

7.  Generate the docs

`yarn docusaurus graphql-to-doc`

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

You can overwrite the generated docs and bypass the plugin\'s diffMethod use `--force`.

`yarn docusaurus graphql-to-doc --force`

8.  Start Docusaurus

``` 
yarn start
```

##### Example Screens[​](#example-screens "Direct link to Example Screens") 

##### Schema Documentation[​](#schema-documentation "Direct link to Schema Documentation") 

![graphql-doc-example-main](/assets/images/schema-doc-c14f24a56e73101ca4dd5aebbfee5ef0.png)

##### Type Example[​](#type-example "Direct link to Type Example") 

![graphql-doc-example-type](/assets/images/contact-type-2c4bd1b5fd6b6f60fa2f8572b6396a8f.png)

##### Query Example[​](#query-example "Direct link to Query Example") 

![graphql-doc-example-query](/assets/images/contact-query-5eadc6a3a5ad60e4903926a381c1499e.png)

##### Mutation Example[​](#mutation-example "Direct link to Mutation Example") 

![graphql-doc-example-mutation](/assets/images/schema-mutation-c5d23d7434814fc4e9d6177ac673951d.png)

##### Directive Example[​](#directive-example "Direct link to Directive Example") 

![graphql-doc-example-directive](/assets/images/schema-directive-28ea17d40b58814062a273159e359a59.png)

##### Scalar Example[​](#scalar-example "Direct link to Scalar Example") 

![graphql-doc-example-scalar](/assets/images/schema-scalar-03839fcdabeb1339a9b60f34c8aa7868.png)

## FAQ[​](#faq "Direct link to FAQ") 

### Why Doesn\'t Redwood Use Something Like Nexus?[​](#why-doesnt-redwood-use-something-like-nexus "Direct link to Why Doesn't Redwood Use Something Like Nexus?") 

This might be one of our most frequently asked questions of all time. Here\'s [Tom\'s response in the forum](https://community.redwoodjs.com/t/anyone-playing-around-with-nexus-js/360/5):

> We started with Nexus, but ended up pulling it out because we felt like it was too much of an abstraction over the SDL. It's so nice being able to just read the raw SDL to see what the GraphQL API is.

## Further Reading[​](#further-reading "Direct link to Further Reading") 

Eager to learn more about GraphQL? Check out some of the resources below:

-   [GraphQL.wtf](https://graphql.wtf) covers most aspects of GraphQL and publishes one short video a week
-   The official GraphQL Yoga (the GraphQL server powering Redwood) [tutorial](https://www.graphql-yoga.com/tutorial/basic/00-introduction) is the best place to get your hands on GraphQL basics
-   And of course, [the official GraphQL docs](https://graphql.org/learn/) are great place to do a deep dive into exactly how GraphQL works

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/graphql.md)