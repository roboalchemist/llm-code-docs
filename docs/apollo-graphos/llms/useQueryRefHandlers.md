# Source: https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md

# useQueryRefHandlers

## [`useQueryRefHandlers`](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers)

A React hook that returns a `refetch` and `fetchMore` function for a given `queryRef`.

This is useful to get access to handlers for a `queryRef` that was created by `createQueryPreloader` or when the handlers for a `queryRef` produced in a different component are inaccessible.

### [Example](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers-example)

TypeScript

```
 const MyComponent({ queryRef }) {
   const { refetch, fetchMore } = useQueryRefHandlers(queryRef);

   // ...
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers-signature)

TypeScript

```
useQueryRefHandlers<TData, TVariables>(
  queryRef: QueryRef<TData, TVariables, DataState<TData>["dataState"]>
): useQueryRefHandlers.Result<TData, TVariables>
```

[(src/react/hooks/useQueryRefHandlers.ts)](https://github.com/apollographql/apollo-client/blob/main/src/react/hooks/useQueryRefHandlers.ts)

### [Parameters](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers-parameters)

Name / Type

Description

[`queryRef`](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers-parameters-queryref)\
`QueryRef<TData, TVariables, DataState<TData>["dataState"]>`

A `QueryRef` returned from `useBackgroundQuery`, `useLoadableQuery`, or `createQueryPreloader`.

Show/hide child attributes

### [Result](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers-result)

```
useQueryRefHandlers.Result<TData, TVariables>
```

Show/hide child attributes

###### [`fetchMore`](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers-result-fetchmore)

`FetchMoreFunction<TData, TVariables>`

A function that helps you fetch the next set of results for a [paginated list field](https://www.apollographql.com/docs/react/pagination/core-api.md).

###### [`refetch`](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers-result-refetch)

`RefetchFunction<TData, TVariables>`

Update the variables of this observable query, and fetch the new results. This method should be preferred over `setVariables` in most use cases.

Returns a `ResultPromise` with an additional `.retain()` method. Calling `.retain()` keeps the network operation running even if the `ObservableQuery` no longer requires the result.

Note: `refetch()` guarantees that a value will be emitted from the observable, even if the result is deep equal to the previous value.

###### [`subscribeToMore`](https://www.apollographql.com/docs/react/api/react/useQueryRefHandlers.md#usequeryrefhandlers-result-subscribetomore)

`SubscribeToMoreFunction<TData, TVariables>`

A function that enables you to execute a [subscription](https://www.apollographql.com/docs/react/data/subscriptions.md), usually to subscribe to specific fields that were included in the query.

This function returns *another* function that you can call to terminate the subscription.
