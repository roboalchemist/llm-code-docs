# Source: https://www.apollographql.com/docs/react/api/core/ApolloClient.md

# class ApolloClient

The `ApolloClient` class encapsulates Apollo's core client-side API. It backs all available view-layer integrations (React, iOS, and so on).

## The `ApolloClient` constructor

Constructs an instance of `ApolloClient`.

Takes an `ApolloClientOptions` parameter that supports the [fields listed below](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#apolloclientoptions).

Returns an initialized `ApolloClient` object.

#### Example

JavaScript

```
 import { ApolloClient, InMemoryCache, HttpLink } from "@apollo/client";

 const cache = new InMemoryCache();
 const link = new HttpLink({ uri: "http://localhost:4000/" });

 const client = new ApolloClient({
   // Provide required constructor fields
   cache: cache,
   link: link,

   // Provide some optional constructor fields
   clientAwareness: {
     name: "react-web-client",
     version: "1.3",
   },
   queryDeduplication: false,
 });
```

For more information on the `defaultOptions` object, see the [Default Options](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#defaultoptions) section below.

## Functions

### [`watchQuery`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchquery)

This watches the cache store of the query according to the options specified and returns an `ObservableQuery`. We can subscribe to this `ObservableQuery` and receive updated results through an observer when the cache store changes.

Note that this method is not an implementation of GraphQL subscriptions. Rather, it uses Apollo's store in order to reactively deliver updates to your query results.

For example, suppose you call watchQuery on a GraphQL query that fetches a person's first and last name and this person has a particular object identifier, provided by `cache.identify`. Later, a different query fetches that same person's first and last name and the first name has now changed. Then, any observers associated with the results of the first query will be updated with a new result object.

Note that if the cache does not change, the subscriber will *not* be notified.

See [here](https://medium.com/apollo-stack/the-concepts-of-graphql-bc68bd819be3#.3mb0cbcmc) for a description of store reactivity.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchquery-signature)

TypeScript

```
watchQuery<TData, TVariables>(
  options: ApolloClient.WatchQueryOptions<TData, TVariables>
): ObservableQuery<TData, TVariables>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchquery-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchquery-parameters-options)\
`ApolloClient.WatchQueryOptions<TData, TVariables>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchquery-result)

```
ObservableQuery<TData, TVariables>
```

### [`query`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#query)

This resolves a single query according to the options specified and returns a `Promise` which is either resolved with the resulting data or rejected with an error.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#query-signature)

TypeScript

```
query<TData, TVariables>(
  options: ApolloClient.QueryOptions<TData, TVariables>
): Promise<ApolloClient.QueryResult<MaybeMasked<TData>>>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#query-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#query-parameters-options)\
`ApolloClient.QueryOptions<TData, TVariables>`

An object of type `QueryOptions` that allows us to describe how this query should be treated e.g. whether it should hit the server at all or just resolve from the cache, etc.

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#query-result)

```
Promise<ApolloClient.QueryResult<MaybeMasked<TData>>>
```

Show/hide child attributes

###### [`data`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#query-result-data)

`MaybeMasked<TData> | undefined`

An object containing the result of your GraphQL query after it completes.

This value might be `undefined` if a query results in one or more errors (depending on the query's `errorPolicy`).

###### [`error`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#query-result-error)

`ErrorLike`

A single ErrorLike object describing the error that occurred during the latest query execution.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

### [`mutate`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#mutate)

This resolves a single mutation according to the options specified and returns a Promise which is either resolved with the resulting data or rejected with an error. In some cases both `data` and `errors` might be undefined, for example when `errorPolicy` is set to `'ignore'`.

It takes options as an object with the following keys and values:

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#mutate-signature)

TypeScript

```
mutate<TData, TVariables, TCache>(
  options: ApolloClient.MutateOptions<TData, TVariables, TCache>
): Promise<ApolloClient.MutateResult<MaybeMasked<TData>>>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#mutate-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#mutate-parameters-options)\
`ApolloClient.MutateOptions<TData, TVariables, TCache>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#mutate-result)

```
Promise<ApolloClient.MutateResult<MaybeMasked<TData>>>
```

Show/hide child attributes

###### [`data`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#mutate-result-data)

`MaybeMasked<TData> | undefined`

The data returned from your mutation. Can be `undefined` if the `errorPolicy` is `all` or `ignore` and the server returns a GraphQL response with `errors` but not `data` or a network error is returned.

###### [`error`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#mutate-result-error)

`ErrorLike`

If the mutation produces one or more errors, this object contains either an array of `graphQLErrors` or a single `networkError`. Otherwise, this value is `undefined`.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

###### [`extensions`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#mutate-result-extensions)

`Record<string, unknown>`

Custom extensions returned from the GraphQL server

### [`subscribe`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#subscribe)

This subscribes to a graphql subscription according to the options specified and returns an `Observable` which either emits received data or an error.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#subscribe-signature)

TypeScript

```
subscribe<TData, TVariables>(
  options: ApolloClient.SubscribeOptions<TData, TVariables>
): SubscriptionObservable<ApolloClient.SubscribeResult<MaybeMasked<TData>>>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#subscribe-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#subscribe-parameters-options)\
`ApolloClient.SubscribeOptions<TData, TVariables>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#subscribe-result)

```
SubscriptionObservable<ApolloClient.SubscribeResult<MaybeMasked<TData>>>
```

### [`readQuery`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readquery)

Tries to read some data from the store in the shape of the provided GraphQL query without making a network request. This method will start at the root query. To start at a specific id returned by `cache.identify` use `readFragment`.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readquery-signature)

TypeScript

```
readQuery<TData, TVariables>(
  options: ApolloClient.ReadQueryOptions<TData, TVariables>
): Unmasked<TData> | null
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readquery-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readquery-parameters-options)\
`ApolloClient.ReadQueryOptions<TData, TVariables>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readquery-result)

```
Unmasked<TData> | null
```

### [`readFragment`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readfragment)

Tries to read some data from the store in the shape of the provided GraphQL fragment without making a network request. This method will read a GraphQL fragment from any arbitrary id that is currently cached, unlike `readQuery` which will only read from the root query.

You must pass in a GraphQL document with a single fragment or a document with multiple fragments that represent what you are reading. If you pass in a document with multiple fragments then you must also specify a `fragmentName`.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readfragment-signature)

TypeScript

```
readFragment<TData, TVariables>(
  options: ApolloClient.ReadFragmentOptions<TData, TVariables>
): Unmasked<TData> | null
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readfragment-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readfragment-parameters-options)\
`ApolloClient.ReadFragmentOptions<TData, TVariables>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#readfragment-result)

```
Unmasked<TData> | null
```

### [`writeQuery`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writequery)

Writes some data in the shape of the provided GraphQL query directly to the store. This method will start at the root query. To start at a specific id returned by `cache.identify` then use `writeFragment`.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writequery-signature)

TypeScript

```
writeQuery<TData, TVariables>(
  options: ApolloClient.WriteQueryOptions<TData, TVariables>
): Reference | undefined
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writequery-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writequery-parameters-options)\
`ApolloClient.WriteQueryOptions<TData, TVariables>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writequery-result)

```
Reference | undefined
```

### [`writeFragment`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writefragment)

Writes some data in the shape of the provided GraphQL fragment directly to the store. This method will write to a GraphQL fragment from any arbitrary id that is currently cached, unlike `writeQuery` which will only write from the root query.

You must pass in a GraphQL document with a single fragment or a document with multiple fragments that represent what you are writing. If you pass in a document with multiple fragments then you must also specify a `fragmentName`.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writefragment-signature)

TypeScript

```
writeFragment<TData, TVariables>(
  options: ApolloClient.WriteFragmentOptions<TData, TVariables>
): Reference | undefined
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writefragment-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writefragment-parameters-options)\
`ApolloClient.WriteFragmentOptions<TData, TVariables>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#writefragment-result)

```
Reference | undefined
```

### [`watchFragment`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchfragment)Requires ≥ 3.10.0

Watches the cache store of the fragment according to the options specified and returns an `Observable`. We can subscribe to this `Observable` and receive updated results through an observer when the cache store changes.

You must pass in a GraphQL document with a single fragment or a document with multiple fragments that represent what you are reading. If you pass in a document with multiple fragments then you must also specify a `fragmentName`.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchfragment-signature)

TypeScript

```
watchFragment<TData, TVariables>(
  options: ApolloClient.WatchFragmentOptions<TData, TVariables> & {
        from: Array<ApolloCache.FromOptionValue<TData>>;
    }
): ApolloClient.ObservableFragment<Array<TData>>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchfragment-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchfragment-parameters-options)\
`ApolloClient.WatchFragmentOptions<TData, TVariables> & { from: Array<ApolloCache.FromOptionValue<TData>>; }`

An object of type `WatchFragmentOptions` that allows the cache to identify the fragment and optionally specify whether to react to optimistic updates.

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchfragment-result)

```
ApolloClient.ObservableFragment<Array<TData>>
```

Show/hide child attributes

(Warning: some properties might be missing from the table due to complex inheritance!)

###### [`getCurrentResult`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#watchfragment-result-getcurrentresult)

`() => ApolloClient.WatchFragmentResult<Array<TData>>`

Return the current result for the fragment.

### [`resetStore`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#resetstore)

Resets your entire store by clearing out your cache and then re-executing all of your active queries. This makes it so that you may guarantee that there is no data left in your store from a time before you called this method.

`resetStore()` is useful when your user just logged out. You’ve removed the user session, and you now want to make sure that any references to data you might have fetched while the user session was active is gone.

It is important to remember that `resetStore()` *will* refetch any active queries. This means that any components that might be mounted will execute their queries again using your network interface. If you do not want to re-execute any queries then you should make sure to stop watching any active queries.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#resetstore-signature)

TypeScript

```
resetStore(): Promise<ApolloClient.QueryResult<any>[] | null>
```

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#resetstore-result)

```
Promise<ApolloClient.QueryResult<any>[] | null>
```

### [`onResetStore`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onresetstore)

Allows callbacks to be registered that are executed when the store is reset. `onResetStore` returns an unsubscribe function that can be used to remove registered callbacks.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onresetstore-signature)

TypeScript

```
onResetStore(
  cb: () => Promise<any>
): () => void
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onresetstore-parameters)

Name / Type

Description

[`cb`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onresetstore-parameters-cb)\
`() => Promise<any>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onresetstore-result)

```
() => void
```

### [`clearStore`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#clearstore)

Remove all data from the store. Unlike `resetStore`, `clearStore` will not refetch any active queries.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#clearstore-signature)

TypeScript

```
clearStore(): Promise<any[]>
```

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#clearstore-result)

```
Promise<any[]>
```

### [`onClearStore`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onclearstore)

Allows callbacks to be registered that are executed when the store is cleared. `onClearStore` returns an unsubscribe function that can be used to remove registered callbacks.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onclearstore-signature)

TypeScript

```
onClearStore(
  cb: () => Promise<any>
): () => void
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onclearstore-parameters)

Name / Type

Description

[`cb`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onclearstore-parameters-cb)\
`() => Promise<any>`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#onclearstore-result)

```
() => void
```

### [`stop`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#stop)

Call this method to terminate any active client processes, making it safe to dispose of this `ApolloClient` instance.

This method performs aggressive cleanup to prevent memory leaks:

* Unsubscribes all active `ObservableQuery` instances by emitting a `completed` event

* Rejects all currently running queries with "QueryManager stopped while query was in flight"

* Removes all queryRefs from the suspense cache

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#stop-signature)

TypeScript

```
stop(): void
```

### [`refetchObservableQueries`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchobservablequeries)

Refetches all of your active queries.

`refetchObservableQueries()` is useful if you want to bring the client back to proper state in case of a network outage

It is important to remember that `refetchObservableQueries()` *will* refetch any active queries. This means that any components that might be mounted will execute their queries again using your network interface. If you do not want to re-execute any queries then you should make sure to stop watching any active queries. Takes optional parameter `includeStandby` which will include queries in standby-mode when refetching.

Note: `cache-only` queries are not refetched by this function.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchobservablequeries-signature)

TypeScript

```
refetchObservableQueries(
  includeStandby?: boolean
): Promise<ApolloClient.QueryResult<any>[]>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchobservablequeries-parameters)

Name / Type

Description

[`includeStandby`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchobservablequeries-parameters-includestandby)\
`boolean`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchobservablequeries-result)

```
Promise<ApolloClient.QueryResult<any>[]>
```

### [`refetchQueries`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries)

Refetches specified active queries. Similar to "refetchObservableQueries()" but with a specific list of queries.

`refetchQueries()` is useful for use cases to imperatively refresh a selection of queries.

It is important to remember that `refetchQueries()` *will* refetch specified active queries. This means that any components that might be mounted will execute their queries again using your network interface. If you do not want to re-execute any queries then you should make sure to stop watching any active queries.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-signature)

TypeScript

```
refetchQueries<TCache, TResult>(
  options: ApolloClient.RefetchQueriesOptions<TCache, TResult>
): ApolloClient.RefetchQueriesResult<TResult>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-parameters)

Name / Type

Description

[`options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-parameters-options)\
`ApolloClient.RefetchQueriesOptions<TCache, TResult>`

Show/hide child attributes

###### [`include`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-parameters-options-include)

`RefetchQueriesInclude`

Optional array specifying queries to refetch. Each element can be either a query's string name or a `DocumentNode` object.

Pass `"active"` as a shorthand to refetch all active queries, or `"all"` to refetch all active and inactive queries.

Analogous to the [`options.refetchQueries`](https://www.apollographql.com/docs/react/data/mutations.md#options) array for mutations.

###### [`onQueryUpdated`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-parameters-options-onqueryupdated)

`OnQueryUpdated<TResult> | null`

Optional callback function that's called once for each `ObservableQuery` that's either affected by `options.updateCache` or listed in `options.include` (or both).

If `onQueryUpdated` is not provided, the default implementation returns the result of calling `observableQuery.refetch()`. When `onQueryUpdated` is provided, it can dynamically decide whether (and how) each query should be refetched.

Returning `false` from `onQueryUpdated` prevents the associated query from being refetched.

###### [`optimistic`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-parameters-options-optimistic)

`boolean`

If `true`, the `options.updateCache` function is executed on a temporary optimistic layer of `InMemoryCache`, so its modifications can be discarded from the cache after observing which fields it invalidated.

Defaults to `false`, meaning `options.updateCache` updates the cache in a lasting way.

###### [`updateCache`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-parameters-options-updatecache)

`(cache: TCache) => void`

Optional function that updates cached fields to trigger refetches of queries that include those fields.

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-result)

```
ApolloClient.RefetchQueriesResult<TResult>
```

Show/hide child attributes

(Warning: some properties might be missing from the table due to complex inheritance!)

###### [`queries`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-result-queries)

`ObservableQuery<any>[]`

An array of ObservableQuery objects corresponding 1:1 to TResult values in the results arrays (both the `result` property and the resolved value).

###### [`results`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#refetchqueries-result-results)

`InternalRefetchQueriesResult<TResult>[]`

An array of results that were either returned by `onQueryUpdated`, or provided by default in the absence of `onQueryUpdated`, including pending promises.

If `onQueryUpdated` returns `false` for a given query, no result is provided for that query.

If `onQueryUpdated` returns `true`, the resulting `Promise<ApolloQueryResult<any>>` is included in the `results` array instead of `true`.

### [`getObservableQueries`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#getobservablequeries)

Get all currently active `ObservableQuery` objects, in a `Set`.

An "active" query is one that has observers and a `fetchPolicy` other than "standby" or "cache-only".

You can include all `ObservableQuery` objects (including the inactive ones) by passing "all" instead of "active", or you can include just a subset of active queries by passing an array of query names or DocumentNode objects.

Note: This method only returns queries that have active subscribers. Queries without subscribers are not tracked by the client.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#getobservablequeries-signature)

TypeScript

```
getObservableQueries(
  include?: RefetchQueriesInclude
): Set<ObservableQuery<any>>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#getobservablequeries-parameters)

Name / Type

Description

[`include`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#getobservablequeries-parameters-include)\
`RefetchQueriesInclude`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#getobservablequeries-result)

```
Set<ObservableQuery<any>>
```

### [`extract`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#extract)

Exposes the cache's complete state, in a serializable format for later restoration.

This can be useful for debugging in order to inspect the full state of the cache.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#extract-signature)

TypeScript

```
extract(
  optimistic?: boolean
): unknown
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#extract-parameters)

Name / Type

Description

[`optimistic`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#extract-parameters-optimistic)\
`boolean`

Determines whether the result contains data from the optimistic layer

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#extract-result)

```
unknown
```

### [`restore`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#restore)

Replaces existing state in the cache (if any) with the values expressed by `serializedState`.

Called when hydrating a cache (server side rendering, or offline storage), and also (potentially) during hot reloads.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#restore-signature)

TypeScript

```
restore(
  serializedState: unknown
): ApolloCache
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#restore-parameters)

Name / Type

Description

[`serializedState`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#restore-parameters-serializedstate)\
`unknown`

#### [Result](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#restore-result)

```
ApolloCache
```

### [`setLink`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#setlink)

Define a new ApolloLink (or link chain) that Apollo Client will use.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#setlink-signature)

TypeScript

```
setLink(
  newLink: ApolloLink
): void
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#setlink-parameters)

Name / Type

Description

[`newLink`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#setlink-parameters-newlink)\
`ApolloLink`

## Types

### [`ApolloClient.Options`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#apolloclient.options)

Properties

Name / Type

Description

###### [`cache`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-cache)

`ApolloCache`

The cache that Apollo Client should use to store query results locally. The recommended cache is `InMemoryCache`, which is provided by the `@apollo/client` package.

For more information, see [Configuring the cache](https://www.apollographql.com/docs/react/caching/cache-configuration.md).

###### [`link`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-link)

`ApolloLink`

An `ApolloLink` instance to serve as Apollo Client's network layer. For more information, see [Advanced HTTP networking](https://www.apollographql.com/docs/react/networking/advanced-http-networking.md).

###### [`defaultOptions`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-defaultoptions)

`ApolloClient.DefaultOptions`

Provide this object to set application-wide default values for options you can provide to the `watchQuery`, `query`, and `mutate` functions. See below for an example object.

See this [example object](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#example-defaultoptions-object).

Other

###### [`assumeImmutableResults`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-assumeimmutableresults)

`boolean`

If `true`, Apollo Client will assume results read from the cache are never mutated by application code, which enables substantial performance optimizations.

###### [`clientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-clientawareness)

`ClientAwarenessLink.ClientAwarenessOptions`

###### [`dataMasking`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-datamasking)

`boolean`

Determines if data masking is enabled for the client.

###### [`defaultContext`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-defaultcontext)

`Partial<DefaultContext>`

###### [`devtools`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-devtools)Requires ≥ 3.11.0

`ApolloClient.DevtoolsOptions`

Configuration used by the [Apollo Client Devtools extension](https://www.apollographql.com/docs/react/development-testing/developer-tooling.md#apollo-client-devtools) for this client.

###### [`documentTransform`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-documenttransform)

`DocumentTransform`

###### [`enhancedClientAwareness`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-enhancedclientawareness)

`ClientAwarenessLink.EnhancedClientAwarenessOptions`

###### [`experiments`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-experiments)

`ApolloClient.Experiment[]`

Allows passing in "experiments", experimental features that might one day become part of Apollo Client's core functionality. Keep in mind that these features might change the core of Apollo Client. Do not pass in experiments that are not provided by Apollo.

###### [`incrementalHandler`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-incrementalhandler)

`Incremental.Handler<any>`

Determines the strategy used to parse incremental chunks from `@defer` queries.

###### [`localState`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-localstate)

`LocalState`

###### [`queryDeduplication`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-querydeduplication)

`boolean`

If `false`, Apollo Client sends every created query to the server, even if a *completely* identical query (identical in terms of query string, variable values, and operationName) is already in flight.

###### [`ssrForceFetchDelay`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-ssrforcefetchdelay)

`number`

The time interval (in milliseconds) before Apollo Client force-fetches queries after a server-side render.

###### [`ssrMode`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#options-ssrmode)

`boolean`

When using Apollo Client for [server-side rendering](https://www.apollographql.com/docs/react/performance/server-side-rendering.md), set this to `true` so that the [`getDataFromTree` function](https://www.apollographql.com/react/ssr/#getdatafromtree) can work effectively.

### [`ApolloClient.DefaultOptions`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#apolloclient.defaultoptions)

Properties

Name / Type

Description

###### [`mutate`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#defaultoptions-mutate)

`Partial<ApolloClient.MutateOptions<any, any, any>>`

###### [`query`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#defaultoptions-query)

`Partial<ApolloClient.QueryOptions<any, any>>`

###### [`watchQuery`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#defaultoptions-watchquery)

`Partial<ApolloClient.WatchQueryOptions<any, any>>`

##### Example `defaultOptions` object

```js
const defaultOptions = {
  watchQuery: {
    fetchPolicy: "cache-and-network",
    errorPolicy: "ignore",
  },
  query: {
    fetchPolicy: "network-only",
    errorPolicy: "all",
  },
  mutate: {
    errorPolicy: "all",
  },
};
```

You can override any default option you specify in this object by providing a
different value for the same option in individual function calls.

> **Note:** The `useQuery` hook uses Apollo Client's `watchQuery` function. To set `defaultOptions` when using the `useQuery` hook, make sure to set them under the `defaultOptions.watchQuery` property.

### [`ApolloClient.DevtoolsOptions`](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#apolloclient.devtoolsoptions)

Properties

Name / Type

Description

###### [`enabled`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#devtoolsoptions-enabled)

`boolean`

If `true`, the [Apollo Client Devtools](https://www.apollographql.com/docs/react/development-testing/developer-tooling.md#apollo-client-devtools) browser extension can connect to this `ApolloClient` instance.

The default value is `false` in production and `true` in development if there is a `window` object.

###### [`name`*(optional)*](https://www.apollographql.com/docs/react/api/core/ApolloClient.md#devtoolsoptions-name)

`string`

Optional name for this `ApolloClient` instance in the devtools. This is useful when you instantiate multiple clients and want to be able to identify them by name.
