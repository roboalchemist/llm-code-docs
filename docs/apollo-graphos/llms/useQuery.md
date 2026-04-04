# Source: https://www.apollographql.com/docs/react/api/react/useQuery.md

# useQuery

## [`useQuery`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery)

A hook for executing queries in an Apollo application.

To run a query within a React component, call `useQuery` and pass it a GraphQL query document.

When your component renders, `useQuery` returns an object from Apollo Client that contains `loading`, `error`, `dataState`, and `data` properties you can use to render your UI.

> Refer to the [Queries](https://www.apollographql.com/docs/react/data/queries.md) section for a more in-depth overview of `useQuery`.

### [Example](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-example)

JavaScript

```
 import { gql } from "@apollo/client";
 import { useQuery } from "@apollo/client/react";
 
 const GET_GREETING = gql`
   query GetGreeting($language: String!) {
     greeting(language: $language) {
       message
     }
   }
 `;
 
 function Hello() {
   const { loading, error, data } = useQuery(GET_GREETING, {
     variables: { language: "english" },
   });
   if (loading) return <p>Loading ...</p>;
   return <h1>Hello {data.greeting.message}!</h1>;
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-signature)

TypeScript

```
useQuery<TData, TVariables>(
  query: DocumentNode | TypedDocumentNode<TData, TVariables>,
  options: useQuery.Options<TData, TVariables>
): useQuery.Result<TData, TVariables>
```

### [Parameters](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters)

Name / Type

Description

[`query`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-query)\
`DocumentNode | TypedDocumentNode<TData, TVariables>`

A GraphQL query document parsed into an AST by `gql`.

[`options`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options)\
`useQuery.Options<TData, TVariables>`

Options to control how the query is executed.

Show/hide child attributes

Operation options

###### [`client`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-client)

`ApolloClient`

The instance of `ApolloClient` to use to execute the query.

By default, the instance that's passed down via context is used, but you can provide a different instance here.

###### [`errorPolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-errorpolicy)

`ErrorPolicy`

Specifies how the query handles a response that returns both GraphQL errors and partial results.

For details, see [GraphQL error policies](https://www.apollographql.com/docs/react/data/error-handling.md#graphql-error-policies).

The default value is `none`, meaning that the query result includes error details but not partial results.

###### [`skip`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-skip)

`boolean`

If true, the query is not executed.

The default value is `false`.

###### [`variables`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-variables)

`TVariables`

An object containing all of the GraphQL variables your query requires to execute.

Each key in the object corresponds to a variable name, and that key's value corresponds to the variable value.

Networking options

###### [`context`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-context)

`DefaultContext`

If you're using [Apollo Link](https://www.apollographql.com/docs/react/api/link/introduction.md), this object is the initial value of the `context` object that's passed along your link chain.

###### [`notifyOnNetworkStatusChange`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-notifyonnetworkstatuschange)

`boolean`

If `true`, the in-progress query's associated component re-renders whenever the network status changes or a network error occurs.

The default value is `true`.

###### [`pollInterval`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-pollinterval)

`number`

Specifies the interval (in milliseconds) at which the query polls for updated results.

The default value is `0` (no polling).

###### [`skipPollAttempt`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-skippollattempt)

`() => boolean`

A callback function that's called whenever a refetch attempt occurs while polling. If the function returns `true`, the refetch is skipped and not reattempted until the next poll interval.

###### [`ssr`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-ssr)

`boolean`

Pass `false` to skip executing the query during [server-side rendering](https://www.apollographql.com/docs/react/performance/server-side-rendering.md).

Caching options

###### [`fetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-fetchpolicy)

`WatchQueryFetchPolicy`

Specifies how the query interacts with the Apollo Client cache during execution (for example, whether it checks the cache for results before sending a request to the server).

For details, see [Setting a fetch policy](https://www.apollographql.com/docs/react/data/queries.md#setting-a-fetch-policy).

The default value is `cache-first`.

###### [`initialFetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-initialfetchpolicy)

`WatchQueryFetchPolicy`

Defaults to the initial value of options.fetchPolicy, but can be explicitly configured to specify the WatchQueryFetchPolicy to revert back to whenever variables change (unless nextFetchPolicy intervenes).

###### [`nextFetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-nextfetchpolicy)

`WatchQueryFetchPolicy | ((this: ApolloClient.WatchQueryOptions<TData, TVariables>, currentFetchPolicy: WatchQueryFetchPolicy, context: InternalTypes.NextFetchPolicyContext<TData, TVariables>) => WatchQueryFetchPolicy)`

Specifies the `FetchPolicy` to be used after this query has completed.

###### [`refetchWritePolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-refetchwritepolicy)

`RefetchWritePolicy`

Specifies whether a `NetworkStatus.refetch` operation should merge incoming field data with existing data, or overwrite the existing data. Overwriting is probably preferable, but merging is currently the default behavior, for backwards compatibility with Apollo Client 3.x.

###### [`returnPartialData`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-parameters-options-returnpartialdata)

`boolean`

If `true`, the query can return partial results from the cache if the cache doesn't contain results for all queried fields.

The default value is `false`.

### [Result](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result)

Query result object

```
useQuery.Result<TData, TVariables>
```

Show/hide child attributes

Operation data

###### [`data`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-data)

`DataValue.Complete<TData> | DataValue.Streaming<TData> | DataValue.Partial<TData> | undefined`

An object containing the result of your GraphQL query after it completes.

This value might be `undefined` if a query results in one or more errors (depending on the query's `errorPolicy`).

###### [`dataState`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-datastate)

`"complete" | "streaming" | "partial" | "empty"`

Describes the completeness of `data`.

* `empty`: No data could be fulfilled from the cache or the result is incomplete. `data` is `undefined`.

* `partial`: Some data could be fulfilled from the cache but `data` is incomplete. This is only possible when `returnPartialData` is `true`.

* `streaming`: `data` is incomplete as a result of a deferred query and the result is still streaming in.

* `complete`: `data` is a fully satisfied query result fulfilled either from the cache or network.

###### [`error`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-error)

`ErrorLike`

A single ErrorLike object describing the error that occurred during the latest query execution.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

###### [`previousData`*(optional)*](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-previousdata)

`MaybeMasked<TData>`

An object containing the result from the most recent *previous* execution of this query.

This value is `undefined` if this is the query's first execution.

###### [`variables`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-variables)

`TReturnVariables`

An object containing the variables that were provided for the query.

Network info

###### [`client`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-client)

`ApolloClient`

The instance of Apollo Client that executed the query. Can be useful for manually executing followup queries or writing data to the cache.

###### [`loading`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-loading)

`boolean`

If `true`, the query is still in flight.

###### [`networkStatus`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-networkstatus)

`NetworkStatus`

A number indicating the current network state of the query's associated request. [See possible values.](https://github.com/apollographql/apollo-client/blob/d96f4578f89b933c281bb775a39503f6cdb59ee8/src/core/networkStatus.ts#L4)

Used in conjunction with the [`notifyOnNetworkStatusChange`](https://www.apollographql.com/docs.md#notifyonnetworkstatuschange) option.

Helper functions

###### [`fetchMore`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-fetchmore)

`<TFetchData = TData, TFetchVars extends OperationVariables = TVariables>(fetchMoreOptions: ObservableQuery.FetchMoreOptions<TData, TVariables, TFetchData, TFetchVars>) => Promise<ApolloClient.QueryResult<MaybeMasked<TFetchData>>>`

A function that helps you fetch the next set of results for a [paginated list field](https://www.apollographql.com/docs/react/pagination/core-api.md).

###### [`refetch`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-refetch)

`(variables?: Partial<TVariables>) => Promise<ApolloClient.QueryResult<MaybeMasked<TData>>>`

A function that enables you to re-execute the query, optionally passing in new `variables`.

To guarantee that the refetch performs a network request, its `fetchPolicy` is set to `network-only` (unless the original query's `fetchPolicy` is `no-cache` or `cache-and-network`, which also guarantee a network request).

See also [Refetching](https://www.apollographql.com/docs/react/data/queries.md#refetching).

Returns a `ResultPromise` with an additional `.retain()` method. Calling `.retain()` keeps the network operation running even if the `ObservableQuery` no longer requires the result.

###### [`startPolling`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-startpolling)

`(pollInterval: number) => void`

A function that instructs the query to begin re-executing at a specified interval (in milliseconds).

###### [`stopPolling`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-stoppolling)

`() => void`

A function that instructs the query to stop polling after a previous call to `startPolling`.

###### [`subscribeToMore`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-subscribetomore)

`SubscribeToMoreFunction<TData, TVariables>`

A function that enables you to execute a [subscription](https://www.apollographql.com/docs/react/data/subscriptions.md), usually to subscribe to specific fields that were included in the query.

This function returns *another* function that you can call to terminate the subscription.

###### [`updateQuery`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-updatequery)

`(mapFn: UpdateQueryMapFn<TData, TVariables>) => void`

A function that enables you to update the query's cached result without executing a followup GraphQL operation.

See [using updateQuery and updateFragment](https://www.apollographql.com/docs/react/caching/cache-interaction.md#using-updatequery-and-updatefragment) for additional information.

Other

###### [`observable`](https://www.apollographql.com/docs/react/api/react/useQuery.md#usequery-result-observable)

`ObservableQuery<TData, TVariables>`

A reference to the internal `ObservableQuery` used by the hook.
