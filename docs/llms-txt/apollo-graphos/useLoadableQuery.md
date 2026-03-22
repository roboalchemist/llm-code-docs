# Source: https://www.apollographql.com/docs/react/api/react/useLoadableQuery.md

# useLoadableQuery

## [`useLoadableQuery`](https://www.apollographql.com/docs/react/api/react/useLoadableQuery.md#useloadablequery)

A hook for imperatively loading a query, such as responding to a user interaction.

> Refer to the [Suspense - Fetching in response to user interaction](https://www.apollographql.com/docs/react/data/suspense.md#fetching-in-response-to-user-interaction) section for a more in-depth overview of `useLoadableQuery`.

### [Example](https://www.apollographql.com/docs/react/api/react/useLoadableQuery.md#useloadablequery-example)

JavaScript

```
 import { gql, useLoadableQuery } from "@apollo/client";
 
 const GET_GREETING = gql`
   query GetGreeting($language: String!) {
     greeting(language: $language) {
       message
     }
   }
 `;
 
 function App() {
   const [loadGreeting, queryRef] = useLoadableQuery(GET_GREETING);
 
   return (
     <>
       <button onClick={() => loadGreeting({ language: "english" })}>
         Load greeting
       </button>
       <Suspense fallback={<div>Loading...</div>}>
         {queryRef && <Hello queryRef={queryRef} />}
       </Suspense>
     </>
   );
 }
 
 function Hello({ queryRef }) {
   const { data } = useReadQuery(queryRef);
 
   return <div>{data.greeting.message}</div>;
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useLoadableQuery.md#useloadablequery-signature)

TypeScript

```
useLoadableQuery<TData, TVariables>(
  query: DocumentNode | TypedDocumentNode<TData, TVariables>,
  options: useLoadableQuery.Options
): useLoadableQuery.Result<TData, TVariables>
```

### [Parameters](https://www.apollographql.com/docs/react/api/react/useLoadableQuery.md#useloadablequery-parameters)

Name / Type

Description

[`query`](https://www.apollographql.com/docs/react/api/react/useLoadableQuery.md#useloadablequery-parameters-query)\
`DocumentNode | TypedDocumentNode<TData, TVariables>`

A GraphQL query document parsed into an AST by `gql`.

[`options`](https://www.apollographql.com/docs/react/api/react/useLoadableQuery.md#useloadablequery-parameters-options)\
`useLoadableQuery.Options`

Options to control how the query is executed.

### [Result](https://www.apollographql.com/docs/react/api/react/useLoadableQuery.md#useloadablequery-result)

TypeScript

```
[
  loadQuery: LoadQueryFunction<TVariables>,
  queryRef: QueryRef<TData, TVariables> | null,
  {
    fetchMore: FetchMoreFunction<TData, TVariables>;
    refetch: RefetchFunction<TData, TVariables>;
    subscribeToMore: SubscribeToMoreFunction<TData, TVariables>;
    reset: ResetFunction;
  }
]
```

A tuple of three values:

Name / Type

Description

`loadQuery`\
`LoadQueryFunction<TVariables>`

A function used to imperatively load a query. Calling this function will create or update the `queryRef` returned by `useLoadableQuery`, which should be passed to `useReadQuery`.

`queryRef`\
`QueryRef<TData, TVariables> | null`

The `queryRef` used by `useReadQuery` to read the query result.

`handlers`\
`{ fetchMore: FetchMoreFunction<TData, TVariables>; refetch: RefetchFunction<TData, TVariables>; subscribeToMore: SubscribeToMoreFunction<TData, TVariables>; reset: ResetFunction; }`

Additional handlers used for the query, such as `refetch`.
