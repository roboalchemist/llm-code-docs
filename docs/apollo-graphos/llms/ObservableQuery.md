# Source: https://www.apollographql.com/docs/react/api/core/ObservableQuery.md

# ObservableQuery

An `ObservableQuery` is created by calling the `client.watchQuery` method.
It represents a query that can be observed for changes, allowing you to reactively update your UI.

## Key Behaviors

### RxJS Integration

`ObservableQuery` implements the [RxJS](https://rxjs.dev/) `InteropObservable` interface which means you can convert it into an RxJS `Observable` via `from(observableQuery)`.
It also provides the `subscribe` and `pipe` functions like an RxJS `Observable`.
Refer to the [RxJS documentation](https://rxjs.dev/guide/overview) for additional context and API options.

To get a single result from an `ObservableQuery` as a Promise, use the `firstValueFrom` helper:

```ts
import { firstValueFrom, from } from "rxjs";

// The `from` is necessary to turn `observableQuery` into an RxJS observable
const result = await firstValueFrom(from(observableQuery));
```

### Subscription Lifecycle

* `ObservableQuery` instances are only registered with `ApolloClient` while they have active subscribers
* Unsubscribing from an `ObservableQuery` while a request is in flight does not terminate the request
* Unsubscribing before any value has been emitted removes the query from the tracked list and makes it ineligible for query deduplication

### Error Handling

* `ObservableQuery` does not terminate on errors - instead it emits a `next` value with an `error` property. This ensures `ObservableQuery` subscriptions can continue receiving updates after errors without resubscription.

### Loading States

* When `notifyOnNetworkStatusChange` is `true` (the default), an initial loading state is emitted when subscribing
* `ObservableQuery` preserves `data` when emitting a loading state unless `query` or `variables` changed (note: `@export` variables are not considered for this check)
* When the query can be fulfilled by the cache or when the link chain responds synchronously, a loading state is omitted
* `cache-only` queries initialize with `networkStatus: NetworkStatus.ready` when there is no data in the cache
* `standby` queries initialize with `networkStatus: NetworkStatus.ready` before subscribing to the query

### Promise-returning Methods and retention

* `refetch()` and `reobserve()` return a `ResultPromise` with an additional `.retain()` method
* By default, the network operation is cancelled when `ObservableQuery` no longer requires the result, such as when `ObservableQuery` is unsubscribed or variables change, and the returned `Promise` will reject with an `AbortError`
* Calling `.retain()` keeps the network operation running even when the `ObservableQuery` no longer requires the result
* `setVariables()` and `refetch()` guarantee that a value will be emitted from the observable, even when the result is deeply equal to the previous result

### Active vs Inactive Queries

* **Active queries**: Have at least one subscriber and are not skipped or have a `fetchPolicy` of `standby`
* **Inactive queries**: Have a subscriber but are either skipped or have a `fetchPolicy` of `standby`
* `ObservableQuery`s without subscribers but with an active network request are handled as if they had a subscriber for the duration of the query
* Only queries with subscribers can be refetched using `ApolloClient.refetchQueries`

## `ObservableQuery` functions

### [`getCurrentResult`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#getcurrentresult)

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#getcurrentresult-signature)

TypeScript

```
getCurrentResult(): ObservableQuery.Result<MaybeMasked<TData>>
```

### [`pipe`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#pipe)

Used to stitch together functional operators into a chain.

#### [Example](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#pipe-example)

TypeScript

```
 import { filter, map } from 'rxjs';
 
 observableQuery
   .pipe(
     filter(...),
     map(...),
   )
   .subscribe(x => console.log(x));
```

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#pipe-signature)

TypeScript

```
pipe(
  operators: OperatorFunctionChain<ObservableQuery.Result<TData>, OperatorResult>
): Observable<OperatorResult>
```

### [`subscribe`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#subscribe)

Subscribes to the `ObservableQuery`.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#subscribe-signature)

TypeScript

```
subscribe(
  observerOrNext: Partial<Observer<ObservableQuery.Result<MaybeMasked<TData>>>> | ((value: ObservableQuery.Result<MaybeMasked<TData>>) => void)
): Subscription
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#subscribe-parameters)

Name / Type

Description

[`observerOrNext`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#subscribe-parameters-observerornext)\
`Partial<Observer<ObservableQuery.Result<MaybeMasked<TData>>>> | ((value: ObservableQuery.Result<MaybeMasked<TData>>) => void)`

Either an RxJS `Observer` with some or all callback methods, or the `next` handler that is called for each value emitted from the subscribed Observable.

### [`refetch`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#refetch)

Update the variables of this observable query, and fetch the new results. This method should be preferred over `setVariables` in most use cases.

Returns a `ResultPromise` with an additional `.retain()` method. Calling `.retain()` keeps the network operation running even if the `ObservableQuery` no longer requires the result.

Note: `refetch()` guarantees that a value will be emitted from the observable, even if the result is deep equal to the previous value.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#refetch-signature)

TypeScript

```
refetch(
  variables?: Partial<TVariables>
): ObservableQuery.ResultPromise<ApolloClient.QueryResult<TData>>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#refetch-parameters)

Name / Type

Description

[`variables`*&#x20;(optional)*](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#refetch-parameters-variables)\
`Partial<TVariables>`

The new set of variables. If there are missing variables, the previous values of those variables will be used.

### [`fetchMore`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#fetchmore)

A function that helps you fetch the next set of results for a [paginated list field](https://www.apollographql.com/docs/react/pagination/core-api.md).

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#fetchmore-signature)

TypeScript

```
fetchMore<TFetchData, TFetchVars>(
  options: ObservableQuery.FetchMoreOptions<TData, TVariables, TFetchData, TFetchVars>
): Promise<ApolloClient.QueryResult<TFetchData>>
```

### [`subscribeToMore`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#subscribetomore)

A function that enables you to execute a [subscription](https://www.apollographql.com/docs/react/data/subscriptions.md), usually to subscribe to specific fields that were included in the query.

This function returns *another* function that you can call to terminate the subscription.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#subscribetomore-signature)

TypeScript

```
subscribeToMore<TSubscriptionData, TSubscriptionVariables>(
  options: ObservableQuery.SubscribeToMoreOptions<TData, TSubscriptionVariables, TSubscriptionData, TVariables>
): () => void
```

### [`stop`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#stop)

Tears down the `ObservableQuery` and stops all active operations by sending a `complete` notification.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#stop-signature)

TypeScript

```
stop(): void
```

### [`setVariables`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#setvariables)

Update the variables of this observable query, and fetch the new results if they've changed. Most users should prefer `refetch` instead of `setVariables` in order to to be properly notified of results even when they come from the cache.

Note: `setVariables()` guarantees that a value will be emitted from the observable, even if the result is deeply equal to the previous value.

Note: the promise will resolve with the last emitted result when either the variables match the current variables or there are no subscribers to the query.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#setvariables-signature)

TypeScript

```
setVariables(
  variables: TVariables
): Promise<ApolloClient.QueryResult<TData>>
```

#### [Parameters](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#setvariables-parameters)

Name / Type

Description

[`variables`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#setvariables-parameters-variables)\
`TVariables`

The new set of variables. If there are missing variables, the previous values of those variables will be used.

### [`updateQuery`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#updatequery)

A function that enables you to update the query's cached result without executing a followup GraphQL operation.

See [using updateQuery and updateFragment](https://www.apollographql.com/docs/react/caching/cache-interaction.md#using-updatequery-and-updatefragment) for additional information.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#updatequery-signature)

TypeScript

```
updateQuery(
  mapFn: UpdateQueryMapFn<TData, TVariables>
): void
```

### [`startPolling`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#startpolling)

A function that instructs the query to begin re-executing at a specified interval (in milliseconds).

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#startpolling-signature)

TypeScript

```
startPolling(
  pollInterval: number
): void
```

### [`stopPolling`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#stoppolling)

A function that instructs the query to stop polling after a previous call to `startPolling`.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#stoppolling-signature)

TypeScript

```
stopPolling(): void
```

### [`reobserve`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#reobserve)

Reevaluate the query, optionally against new options. New options will be merged with the current options when given.

Note: `variables` can be reset back to their defaults (typically empty) by calling `reobserve` with `variables: undefined`.

#### [Signature](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#reobserve-signature)

TypeScript

```
reobserve(
  newOptions?: Partial<ObservableQuery.Options<TData, TVariables>>
): ObservableQuery.ResultPromise<ApolloClient.QueryResult<MaybeMasked<TData>>>
```

## Types

### [`NetworkStatus`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus)

The current status of a query’s execution in our system.

Enumeration Members

#### [`error`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus-member-error)

No request is in flight for this query, but one or more errors were detected.

#### [`fetchMore`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus-member-fetchmore)

Indicates that `fetchMore` was called on this query and that the query created is currently in flight.

#### [`loading`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus-member-loading)

The query has never been run before and the query is now currently running. A query will still have this network status even if a partial data result was returned from the cache, but a query was dispatched anyway.

#### [`poll`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus-member-poll)

Indicates that a polling query is currently in flight. So for example if you are polling a query every 10 seconds then the network status will switch to `poll` every 10 seconds whenever a poll request has been sent but not resolved.

#### [`ready`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus-member-ready)

No request is in flight for this query, and no errors happened. Everything is OK.

#### [`refetch`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus-member-refetch)

Similar to the `setVariables` network status. It means that `refetch` was called on a query and the refetch request is currently in flight.

#### [`setVariables`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus-member-setvariables)

If `setVariables` was called and a query was fired because of that then the network status will be `setVariables` until the result of that query comes back.

#### [`streaming`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#networkstatus-member-streaming)

Indicates that a `@defer` query has received at least the first chunk of the result but the full result has not yet been fully streamed to the client.

### [`ApolloQueryResult`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#apolloqueryresult)

Properties

Name / Type

Description

Operation data

###### [`data`*(optional)*](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#apolloqueryresult-data)

`DataValue.Complete<TData> | DataValue.Streaming<TData> | DataValue.Partial<TData> | undefined`

An object containing the result of your GraphQL query after it completes.

This value might be `undefined` if a query results in one or more errors (depending on the query's `errorPolicy`).

###### [`dataState`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#apolloqueryresult-datastate)

`"complete" | "streaming" | "partial" | "empty"`

Describes the completeness of `data`.

* `empty`: No data could be fulfilled from the cache or the result is incomplete. `data` is `undefined`.

* `partial`: Some data could be fulfilled from the cache but `data` is incomplete. This is only possible when `returnPartialData` is `true`.

* `streaming`: `data` is incomplete as a result of a deferred query and the result is still streaming in.

* `complete`: `data` is a fully satisfied query result fulfilled either from the cache or network.

###### [`error`*(optional)*](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#apolloqueryresult-error)

`ErrorLike`

A single ErrorLike object describing the error that occurred during the latest query execution.

For more information, see [Handling operation errors](https://www.apollographql.com/docs/react/data/error-handling.md).

###### [`partial`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#apolloqueryresult-partial)

`boolean`

> ⚠️ Deprecated
>
> This field will be removed in a future version of Apollo Client.

Describes whether `data` is a complete or partial result. This flag is only set when `returnPartialData` is `true` in query options.

Network info

###### [`loading`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#apolloqueryresult-loading)

`boolean`

If `true`, the query is still in flight.

###### [`networkStatus`](https://www.apollographql.com/docs/react/api/core/ObservableQuery.md#apolloqueryresult-networkstatus)

`NetworkStatus`

A number indicating the current network state of the query's associated request. [See possible values.](https://github.com/apollographql/apollo-client/blob/d96f4578f89b933c281bb775a39503f6cdb59ee8/src/core/networkStatus.ts#L4)

Used in conjunction with the [`notifyOnNetworkStatusChange`](https://www.apollographql.com/docs.md#notifyonnetworkstatuschange) option.
