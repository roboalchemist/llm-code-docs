# Source: https://redux-toolkit.js.org/rtk-query/usage/manual-cache-updates

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [Using RTK Query]
-   [Common Use Cases]
-   [Manual Cache Updates]

On this page

 

<div>

# Manual Cache Updates

</div>

## Overview[​](#overview "Direct link to Overview") 

For most cases, in order to receive up to date data after a triggering a change in the backend, you can take advantage of cache tag invalidation to perform [automated re-fetching](/rtk-query/usage/automated-refetching). This will cause a query to re-fetch its data when it has been told that a mutation has occurred which would cause its data to become out of date.

We recommend using automated re-fetching as a preference over manual cache updates in most situations.

However, there *are* use cases when manual cache updates are necessary, such as \"optimistic\" or \"pessimistic\" updates, or modifying data as part of cache entry lifecycles.

RTK Query exports thunks for these use cases, attached to `api.utils`:

-   [`updateQueryData`](/rtk-query/api/created-api/api-slice-utils#updatequerydata): updates an already existing cache entry
-   [`upsertQueryData`](/rtk-query/api/created-api/api-slice-utils#upsertquerydata): creates or replaces cache entries

Since these are thunks, you can dispatch them anywhere you have access to `dispatch`.

### Updating existing cache entries[​](#updating-existing-cache-entries "Direct link to Updating existing cache entries") 

For updates of existing cache entries, use [`updateQueryData`](/rtk-query/api/created-api/api-slice-utils#updatequerydata).

`updateQueryData` is strictly intended to perform *updates* to existing cache entries, not create new entries. If an `updateQueryData` thunk action is dispatched and the `endpointName` + `args` combination that does not match any existing cache entry, the provided `recipe` callback will not be called, and no `patches` or `inversePatches` will be returned.

Use cases for manual update of cache entries:

-   Providing immediate feedback to the user when a mutation is attempted
-   After a mutation, updating a single item in a large list of items that is already cached, rather than re-fetching the whole list
-   Debouncing a large number of mutations with immediate feedback as though they are being applied, followed by a single request sent to the server to update the debounced attempts

### Creating new cache entries or replacing existing ones[​](#creating-new-cache-entries-or-replacing-existing-ones "Direct link to Creating new cache entries or replacing existing ones") 

To create or replace existing cache entries, use [`upsertQueryData`](/rtk-query/api/created-api/api-slice-utils#upsertquerydata).

`upsertQueryData` is intended to perform *replacements* to existing cache entries or *creation* of new ones. Since `upsertQueryData` does not have access to the previous state of the cache entry, the update may be performed only as a replacement. In comparison, `updateQueryData` allows patching of the existing cache entry, but cannot create a new one.

One example use case is [pessimistic updates](/rtk-query/usage/manual-cache-updates#pessimistic-updates). If the client makes an API call to create a `Post`, the backend could return its complete data including the `id`. Then we can use `upsertQueryData` to create a new cache entry for the `getPostById(id)` query, preventing an extra fetch to retrieve the item later.

## Recipes[​](#recipes "Direct link to Recipes") 

### Optimistic Updates[​](#optimistic-updates "Direct link to Optimistic Updates") 

When you wish to perform an update to cache data immediately after a [`mutation`](/rtk-query/usage/mutations) is triggered, you can apply an `optimistic update`. This can be a useful pattern for when you want to give the user the impression that their changes are immediate, even while the mutation request is still in flight.

The core concepts for an optimistic update are:

-   when you start a query or mutation, `onQueryStarted` will be executed
-   you manually update the cached data by dispatching `api.util.updateQueryData` within `onQueryStarted`
-   then, in the case that `queryFulfilled` rejects:
    -   you roll it back via the `.undo` property of the object you got back from the earlier dispatch, OR
    -   you invalidate the cache data via `api.util.invalidateTags` to trigger a full re-fetch of the data

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Where many mutations are potentially triggered in short succession causing overlapping requests, you may encounter race conditions if attempting to roll back patches using the `.undo` property on failures. For these scenarios, it is often simplest and safest to invalidate the tags on error instead, and re-fetch truly up-to-date data from the server.

-   TypeScript
-   JavaScript

Optimistic update mutation example (async await)

``` 
import  from '@reduxjs/toolkit/query'
import type  from './types'

const api = createApi(),
  tagTypes: ['Post'],
  endpoints: (build) => (`,
      providesTags: ['Post'],
    }),
    updatePost: build.mutation<void, Pick<Post, 'id'> & Partial<Post>>() => (`,
        method: 'PATCH',
        body: patch,
      }),
      async onQueryStarted(, ) ),
        )
        try  catch 
      },
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Optimistic update mutation example (async await)

``` 
import  from '@reduxjs/toolkit/query'

const api = createApi(),
  tagTypes: ['Post'],
  endpoints: (build) => (`,
      providesTags: ['Post'],
    }),
    updatePost: build.mutation() => (`,
        method: 'PATCH',
        body: patch,
      }),
      async onQueryStarted(, ) ),
        )
        try  catch 
      },
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

or, if you prefer the slightly shorter version with `.catch`

``` 
-      async onQueryStarted(, ) , ) )
        )
-       try  catch 
+       queryFulfilled.catch(patchResult.undo)
      }
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

#### Example[​](#example "Direct link to Example") 

[React Optimistic Updates](/rtk-query/usage/examples#react-optimistic-updates)

### Pessimistic Updates[​](#pessimistic-updates "Direct link to Pessimistic Updates") 

When you wish to perform an update to cache data based on the response received from the server after a [`mutation`](/rtk-query/usage/mutations) is triggered, you can apply a `pessimistic update`. The distinction between a `pessimistic update` and an `optimistic update` is that the `pessimistic update` will instead wait for the response from the server prior to updating the cached data.

The core concepts for a pessimistic update are:

-   when you start a query or mutation, `onQueryStarted` will be executed
-   you await `queryFulfilled` to resolve to an object containing the transformed response from the server in the `data` property
-   you manually update the cached data by dispatching `api.util.updateQueryData` within `onQueryStarted`, using the data in the response from the server for your draft updates
-   you manually create a new cache entry by dispatching `api.util.upsertQueryData` within `onQueryStarted`, using the complete Post object returned by backend.

-   TypeScript
-   JavaScript

Pessimistic update mutation example (async await)

``` 
import  from '@reduxjs/toolkit/query'
import type  from './types'

const api = createApi(),
  tagTypes: ['Post'],
  endpoints: (build) => (`,
      providesTags: ['Post'],
    }),
    updatePost: build.mutation<Post, Pick<Post, 'id'> & Partial<Post>>() => (`,
        method: 'PATCH',
        body: patch,
      }),
      async onQueryStarted(, )  = await queryFulfilled
          const patchResult = dispatch(
            api.util.updateQueryData('getPost', id, (draft) => ),
          )
        } catch 
      },
    }),
    createPost: build.mutation<Post, Pick<Post, 'id'> & Partial<Post>>() => (`,
        method: 'POST',
        body,
      }),
      async onQueryStarted(, )  = await queryFulfilled
          const patchResult = dispatch(
            api.util.upsertQueryData('getPost', id, createdPost),
          )
        } catch 
      },
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Pessimistic update mutation example (async await)

``` 
import  from '@reduxjs/toolkit/query'

const api = createApi(),
  tagTypes: ['Post'],
  endpoints: (build) => (`,
      providesTags: ['Post'],
    }),
    updatePost: build.mutation() => (`,
        method: 'PATCH',
        body: patch,
      }),
      async onQueryStarted(, )  = await queryFulfilled
          const patchResult = dispatch(
            api.util.updateQueryData('getPost', id, (draft) => ),
          )
        } catch 
      },
    }),
    createPost: build.mutation() => (`,
        method: 'POST',
        body,
      }),
      async onQueryStarted(, )  = await queryFulfilled
          const patchResult = dispatch(
            api.util.upsertQueryData('getPost', id, createdPost),
          )
        } catch 
      },
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### General Updates[​](#general-updates "Direct link to General Updates") 

If you find yourself wanting to update cache data elsewhere in your application, you can do so anywhere you have access to the `store.dispatch` method, including within React components via the [useDispatch](https://react-redux.js.org/api/hooks#usedispatch) hook (or a typed version such as [useAppDispatch](https://react-redux.js.org/using-react-redux/usage-with-typescript#define-typed-hooks) for typescript users).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

You should generally avoid manually updating the cache outside of the `onQueryStarted` callback for a mutation without a good reason, as RTK Query is intended to be used by considering your cached data as a reflection of the server-side state.

General manual cache update example

``` 
import  from './api'
import  from './store/hooks'

function App() )
      }),
    )
  }

  return <button onClick=>Add post to cache</button>
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/usage/manual-cache-updates.mdx)

[Last updated on **Jan 29, 2024**]