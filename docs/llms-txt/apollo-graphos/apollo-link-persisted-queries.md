# Source: https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md

# PersistedQueryLink

`PersistedQueryLink` is a non-terminating link that enables the use of persisted queries, a technique that reduces bandwidth by sending query hashes instead of full query strings.

TypeScript

```
 import { PersistedQueryLink } from "@apollo/client/link/persisted-queries";
 import { sha256 } from "crypto-hash";

 const link = new PersistedQueryLink({
   sha256: (queryString) => sha256(queryString),
 });
```

Read the [Persisted queries](https://www.apollographql.com/docs/react/data/persisted-queries) guide to learn how to use persisted queries with Apollo Client.

## Constructor signature

```ts
constructor(
  options: PersistedQueryLink.Options
): PersistedQueryLink
```

#### `PersistedQueryLink` options

The `PersistedQueryLink` class takes a configuration object:

* `sha256`: a SHA-256 hashing function. Can be sync or async. Providing a SHA-256 hashing function is required, unless you're defining a fully custom hashing approach via `generateHash`.
* `generateHash`: an optional function that takes the query document and returns the hash. If provided this custom function will override the default hashing approach that uses the supplied `sha256` function. If not provided, the persisted queries link will use a fallback hashing approach leveraging the `sha256` function.
* `useGETForHashedQueries`: set to `true` to use the HTTP `GET` method when sending the hashed version of queries (but not for mutations). `GET` requests are not compatible with `@apollo/client/link/batch-http`.
  > If you want to use `GET` for non-mutation queries whether or not they are hashed, pass `useGETForQueries: true` option to `HttpLink` instead. If you want to use `GET` for all requests, pass `fetchOptions: {method: 'GET'}` to `HttpLink`.
* `disable`: a function which takes a [`PersistedQueryLink.DisableFunctionOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#persistedquerylinkdisablefunctionoptions) object and returns a boolean to disable any future persisted queries for that session. This defaults to disabling on `PersistedQueryNotSupported` error.
* `retry`: a function which takes a [`PersistedQueryLink.RetryFunctionOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#persistedquerylinkretryfunctionoptions) object and returns a boolean to retry the request with the full query text included. This defaults to `true` on `PersistedQueryNotSupported` or `PersistedQueryNotFound` errors.

## Types

### [`PersistedQueryLink.DisableFunctionOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#persistedquerylink.disablefunctionoptions)

Options passed to the `disable` function when a persisted query request fails.

Properties

Name / Type

Description

###### [`error`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#disablefunctionoptions-error)

`ErrorLike`

The error that occurred during the request.

###### [`meta`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#disablefunctionoptions-meta)

`PersistedQueryLink.ErrorMeta`

Metadata about the persisted query error.

###### [`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#disablefunctionoptions-operation)

`ApolloLink.Operation`

The GraphQL operation that failed.

###### [`result`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#disablefunctionoptions-result)

`FormattedExecutionResult`

The GraphQL result, if available.

### [`PersistedQueryLink.ErrorMeta`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#persistedquerylink.errormeta)

Metadata about persisted query errors extracted from the response.

Properties

Name / Type

Description

###### [`persistedQueryNotFound`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#errormeta-persistedquerynotfound)

`boolean`

Whether the server responded with a "PersistedQueryNotFound" error.

When `true`, indicates the server doesn't recognize the query hash and needs the full query text.

###### [`persistedQueryNotSupported`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#errormeta-persistedquerynotsupported)

`boolean`

Whether the server responded with a "PersistedQueryNotSupported" error.

When `true`, indicates the server doesn't support persisted queries or has disabled them for this client.

### [`PersistedQueryLink.GenerateHashFunction`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#persistedquerylink.generatehashfunction)

A function that generates a hash for a GraphQL document.

#### [Example](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashfunction-example)

TypeScript

```
 import { print } from "graphql";
 import { sha256 } from "crypto-hash";

 const link = new PersistedQueryLink({
   generateHash: async (document) => {
     const query = print(document);
     return sha256(query);
   },
 });
```

#### [Signature](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashfunction-signature)

TypeScript

```
GenerateHashFunction(
  document: DocumentNode
): string | PromiseLike<string>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashfunction-parameters)

Name / Type

Description

[`document`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashfunction-parameters-document)\
`DocumentNode`

The GraphQL document to hash

### [`PersistedQueryLink.GenerateHashOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#persistedquerylink.generatehashoptions)

Options for using custom hash generation with persisted queries.

Use this configuration when you need custom control over how query hashes are generated (e.g., using pre-computed hashes).

Properties

Name / Type

Description

###### [`disable`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashoptions-disable)

`(options: PersistedQueryLink.DisableFunctionOptions) => boolean`

A function to disable persisted queries for the current session.

This function is called when an error occurs and determines whether to disable persisted queries for all future requests in this session.

###### [`generateHash`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashoptions-generatehash)

`PersistedQueryLink.GenerateHashFunction`

A custom function for generating query hashes. This function receives the GraphQL document and should return a hash. Useful for custom hashing strategies or when using build-time generated hashes.

###### [`retry`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashoptions-retry)

`(options: PersistedQueryLink.RetryFunctionOptions) => boolean`

A function to determine whether to retry a request with the full query.

When a persisted query fails, this function determines whether to retry the request with the full query text included.

###### [`sha256`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashoptions-sha256)

`never`

###### [`useGETForHashedQueries`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#generatehashoptions-usegetforhashedqueries)

`boolean`

Whether to use HTTP GET for hashed queries (excluding mutations).

**note**

If you want to use `GET` for non-mutation queries whether or not they are hashed, pass `useGETForQueries: true` option to `HttpLink` instead. If you want to use GET for all requests, pass `fetchOptions: {method: 'GET'}` to `HttpLink`.

### [`PersistedQueryLink.RetryFunctionOptions`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#persistedquerylink.retryfunctionoptions)

Options passed to the `retry` function when a persisted query request fails.

Properties

Name / Type

Description

###### [`error`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#retryfunctionoptions-error)

`ErrorLike`

The error that occurred during the request.

###### [`meta`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#retryfunctionoptions-meta)

`PersistedQueryLink.ErrorMeta`

Metadata about the persisted query error.

###### [`operation`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#retryfunctionoptions-operation)

`ApolloLink.Operation`

The GraphQL operation that failed.

###### [`result`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#retryfunctionoptions-result)

`FormattedExecutionResult`

The GraphQL result, if available.

### [`PersistedQueryLink.SHA256Options`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#persistedquerylink.sha256options)

Options for using SHA-256 hashing with persisted queries.

Use this configuration when you want the link to handle query printing and hashing using a SHA-256 function.

Properties

Name / Type

Description

###### [`disable`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#sha256options-disable)

`(options: PersistedQueryLink.DisableFunctionOptions) => boolean`

A function to disable persisted queries for the current session.

This function is called when an error occurs and determines whether to disable persisted queries for all future requests in this session.

###### [`generateHash`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#sha256options-generatehash)

`never`

###### [`retry`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#sha256options-retry)

`(options: PersistedQueryLink.RetryFunctionOptions) => boolean`

A function to determine whether to retry a request with the full query.

When a persisted query fails, this function determines whether to retry the request with the full query text included.

###### [`sha256`](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#sha256options-sha256)

`PersistedQueryLink.SHA256Function`

The SHA-256 hash function to use for hashing queries. This function receives the printed query string and should return a SHA-256 hash. Can be synchronous or asynchronous.

###### [`useGETForHashedQueries`*(optional)*](https://www.apollographql.com/docs/react/api/link/apollo-link-persisted-queries.md#sha256options-usegetforhashedqueries)

`boolean`

Whether to use HTTP GET for hashed queries (excluding mutations).

**note**

If you want to use `GET` for non-mutation queries whether or not they are hashed, pass `useGETForQueries: true` option to `HttpLink` instead. If you want to use GET for all requests, pass `fetchOptions: {method: 'GET'}` to `HttpLink`.
