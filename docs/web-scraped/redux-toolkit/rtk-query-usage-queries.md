# Source: https://redux-toolkit.js.org/rtk-query/usage/queries

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [Using RTK Query]
-   [Standard Usage]
-   [Queries]

On this page

 

<div>

# Queries

</div>

## Overview[​](#overview "Direct link to Overview") 

Queries are operations that fetch data from the server and cache it within the client. This is the most common use case for RTK Query. A query operation can be performed with any data fetching library of your choice, but the general recommendation is that you only use queries for requests that retrieve data. For anything that alters data on the server or will possibly invalidate the cache, you should use a [Mutation](/rtk-query/usage/mutations).

A query can cache the status and result of any async/promise method. Since the most common type of query is an HTTP request, RTK Query ships with [`fetchBaseQuery`](/rtk-query/api/fetchBaseQuery), which is a lightweight [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) wrapper that automatically handles request headers and response parsing in a manner similar to common libraries like `axios`. See [Customizing Queries](/rtk-query/usage/customizing-queries) if `fetchBaseQuery` does not handle your requirements.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Depending on your environment, you may need to polyfill `fetch` with `node-fetch` or `cross-fetch` if you choose to use `fetchBaseQuery` or `fetch` on its own.

See [`useQuery`](/rtk-query/api/created-api/hooks#usequery) for the hook signature and additional details.

## Defining Query Endpoints[​](#defining-query-endpoints "Direct link to Defining Query Endpoints") 

Query endpoints are defined by returning an object inside the `endpoints` section of `createApi`, and defining the fields using the `build.query()` method.

Query endpoints should define either a `query` callback that constructs the URL (including any URL query params), or [a `queryFn` callback](/rtk-query/usage/customizing-queries#customizing-queries-with-queryfn) that may do arbitrary async logic and return a result.

If the `query` callback needs additional data to generate the URL, it should be written to take a single argument. If you need to pass in multiple parameters, pass them formatted as a single \"options object\".

Query endpoints may also modify the response contents before the result is cached, define \"tags\" to identify cache invalidation, and provide cache entry lifecycle callbacks to run additional logic as cache entries are added and removed.

When used with TypeScript, you should supply generics for the return type and the expected query argument: `build.query<ReturnType, ArgType>`. If there is no argument, use `void` for the arg type instead.

-   TypeScript
-   JavaScript

Example of all query endpoint options

``` 
// Or from '@reduxjs/toolkit/query/react'
import  from '@reduxjs/toolkit/query'
import type  from './types'

const api = createApi(),
  tagTypes: ['Post'],
  endpoints: (build) => (` }),
      // Pick out data and prevent nested properties in a hook or selector
      transformResponse: (response: , meta, arg) => response.data,
      // Pick out errors and prevent nested properties in a hook or selector
      transformErrorResponse: (
        response: ,
        meta,
        arg,
      ) => response.status,
      providesTags: (result, error, id) => [],
      // The 2nd parameter is the destructured `QueryLifecycleApi`
      async onQueryStarted(
        arg,
        ,
      ) ,
      // The 2nd parameter is the destructured `QueryCacheLifecycleApi`
      async onCacheEntryAdded(
        arg,
        ,
      ) ,
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Example of all query endpoint options

``` 
// Or from '@reduxjs/toolkit/query/react'
import  from '@reduxjs/toolkit/query'

const api = createApi(),
  tagTypes: ['Post'],
  endpoints: (build) => (` }),
      // Pick out data and prevent nested properties in a hook or selector
      transformResponse: (response, meta, arg) => response.data,
      // Pick out errors and prevent nested properties in a hook or selector
      transformErrorResponse: (response, meta, arg) => response.status,
      providesTags: (result, error, id) => [],
      // The 2nd parameter is the destructured `QueryLifecycleApi`
      async onQueryStarted(
        arg,
        ,
      ) ,
      // The 2nd parameter is the destructured `QueryCacheLifecycleApi`
      async onCacheEntryAdded(
        arg,
        ,
      ) ,
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Performing Queries with React Hooks[​](#performing-queries-with-react-hooks "Direct link to Performing Queries with React Hooks") 

If you\'re using React Hooks, RTK Query does a few additional things for you. The primary benefit is that you get a render-optimized hook that allows you to have \'background fetching\' as well as [derived booleans](#frequently-used-query-hook-return-values) for convenience.

Hooks are automatically generated based on the name of the `endpoint` in the service definition. An endpoint field with `getPost: build.query()` will generate a hook named `useGetPostQuery`, as well as a generically-named hook attached to the endpoint, like `api.endpoints.getPost.useQuery`.

### Hook types[​](#hook-types "Direct link to Hook types") 

There are 5 query-related hooks:

1.  [`useQuery`](/rtk-query/api/created-api/hooks#usequery)
    -   Composes `useQuerySubscription` and `useQueryState` and is the primary hook. Automatically triggers fetches of data from an endpoint, \'subscribes\' the component to the cached data, and reads the request status and cached data from the Redux store.
2.  [`useQuerySubscription`](/rtk-query/api/created-api/hooks#usequerysubscription)
    -   Returns a `refetch` function and accepts all hook options. Automatically triggers fetches of data from an endpoint, and \'subscribes\' the component to the cached data.
3.  [`useQueryState`](/rtk-query/api/created-api/hooks#usequerystate)
    -   Returns the query state and accepts `skip` and `selectFromResult`. Reads the request status and cached data from the Redux store.
4.  [`useLazyQuery`](/rtk-query/api/created-api/hooks#uselazyquery)
    -   Returns a tuple with a `trigger` function, the query result, and last promise info. Similar to `useQuery`, but with manual control over when the data fetching occurs. **Note: the `trigger` function takes a second argument of `preferCacheValue?: boolean` in the event you want to skip making a request if cached data already exists.**
5.  [`useLazyQuerySubscription`](/rtk-query/api/created-api/hooks#uselazyquerysubscription)
    -   Returns a tuple with a `trigger` function, and last promise info. Similar to `useQuerySubscription`, but with manual control over when the data fetching occurs. **Note: the `trigger` function takes a second argument of `preferCacheValue?: boolean` in the event you want to skip making a request if cached data already exists.**

In practice, the standard `useQuery`-based hooks such as `useGetPostQuery` will be the primary hooks used in your application, but the other hooks are available for specific use cases.

### Query Hook Options[​](#query-hook-options "Direct link to Query Hook Options") 

The query hooks expect two parameters: `(queryArg?, queryOptions?)`.

The `queryArg` param will be passed through to the underlying `query` callback to generate the URL.

The `queryOptions` object accepts several additional parameters that can be used to control the behavior of the data fetching:

-   [skip](/rtk-query/usage/conditional-fetching) - Allows a query to \'skip\' running for that render. Defaults to `false`
-   [pollingInterval](/rtk-query/usage/polling) - Allows a query to automatically refetch on a provided interval, specified in milliseconds. Defaults to `0` *(off)*
-   [selectFromResult](#selecting-data-from-a-query-result) - Allows altering the returned value of the hook to obtain a subset of the result, render-optimized for the returned subset.
-   [refetchOnMountOrArgChange](/rtk-query/api/createApi#refetchonmountorargchange) - Allows forcing the query to always refetch on mount (when `true` is provided). Allows forcing the query to refetch if enough time (in seconds) has passed since the last query for the same cache (when a `number` is provided). Defaults to `false`
-   [refetchOnFocus](/rtk-query/api/createApi#refetchonfocus) - Allows forcing the query to refetch when the browser window regains focus. Defaults to `false`
-   [refetchOnReconnect](/rtk-query/api/createApi#refetchonreconnect) - Allows forcing the query to refetch when regaining a network connection. Defaults to `false`

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

All `refetch`-related options will override the defaults you may have set in [createApi](/rtk-query/api/createApi)

### Frequently Used Query Hook Return Values[​](#frequently-used-query-hook-return-values "Direct link to Frequently Used Query Hook Return Values") 

The query hook returns an object containing properties such as the latest `data` for the query request, as well as status booleans for the current request lifecycle state. Below are some of the most frequently used properties. Refer to [`useQuery`](/rtk-query/api/created-api/hooks#usequery) for an extensive list of all returned properties.

-   `data` - The latest returned result regardless of hook arg, if present.
-   `currentData` - The latest returned result for the current hook arg, if present.
-   `error` - The error result if present.
-   `isUninitialized` - When true, indicates that the query has not started yet.
-   `isLoading` - When true, indicates that the query is currently loading for the first time, and has no data yet. This will be `true` for the first request fired off, but *not* for subsequent requests.
-   `isFetching` - When true, indicates that the query is currently fetching, but might have data from an earlier request. This will be `true` for both the first request fired off, as well as subsequent requests.
-   `isSuccess` - When true, indicates that the query has data from a successful request.
-   `isError` - When true, indicates that the query is in an `error` state.
-   `refetch` - A function to force refetch the query

In most cases, you will probably read `data` and either `isLoading` or `isFetching` in order to render your UI.

### Query Hook Usage Example[​](#query-hook-usage-example "Direct link to Query Hook Usage Example") 

Here is an example of a `PostDetail` component:

Example

``` 
export const PostDetail = (: ) =>  = useGetPostQuery(id, )

  if (isLoading) return <div>Loading...</div>
  if (!post) return <div>Missing post!</div>

  return (
    <div>
       
    </div>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The way that this component is setup would have some nice traits:

1.  It only shows \'Loading\...\' on the **initial load**
    -   **Initial load** is defined as a query that is pending and does not have data in the cache
2.  When the request is re-triggered by the polling interval, it will add \'\...refetching\' to the post name
3.  If a user closed this `PostDetail`, but then re-opened it within [the allowed time](/rtk-query/api/createApi#keepunuseddatafor), they would immediately be served a cached result and polling would resume with the previous behavior.

### Query Loading State[​](#query-loading-state "Direct link to Query Loading State") 

The auto-generated React hooks created by the React-specific version of `createApi` provide [derived booleans](#frequently-used-query-hook-return-values) that reflect the current state of a given query. Derived booleans are preferred for the generated React hooks as opposed to a `status` flag, as the derived booleans are able to provide a greater amount of detail which would not be possible with a single `status` flag, as multiple statuses may be true at a given time (such as `isFetching` and `isSuccess`).

For query endpoints, RTK Query maintains a semantic distinction between `isLoading` and `isFetching` in order to provide more flexibility with the derived information provided.

-   `isLoading` refers to a query being in flight for the *first time* for the given hook. No data will be available at this time.
-   `isFetching` refers to a query being in flight for the given endpoint + query param combination, but not necessarily for the first time. Data may be available from an earlier request done by this hook, maybe with the previous query param.

This distinction allows for greater control when handling UI behavior. For example, `isLoading` can be used to display a skeleton while loading for the first time, while `isFetching` can be used to grey out old data when changing from page 1 to page 2 or when data is invalidated and re-fetched.

Managing UI behavior with Query Loading States

``` 
import  from './Skeleton'
import  from './api'

function App()  = useGetPostsQuery()

  if (isError) return <div>An error has occurred!</div>

  if (isLoading) return <Skeleton />

  return (
    <div className=>
      
          id=
          name=
          disabled=
        />
      ))}
    </div>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

While `data` is expected to be used in the majority of situations, `currentData` is also provided, which allows for a further level of granularity. For example, if you wanted to show data in the UI as translucent to represent a re-fetching state, you can use `data` in combination with `isFetching` to achieve this. However, if you also wish to *only* show data corresponding to the current arg, you can instead use `currentData` to achieve this.

In the example below, if posts are being fetched for the first time, a loading skeleton will be shown. If posts for the current user have previously been fetched, and are re-fetching (e.g. as a result of a mutation), the UI will show the previous data, but will grey out the data. If the user changes, it will instead show the skeleton again as opposed to greying out data for the previous user.

Managing UI behavior with currentData

``` 
import  from './Skeleton'
import  from './api'

function PostsList(: )  = useGetPostsByUserQuery(userName)

  if (isError) return <div>An error has occurred!</div>

  if (isFetching && !currentData) return <Skeleton />

  return (
    <div className=>
      
              id=
              name=
              disabled=
            />
          ))
        : 'No data available'}
    </div>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Query Cache Keys[​](#query-cache-keys "Direct link to Query Cache Keys") 

When you perform a query, RTK Query automatically serializes the request parameters and creates an internal `queryCacheKey` for the request. Any future request that produces the same `queryCacheKey` will be de-duped against the original, and will share updates if a `refetch` is triggered on the query from any subscribed component.

### Selecting data from a query result[​](#selecting-data-from-a-query-result "Direct link to Selecting data from a query result") 

Sometimes you may have a parent component that is subscribed to a query, and then in a child component you want to pick an item from that query. In most cases you don\'t want to perform an additional request for a `getItemById`-type query when you know that you already have the result.

`selectFromResult` allows you to get a specific segment from a query result in a performant manner. When using this feature, the component will not rerender unless the underlying data of the selected item has changed. If the selected item is one element in a larger collection, it will disregard changes to elements in the same collection.

Using selectFromResult to extract a single result

``` 
function PostsList()  = api.useGetPostsQuery()

  return (
    <ul>
       id= />)}
    </ul>
  )
}

function PostById(: )  = api.useGetPostsQuery(undefined, ) => (),
  })

  return <li></li>
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Note that a shallow equality check is performed on the overall return value of `selectFromResult` to determine whether to force a rerender. i.e. it will trigger a rerender if any of the returned object values change reference. If a new array/object is created and used as a return value within the callback, it will hinder the performance benefits due to being identified as a new item each time the callback is run. When intentionally providing an empty array/object, in order to avoid re-creating it each time the callback runs, you can declare an empty array/object outside of the component in order to maintain a stable reference.

Using selectFromResult with a stable empty array

``` 
// An array declared here will maintain a stable reference rather than be re-created again
const emptyArray: Post[] = []

function PostsList()  = api.useGetPostsQuery(undefined, ) => (),
  })

  return (
    <ul>
       id= />
      ))}
    </ul>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

To summarize the above behavior - the returned values must be correctly memoized. See also [Deriving Data with Selectors](https://redux.js.org/usage/deriving-data-selectors) and [Redux Essentials - RTK Query Advanced Patterns](https://redux.js.org/tutorials/essentials/part-8-rtk-query-advanced#selecting-values-from-results) for additional information.

### Avoiding unnecessary requests[​](#avoiding-unnecessary-requests "Direct link to Avoiding unnecessary requests") 

By default, if you add a component that makes the same query as an existing one, no request will be performed.

In some cases, you may want to skip this behavior and force a refetch - in that case, you can call `refetch` that is returned by the hook.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

If you\'re not using React Hooks, you can access `refetch` like this:

``` 
const  = dispatch(
  pokemonApi.endpoints.getPokemon.initiate('bulbasaur'),
)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Runtime Validation using Schemas[​](#runtime-validation-using-schemas "Direct link to Runtime Validation using Schemas") 

Endpoints can use any [Standard Schema](https://standardschema.dev/) compliant library for runtime validation of query args, responses, and errors. See [API reference](/rtk-query/api/createApi#schema-validation) for full list of available schemas.

When used with TypeScript, schemas can also be used to [infer the type of that value instead of having to declare it](/rtk-query/usage-with-typescript#schema-validation).

Most commonly, you\'ll want to use `responseSchema` to validate the response from the server (or `rawResponseSchema` when using `transformResponse`).

Using responseSchema

``` 
import  from '@reduxjs/toolkit/query/react'
import * as v from 'valibot'

const postSchema = v.object()
type Post = v.InferOutput<typeof postSchema>
const transformedPost = v.object()
type TransformedPost = v.InferOutput<typeof transformedPost>

const api = createApi(),
  endpoints: (build) => (>() => `/post/$`,
      responseSchema: postSchema,
    }),
    getTransformedPost: build.query<TransformedPost, >() => `/post/$`,
      rawResponseSchema: postSchema,
      transformResponse: (response) => (),
      // responseSchema can still be provided, to validate the transformed response
      responseSchema: transformedPost,
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Example: Observing caching behavior[​](#example-observing-caching-behavior "Direct link to Example: Observing caching behavior") 

This example demonstrates request deduplication and caching behavior:

1.  The first `Pokemon` component mounts and immediately fetches \'bulbasaur\'
2.  A second later, another `Pokemon` component is rendered with \'bulbasaur\'
    -   Notice that this one doesn\'t ever show \'Loading\...\' and no new network request happens? It\'s using the cache here.
3.  A moment after that, a `Pokemon` component for \'pikachu\' is added, and a new request happens.
4.  When you click \'Refetch\' for a specific `Pokemon`, it\'ll update all instances of that `Pokemon` with one request.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]Try it out

Click the \'Add bulbasaur\' button. You\'ll observe the same behavior described above until you click the \'Refetch\' button on one of the components.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/usage/queries.mdx)

[Last updated on **Apr 12, 2025**]