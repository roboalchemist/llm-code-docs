# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md

# BatchHttpLink

`BatchHttpLink` is a terminating link that batches array of individual GraphQL operations into a single HTTP request that's sent to a single GraphQL endpoint. It combines the functionality of `BaseBatchHttpLink` and `ClientAwarenessLink` into a single link.

TypeScript

```
 import { BatchHttpLink } from "@apollo/client/link/batch-http";

 const link = new BatchHttpLink({
   uri: "http://localhost:4000/graphql",
   batchMax: 5, // No more than 5 operations per batch
   batchInterval: 20, // Wait no more than 20ms after first batched operation
 });
```

If you use `BatchHttpLink` instead of `HttpLink` as your terminating link, Apollo Client automatically batches executed GraphQL operations and transmits them to your server according to the batching options you provide.

## Constructor signature

```ts
constructor(
  options: BatchHttpLink.Options & ClientAwarenessLink.Options = {}
): BatchHttpLink
```

## Context

The batch HTTP link currently uses the context in two different ways, per batch and per query. The context fields below are used per batch and taken from the first operation in the batch.

| Option         | Description                                                              |
| -------------- | ------------------------------------------------------------------------ |
| `headers`      | An object representing values to be sent as headers on the request       |
| `credentials`  | A string representing the credentials policy you want for the fetch call |
| `uri`          | A string of the endpoint you want to fetch from                          |
| `fetchOptions` | Any overrides of the fetch options argument to pass to the fetch call    |

For each query, the `http` field is used to modify each individual query in the batch, such as persisted queries (see below).

## Operation results

After your GraphQL endpoint successfully responds with the result of an operation, `BatchHttpLink` sets the `Response` object as the `response` field of the operation `context`. This enables each previous link in your link chain to interact with the response.

## Custom fetching

See [Customizing `fetch`](https://www.apollographql.com/docs/react/api/link/apollo-link-http/#customizing-fetch).

## Types

### [`BatchHttpLink.Options`](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#batchhttplink.options)

Options provided to the `BatchHttpLink` constructor.

Properties

Name / Type

Description

###### [`uri`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-uri)

`string | BaseHttpLink.UriFunction`

The URL of the GraphQL endpoint to send requests to. Can also be a function that accepts an `ApolloLink.Operation` object and returns the string URL to use for that operation.

###### [`headers`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-headers)

`Record<string, string>`

An object representing headers to include in every HTTP request.

JSON

```
 {
   "Authorization": "Bearer 1234"
 }
```

###### [`credentials`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-credentials)

`RequestCredentials`

The credentials policy to use for each `fetch` call.

###### [`fetchOptions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-fetchoptions)

`RequestInit`

Any overrides of the fetch options argument to pass to the fetch call.

An object containing options to use for each call to `fetch`. If a particular option is not included in this object, the default value of that option is used.

**note**

If you set `fetchOptions.method` to `GET`, `HttpLink` follows [standard GraphQL HTTP GET encoding](http://graphql.org/learn/serving-over-http/#get-request).

See [available options](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch#Parameters)

Other

###### [`batchDebounce`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-batchdebounce)

`boolean`

"batchInterval" is a throttling behavior by default, if you instead wish to debounce outbound requests, set "batchDebounce" to true. More useful for mutations than queries.

###### [`batchInterval`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-batchinterval)

`number`

The interval at which to batch, in milliseconds.

###### [`batchKey`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-batchkey)

`(operation: ApolloLink.Operation) => string`

Creates the key for a batch

###### [`batchMax`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-batchmax)

`number`

The maximum number of operations to include in a single batch.

###### [`clientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-clientawareness)

`ClientAwarenessLink.ClientAwarenessOptions`

Configures the "client awareness" feature. This feature allows you to identify distinct applications in Apollo Studio and Apollo Server logs (and other monitoring or analytics tools) by adding information about the your application to outgoing requests.

###### [`enhancedClientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-enhancedclientawareness)

`ClientAwarenessLink.EnhancedClientAwarenessOptions`

Configures the "enhanced client awareness" feature. This feature allows you to identify the version of the Apollo Client library used in your application in Apollo Studio (and other monitoring or analytics tools) by adding information about the Apollo Client library to outgoing requests.

###### [`fetch`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-fetch)

`typeof fetch`

A function to use instead of calling the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) directly when sending HTTP requests to your GraphQL endpoint. The function must conform to the signature of `fetch`.

By default, the Fetch API is used unless it isn't available in your runtime environment.

See [Customizing `fetch`](https://apollographql.com/docs/react/api/link/introduction#customizing-fetch).

###### [`includeExtensions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-includeextensions)

`boolean`

If `true`, includes the `extensions` field in operations sent to your GraphQL endpoint.

###### [`includeUnusedVariables`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-includeunusedvariables)

`boolean`

If `true`, unused variables from the operation will not be stripped from the request and will instead be sent to the GraphQL endpoint.

Read more...

Unused variables are likely to trigger server-side validation errors, per [https://spec.graphql.org/draft/#sec-All-Variables-Used](https://spec.graphql.org/draft/#sec-All-Variables-Used). `includeUnusedVariables` can be useful if your server deviates from the GraphQL specification by not strictly enforcing that rule.

###### [`preserveHeaderCase`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-preserveheadercase)

`boolean`

If `true`, header names won't be automatically normalized to lowercase. This allows for non-http-spec-compliant servers that might expect capitalized header names.

###### [`print`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#options-print)

`BaseHttpLink.Printer`

A function to use when transforming a GraphQL document into a string. It accepts an `ASTNode` (typically a `DocumentNode`) and the original `print` function as arguments, and is expected to return a string. This option enables you to, for example, use `stripIgnoredCharacters` to remove whitespace from queries.

By default the [GraphQL `print` function](https://graphql.org/graphql-js/language/#print) is used.

TypeScript

```
 import { stripIgnoredCharacters } from "graphql";

 const httpLink = new HttpLink({
   uri: "/graphql",
   print: (ast, originalPrint) => stripIgnoredCharacters(originalPrint(ast)),
 });
```

### [`BatchHttpLink.ContextOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#batchhttplink.contextoptions)

Options passed to `BatchHttpLink` through [request context](https://apollographql.com/docs/react/api/link/introduction#managing-context). Previous non-terminating links in the link chain also can set these values to customize the behavior of `BatchHttpLink` for each operation.

**note**

Some of these values can also be provided to the `BatchHttpLink` constructor. If a value is provided to both, the value in `context` takes precedence.

Properties

Name / Type

Description

###### [`clientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#contextoptions-clientawareness)

`ClientAwarenessLink.ClientAwarenessOptions`

Configures the "client awareness" feature. This feature allows you to identify distinct applications in Apollo Studio and Apollo Server logs (and other monitoring or analytics tools) by adding information about the your application to outgoing requests.

###### [`credentials`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#contextoptions-credentials)

`RequestCredentials`

The credentials policy to use for each `fetch` call.

###### [`fetchOptions`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#contextoptions-fetchoptions)

`RequestInit`

Any overrides of the fetch options argument to pass to the fetch call.

An object containing options to use for each call to `fetch`. If a particular option is not included in this object, the default value of that option is used.

**note**

If you set `fetchOptions.method` to `GET`, `HttpLink` follows [standard GraphQL HTTP GET encoding](http://graphql.org/learn/serving-over-http/#get-request).

See [available options](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch#Parameters)

###### [`headers`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#contextoptions-headers)

`Record<string, string>`

An object representing headers to include in every HTTP request.

JSON

```
 {
   "Authorization": "Bearer 1234"
 }
```

###### [`http`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#contextoptions-http)

`BaseHttpLink.HttpOptions`

An object that configures advanced functionality, such as support for persisted queries.

###### [`uri`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-batch-http.md#contextoptions-uri)

`string | BaseHttpLink.UriFunction`

The URL of the GraphQL endpoint to send requests to. Can also be a function that accepts an `ApolloLink.Operation` object and returns the string URL to use for that operation.
