# Source: https://redux-toolkit.js.org/rtk-query/usage/cache-behavior

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [Using RTK Query]
-   [Standard Usage]
-   [Cache Behavior]

On this page

 

<div>

# Cache Behavior

</div>

A key feature of RTK Query is its management of cached data. When data is fetched from the server, RTK Query will store the data in the Redux store as a \'cache\'. When an additional request is performed for the same data, RTK Query will provide the existing cached data rather than sending an additional request to the server.

RTK Query provides a number of concepts and tools to manipulate the cache behavior and adjust it to your needs.

## Default Cache Behavior[​](#default-cache-behavior "Direct link to Default Cache Behavior") 

With RTK Query, caching is based on:

-   API endpoint definitions
-   The serialized query parameters used when components subscribe to data from an endpoint
-   Active subscription reference counts

When a subscription is started, the parameters used with the endpoint are serialized and stored internally as a `queryCacheKey` for the request. Any future request that produces the same `queryCacheKey` (i.e. called with the same parameters, factoring serialization) will be de-duped against the original, and will share the same data and updates. i.e. two separate components performing the same request will use the same cached data.

When a request is attempted, if the data already exists in the cache, then that data is served and no new request is sent to the server. Otherwise, if the data does not exist in the cache, then a new request is sent, and the returned response is stored in the cache.

Subscriptions are reference-counted. Additional subscriptions that ask for the same endpoint+params increment the reference count. As long as there is an active \'subscription\' to the data (e.g. if a component is mounted that calls a `useQuery` hook for the endpoint), then the data will remain in the cache. Once the subscription is removed (e.g. when last component subscribed to the data unmounts), after an amount of time (default 60 seconds), the data will be removed from the cache. The expiration time can be configured with the `keepUnusedDataFor` property for the [API definition as a whole](/rtk-query/api/createApi#keepunuseddatafor), as well as on a [per-endpoint](/rtk-query/api/createApi#keepunuseddatafor-1) basis.

### Cache lifetime & subscription example[​](#cache-lifetime--subscription-example "Direct link to Cache lifetime & subscription example") 

Imagine an endpoint that expects an `id` as the query param, and 4 components mounted which are requesting data from this same endpoint:

``` 
import  from './api.ts'

function ComponentOne()  = useGetUserQuery(1)

  return <div>...</div>
}

function ComponentTwo()  = useGetUserQuery(2)

  return <div>...</div>
}

function ComponentThree()  = useGetUserQuery(3)

  return <div>...</div>
}

function ComponentFour()  = useGetUserQuery(3)

  return <div>...</div>
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

While four components are subscribed to the endpoint, there are only three distinct combinations of endpoint + query parameters. Query parameters `1` and `2` will each have a single subscriber, while query parameter `3` has two subscribers. RTK Query will make three distinct fetches; one for each unique set of query parameters per endpoint.

Data is kept in the cache as long as at least one active subscriber is interested in that endpoint + parameter combination. When the subscriber reference count reaches zero, a timer is set, and if there are no new subscriptions to that data by the time the timer expires, the cached data will be removed. The default expiration is 60 seconds, which can be configured both for the [API definition as a whole](/rtk-query/api/createApi#keepunuseddatafor), as well as on a [per-endpoint](/rtk-query/api/createApi#keepunuseddatafor-1) basis.

If \'ComponentThree\' is unmounted in the example above, regardless of how much time passes, the data will remain in the cache due to \'ComponentFour\' still being subscribed to the same data, and the subscribe reference count will be `1`. However, once \'ComponentFour\' unmounts, the subscriber reference count will be `0`. The data will remain in the cache for the remainder of the expiration time. If no new subscription has been created before the timer expires, the cached data will finally be removed.

## Manipulating Cache Behavior[​](#manipulating-cache-behavior "Direct link to Manipulating Cache Behavior") 

On top of the default behavior, RTK Query provides a number of methods to re-fetch data earlier in scenarios where it should be considered invalid, or is otherwise deemed suitable to be \'refreshed\'.

### Reducing subscription time with `keepUnusedDataFor`[​](#reducing-subscription-time-with-keepunuseddatafor "Direct link to reducing-subscription-time-with-keepunuseddatafor") 

As mentioned above under [Default Cache Behavior](#default-cache-behavior) and [Cache lifetime & subscription example](#cache-lifetime--subscription-example), by default, data will remain in the cache for 60 seconds after the subscriber reference count hits zero.

This value can be configured using the `keepUnusedDataFor` option for both the API definition, as well as per-endpoint. Note that the per-endpoint version, if provided, will overrule a setting on the API definition.

Providing a value to `keepUnusedDataFor` as a number in seconds specifies how long the data should be kept in the cache after the subscriber reference count reaches zero.

-   TypeScript
-   JavaScript

keepUnusedDataFor configuration

``` 
import  from '@reduxjs/toolkit/query/react'
import type  from './types'

export const api = createApi(),
  // global configuration for the api
  keepUnusedDataFor: 30,
  endpoints: (build) => (),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

keepUnusedDataFor configuration

``` 
import  from '@reduxjs/toolkit/query/react'

export const api = createApi(),
  // global configuration for the api
  keepUnusedDataFor: 30,
  endpoints: (build) => (),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Re-fetching on demand with `refetch`/`initiate`[​](#re-fetching-on-demand-with-refetchinitiate "Direct link to re-fetching-on-demand-with-refetchinitiate") 

In order to achieve complete granular control over re-fetching data, you can use the `refetch` function returned as a result property from a [`useQuery`](/rtk-query/api/created-api/hooks#usequery) or [`useQuerySubscription`](/rtk-query/api/created-api/hooks#usequerysubscription) hook.

Calling the `refetch` function will force refetch the associated query.

Alternatively, you can dispatch the `initiate` thunk action for an endpoint, passing the option `forceRefetch: true` to the thunk action creator for the same effect.

Force refetch example

``` 
import  from 'react-redux'
import  from './api'

const Component = () =>  = useGetPostsQuery()

  function handleRefetchOne() 

  function handleRefetchTwo() ,
        ,
      ),
    )
  }

  return (
    <div>
      <button onClick=>Force re-fetch 1</button>
      <button onClick=>Force re-fetch 2</button>
    </div>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Encouraging re-fetching with `refetchOnMountOrArgChange`[​](#encouraging-re-fetching-with-refetchonmountorargchange "Direct link to encouraging-re-fetching-with-refetchonmountorargchange") 

Queries can be encouraged to re-fetch more frequently than usual via the [`refetchOnMountOrArgChange`](/rtk-query/api/createApi#refetchonmountorargchange) property. This can be passed to the endpoint as a whole, to individual hook calls, or when dispatching the [`initiate`](/rtk-query/api/created-api/endpoints#initiate) action (the name of the action creator\'s option is `forceRefetch`).

`refetchOnMountOrArgChange` is used to encourage re-fetching in additional situations where the default behavior would instead serve cached data.

`refetchOnMountOrArgChange` accepts either a boolean value, or a number as time in seconds.

Passing `false` (the default value) for this property will use the default behavior [described above](#default-cache-behavior).

Passing `true` for this property will cause the endpoint to always refetch when a new subscriber to the query is added. If passed to an individual hook call and not the api definition itself, then this applies only to that hook call. I.e., when the component calling the hook mounts, or the argument changes, it will always refetch, regardless of whether cached data for the endpoint + arg combination already exists.

Passing a `number` as a value in seconds will use the following behavior:

-   At the time a query subscription is created:
    -   if there is an existing query in the cache, it will compare the current time vs the last fulfilled timestamp for that query,
    -   It will refetch if the provided amount of time in seconds has elapsed.
-   If there is no query, it will fetch the data.
-   If there is an existing query, but the amount of time specified since the last query has not elapsed, it will serve the existing cached data.

-   TypeScript
-   JavaScript

Configuring re-fetching on subscription if data exceeds a given time

``` 
import  from '@reduxjs/toolkit/query/react'
import type  from './types'

export const api = createApi(),
  // global configuration for the api
  refetchOnMountOrArgChange: 30,
  endpoints: (build) => (),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Configuring re-fetching on subscription if data exceeds a given time

``` 
import  from '@reduxjs/toolkit/query/react'

export const api = createApi(),
  // global configuration for the api
  refetchOnMountOrArgChange: 30,
  endpoints: (build) => (),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Forcing refetch on component mount

``` 
import  from './api'

const Component = () =>  = useGetPostsQuery(
    ,
    // this overrules the api definition setting,
    // forcing the query to always fetch when this component is mounted
    ,
  )

  return <div>...</div>
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Re-fetching on window focus with `refetchOnFocus`[​](#re-fetching-on-window-focus-with-refetchonfocus "Direct link to re-fetching-on-window-focus-with-refetchonfocus") 

The [`refetchOnFocus`](/rtk-query/api/createApi#refetchonfocus) option allows you to control whether RTK Query will try to refetch all subscribed queries after the application window regains focus.

If you specify this option alongside `skip: true`, this will not be evaluated until skip is false.

Note that this requires [`setupListeners`](/rtk-query/api/setupListeners) to have been called.

This option is available on both the api definition with [`createApi`](/rtk-query/api/createApi), as well as on the [`useQuery`](/rtk-query/api/created-api/hooks#usequery), [`useQuerySubscription`](/rtk-query/api/created-api/hooks#usequerysubscription), [`useLazyQuery`](/rtk-query/api/created-api/hooks#uselazyquery), and [`useLazyQuerySubscription`](/rtk-query/api/created-api/hooks#uselazyquerysubscription) hooks.

-   TypeScript
-   JavaScript

src/services/api.ts

``` 
import  from '@reduxjs/toolkit/query/react'
import type  from './types'

export const api = createApi(),
  // global configuration for the api
  refetchOnFocus: true,
  endpoints: (build) => (),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/services/api.js

``` 
import  from '@reduxjs/toolkit/query/react'

export const api = createApi(),
  // global configuration for the api
  refetchOnFocus: true,
  endpoints: (build) => (),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   TypeScript
-   JavaScript

src/store.ts

``` 
import  from '@reduxjs/toolkit'
import  from '@reduxjs/toolkit/query'
import  from './services/api'

export const store = configureStore(,
  middleware: (gDM) => gDM().concat(api.middleware),
})

// enable listener behavior for the store
setupListeners(store.dispatch)

export type RootState = ReturnType<typeof store.getState>
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/store.js

``` 
import  from '@reduxjs/toolkit'
import  from '@reduxjs/toolkit/query'
import  from './services/api'

export const store = configureStore(,
  middleware: (gDM) => gDM().concat(api.middleware),
})

// enable listener behavior for the store
setupListeners(store.dispatch)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Re-fetching on network reconnection with `refetchOnReconnect`[​](#re-fetching-on-network-reconnection-with-refetchonreconnect "Direct link to re-fetching-on-network-reconnection-with-refetchonreconnect") 

The [`refetchOnReconnect`](/rtk-query/api/createApi#refetchonreconnect) option on [`createApi`](/rtk-query/api/createApi) allows you to control whether RTK Query will try to refetch all subscribed queries after regaining a network connection.

If you specify this option alongside `skip: true`, this **will not be evaluated** until `skip` is false.

Note that this requires [`setupListeners`](/rtk-query/api/setupListeners) to have been called.

This option is available on both the api definition with [`createApi`](/rtk-query/api/createApi), as well as on the [`useQuery`](/rtk-query/api/created-api/hooks#usequery), [`useQuerySubscription`](/rtk-query/api/created-api/hooks#usequerysubscription), [`useLazyQuery`](/rtk-query/api/created-api/hooks#uselazyquery), and [`useLazyQuerySubscription`](/rtk-query/api/created-api/hooks#uselazyquerysubscription) hooks.

-   TypeScript
-   JavaScript

src/services/api.ts

``` 
import  from '@reduxjs/toolkit/query/react'
import type  from './types'

export const api = createApi(),
  // global configuration for the api
  refetchOnReconnect: true,
  endpoints: (build) => (),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/services/api.js

``` 
import  from '@reduxjs/toolkit/query/react'

export const api = createApi(),
  // global configuration for the api
  refetchOnReconnect: true,
  endpoints: (build) => (),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   TypeScript
-   JavaScript

src/store.ts

``` 
import  from '@reduxjs/toolkit'
import  from '@reduxjs/toolkit/query'
import  from './services/api'

export const store = configureStore(,
  middleware: (gDM) => gDM().concat(api.middleware),
})

// enable listener behavior for the store
setupListeners(store.dispatch)

export type RootState = ReturnType<typeof store.getState>
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/store.js

``` 
import  from '@reduxjs/toolkit'
import  from '@reduxjs/toolkit/query'
import  from './services/api'

export const store = configureStore(,
  middleware: (gDM) => gDM().concat(api.middleware),
})

// enable listener behavior for the store
setupListeners(store.dispatch)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Re-fetching after mutations by invalidating cache tags[​](#re-fetching-after-mutations-by-invalidating-cache-tags "Direct link to Re-fetching after mutations by invalidating cache tags") 

RTK Query uses an optional [cache tag](/rtk-query/usage/automated-refetching#cache-tags) system to automate re-fetching for query endpoints that have data affected by mutation endpoints.

See [Automated Re-fetching](/rtk-query/usage/automated-refetching) for full details on this concept.

## Tradeoffs[​](#tradeoffs "Direct link to Tradeoffs") 

### No Normalized or De-duplicated Cache[​](#no-normalized-or-de-duplicated-cache "Direct link to No Normalized or De-duplicated Cache") 

RTK Query deliberately **does *not* implement a cache that would deduplicate identical items across multiple requests**. There are several reasons for this:

-   A fully normalized shared-across-queries cache is a *hard* problem to solve
-   We don\'t have the time, resources, or interest in trying to solve that right now
-   In many cases, simply re-fetching data when it\'s invalidated works well and is easier to understand
-   At a minimum, RTKQ can help solve the general use case of \"fetch some data\", which is a big pain point for a lot of people

As an example, say that we have an API slice with `getTodos` and `getTodo` endpoints, and our components make the following queries:

-   `getTodos()`
-   `getTodos()`
-   `getTodo()`

Each of these query results would include a Todo object that looks like ``.

In a fully normalized de-duplicating cache, only a single copy of this Todo object would be stored. However, RTK Query saves each query result independently in the cache. So, this would result in three separate copies of this Todo being cached in the Redux store. However, if all the endpoints are consistently providing the same tags (such as ``), then invalidating that tag will force all the matching endpoints to refetch their data for consistency.

The Redux docs have always recommended [keeping data in a normalized lookup table](https://redux.js.org/recipes/structuring-reducers/normalizing-state-shape) to enable easily finding items by ID and updating them in the store, and [RTK\'s `createEntityAdapter`](/api/createEntityAdapter) was designed to help manage normalized state. Those concepts are still valuable and don\'t go away. However, if you\'re using RTK Query to manage caching data, there\'s less need to manipulate the data that way yourself.

There are a couple additional points that can help here:

-   The generated query hooks have [a `selectFromResult` option](/rtk-query/api/created-api/hooks#usequery) that allow components to read individual pieces of data from a query result. As an example, a `<TodoList>` component might call `useTodosQuery()`, and each individual `<TodoListItem>` could use the same query hook but select from the result to get the right todo object.
-   You can use the [`transformResponse` endpoint option](/rtk-query/api/createApi#transformresponse) to modify the fetched data so that it\'s [stored in a different shape](/rtk-query/usage/customizing-queries#customizing-query-responses-with-transformresponse), such as using `createEntityAdapter` to normalize the data *for this one response* before it\'s inserted into the cache.

### Further information[​](#further-information "Direct link to Further information") 

-   [Reddit: discussion of why RTKQ doesn\'t have a normalized cache, and tradeoffs](https://www.reddit.com/r/reactjs/comments/my9vrq/redux_toolkit_v16_alpha1_rtk_query_apis/gvxi5t7/)

## Examples[​](#examples "Direct link to Examples") 

### Cache Subscription Lifetime Demo[​](#cache-subscription-lifetime-demo "Direct link to Cache Subscription Lifetime Demo") 

This example is a live demo of how the subscriber reference count and the value of `keepUnusedDataFor` interact with each other. The `Subscriptions` and `Queries` (including the cached data) are shown in the demo for you to visualize (note that this can also be viewed in the [Redux Devtools Extension](https://github.com/reduxjs/redux-devtools)).

Two components are mounted, each with the same endpoints query (`useGetUsersQuery(2)`). You will be able to observe that when toggling off the components, the subscriber reference count will be reduced. After toggling off both components such that the subscriber reference count reaches zero, you will observe the cached data under the `Queries` section will persist for 5 seconds (the value of `keepUnusedDataFor` provided for the endpoint in this demo). If the subscriber reference count remains at 0 for the full duration, the cached data will then be removed from the store.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/usage/cache-behavior.mdx)

[Last updated on **Sep 2, 2025**]