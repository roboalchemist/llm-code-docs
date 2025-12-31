# Source: https://redux-toolkit.js.org/rtk-query/usage/usage-without-react-hooks

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [Using RTK Query]
-   [Advanced Use Cases]
-   [Usage Without React Hooks]

On this page

 

<div>

# Usage Without React Hooks

</div>

Like the Redux core and Redux Toolkit, RTK Query\'s primary functionality is UI-agnostic and can be used with any UI layer. RTK Query also includes a version of [`createApi`](/rtk-query/api/createApi) designed specifically for use with React, which [automatically generates React hooks](/rtk-query/api/created-api/hooks).

While React hooks are the primary way that the majority of users are expected to be using RTK Query, the library itself uses plain JS logic and can be used both with React Class components, and independent of React itself.

This page documents how to interact with RTK Query when used without React Hooks, in order to make proper use of RTK Query [`cache behavior`](/rtk-query/usage/cache-behavior).

## Adding a subscription[​](#adding-a-subscription "Direct link to Adding a subscription") 

Cache subscriptions are used to tell RTK Query that it needs to fetch data for an endpoint. A subscription for an endpoint can be added by dispatching the result of the [`initiate`](/rtk-query/api/created-api/endpoints#initiate) thunk action creator attached to a query endpoint.

With React hooks, this behavior is instead handled within [`useQuery`](/rtk-query/api/created-api/hooks#usequery), [`useQuerySubscription`](/rtk-query/api/created-api/hooks#usequerysubscription), [`useLazyQuery`](/rtk-query/api/created-api/hooks#uselazyquery), and [`useLazyQuerySubscription`](/rtk-query/api/created-api/hooks#uselazyquerysubscription).

Subscribing to cached data

``` 
const promise = dispatch(api.endpoints.getPosts.initiate())
const  = promise
// interact with the cache in the same way as you would with a useFetch...() hook
const  = await promise
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Removing a subscription[​](#removing-a-subscription "Direct link to Removing a subscription") 

Removing a cache subscription is necessary for RTK Query to identify that cached data is no longer required. This allows RTK Query to clean up and remove old cache data.

The result of dispatching the [`initiate`](/rtk-query/api/created-api/endpoints#initiate) thunk action creator of a query endpoint is a Promise with an `unsubscribe` property. This property is a function that when called, will remove the corresponding cache subscription.

With React hooks, this behavior is instead handled within [`useQuery`](/rtk-query/api/created-api/hooks#usequery), [`useQuerySubscription`](/rtk-query/api/created-api/hooks#usequerysubscription), [`useLazyQuery`](/rtk-query/api/created-api/hooks#uselazyquery), and [`useLazyQuerySubscription`](/rtk-query/api/created-api/hooks#uselazyquerysubscription).

Unsubscribing from cached data

``` 
// Adding a cache subscription
const promise = dispatch(api.endpoints.getPosts.initiate())

// Removing the corresponding cache subscription
promise.unsubscribe()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Accessing cached data & request status[​](#accessing-cached-data--request-status "Direct link to Accessing cached data & request status") 

Accessing cache data and request status information can be performed using the `select` function property of a query endpoint to create a selector and call that with the Redux state. This provides a snapshot of the cache data and request status information at the time it is called.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

The `endpoint.select(arg)` function creates a *new* selector instance - it isn\'t the actual selector function itself!

With React hooks, this behavior is instead handled within [`useQuery`](/rtk-query/api/created-api/hooks#usequery), [`useQueryState`](/rtk-query/api/created-api/hooks#usequerystate), and [`useLazyQuery`](/rtk-query/api/created-api/hooks#uselazyquery).

Accessing cached data & request status

``` 
const result = api.endpoints.getPosts.select()(state)
const  = result
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Note that unlike with the auto-generated hooks, there is no `isFetching` flag, and the `isLoading` flag will be true if the status is pending, regardless of if there is already data.

### Memoization[​](#memoization "Direct link to Memoization") 

Because the `endpoint.select(arg)` function returns a new selector each time it\'s called, and because this instance itself is memoized, it can be desirable to memoize the creation of a selector (for example, to then use that memoized instance in another selector). This can be done with `createSelector`:

Creating a memoized selector creator

``` 
const createGetPostSelector = createSelector(
  (id: string) => id,
  (id) => api.endpoints.getPost.select(id),
)

const selectGetPostError = createSelector(
  (state: RootState) => state,
  (state: RootState, id: string) => createGetPostSelector(id),
  (state, selectGetPost) => selectGetPost(state).error,
)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Performing mutations[​](#performing-mutations "Direct link to Performing mutations") 

[Mutations](/rtk-query/usage/mutations) are used in order to update data on the server. Mutations can be performed by dispatching the result of the [`initiate`](/rtk-query/api/created-api/endpoints#initiate) thunk action creator attached to a mutation endpoint.

With React hooks, this behavior is instead handled within [`useMutation`](/rtk-query/api/created-api/hooks#usemutation).

Triggering a mutation endpoint

``` 
dispatch(api.endpoints.addPost.initiate())
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Examples[​](#examples "Direct link to Examples") 

Examples of usage without React hooks can be found under the following:

-   The `PostDetail` component in the [`React Class Components` example](/rtk-query/usage/examples#react-class-components)
-   The [`Svelte` example](/rtk-query/usage/examples#svelte)
-   The below `Cache Lifetime Subscription Class Component` example:

## Further Information[​](#further-information "Direct link to Further Information") 

-   NgRx maintainer Brandon Roberts has written a post called [Cousins playing nicely: Experimenting with NgRx Store and RTK Query](https://dev.to/brandontroberts/cousins-playing-nicely-experimenting-with-ngrx-store-and-rtk-query-25f4), which demonstrates some approaches for integrating RTK Query into NgRx
-   [`saulmoro/ngrx-rtk-query`](https://github.com/SaulMoro/ngrx-rtk-query) implements an NgRx equivalent of the subscription lifecycle managed in RTKQ\'s own React hooks

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/usage/usage-without-react-hooks.mdx)

[Last updated on **Aug 11, 2024**]