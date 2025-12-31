# Source: https://redux-toolkit.js.org/rtk-query/api/created-api/hooks

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [API Reference]
-   [Generated API Slices]
-   [React Hooks]

On this page

 

<div>

# API Slices: React Hooks

</div>

## Hooks Overview[​](#hooks-overview "Direct link to Hooks Overview") 

The core RTK Query `createApi` method is UI-agnostic, in the same way that the Redux core library and Redux Toolkit are UI-agnostic. They are all plain JS logic that can be used anywhere. So, if you import `createApi` from `'@reduxjs/toolkit/query'`, it does not have any specific UI integrations included.

However, RTK Query also provides the ability to auto-generate React hooks for each of your endpoints. Since this specifically depends on React itself, RTK Query provides an additional entry point that exposes a customized version of `createApi` that includes that functionality:

``` 
import  from '@reduxjs/toolkit/query/react'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

If you have used the React-specific version of `createApi`, the generated `api` slice structure will also contain a set of React hooks. The primary endpoint hooks are available as `api.endpoints[endpointName].useQuery`, `api.endpoints[endpointName].useMutation`, and `api.endpoints[endpointName].useInfiniteQuery`, matching how you defined that endpoint.

### Generated Hook Names[​](#generated-hook-names "Direct link to Generated Hook Names") 

The same hooks are also added to the `api` object itself, and given auto-generated names based on the endpoint name and query/mutation type.

For example, if you had endpoints for `getPosts` and `updatePost`, these options would be available:

Generated React Hook names

``` 
// Hooks attached to the endpoint definition
const  = api.endpoints.getPosts.useQuery()
const [updatePost, ] = api.endpoints.updatePost.useMutation()

// Same hooks, but given unique names and attached to the API slice object
const  = api.useGetPostsQuery()
const [updatePost, ] = api.useUpdatePostMutation()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The general format is `use(Endpointname)(Query|Mutation|InfiniteQuery)` - `use` is prefixed, the first letter of your endpoint name is capitalized, then `Query` or `Mutation` or `InfiniteQuery` is appended depending on the type.

### Available Hooks[​](#available-hooks "Direct link to Available Hooks") 

RTK Query provides additional hooks for more advanced use-cases, although not all are generated directly on the `api` object as well.

Most of the hooks are generated on a per-endpoint basis.

The full list of hooks generated in the React-specific version of `createApi` is:

-   Endpoint-specific, generated the `api` object with a unique name and on the endpoint object with a generic name:
    -   [`useQuery`](#usequery) (all standard queries)
    -   [`useMutation`](#usemutation) (all mutations)
    -   [`useInfiniteQuery`](#useinfinitequery) (only infinite queries)
    -   [`useLazyQuery`](#uselazyquery) (all standard queries)
-   Endpoint-specific, only generated on the endpoint object with a generic name:
    -   [`useQueryState`](#usequerystate)
    -   [`useQuerySubscription`](#usequerysubscription)
    -   [`useLazyQuerySubscription`](#uselazyquerysubscription)
    -   [`useInfiniteQueryState`](#useinfinitequerystate)
    -   [`useInfiniteQuerySubscription`](#useinfinitequerysubscription)
-   Endpoint-agnostic, generated on the `api` object:
    -   [`usePrefetch`](#useprefetch)

For the example above, the full set of generated hooks for the api would be like so:

Generated React Hooks

``` 
/* Hooks attached to the `getPosts` query endpoint definition */
api.endpoints.getPosts.useQuery(arg, options)
api.endpoints.getPosts.useQueryState(arg, options)
api.endpoints.getPosts.useQuerySubscription(arg, options)
api.endpoints.getPosts.useLazyQuery(options)
api.endpoints.getPosts.useLazyQuerySubscription(options)

/* hooks attached to the `getManyPosts` infinite query endpoint definition */
api.endpoints.getManyPosts.useInfiniteQuery(arg, options)
api.endpoints.getManyPosts.useInfiniteQueryState(arg, options)
api.endpoints.getManyPosts.useInfiniteQuerySubscription(arg, options)

/* Hooks attached to the `updatePost` mutation endpoint definition */
api.endpoints.updatePost.useMutation(options)

/* Hooks attached to the `api` object */
// same as api.endpoints.getPosts.useQuery
api.useGetPostsQuery(arg, options)
// same as api.endpoints.getPosts.useLazyQuery
api.useLazyGetPostsQuery(arg, options)
// same as api.endpoints.updatePost.useMutation
api.useUpdatePostMutation(arg, options)
// same as api.endpoints.getManyPosts.useInfiniteQuery
api.useGetManyPostsInfiniteQuery(arg, options)
// Generic, used for any endpoint
api.usePrefetch(endpointName, options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Feature Comparison[​](#feature-comparison "Direct link to Feature Comparison") 

The provided hooks have a degree of feature overlap in order to provide options optimized for a given situation. The table below provides a comparison of the core features for each hook.

Feature

[useQuery](#usequery)

[useMutation](#usemutation)

[useQueryState](#usequerystate)

[useQuerySubscription](#usequerysubscription)

[useLazyQuery](#uselazyquery)

[useLazyQuerySubscription](#uselazyquerysubscription)

[usePrefetch](#useprefetch)

Automatically triggers query requests

✔️

✔️

Allows manually triggering query requests

✔️

✔️

✔️

✔️

✔️

Allows manually triggering mutation requests

✔️

Subscribes a component to keep cached data in the store

✔️

✔️

✔️

✔️

✔️

Returns request status and cached data from the store

✔️

✔️

✔️

✔️

Re-renders as request status and data become available

✔️

✔️

✔️

✔️

Accepts polling/re-fetching options to trigger automatic re-fetches

✔️

✔️

✔️

✔️

## Primary Hooks[​](#primary-hooks "Direct link to Primary Hooks") 

These hooks are the main methods you will use to interact with RTK Query in your React components. They encapsulate all of logic and options needed for most data fetching and update use cases.

### `useQuery`[​](#usequery "Direct link to usequery") 

Accessing a useQuery hook

``` 
const useQueryResult = api.endpoints.getPosts.useQuery(arg, options)
// or
const useQueryResult = api.useGetPostsQuery(arg, options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook that automatically triggers fetches of data from an endpoint, \'subscribes\' the component to the cached data, and reads the request status and cached data from the Redux store. The component will re-render as the loading status changes and the data becomes available.

The query arg is used as a cache key. Changing the query arg will tell the hook to re-fetch the data if it does not exist in the cache already, and the hook will return the data for that query arg once it\'s available.

This hook combines the functionality of both [`useQueryState`](#usequerystate) and [`useQuerySubscription`](#usequerysubscription) together, and is intended to be used in the majority of situations.

#### Features

-   Automatically triggers requests to retrieve data based on the hook argument and whether cached data exists by default
-   \'Subscribes\' the component to keep cached data in the store, and \'unsubscribes\' when the component unmounts
-   Accepts polling/re-fetching options to trigger automatic re-fetches when the corresponding criteria is met
-   Returns the latest request status and cached data from the Redux store
-   Re-renders as the request status changes and data becomes available

#### `useQuery` Signature[​](#usequery-signature "Direct link to usequery-signature") 

``` 
type UseQuery = (
  arg: any | SkipToken,
  options?: UseQueryOptions,
) => UseQueryResult

type UseQueryOptions = 

type UseQueryResult<T> = 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   **Parameters**
    -   `arg`: The query argument to be used in constructing the query itself, and as a cache key for the query. You can also pass in `skipToken` here as an alternative way of skipping the query, see [skipToken](#skiptoken)
    -   `options`: A set of options that control the fetching behavior of the hook
-   **Returns**
    -   A query result object containing the current loading state, the actual data or error returned from the API call, metadata about the request, and a function to `refetch` the data. Can be customized with `selectFromResult`

#### `skipToken`[​](#skiptoken "Direct link to skiptoken") 

Can be passed into `useQuery`, `useQueryState` or `useQuerySubscription` instead of the query argument to get the same effect as if setting `skip: true` in the query options.

Useful for scenarios where a query should be skipped when `arg` is `undefined` and TypeScript complains about it because `arg` is not allowed to be passed in as `undefined`, such as

will error if the query argument is not allowed to be undefined

``` 
useSomeQuery(arg, )
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

using skipToken instead

``` 
useSomeQuery(arg ?? skipToken)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

If passed directly into a query or mutation selector, that selector will always return an uninitialized state.

See also [Skipping queries with TypeScript using `skipToken`](/rtk-query/usage-with-typescript#skipping-queries-with-typescript-using-skiptoken)

### `useMutation`[​](#usemutation "Direct link to usemutation") 

Accessing a useMutation hook

``` 
const useMutationResult = api.endpoints.updatePost.useMutation(options)
// or
const useMutationResult = api.useUpdatePostMutation(options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook that lets you trigger an update request for a given endpoint, and subscribes the component to read the request status from the Redux store. The component will re-render as the loading status changes.

#### Features

-   Manual control over firing a request to alter data on the server or possibly invalidate the cache
-   \'Subscribes\' the component to keep cached data in the store, and \'unsubscribes\' when the component unmounts
-   Returns the latest request status and cached data from the Redux store
-   Re-renders as the request status changes and data becomes available

#### `useMutation` Signature[​](#usemutation-signature "Direct link to usemutation-signature") 

``` 
type UseMutation = (
  options?: UseMutationStateOptions,
) => [UseMutationTrigger, UseMutationResult | SelectedUseMutationResult]

type UseMutationStateOptions = 

type UseMutationTrigger<T> = (arg: any) => Promise<
   | 
> & 

type UseMutationResult<T> = 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

The generated `UseMutation` hook will cause a component to re-render by default after the trigger callback is fired, as it affects the properties of the result. If you want to call the trigger but don\'t care about subscribing to the result with the hook, you can use the `selectFromResult` option to limit the properties that the hook cares about.

Returning a completely empty object will mean that any individual mutation call will cause only one re-render at most, e.g.

``` 
selectFromResult: () => ()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   **Parameters**

    -   `options`: A set of options that control the subscription behavior of the hook:
        -   `selectFromResult`: A callback that can be used to customize the mutation result returned as the second item in the tuple
        -   `fixedCacheKey`: An optional string used to enable shared results across hook instances

-   **Returns**: A tuple containing:

    -   `trigger`: A function that triggers an update to the data based on the provided argument. The trigger function returns a promise with the properties shown above that may be used to handle the behavior of the promise
    -   `mutationState`: A query status object containing the current loading state and metadata about the request, or the values returned by the `selectFromResult` option where applicable. Additionally, this object will contain
        -   a `reset` method to reset the hook back to its original state and remove the current result from the cache
        -   an `originalArgs` property that contains the argument passed to the last call of the `trigger` function.

### `useInfiniteQuery`[​](#useinfinitequery "Direct link to useinfinitequery") 

Accessing a useQuery hook

``` 
const useQueryResult = api.endpoints.getManyPosts.useInfiniteQuery(arg, options)
// or
const useQueryResult = api.useGetManyPostsInfiniteQuery(arg, options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook that automatically triggers fetches of data from an endpoint, \'subscribes\' the component to the cached data, and reads the request status and cached data from the Redux store. The component will re-render as the loading status changes and the data becomes available. Additionally, it will cache multiple \"pages\" worth of responses within a single cache entry, and allows fetching more pages forwards and backwards from the current cached pages.

The query arg is used as a cache key. Changing the query arg will tell the hook to re-fetch the data if it does not exist in the cache already, and the hook will return the data for that query arg once it\'s available.

The `data` field will be a `` structure containing all fetched page responses and the corresponding page param values for each page. You may use this to render individual pages, combine all pages into a single infinite list, or other display logic as needed.

This hook combines the functionality of both [`useInfiniteQueryState`](#useinfinitequerystate) and [`useInfiniteQuerySubscription`](#useinfinitequerysubscription) together, and is intended to be used in the majority of situations.

As with normal query hooks, `skipToken` is a valid argument that will skip the query from executing.

By default, the initial request will use the `initialPageParam` value that was defined on the infinite query endpoint. If you want to start from a different value, you can pass `initialPageParam` as part of the hook options to override that initial request value.

Use the returned `fetchNextPage` and `fetchPreviousPage` methods on the hook result object to trigger fetches forwards and backwards. These will always calculate the next or previous page param based on the current cached pages and the provided `getNext/PreviousPageParam` callbacks defined in the endpoint.

#### Features

-   Automatically triggers requests to retrieve data based on the hook argument and whether cached data exists by default
-   \'Subscribes\' the component to keep cached data in the store, and \'unsubscribes\' when the component unmounts
-   Caches multiple pages worth of responses, and provides methods to trigger more page fetches forwards and backwards
-   Accepts polling/re-fetching options to trigger automatic re-fetches when the corresponding criteria is met
-   Returns the latest request status and cached data from the Redux store
-   Re-renders as the request status changes and data becomes available

#### `useInfiniteQuery` Signature[​](#useinfinitequery-signature "Direct link to useinfinitequery-signature") 

``` 
type UseInfiniteQuery = (
  arg: any | SkipToken,
  options?: UseQueryOptions,
) => UseInfiniteQueryResult

type InfiniteData<Data, PageParam> = 

type UseInfiniteQueryOptions = 

type UseInfiniteQueryResult<Data, PageParam> = ) => InfiniteQueryActionCreatorResult

  // Triggers a fetch for the next page, based on the current cache
  fetchNextPage: () => InfiniteQueryActionCreatorResult
  // Triggers a fetch for the previous page, based on the current cache
  fetchPreviousPage: () => InfiniteQueryActionCreatorResult
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   **Parameters**
    -   `arg`: The query argument to be used in constructing the query itself, and as a cache key for the query. You can also pass in `skipToken` here as an alternative way of skipping the query, see [skipToken](#skiptoken)
    -   `options`: A set of options that control the fetching behavior of the hook
-   **Returns**
    -   A query result object containing the current loading state, the actual data or error returned from the API call, metadata about the request, and a function to `refetch` the data. Can be customized with `selectFromResult`

## Secondary Hooks[​](#secondary-hooks "Direct link to Secondary Hooks") 

These hooks are useful for specific additional use cases in your application, but will probably not be used that frequently.

### `useLazyQuery`[​](#uselazyquery "Direct link to uselazyquery") 

Accessing a useLazyQuery hook

``` 
const [trigger, result, lastPromiseInfo] =
  api.endpoints.getPosts.useLazyQuery(options)
// or
const [trigger, result, lastPromiseInfo] = api.useLazyGetPostsQuery(options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook similar to [`useQuery`](#usequery), but with manual control over when the data fetching occurs.

This hook includes the functionality of [`useLazyQuerySubscription`](#uselazyquerysubscription).

#### Features

-   Manual control over firing a request to retrieve data
-   \'Subscribes\' the component to keep cached data in the store, and \'unsubscribes\' when the component unmounts
-   Returns the latest request status and cached data from the Redux store
-   Re-renders as the request status changes and data becomes available
-   Accepts polling/re-fetching options to trigger automatic re-fetches when the corresponding criteria is met and the fetch has been manually called at least once

#### Note

When the trigger function returned from a LazyQuery is called, it always initiates a new request to the server even if there is cached data. Set `preferCacheValue`(the second argument to the function) as `true` if you want it to immediately return a cached value if one exists.

#### `useLazyQuery` Signature[​](#uselazyquery-signature "Direct link to uselazyquery-signature") 

``` 
type UseLazyQuery = (
  options?: UseLazyQueryOptions
) => [UseLazyQueryTrigger, UseLazyQueryStateResult, UseLazyQueryLastPromiseInfo]

type UseLazyQueryOptions = 

type UseLazyQueryTrigger<T> = (arg: any, preferCacheValue?: boolean) => Promise<
  QueryResultSelectorResult
> & 

type UseLazyQueryStateResult<T> = 

type UseLazyQueryLastPromiseInfo = 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   **Parameters**

    -   `options`: A set of options that control the fetching behavior and returned result value of the hook. Options affecting fetching behavior will only have an effect after the lazy query has been triggered at least once.

-   **Returns**: A tuple containing:

    -   `trigger`: A function that fetches the corresponding data for the endpoint when called
    -   `result`: A query result object containing the current loading state, the actual data or error returned from the API call and metadata about the request. Can be customized with `selectFromResult`
    -   `lastPromiseInfo`: An object containing the last argument used to call the trigger function

### `usePrefetch`[​](#useprefetch "Direct link to useprefetch") 

Accessing a usePrefetch hook

``` 
const prefetchCallback = api.usePrefetch(endpointName, options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook which can be used to initiate fetching data ahead of time.

##### Features[​](#features "Direct link to Features") 

-   Manual control over firing a request to retrieve data

##### Signature[​](#signature "Direct link to Signature") 

``` 
type UsePrefetch = (
  endpointName: string,
  options?: UsePrefetchOptions,
) => PrefetchCallback

type UsePrefetchOptions =
  | 
  | 

type PrefetchCallback = (arg: any, options?: UsePrefetchOptions) => void
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   **Parameters**

    -   `endpointName`: The name of the endpoint to prefetch data for
    -   `options`: A set of options that control whether the prefetch request should occur

-   **Returns**

    -   A `prefetch` callback that when called, will initiate fetching the data for the provided endpoint

## Implementation Hooks[​](#implementation-hooks "Direct link to Implementation Hooks") 

This hooks exist as implementation details of the primary hooks. They may be useful in rare cases, but you should generally use the primary hooks in your apps.

### `useQueryState`[​](#usequerystate "Direct link to usequerystate") 

Accessing a useQuery hook

``` 
const useQueryStateResult = api.endpoints.getPosts.useQueryState(arg, options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook that reads the request status and cached data from the Redux store. The component will re-render as the loading status changes and the data becomes available.

Note that this hook does not trigger fetching new data. For that use-case, see [`useQuery`](#usequery) or [`useQuerySubscription`](#usequerysubscription).

#### Features 

-   Returns the latest request status and cached data from the Redux store
-   Re-renders as the request status changes and data becomes available

##### `useQueryState` Signature[​](#usequerystate-signature "Direct link to usequerystate-signature") 

``` 
type UseQueryState = (
  arg: any | SkipToken,
  options?: UseQueryStateOptions,
) => UseQueryStateResult | SelectedQueryStateResult

type UseQueryStateOptions = 

type UseQueryStateResult<T> = 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   **Parameters**

    -   `arg`: The argument passed to the query defined in the endpoint. You can also pass in `skipToken` here as an alternative way of skipping the selection, see [skipToken](#skiptoken)
    -   `options`: A set of options that control the return value for the hook

-   **Returns**

    -   A query result object containing the current loading state, the actual data or error returned from the API call and metadata about the request. Can be customized with `selectFromResult`

### `useQuerySubscription`[​](#usequerysubscription "Direct link to usequerysubscription") 

Accessing a useQuerySubscription hook

``` 
const  = api.endpoints.getPosts.useQuerySubscription(arg, options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook that automatically triggers fetches of data from an endpoint, and \'subscribes\' the component to the cached data.

The query arg is used as a cache key. Changing the query arg will tell the hook to re-fetch the data if it does not exist in the cache already.

Note that this hook does not return a request status or cached data. For that use-case, see [`useQuery`](#usequery) or [`useQueryState`](#usequerystate).

#### Features 

-   Automatically triggers requests to retrieve data based on the hook argument and whether cached data exists by default
-   \'Subscribes\' the component to keep cached data in the store, and \'unsubscribes\' when the component unmounts
-   Accepts polling/re-fetching options to trigger automatic re-fetches when the corresponding criteria is met

##### `useQuerySubscription` Signature[​](#usequerysubscription-signature "Direct link to usequerysubscription-signature") 

``` 
type UseQuerySubscription = (
  arg: any | SkipToken,
  options?: UseQuerySubscriptionOptions,
) => UseQuerySubscriptionResult

type UseQuerySubscriptionOptions = 

type UseQuerySubscriptionResult = 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   **Parameters**

    -   `arg`: The argument passed to the query defined in the endpoint. You can also pass in `skipToken` here as an alternative way of skipping the query, see [skipToken](#skiptoken)
    -   `options`: A set of options that control the fetching behavior of the hook

-   **Returns**

    -   An object containing a function to `refetch` the data

### `useInfiniteQueryState`[​](#useinfinitequerystate "Direct link to useinfinitequerystate") 

Accessing a useInfiniteQueryState hook

``` 
const useInfiniteQueryStateResult =
  api.endpoints.getManyPosts.useInfiniteQueryState(arg, options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook that reads the request status and cached data from the Redux store. The component will re-render as the loading status changes and the data becomes available.

Note that this hook does not trigger fetching new data. For that use-case, see [`useInfiniteQuery`](#useinfinitequery) or [`useInfiniteQuerySubscription`](#useinfinitequerysubscription).

#### Features 

-   Returns the latest request status and cached data from the Redux store
-   Re-renders as the request status changes and data becomes available

### `useInfiniteQuerySubscription`[​](#useinfinitequerysubscription "Direct link to useinfinitequerysubscription") 

Accessing a useInfiniteQuerySubscription hook

``` 
const useInfiniteQuerySubscriptionResult =
  api.endpoints.getManyPosts.useInfiniteQuerySubscription(arg, options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook that automatically triggers fetches of data from an endpoint, and \'subscribes\' the component to the cached data. Additionally, it will cache multiple \"pages\" worth of responses within a single cache entry, and allows fetching more pages forwards and backwards from the current cached pages.

The query arg is used as a cache key. Changing the query arg will tell the hook to re-fetch the data if it does not exist in the cache already.

Note that this hook does not return a request status or cached data. For that use-case, see [`useInfiniteQuery`](#useinfinitequery) or [`useInfiniteQueryState`](#useinfinitequerystate).

#### Features 

-   Automatically triggers requests to retrieve data based on the hook argument and whether cached data exists by default
-   \'Subscribes\' the component to keep cached data in the store, and \'unsubscribes\' when the component unmounts
-   Caches multiple pages worth of responses, and provides methods to trigger more page fetches forwards and backwards
-   Accepts polling/re-fetching options to trigger automatic re-fetches when the corresponding criteria is met

### `useLazyQuerySubscription`[​](#uselazyquerysubscription "Direct link to uselazyquerysubscription") 

Accessing a useLazyQuerySubscription hook

``` 
const [trigger, lastArg] =
  api.endpoints.getPosts.useLazyQuerySubscription(options)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A React hook similar to [`useQuerySubscription`](#usequerysubscription), but with manual control over when the data fetching occurs.

Note that this hook does not return a request status or cached data. For that use-case, see [`useLazyQuery`](#uselazyquery).

#### Features 

-   Manual control over firing a request to retrieve data
-   \'Subscribes\' the component to keep cached data in the store, and \'unsubscribes\' when the component unmounts
-   Accepts polling/re-fetching options to trigger automatic re-fetches when the corresponding criteria is met and the fetch has been manually called at least once

##### `useLazyQuerySubscription` Signature[​](#uselazyquerysubscription-signature "Direct link to uselazyquerysubscription-signature") 

``` 
type UseLazyQuerySubscription = (
  options?: UseLazyQuerySubscriptionOptions,
) => [UseLazyQuerySubscriptionTrigger, LastArg]

type UseLazyQuerySubscriptionOptions = 

type UseLazyQuerySubscriptionTrigger = (
  arg: any,
  preferCacheValue?: boolean,
) => void
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   **Parameters**

    -   `options`: A set of options that control the fetching behavior of the hook. The options will only have an effect after the lazy query has been triggered at least once.

-   **Returns**: A tuple containing:

    -   `trigger`: A function that fetches the corresponding data for the endpoint when called
    -   `lastArg`: The last argument used to call the trigger function

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/api/created-api/hooks.mdx)

[Last updated on **Nov 23, 2025**]