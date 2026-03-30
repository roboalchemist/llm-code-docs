# Source: https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md

# useBackgroundQuery

## [`useBackgroundQuery`](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery)

For a detailed explanation of useBackgroundQuery, see the [fetching with Suspense reference](https://www.apollographql.com/docs/react/data/suspense.md).

### [Example](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-example)

JavaScript

```
 import { Suspense } from "react";
 import { ApolloClient, InMemoryCache, HttpLink } from "@apollo/client";
 import { useBackgroundQuery, useReadQuery } from "@apollo/client/react";
 
 const query = gql`
   foo {
     bar
   }
 `;
 
 const client = new ApolloClient({
   link: new HttpLink({ uri: "http://localhost:4000/graphql" }),
   cache: new InMemoryCache(),
 });
 
 function SuspenseFallback() {
   return <div>Loading...</div>;
 }
 
 function Child({ queryRef }) {
   const { data } = useReadQuery(queryRef);
 
   return <div>{data.foo.bar}</div>;
 }
 
 function Parent() {
   const [queryRef] = useBackgroundQuery(query);
 
   return (
     <Suspense fallback={<SuspenseFallback />}>
       <Child queryRef={queryRef} />
     </Suspense>
   );
 }
 
 function App() {
   return (
     <ApolloProvider client={client}>
       <Parent />
     </ApolloProvider>
   );
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-signature)

TypeScript

```
useBackgroundQuery<TData, TVariables>(
  query: DocumentNode | TypedDocumentNode<TData, TVariables>,
  options: SkipToken | useBackgroundQuery.Options<TVariables>
): [
            QueryRef<TData, TVariables> | undefined,
            useBackgroundQuery.Result<TData, TVariables>
        ]
```

### [Parameters](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-parameters)

Name / Type

Description

[`query`](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-parameters-query)\
`DocumentNode | TypedDocumentNode<TData, TVariables>`

A GraphQL query document parsed into an AST by `gql`.

[`options`](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-parameters-options)\
`SkipToken | useBackgroundQuery.Options<TVariables>`

An optional object containing options for the query. Instead of passing a `useBackgroundQuery.Options` object into the hook, you can also pass a [`skipToken`](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#skiptoken) to prevent the `useBackgroundQuery` hook from executing the query or suspending.

### [Result](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-result)

TypeScript

```
[
  QueryRef<TData, TVariables> | undefined,
  useBackgroundQuery.Result<TData, TVariables>,
];
```

A tuple of two values:

Name / Type

Description

`queryRef`\
`QueryRef<TData, TVariables> | undefined`

A `QueryRef` that can be passed to `useReadQuery` to read the query result. The `queryRef` is `undefined` if the query is skipped.

`result`\
`useBackgroundQuery.Result<TData, TVariables>`

An object containing helper functions for the query:

* `refetch`: A function to re-execute the query
* `fetchMore`: A function to fetch more results for pagination
* `subscribeToMore`: A function to subscribe to updates

Show/hide child attributes

Helper functions

###### [`refetch`](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-result-result-refetch)

`RefetchFunction<TData, TVariables>`

A function that enables you to re-execute the query, optionally passing in new `variables`.

To guarantee that the refetch performs a network request, its `fetchPolicy` is set to `network-only` (unless the original query's `fetchPolicy` is `no-cache` or `cache-and-network`, which also guarantee a network request).

See also [Refetching](https://www.apollographql.com/docs/react/data/queries.md#refetching).

Returns a `ResultPromise` with an additional `.retain()` method. Calling `.retain()` keeps the network operation running even if the `ObservableQuery` no longer requires the result.

Read more...

Calling this function will cause the component to re-suspend, unless the call site is wrapped in [`startTransition`](https://react.dev/reference/react/startTransition).

Other

###### [`fetchMore`](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-result-result-fetchmore)

`FetchMoreFunction<TData, TVariables>`

A function that helps you fetch the next set of results for a [paginated list field](https://www.apollographql.com/docs/react/pagination/core-api.md).

Read more...

Calling this function will cause the component to re-suspend, unless the call site is wrapped in [`startTransition`](https://react.dev/reference/react/startTransition).

###### [`subscribeToMore`](https://www.apollographql.com/docs/react/api/react/useBackgroundQuery.md#usebackgroundquery-result-result-subscribetomore)

`SubscribeToMoreFunction<TData, TVariables>`

A function that enables you to execute a [subscription](https://www.apollographql.com/docs/react/data/subscriptions.md), usually to subscribe to specific fields that were included in the query.

This function returns *another* function that you can call to terminate the subscription.

If no query has been executed yet and you skip the query, the hook will return `undefined` instead of a `queryRef`.
