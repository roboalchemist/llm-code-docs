# Source: https://www.apollographql.com/docs/react/api/react/useMutation.md

# useMutation

## [`useMutation`](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation)

> Refer to the [Mutations](https://www.apollographql.com/docs/react/data/mutations.md) section for a more in-depth overview of `useMutation`.

### [Example](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-example)

JavaScript

```
 import { gql, useMutation } from "@apollo/client";

 const ADD_TODO = gql`
   mutation AddTodo($type: String!) {
     addTodo(type: $type) {
       id
       type
     }
   }
 `;

 function AddTodo() {
   let input;
   const [addTodo, { data }] = useMutation(ADD_TODO);

   return (
     <div>
       <form
         onSubmit={(e) => {
           e.preventDefault();
           addTodo({ variables: { type: input.value } });
           input.value = "";
         }}
       >
         <input
           ref={(node) => {
             input = node;
           }}
         />
         <button type="submit">Add Todo</button>
       </form>
     </div>
   );
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-signature)

TypeScript

```
useMutation<TData, TVariables, TCache, TConfiguredVariables>(
  mutation: DocumentNode | TypedDocumentNode<TData, TVariables>,
  options?: useMutation.Options<NoInfer<TData>, NoInfer<TVariables>, TCache, {
    [K in keyof TConfiguredVariables]: K extends keyof TVariables ? TConfiguredVariables[K] : never;
}>
): useMutation.ResultTuple<TData, MakeRequiredVariablesOptional<TVariables, TConfiguredVariables>, TCache>
```

[(src/react/hooks/useMutation.ts)](https://github.com/apollographql/apollo-client/blob/main/src/react/hooks/useMutation.ts)

### [Parameters](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters)

Name / Type

Description

[`mutation`](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-mutation)\
`DocumentNode | TypedDocumentNode<TData, TVariables>`

A GraphQL mutation document parsed into an AST by `gql`.

[`options`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options)\
`useMutation.Options<NoInfer<TData>, NoInfer<TVariables>, TCache, { [K in keyof TConfiguredVariables]: K extends keyof TVariables ? TConfiguredVariables[K] : never; }>`

Options to control how the mutation is executed.

Show/hide child attributes

Operation options

###### [`awaitRefetchQueries`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-awaitrefetchqueries)

`boolean`

If `true`, makes sure all queries included in `refetchQueries` are completed before the mutation is considered complete.

The default value is `false` (queries are refetched asynchronously).

###### [`errorPolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-errorpolicy)

`ErrorPolicy`

Specifies how the mutation handles a response that returns both GraphQL errors and partial results.

For details, see [GraphQL error policies](https://www.apollographql.com/docs/react/data/error-handling.md#graphql-error-policies).

The default value is `none`, meaning that the mutation result includes error details but *not* partial results.

###### [`onCompleted`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-oncompleted)

`(data: MaybeMasked<TData>, clientOptions?: Options<TData, TVariables, TCache>) => void`

A callback function that's called when your mutation successfully completes with zero errors (or if `errorPolicy` is `ignore` and partial data is returned).

This function is passed the mutation's result `data` and any options passed to the mutation.

###### [`onError`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-onerror)

`(error: ErrorLike, clientOptions?: Options<TData, TVariables, TCache>) => void`

A callback function that's called when the mutation encounters one or more errors (unless `errorPolicy` is `ignore`).

This function is passed an [`ApolloError`](https://github.com/apollographql/apollo-client/blob/d96f4578f89b933c281bb775a39503f6cdb59ee8/src/errors/index.ts#L36-L39) object that contains either a `networkError` object or a `graphQLErrors` array, depending on the error(s) that occurred, as well as any options passed the mutation.

###### [`onQueryUpdated`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-onqueryupdated)

`OnQueryUpdated<any>`

Optional callback for intercepting queries whose cache data has been updated by the mutation, as well as any queries specified in the `refetchQueries: [...]` list passed to `client.mutate`.

Returning a `Promise` from `onQueryUpdated` will cause the final mutation `Promise` to await the returned `Promise`. Returning `false` causes the query to be ignored.

###### [`refetchQueries`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-refetchqueries)

`((result: NormalizedExecutionResult<Unmasked<TData>>) => InternalRefetchQueriesInclude) | InternalRefetchQueriesInclude`

An array (or a function that *returns* an array) that specifies which queries you want to refetch after the mutation occurs.

Each array value can be either:

* An object containing the `query` to execute, along with any `variables`

* A string indicating the operation name of the query to refetch

###### [`variables`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-variables)

`Partial<TVariables> & TConfiguredVariables`

An object containing all of the GraphQL variables your mutation requires to execute.

Each key in the object corresponds to a variable name, and that key's value corresponds to the variable value.

Networking options

###### [`client`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-client)

`ApolloClient`

The instance of `ApolloClient` to use to execute the mutation.

By default, the instance that's passed down via context is used, but you can provide a different instance here.

###### [`context`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-context)

`DefaultContext`

If you're using [Apollo Link](https://www.apollographql.com/docs/react/api/link/introduction.md), this object is the initial value of the `context` object that's passed along your link chain.

###### [`notifyOnNetworkStatusChange`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-notifyonnetworkstatuschange)

`boolean`

If `true`, the in-progress mutation's associated component re-renders whenever the network status changes or a network error occurs.

The default value is `true`.

Caching options

###### [`fetchPolicy`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-fetchpolicy)

`MutationFetchPolicy`

Provide `no-cache` if the mutation's result should *not* be written to the Apollo Client cache.

The default value is `network-only` (which means the result *is* written to the cache).

Unlike queries, mutations *do not* support [fetch policies](https://www.apollographql.com/docs/react/data/queries.md#setting-a-fetch-policy) besides `network-only` and `no-cache`.

###### [`optimisticResponse`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-optimisticresponse)

`Unmasked<NoInfer<TData>> | ((vars: TVariables, { IGNORE }: { IGNORE: IgnoreModifier; }) => Unmasked<NoInfer<TData>> | IgnoreModifier)`

By providing either an object or a callback function that, when invoked after a mutation, allows you to return optimistic data and optionally skip updates via the `IGNORE` sentinel object, Apollo Client caches this temporary (and potentially incorrect) response until the mutation completes, enabling more responsive UI updates.

For more information, see [Optimistic mutation results](https://www.apollographql.com/docs/react/performance/optimistic-ui.md).

###### [`update`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-update)

`MutationUpdaterFunction<TData, TVariables, TCache>`

A function used to update the Apollo Client cache after the mutation completes.

For more information, see [Updating the cache after a mutation](https://www.apollographql.com/docs/react/data/mutations.md#updating-the-cache-after-a-mutation).

Other

###### [`keepRootFields`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-keeprootfields)

`boolean`

To avoid retaining sensitive information from mutation root field arguments, Apollo Client v3.4+ automatically clears any `ROOT_MUTATION` fields from the cache after each mutation finishes. If you need this information to remain in the cache, you can prevent the removal by passing `keepRootFields: true` to the mutation. `ROOT_MUTATION` result data are also passed to the mutation `update` function, so we recommend obtaining the results that way, rather than using this option, if possible.

###### [`updateQueries`*(optional)*](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-parameters-options-updatequeries)

`MutationQueryReducersMap<TData>`

A `MutationQueryReducersMap`, which is map from query names to mutation query reducers. Briefly, this map defines how to incorporate the results of the mutation into the results of queries that are currently being watched by your application.

### [Result](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-result)

TypeScript

```
[
  mutate: (options?: MutationFunctionOptions<TData, TVariables>) => Promise<FetchResult<TData>>,
  result: MutationResult<TData>
]
```

A tuple of two values:

Name / Type

Description

`mutate`\
`( options?: MutationFunctionOptions<TData, TVariables> ) => Promise<FetchResult<TData>>`

A function to trigger the mutation from your UI. You can optionally pass this function any of the following options:

* `awaitRefetchQueries`
* `context`
* `fetchPolicy`
* `onCompleted`
* `onError`
* `optimisticResponse`
* `refetchQueries`
* `onQueryUpdated`
* `update`
* `variables`
* `client`

Any option you pass here overrides any existing value for that option that you passed to `useMutation`.The mutate function returns a promise that fulfills with your mutation result.

`result`\
`MutationResult<TData>`

The result of the mutation.

Show/hide child attributes

###### [`called`](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-result-result-called)

`boolean`

If `true`, the mutation's mutate function has been called.

###### [`client`](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-result-result-client)

`ApolloClient`

The instance of Apollo Client that executed the mutation.

Can be useful for manually executing followup operations or writing data to the cache.

###### [`data`](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-result-result-data)

`MaybeMasked<TData> | null | undefined`

The data returned from your mutation. Can be `undefined` if the `errorPolicy` is `all` or `ignore` and the server returns a GraphQL response with `errors` but not `data` or a network error is returned.

###### [`error`](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-result-result-error)

`ErrorLike | undefined`

If the mutation produces one or more errors, this object contains either an array of `graphQLErrors` or a single `networkError`. Otherwise, this value is `undefined`.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

###### [`loading`](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-result-result-loading)

`boolean`

If `true`, the mutation is currently in flight.

###### [`reset`](https://www.apollographql.com/docs/react/api/react/useMutation.md#usemutation-result-result-reset)

`() => void`

A function that you can call to reset the mutation's result to its initial, uncalled state.
