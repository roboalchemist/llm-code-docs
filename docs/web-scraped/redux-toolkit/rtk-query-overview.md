# Source: https://redux-toolkit.js.org/rtk-query/overview

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [RTK Query Overview]

On this page

 

<div>

# RTK Query Overview

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]What You\'ll Learn

-   What RTK Query is and what problems it solves
-   What APIs are included in RTK Query
-   Basic RTK Query usage

**RTK Query** is a powerful data fetching and caching tool. It is designed to simplify common cases for loading data in a web application, **eliminating the need to hand-write data fetching & caching logic yourself**.

RTK Query is **an optional addon included in the Redux Toolkit package**, and its functionality is built on top of the other APIs in Redux Toolkit.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

To learn how to use RTK Query, see the full [\"Redux Essentials\" tutorial](https://redux.js.org/tutorials/essentials/part-7-rtk-query-basics) on the Redux core docs site.

If you prefer a video course, you can [watch this RTK Query video course by Lenz Weber-Tronic, the creator of RTK Query, for free at Egghead](https://egghead.io/courses/rtk-query-basics-query-endpoints-data-flow-and-typescript-57ea3c43?af=7pnhj6) or take a look at the first lesson right here:

[Play Video]

## Motivation[​](#motivation "Direct link to Motivation") 

Web applications normally need to fetch data from a server in order to display it. They also usually need to make updates to that data, send those updates to the server, and keep the cached data on the client in sync with the data on the server. This is made more complicated by the need to implement other behaviors used in today\'s applications:

-   Tracking loading state in order to show UI spinners
-   Avoiding duplicate requests for the same data
-   Optimistic updates to make the UI feel faster
-   Managing cache lifetimes as the user interacts with the UI

The Redux core has always been very minimal - it\'s up to developers to write all the actual logic. That means that Redux has never included anything built in to help solve these use cases. The Redux docs have taught [some common patterns for dispatching actions around the request lifecycle to track loading state and request results](https://redux.js.org/tutorials/fundamentals/part-7-standard-patterns#async-request-status), and [Redux Toolkit\'s `createAsyncThunk` API](/api/createAsyncThunk) was designed to abstract that typical pattern. However, users still have to write significant amounts of reducer logic to manage the loading state and the cached data.

Over the last couple years, the React community has come to realize that **\"data fetching and caching\" is really a different set of concerns than \"state management\"**. While you can use a state management library like Redux to cache data, the use cases are different enough that it\'s worth using tools that are purpose-built for the data fetching use case.

RTK Query takes inspiration from other tools that have pioneered solutions for data fetching, like Apollo Client, React Query, Urql, and SWR, but adds a unique approach to its API design:

-   The data fetching and caching logic is built on top of Redux Toolkit\'s `createSlice` and `createAsyncThunk` APIs
-   Because Redux Toolkit is UI-agnostic, RTK Query\'s functionality can be used with any UI layer
-   API endpoints are defined ahead of time, including how to generate query parameters from arguments and transform responses for caching
-   RTK Query can also generate React hooks that encapsulate the entire data fetching process, provide `data` and `isLoading` fields to components, and manage the lifetime of cached data as components mount and unmount
-   RTK Query provides \"cache entry lifecycle\" options that enable use cases like streaming cache updates via websocket messages after fetching the initial data
-   We have early working examples of code generation of API slices from OpenAPI and GraphQL schemas
-   Finally, RTK Query is completely written in TypeScript, and is designed to provide an excellent TS usage experience

## What\'s included[​](#whats-included "Direct link to What's included") 

### APIs[​](#apis "Direct link to APIs") 

RTK Query is included within the installation of the core Redux Toolkit package. It is available via either of the two entry points below:

``` 
import  from '@reduxjs/toolkit/query'

/* React-specific entry point that automatically generates
   hooks corresponding to the defined endpoints */
import  from '@reduxjs/toolkit/query/react'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

RTK Query includes these APIs:

-   [`createApi()`](/rtk-query/api/createApi): The core of RTK Query\'s functionality. It allows you to define a set of \"endpoints\" that describe how to retrieve data from backend APIs and other async sources, including the configuration of how to fetch and transform that data. In most cases, you should use this once per app, with \"one API slice per base URL\" as a rule of thumb.
-   [`fetchBaseQuery()`](/rtk-query/api/fetchBaseQuery): A small wrapper around [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) that aims to simplify requests. Intended as the recommended `baseQuery` to be used in `createApi` for the majority of users.
-   [`<ApiProvider />`](/rtk-query/api/ApiProvider): Can be used as a `Provider` if you **do not already have a Redux store**.
-   [`setupListeners()`](/rtk-query/api/setupListeners): A utility used to enable `refetchOnMount` and `refetchOnReconnect` behaviors.

### Bundle Size[​](#bundle-size "Direct link to Bundle Size") 

RTK Query adds a fixed one-time amount to your app\'s bundle size. Since RTK Query builds on top of Redux Toolkit and React-Redux, the added size varies depending on whether you are already using those in your app. The estimated min+gzip bundle sizes are:

-   If you are using RTK already: \~9kb for RTK Query and \~2kb for the hooks.
-   If you are not using RTK already:
    -   Without React: 17 kB for RTK+dependencies+RTK Query
    -   With React: 19kB + React-Redux, which is a peer dependency

Adding additional endpoint definitions should only increase size based on the actual code inside the `endpoints` definitions, which will typically be just a few bytes.

The functionality included in RTK Query quickly pays for the added bundle size, and the elimination of hand-written data fetching logic should be a net improvement in size for most meaningful applications.

## Basic Usage[​](#basic-usage "Direct link to Basic Usage") 

### Create an API Slice[​](#create-an-api-slice "Direct link to Create an API Slice") 

RTK Query is included within the installation of the core Redux Toolkit package. It is available via either of the two entry points below:

``` 
import  from '@reduxjs/toolkit/query'

/* React-specific entry point that automatically generates
   hooks corresponding to the defined endpoints */
import  from '@reduxjs/toolkit/query/react'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

For typical usage with React, start by importing `createApi` and defining an \"API slice\" that lists the server\'s base URL and which endpoints we want to interact with:

``` 
import  from '@reduxjs/toolkit/query/react'
import type  from './types'

// Define a service using a base URL and expected endpoints
export const pokemonApi = createApi(),
  endpoints: (build) => (`,
    }),
  }),
})

// Export hooks for usage in functional components, which are
// auto-generated based on the defined endpoints
export const  = pokemonApi
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Configure the Store[​](#configure-the-store "Direct link to Configure the Store") 

The \"API slice\" also contains an auto-generated Redux slice reducer and a custom middleware that manages subscription lifetimes. Both of those need to be added to the Redux store:

``` 
import  from '@reduxjs/toolkit'
// Or from '@reduxjs/toolkit/query/react'
import  from '@reduxjs/toolkit/query'
import  from './services/pokemon'

export const store = configureStore(,
  // Adding the api middleware enables caching, invalidation, polling,
  // and other useful features of `rtk-query`.
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(pokemonApi.middleware),
})

// optional, but required for refetchOnFocus/refetchOnReconnect behaviors
// see `setupListeners` docs - takes an optional callback as the 2nd arg for customization
setupListeners(store.dispatch)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Use Hooks in Components[​](#use-hooks-in-components "Direct link to Use Hooks in Components") 

Finally, import the auto-generated React hooks from the API slice into your component file, and call the hooks in your component with any needed parameters. RTK Query will automatically fetch data on mount, re-fetch when parameters change, provide `` values in the result, and re-render the component as those values change:

``` 
import * as React from 'react'
import  from './services/pokemon'

export default function App()  = useGetPokemonByNameQuery('bulbasaur')
  // Individual hooks are also accessible under the generated endpoints:
  // const  = pokemonApi.endpoints.getPokemonByName.useQuery('bulbasaur')

  // render UI based on data and loading state
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Further Information[​](#further-information "Direct link to Further Information") 

See the [**RTK Query Quick Start tutorial**](/tutorials/rtk-query) for examples of how to add RTK Query to a project that uses Redux Toolkit, set up an \"API slice\" with endpoint definitions, and how to use the auto-generated React hooks in your components.

The [**RTK Query usage guide section**](/rtk-query/usage/queries) has information on topics like [querying data](/rtk-query/usage/queries), [using mutations to send updates to the server](/rtk-query/usage/mutations), [streaming cache updates](/rtk-query/usage/streaming-updates), and much more.

The [**Examples page**](/rtk-query/usage/examples) has runnable CodeSandboxes that demonstrate topics like [making queries with GraphQL](/rtk-query/usage/examples#react-with-graphql), [authentication](/rtk-query/usage/examples#authentication), and even [using RTK Query with other UI libraries like Svelte](/rtk-query/usage/examples#svelte).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/overview.md)

[Last updated on **Feb 23, 2025**]