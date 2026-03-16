# Source: https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md

# API Reference: @apollo/gateway

This API reference documents the exports from the `@apollo/gateway` package. This package enables you to use Apollo Server as a gateway for a federated supergraph. For more information, see [Implementing a gateway with Apollo Server](https://www.apollographql.com/docs/apollo-server/using-federation/apollo-gateway-setup).

> We recommend that all supergraphs use the GraphOS Router instead of this Node.js-based gateway. See [Choosing a router library](https://www.apollographql.com/docs/federation/building-supergraphs/router/#choosing-a-router-library).

## `class ApolloGateway`

The core class of Apollo Server's federated gateway implementation. For an
example of using `ApolloGateway`, see [Implementing a gateway with Apollo Server](https://www.apollographql.com/docs/apollo-server/using-federation/apollo-gateway-setup).

### Methods

#### `constructor`

Returns an initialized `ApolloGateway` instance, which you can then pass as the `gateway` configuration option to the `ApolloServer` constructor, like so:

```ts
const server = new ApolloServer({
  // highlight-start
  gateway: new ApolloGateway({
    serviceList: [
      // ...
    ],
  }),
  // highlight-end
});
```

Takes an `options` object as a parameter. Supported fields of this object are described below.

##### Examples

###### Providing a `serviceList` and headers to authorize introspection

```ts
const gateway = new ApolloGateway({
  serviceList: [
    { name: 'products', url: 'https://products-service.dev/graphql' },
    { name: 'reviews', url: 'https://reviews-service.dev/graphql' },
  ],
  introspectionHeaders: {
    Authorization: 'Bearer abc123',
  },
});
```

###### Configuring the subgraph fetcher

If you provide a [`buildService` function](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#the-buildservice-function) to the constructor of `ApolloGateway`, the function is called once for each of your graph's subgraphs. This function can return a `RemoteGraphQLDataSource` with a custom `fetcher`, which is then used for all communication with subgraphs:

```ts
const gateway = new ApolloGateway({
  buildService({ url, name }) {
    return new (class extends RemoteGraphQLDataSource {
      fetcher = require('make-fetch-happen').defaults({
        onRetry() {
          console.log('We will retry!');
        },
      });
    })({
      url,
      name,
    });
  },
});
```

###### Configuring the managed federation fetcher

> This *only* configures the fetcher that your gateway uses to fetch [managed federation](https://www.apollographql.com/docs/federation/managed-federation/overview/) configuration from Apollo.
>
> See also [Configuring the subgraph fetcher](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#configuring-the-subgraph-fetcher).

```ts
const gateway = new ApolloGateway({
  fetcher: require('make-fetch-happen').defaults({
    onRetry() {
      console.log('We will retry!');
    },
  }),
});
```

##### Options

Name /Type
Description

###### `supergraphSdl`

`string | SupergraphSdlHook | SupergraphManager`

You provide your supergraph schema to the gateway with this option. You can provide it as a `string`, via a `SupergraphSdlHook`, or via a `SupergraphManager`.

**When `supergraphSdl` is a `string`:** A [supergraph schema](https://www.apollographql.com/docs/federation/federated-schemas/#supergraph-schema) ([generated with the Rover CLI](https://www.apollographql.com/docs/rover/commands/supergraphs/#composing-a-supergraph-schema)) that's composed from your subgraph schemas. The supergraph schema includes directives that specify routing information for each subgraph.

**When `supergraphSdl` is a `SupergraphSdlHook`:** This is an `async` function that returns an object containing a `supergraphSdl` string as well as a `cleanup` function. The hook accepts an object containing the following properties:

* `update`: A function that updates the supergraph schema
* `healthCheck`: A function that issues a health check against the subgraphs
* `getDataSource`: A function that gets a data source for a particular subgraph from the gateway

**When `supergraphSdl` is a `SupergraphManager`:** An object containing an `initialize` property. `initialize` is an `async` function of the `SupergraphSdlHook` type described directly above.

**If you are using managed federation,** do not provide this field.

**If you *aren't* using managed federation,** either this field or `serviceList` is required. Do not provide both.

###### `serviceList`

`Array<ServiceEndpointDefinition>`

**This option is deprecated in favor of the drop-in replacement, [`IntrospectAndCompose`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#class-introspectandcompose).**

An array of objects that each specify the `name` and `url` of one subgraph in your federated graph. On startup, the gateway uses this array to obtain your subgraph schemas via introspection and compose a supergraph schema.

You can specify any string value for the `name` field, which is used for identifying the subgraph in log output and error messages, and for reporting metrics to Apollo Studio.

**If you are using managed federation,** do not provide this field.

**If you *aren't* using managed federation,** either this field or `supergraphSdl` is required. Do not provide both.

###### `introspectionHeaders`

`Object | (service: ServiceEndpointDefinition) => (Promise<Object> | Object)`

**This option is deprecated in favor of the drop-in replacement, [`IntrospectAndCompose`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#class-introspectandcompose).**

An object (or an optionally async function *returning* an object) that contains the names and values of HTTP headers that the gateway includes *only* when making introspection requests to your subgraphs.

**If you are using managed federation,** do not provide this field.

**If you define a [`buildService`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#buildservice) function,** specify these headers in that function instead of providing this option. This ensures that your `buildService` function doesn't inadvertently overwrite the values of any headers you provide here.

###### `debug`

`Boolean`

If `true`, enables development mode helpers and logs messages of all severity levels (`debug` through `error`). If `false`, only `warn`- and `error`-level messages are logged.

The default value is `false`.

###### `logger`

[`Logger`](https://github.com/apollographql/apollo-utils/tree/main/packages/logger)

An object to use for logging in place of `console`. If provided, this object must implement all methods of [the `Logger` interface](https://github.com/apollographql/apollo-utils/tree/main/packages/logger).

If you provide this value, the gateway automatically logs all messages of *all* severity levels (`debug` through `error`), regardless of whether the `debug` option is set to `true`. It is the responsibility of the logger to determine how to handle logged messages of each level.

This logger is automatically added to the `GraphQLRequestContext` object that's passed to all Apollo Server [plugin functions](https://www.apollographql.com/docs/apollo-server/integrations/plugins/).

###### `fetcher`

[`Fetcher`](https://www.npmjs.com/package/@apollo/utils.fetcher)

Specifies which [Fetch API](https://fetch.spec.whatwg.org/#fetch-api) implementation to use with [managed federation](https://www.apollographql.com/docs/federation/managed-federation/overview/) when fetching configuration from Apollo.

By default, the gateway uses the default configuration of [`make-fetch-happen`](https://npm.im/make-fetch-happen). You can specify another valid implementation (such as [`node-fetch`](https://npm.im/node-fetch)) by setting this field's value to `require('node-fetch')`.

As shown in the example above, you can also provide [`make-fetch-happen`](https://www.npmjs.com/package/make-fetch-happen#extra-options) to this option if you want to override the library's default configuration.

###### `serviceHealthCheck`

`Boolean`

If `true`, the gateway sends a small query (`{ __typename }`) to all subgraphs on gateway startup. It also does the same on each live schema update if you're using managed federation.

**On startup,** the gateway throws an error if any of these requests fail.

**On schema update,** the gateway does not roll over to the new schema or graph configuration if any of these requests fail. The gateway retries the requests at each polling interval until they succeed.

The default value is `false`.

###### `uplinkEndpoints`

`Array<string>`

A list of Apollo Uplink URLs the gateway uses to poll for its managed configuration. For details and defaults, see [Apollo Uplink](https://www.apollographql.com/docs/federation/managed-federation/uplink/).

Provide this field **only** if you are using managed federation *and* your use case specifically requires it (this is uncommon).

###### `uplinkMaxRetries`

`number`

The maximum number of times the gateway retries a failed poll request to Apollo Uplink, cycling through its list of [`uplinkEndpoints`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#uplinkendpoints).

The default value is to try each of your uplinkEndpoints three times (i.e., 5 retries with the default list of two endpoints).

Provide this field **only** if you are using managed federation.

###### `fallbackPollIntervalInMs` (managed mode only)

`number`

Specify this option as a fallback if Uplink fails to provide a polling interval. This will also take effect if `fallbackPollIntervalInMs` is greater than the Uplink defined interval.

###### `buildService`

`Function`

Define this function to customize your gateway's data transport to some or all of your subgraphs. This customization can include using a protocol besides HTTP. For details, see [The `buildService` function](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#the-buildservice-function).

##### The `buildService` function

If you provide this function, the gateway calls it once for each subgraph. The function must return an object that implements the [`GraphQLDataSource` interface](https://github.com/apollographql/federation/blob/main/gateway-js/src/datasources/types.ts), such as an instance of [RemoteGraphQLDataSource](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#class-remotegraphqldatasource) or a subclass of it.

The example below demonstrates adding an `x-user-id` HTTP header to every request the gateway sends to a subgraph:

```ts
class AuthenticatedDataSource extends RemoteGraphQLDataSource {
  willSendRequest({ request, context }) {
    request.http.headers.set('x-user-id', context.userId);
  }
}

const gateway = new ApolloGateway({
  // ...other options...
  // highlight-start
  buildService({ name, url }) {
    return new AuthenticatedDataSource({ url });
  },
  // highlight-end
});
```

##### Experimental options

**These options are experimental.** They might be removed or change at any time, even within a patch release.

Name /Type
Description

###### `experimental_approximateQueryPlanStoreMiB`

`number`

Sets the approximate size (in MiB) of the gateway's query plan store. This cache is used to save query plans for reuse on subsequent queries that resolve to a previously observed `queryHash` (the SHA-256 of the incoming operation).

The default value is `30`, which is usually sufficient unless the server processes a large number of unique operations.

#### `serviceHealthCheck`

When called, the gateway sends a small query (`{ __typename }`) to each subgraph to verify that they're all responsive. This function `throw`s on failure and returns a `Promise` to be `await`ed.

##### Parameters

Name /Type
Description

###### `serviceMap`

`Object` (`DataSourceMap`)

If provided, the gateway sends health check requests to only the data sources included in the map.

By default, the gateway uses `this.serviceMap` (i.e., it sends health check requests to all known subgraphs).

## `class RemoteGraphQLDataSource`

Represents a connection between your federated gateway and *one* of your subgraphs.

You can customize this connection by extending this class and overriding its `willSendRequest` and/or `didReceiveResponse` methods:

* Override `willSendRequest` to modify your gateway's requests to the subgraph before they're sent.
* Override `didReceiveResponse` to modify the subgraph's responses before the gateway passes them along to the requesting client.

These methods are described in detail below.

### Methods

#### `constructor`

Returns an initialized `RemoteGraphQLDataSource` instance:

```ts
const productsDataSource = new RemoteGraphQLDataSource({
  url: 'https://products-service.dev/graphql',
});
```

Takes an `options` object as a parameter. Supported fields of this object are described below.

##### Options

Name /Type
Description

###### `url`

`String`

**Required.** The subgraph's URL for sending fetch requests via HTTP.

###### `apq`

`Boolean`

If `true`, the gateway attempts to use [automated persisted queries (APQ)](https://www.apollographql.com/docs/apollo-server/performance/apq/) when sending queries to this subgraph. APQ can dramatically reduce the size of most requests sent over the network, especially for more complex queries.

The subgraph must also enable support for APQ for the gateway to use this feature (Apollo Server enables APQ by default).

#### `willSendRequest`

Override this method in a subclass to modify each outgoing fetch request before it's sent to the subgraph:

```ts
// Adds an `x-user-id` header to each outgoing fetch request
class AuthenticatedDataSource extends RemoteGraphQLDataSource {
  willSendRequest({ request, context }) {
    request.http.headers.set('x-user-id', context.userId);
  }
};
```

This method takes a `requestContext` object that contains both the original unmodified `request` and the current `context` object (i.e., the `contextValue` object).

#### `didReceiveResponse`

Override this method in a subclass to customize the gateway's behavior after it completes a fetch to the subgraph, but *before* it sends a response to the requesting client:

```ts
class CookieDataSource extends RemoteGraphQLDataSource {
  didReceiveResponse({ response, request, context }) {
    const cookie = request.http.headers.get('Cookie');
    if (cookie) {
      context.responseCookies.push(cookie);
    }

    // Return the response, even when unchanged.
    return response;
  }
}
```

This method takes a `requestContext` object that contains:

* The subgraph's `response`
* The gateway's `request` to the subgraph
* The current operation's `context` (i.e., the `contextValue` object)

This enables you to modify any combination of the operation's `contextValue` and the response of the fetch.

The `http` property of the `request` and `response` objects contains additional HTTP-specific properties, such as `headers`.

This method must return an object that matches the structure of a [`GraphQLResponse`](https://github.com/apollographql/apollo-server/blob/dd15bc1d7df6b5614b53e5cad62699222dc44279/packages/server/src/externalTypes/graphql.ts#L44-L52). If no modifications are necessary, return the original `response`.

#### `didEncounterError`

Override this method in a subclass to customize the gateway's behavior after it encounters an error while communicating with the subgraph or while parsing its response (e.g., if the response is not well-formed JSON).

If you *don't* override this method, the default implementation `throw`s the error, like so:

```ts
class MyDataSource extends RemoteGraphQLDataSource {
  didEncounterError(error, fetchRequest, fetchResponse, context) {
    throw error;
  }
}
```

Note that if you *don't* `throw error` (or a different `Error`) in this method, `error` is thrown immediately after this method returns.

This method takes the following positional parameters:

Name /Type
Description

###### `error`

`Error`

The error that occurred during communication.

###### `fetchRequest`

`Request`

The details of the `fetch` request sent to the subgraph.

###### `fetchResponse`

`Response`

The details of the `fetch` response sent by the subgraph.

###### `context`

`TContext`

[The `contextValue` object](https://www.apollographql.com/docs/apollo-server/data/context#the-contextvalue-object) passed between the GraphQL operation's resolvers.

## `class IntrospectAndCompose`

> ⚠️ **We strongly recommend *against* using `IntrospectAndCompose` in production.** For details, see [Limitations of `IntrospectAndCompose`](https://www.apollographql.com/docs/apollo-server/using-federation/apollo-gateway-setup#limitations-of-introspectandcompose).

`IntrospectAndCompose` is a development tool for fetching and composing subgraph SDL into a supergraph for your gateway. Given a list of subgraphs and their URLs, `IntrospectAndCompose` will issue queries for their SDL, compose them into a supergraph, and provide that supergraph to the gateway. It can also be configured to update via polling and perform subgraph health checks to ensure that supergraphs are updated safely. `IntrospectAndCompose` implements the `SupergraphManager` interface and is passed in to `ApolloGateway`'s `supergraphSdl` constructor option.

> `IntrospectAndCompose` is the drop-in replacement for `serviceList`.

### Methods

#### `constructor`

Returns an initialized `IntrospectAndCompose` instance, which you can then pass to the `supergraphSdl` configuration option of the `ApolloGateway` constructor, like so:

```ts
const server = new ApolloServer({
  gateway: new ApolloGateway({
    // highlight-start
    supergraphSdl: new IntrospectAndCompose({
      subgraphs: [
        // ...
      ],
    }),
    // highlight-end
  }),
});
```

Takes an `options` object as a parameter. Supported properties of this object are described below.

##### Examples

###### Providing a `subgraphs` list and headers to authorize introspection

```ts
const gateway = new ApolloGateway({
  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: 'products', url: 'https://products-service.dev/graphql' },
      { name: 'reviews', url: 'https://reviews-service.dev/graphql' },
    ],
    introspectionHeaders: {
      Authorization: 'Bearer abc123',
    },
  }),
});
```

###### Configuring the subgraph fetcher

`IntrospectAndCompose` uses the data sources constructed by `ApolloGateway`. To customize the gateway's data sources, you can provide a [`buildService`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#buildservice) function to the `ApolloGateway` constructor. In the example below, `IntrospectAndCompose` makes authenticated requests to the subgraphs
via the `AuthenticatedDataSource`s that we construct in the gateway's `buildService` function.

```ts
const gateway = new ApolloGateway({
  buildService({ name, url }) {
    return new AuthenticatedDataSource({ url });
  },
  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: 'products', url: 'https://products-service.dev/graphql' },
      { name: 'reviews', url: 'https://reviews-service.dev/graphql' },
    ],
  }),
});
```

##### Options

Name /Type
Description

###### `subgraphs`

`Array<ServiceEndpointDefinition>`

An array of objects that each specify the `name` and `url` of one subgraph in your federated graph. On startup, `IntrospectAndCompose` uses this array to obtain your subgraph schemas via introspection and compose a supergraph schema.

The `name` field is a string that should be treated as a subgraph's unique identifier. It is used for query planning, logging, and reporting metrics to Apollo Studio.

> For Studio users, subgraph names **must:**

* Begin with a letter (capital or lowercase)
* Include only letters, numbers, underscores (\_), and hyphens (-)
* Have a maximum of 64 characters

###### `introspectionHeaders`

`Object | (service: ServiceEndpointDefinition) => (Promise<Object> | Object)`

An object (or an optionally async function *returning* an object)that contains the names and values of HTTP headers that the gateway includes *only* when making introspection requests to your subgraphs.

\*\*If you define a [`buildService`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-gateway.md#buildservice) function in your `ApolloGateway` config, \*\* specify these headers in that function instead of providing this option. This ensures that your `buildService` function doesn't inadvertently overwrite the values of any headers you provide here.

###### `pollIntervalInMs`

`number`

Specify this option to enable supergraph updates via subgraph polling. `IntrospectAndCompose` polls each subgraph at the given interval.

###### `subgraphHealthCheck`

`boolean`

> This option applies only to subgraphs that are configured for polling via the `pollIntervalInMs` option.
> If `true`, the gateway performs a health check on each subgraph before performing a supergraph update. Errors during health checks will result in skipping the supergraph update, but polling will continue. The health check is a simple GraphQL query (`query __ApolloServiceHealthCheck__ { __typename }`) to ensure that subgraphs are reachable and can successfully respond to GraphQL requests.

**This option is the `IntrospectAndCompose` equivalent of `ApolloGateway`'s `serviceHealthCheck` option. If you are using `IntrospectAndCompose`, enabling `serviceHealthCheck` on your `ApolloGateway` instance has no effect.**

###### `logger`

[`Logger`](https://github.com/apollographql/apollo-utils/tree/main/packages/logger)

An object to use for logging in place of `console`. If provided, this object must implement all methods of [the `Logger` interface](https://github.com/apollographql/apollo-utils/tree/main/packages/logger).

`IntrospectAndCompose` doesn't share the same logger as the `ApolloGateway` it's configured with. In most cases, you probably want to pass the same logger to both `ApolloGateway` and `IntrospectAndCompose`.
