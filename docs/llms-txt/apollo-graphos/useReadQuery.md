# Source: https://www.apollographql.com/docs/react/api/react/useReadQuery.md

# useReadQuery

## [`useReadQuery`](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery)

For a detailed explanation of `useReadQuery`, see the [fetching with Suspense reference](https://www.apollographql.com/docs/react/data/suspense.md#avoiding-request-waterfalls).

### [Example](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-example)

JavaScript

```
 import { Suspense } from "react";
 import { useBackgroundQuery, useReadQuery } from "@apollo/client";
 
 function Parent() {
   const [queryRef] = useBackgroundQuery(query);
 
   return (
     <Suspense fallback={<div>Loading...</div>}>
       <Child queryRef={queryRef} />
     </Suspense>
   );
 }
 
 function Child({ queryRef }) {
   const { data } = useReadQuery(queryRef);
 
   return <div>{data.name}</div>;
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-signature)

TypeScript

```
useReadQuery<TData>(
  queryRef: QueryRef<TData>
): useReadQuery.Result<TData>
```

### [Parameters](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-parameters)

Name / Type

Description

[`queryRef`](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-parameters-queryref)\
`QueryRef<TData>`

The `QueryRef` that was generated via `useBackgroundQuery`.

### [Result](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-result)

An object containing the query result data, error, and network status.

```
useReadQuery.Result<TData>
```

Show/hide child attributes

Operation data

###### [`data`*(optional)*](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-result-data)

`DataValue.Complete<TData> | DataValue.Streaming<TData> | DataValue.Partial<TData> | undefined`

An object containing the result of your GraphQL query after it completes.

This value might be `undefined` if a query results in one or more errors (depending on the query's `errorPolicy`).

###### [`dataState`](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-result-datastate)

`"complete" | "streaming" | "partial" | "empty"`

Describes the completeness of `data`.

* `empty`: No data could be fulfilled from the cache or the result is incomplete. `data` is `undefined`.

* `partial`: Some data could be fulfilled from the cache but `data` is incomplete. This is only possible when `returnPartialData` is `true`.

* `streaming`: `data` is incomplete as a result of a deferred query and the result is still streaming in.

* `complete`: `data` is a fully satisfied query result fulfilled either from the cache or network.

Operation data This property can be ignored when using the default \`errorPolicy\` or an \`errorPolicy\` of \`none\`. The hook will throw the error instead of setting this property.

###### [`error`](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-result-error)

`ErrorLike | undefined`

A single ErrorLike object describing the error that occurred during the latest query execution.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

Network info

###### [`networkStatus`](https://www.apollographql.com/docs/react/api/react/useReadQuery.md#usereadquery-result-networkstatus)

`NetworkStatus`

A number indicating the current network state of the query's associated request. [See possible values.](https://github.com/apollographql/apollo-client/blob/d96f4578f89b933c281bb775a39503f6cdb59ee8/src/core/networkStatus.ts#L4)

Used in conjunction with the [`notifyOnNetworkStatusChange`](https://www.apollographql.com/docs.md#notifyonnetworkstatuschange) option.
