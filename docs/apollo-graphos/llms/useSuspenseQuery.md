# Source: https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md

# useSuspenseQuery

## [`useSuspenseQuery`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery)

Test For a detailed explanation of `useSuspenseQuery`, see the [fetching with Suspense reference](https://www.apollographql.com/docs/react/data/suspense.md).

### [Example](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-example)

JavaScript

```
 import { Suspense } from "react";
 import { useSuspenseQuery } from "@apollo/client";
 
 const listQuery = gql`
   query {
     list {
       id
     }
   }
 `;
 
 function App() {
   return (
     <Suspense fallback={<Spinner />}>
       <List />
     </Suspense>
   );
 }
 
 function List() {
   const { data } = useSuspenseQuery(listQuery);
 
   return (
     <ol>
       {data.list.map((item) => (
         <Item key={item.id} id={item.id} />
       ))}
     </ol>
   );
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-signature)

TypeScript

```
useSuspenseQuery<TData, TVariables>(
  query: DocumentNode | TypedDocumentNode<TData, TVariables>,
  options?: useSuspenseQuery.Options<TVariables>
): useSuspenseQuery.Result<TData, TVariables>
```

### [Parameters](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters)

Name / Type

Description

[`query`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-query)\
`DocumentNode | TypedDocumentNode<TData, TVariables>`

A GraphQL query document parsed into an AST by `gql`.

[`options`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options)\
`useSuspenseQuery.Options<TVariables>`

An optional object containing options for the query. Instead of passing a `useSuspenseQuery.Options` object into the hook, you can also pass a [`skipToken`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#skiptoken) to prevent the `useSuspenseQuery` hook from executing the query or suspending.

Show/hide child attributes

Operation options

###### [`client`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-client)

`ApolloClient`

The instance of `ApolloClient` to use to execute the query.

By default, the instance that's passed down via context is used, but you can provide a different instance here.

###### [`errorPolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-errorpolicy)

`ErrorPolicy`

Specifies how the query handles a response that returns both GraphQL errors and partial results.

For details, see [GraphQL error policies](https://www.apollographql.com/docs/react/data/error-handling.md#graphql-error-policies).

The default value is `none`, meaning that the query result includes error details but not partial results.

###### [`queryKey`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-querykey)

`string | number | any[]`

A unique identifier for the query. Each item in the array must be a stable identifier to prevent infinite fetches.

This is useful when using the same query and variables combination in more than one component, otherwise the components may clobber each other. This can also be used to force the query to re-evaluate fresh.

###### [`variables`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-variables)

`TVariables`

An object containing all of the GraphQL variables your query requires to execute.

Each key in the object corresponds to a variable name, and that key's value corresponds to the variable value.

###### [`skip`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-skip)

`boolean`

> ⚠️ Deprecated
>
> We recommend using `skipToken` in place of the `skip` option as it is more type-safe.
>
> This option is deprecated and only supported to ease the migration from `useQuery`. It will be removed in a future release. Please use [`skipToken`](https://www.apollographql.com/docs/react/api/react/hooks.md#skiptoken) instead of the `skip` option as it is more type-safe.

If `true`, the query is not executed. The default value is `false`.

Recommended usage of `skipToken`:

TypeScript

```
import { skipToken, useSuspenseQuery } from "@apollo/client";

const { data } = useSuspenseQuery(
  query,
  id ? { variables: { id } } : skipToken
);
```

Networking options

###### [`context`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-context)

`DefaultContext`

If you're using [Apollo Link](https://www.apollographql.com/docs/react/api/link/introduction.md), this object is the initial value of the `context` object that's passed along your link chain.

Caching options

###### [`fetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-fetchpolicy)

`FetchPolicy`

Specifies how the query interacts with the Apollo Client cache during execution (for example, whether it checks the cache for results before sending a request to the server).

For details, see [Setting a fetch policy](https://www.apollographql.com/docs/react/data/queries.md#setting-a-fetch-policy).

The default value is `cache-first`.

###### [`refetchWritePolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-refetchwritepolicy)

`RefetchWritePolicy`

Watched queries must opt into overwriting existing data on refetch, by passing refetchWritePolicy: "overwrite" in their WatchQueryOptions.

The default value is "overwrite".

###### [`returnPartialData`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-parameters-options-returnpartialdata)

`boolean`

If `true`, the query can return partial results from the cache if the cache doesn't contain results for all queried fields.

The default value is `false`.

### [Result](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result)

```
useSuspenseQuery.Result<TData, TVariables>
```

Show/hide child attributes

Operation data

###### [`data`*(optional)*](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result-data)

`DataValue.Complete<TData> | DataValue.Streaming<TData> | DataValue.Partial<TData> | undefined`

An object containing the result of your GraphQL query after it completes.

This value might be `undefined` if a query results in one or more errors (depending on the query's `errorPolicy`).

###### [`dataState`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result-datastate)

`"complete" | "streaming" | "partial" | "empty"`

Describes the completeness of `data`.

* `empty`: No data could be fulfilled from the cache or the result is incomplete. `data` is `undefined`.

* `partial`: Some data could be fulfilled from the cache but `data` is incomplete. This is only possible when `returnPartialData` is `true`.

* `streaming`: `data` is incomplete as a result of a deferred query and the result is still streaming in.

* `complete`: `data` is a fully satisfied query result fulfilled either from the cache or network.

###### [`error`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result-error)

`ErrorLike | undefined`

A single ErrorLike object describing the error that occurred during the latest query execution.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

Operation options

###### [`client`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result-client)

`ApolloClient`

The instance of `ApolloClient` to use to execute the query.

By default, the instance that's passed down via context is used, but you can provide a different instance here.

Network info

###### [`networkStatus`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result-networkstatus)

`NetworkStatus`

A number indicating the current network state of the query's associated request. [See possible values.](https://github.com/apollographql/apollo-client/blob/d96f4578f89b933c281bb775a39503f6cdb59ee8/src/core/networkStatus.ts#L4)

Used in conjunction with the [`notifyOnNetworkStatusChange`](https://www.apollographql.com/docs.md#notifyonnetworkstatuschange) option.

Helper functions

###### [`fetchMore`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result-fetchmore)

`FetchMoreFunction<TData, TVariables>`

A function that helps you fetch the next set of results for a [paginated list field](https://www.apollographql.com/docs/react/pagination/core-api.md).

Read more...

Calling this function will cause the component to re-suspend, unless the call site is wrapped in [`startTransition`](https://react.dev/reference/react/startTransition).

###### [`refetch`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result-refetch)

`RefetchFunction<TData, TVariables>`

A function that enables you to re-execute the query, optionally passing in new `variables`.

To guarantee that the refetch performs a network request, its `fetchPolicy` is set to `network-only` (unless the original query's `fetchPolicy` is `no-cache` or `cache-and-network`, which also guarantee a network request).

See also [Refetching](https://www.apollographql.com/docs/react/data/queries.md#refetching).

Returns a `ResultPromise` with an additional `.retain()` method. Calling `.retain()` keeps the network operation running even if the `ObservableQuery` no longer requires the result.

Read more...

Calling this function will cause the component to re-suspend, unless the call site is wrapped in [`startTransition`](https://react.dev/reference/react/startTransition).

###### [`subscribeToMore`](https://www.apollographql.com/docs/react/api/react/useSuspenseQuery.md#usesuspensequery-result-subscribetomore)

`SubscribeToMoreFunction<TData, TVariables>`

A function that enables you to execute a [subscription](https://www.apollographql.com/docs/react/data/subscriptions.md), usually to subscribe to specific fields that were included in the query.

This function returns *another* function that you can call to terminate the subscription.
