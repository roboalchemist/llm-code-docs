# Source: https://redux-toolkit.js.org/rtk-query/usage/mutations

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [Using RTK Query]
-   [Standard Usage]
-   [Mutations]

On this page

 

<div>

# Mutations

</div>

## Overview[​](#overview "Direct link to Overview") 

Mutations are used to send data updates to the server and apply the changes to the local cache. Mutations can also invalidate cached data and force re-fetches.

## Defining Mutation Endpoints[​](#defining-mutation-endpoints "Direct link to Defining Mutation Endpoints") 

Mutation endpoints are defined by returning an object inside the `endpoints` section of `createApi`, and defining the fields using the `build.mutation()` method.

Mutation endpoints should define either a `query` callback that constructs the URL (including any URL query params), or [a `queryFn` callback](/rtk-query/usage/customizing-queries#customizing-queries-with-queryfn) that may do arbitrary async logic and return a result. The `query` callback may also return an object containing the URL, the HTTP method to use and a request body.

If the `query` callback needs additional data to generate the URL, it should be written to take a single argument. If you need to pass in multiple parameters, pass them formatted as a single \"options object\".

Mutation endpoints may also modify the response contents before the result is cached, define \"tags\" to identify cache invalidation, and provide cache entry lifecycle callbacks to run additional logic as cache entries are added and removed.

When used with TypeScript, you should supply generics for the return type and the expected query argument: `build.mutation<ReturnType, ArgType>`. If there is no argument, use `void` for the arg type instead.

-   TypeScript
-   JavaScript

Example of all mutation endpoint options

``` 
import  from '@reduxjs/toolkit/query'
import type  from './types'

const api = createApi(),
  tagTypes: ['Post'],
  endpoints: (build) => () => (`,
        method: 'PATCH',
        body: patch,
      }),
      // Pick out data and prevent nested properties in a hook or selector
      transformResponse: (response: , meta, arg) => response.data,
      // Pick out errors and prevent nested properties in a hook or selector
      transformErrorResponse: (
        response: ,
        meta,
        arg,
      ) => response.status,
      invalidatesTags: ['Post'],
      // onQueryStarted is useful for optimistic updates
      // The 2nd parameter is the destructured `MutationLifecycleApi`
      async onQueryStarted(
        arg,
        ,
      ) ,
      // The 2nd parameter is the destructured `MutationCacheLifecycleApi`
      async onCacheEntryAdded(
        arg,
        ,
      ) ,
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Example of all mutation endpoint options

``` 
import  from '@reduxjs/toolkit/query'

const api = createApi(),
  tagTypes: ['Post'],
  endpoints: (build) => () => (`,
        method: 'PATCH',
        body: patch,
      }),
      // Pick out data and prevent nested properties in a hook or selector
      transformResponse: (response, meta, arg) => response.data,
      // Pick out errors and prevent nested properties in a hook or selector
      transformErrorResponse: (response, meta, arg) => response.status,
      invalidatesTags: ['Post'],
      // onQueryStarted is useful for optimistic updates
      // The 2nd parameter is the destructured `MutationLifecycleApi`
      async onQueryStarted(
        arg,
        ,
      ) ,
      // The 2nd parameter is the destructured `MutationCacheLifecycleApi`
      async onCacheEntryAdded(
        arg,
        ,
      ) ,
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

The `onQueryStarted` method can be used for [optimistic updates](/rtk-query/usage/manual-cache-updates#optimistic-updates)

## Performing Mutations with React Hooks[​](#performing-mutations-with-react-hooks "Direct link to Performing Mutations with React Hooks") 

### Mutation Hook Behavior[​](#mutation-hook-behavior "Direct link to Mutation Hook Behavior") 

Unlike `useQuery`, `useMutation` returns a tuple. The first item in the tuple is the \"trigger\" function and the second element contains an object with `status`, `error`, and `data`.

Unlike the `useQuery` hook, the `useMutation` hook doesn\'t execute automatically. To run a mutation you have to call the trigger function returned as the first tuple value from the hook.

See [`useMutation`](/rtk-query/api/created-api/hooks#usemutation) for the hook signature and additional details.

### Frequently Used Mutation Hook Return Values[​](#frequently-used-mutation-hook-return-values "Direct link to Frequently Used Mutation Hook Return Values") 

The `useMutation` hook returns a tuple containing a \"mutation trigger\" function, as well as an object containing properties about the \"mutation result\".

The \"mutation trigger\" is a function that when called, will fire off the mutation request for that endpoint. Calling the \"mutation trigger\" returns a promise with an `unwrap` property, which can be called to unwrap the mutation call and provide the raw response/error. This can be useful if you wish to determine whether the mutation succeeds/fails inline at the call-site.

The \"mutation result\" is an object containing properties such as the latest `data` for the mutation request, as well as status booleans for the current request lifecycle state.

Below are some of the most frequently used properties on the \"mutation result\" object. Refer to [`useMutation`](/rtk-query/api/created-api/hooks#usemutation) for an extensive list of all returned properties.

-   `data` - The data returned from the latest trigger response, if present. If subsequent triggers from the same hook instance are called, this will return undefined until the new data is received. Consider component level caching if the previous response data is required for a smooth transition to new data.
-   `error` - The error result if present.
-   `isUninitialized` - When true, indicates that the mutation has not been fired yet.
-   `isLoading` - When true, indicates that the mutation has been fired and is awaiting a response.
-   `isSuccess` - When true, indicates that the last mutation fired has data from a successful request.
-   `isError` - When true, indicates that the last mutation fired resulted in an error state.
-   `reset` - A method to reset the hook back to its original state and remove the current result from the cache

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

With RTK Query, a mutation does not contain a semantic distinction between \'loading\' and \'fetching\' in the way that a [query does](/rtk-query/usage/queries#frequently-used-query-hook-return-values). For a mutation, subsequent calls are not assumed to be necessarily related, so a mutation is either \'loading\' or \'not loading\', with no concept of \'re-fetching\'.

### Shared Mutation Results[​](#shared-mutation-results "Direct link to Shared Mutation Results") 

By default, separate instances of a `useMutation` hook are not inherently related to each other. Triggering one instance will not affect the result for a separate instance. This applies regardless of whether the hooks are called within the same component, or different components.

``` 
export const ComponentOne = () => 

export const ComponentTwo = () => 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

RTK Query provides an option to share results across mutation hook instances using the `fixedCacheKey` option. Any `useMutation` hooks with the same `fixedCacheKey` string will share results between each other when any of the trigger functions are called. This should be a unique string shared between each mutation hook instance you wish to share results.

``` 
export const ComponentOne = () => )

  return <div>...</div>
}

export const ComponentTwo = () => )

  return <div>...</div>
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

When using `fixedCacheKey`, the `originalArgs` property is not able to be shared and will always be `undefined`.

### Standard Mutation Example[​](#standard-mutation-example "Direct link to Standard Mutation Example") 

This is a modified version of the complete example you can see at the bottom of the page to highlight the `updatePost` mutation. In this scenario, a post is fetched with `useQuery`, and then an `EditablePostName` component is rendered that allows us to edit the name of the post.

src/features/posts/PostDetail.tsx

``` 
export const PostDetail = () =>  = useParams<>()

  const  = useGetPostQuery(id)

  const [
    updatePost, // This is the mutation trigger
    , // This is the destructured mutation result
  ] = useUpdatePostMutation()

  return (
    <Box p=>
      <EditablePostName
        name=
        onUpdate=)
          )
        }}
        isLoading=
      />
    </Box>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Advanced Mutations with Revalidation[​](#advanced-mutations-with-revalidation "Direct link to Advanced Mutations with Revalidation") 

In the real world, it\'s very common that a developer would want to resync their local data cache with the server after performing a mutation (aka \"revalidation\"). RTK Query takes a more centralized approach to this and requires you to configure the invalidation behavior in your API service definition. See [Advanced Invalidation with abstract tag IDs](/rtk-query/usage/automated-refetching#advanced-invalidation-with-abstract-tag-ids) for details on advanced invalidation handling with RTK Query.

### Revalidation Example[​](#revalidation-example "Direct link to Revalidation Example") 

This is an example of a [CRUD service](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) for Posts. This implements the [Selectively invalidating lists](/rtk-query/usage/automated-refetching#selectively-invalidating-lists) strategy and will most likely serve as a good foundation for real applications.

-   TypeScript
-   JavaScript

src/app/services/posts.ts

``` 
// Or from '@reduxjs/toolkit/query' if not using the auto-generated hooks
import  from '@reduxjs/toolkit/query/react'

export interface Post 

type PostsResponse = Post[]

export const postApi = createApi(),
  tagTypes: ['Posts'],
  endpoints: (build) => () => () as const),
              ,
            ]
          : // an error occurred, but we still want to refetch this query when `` is invalidated
            [],
    }),
    addPost: build.mutation<Post, Partial<Post>>(
      },
      // Invalidates all Post-type queries providing the `LIST` id - after all, depending of the sort order,
      // that newly created post could show up in any lists.
      invalidatesTags: [],
    }),
    getPost: build.query<Post, number>(`,
      providesTags: (result, error, id) => [],
    }),
    updatePost: build.mutation<Post, Partial<Post>>( = data
        return `,
          method: 'PUT',
          body,
        }
      },
      // Invalidates all queries that subscribe to this Post `id` only.
      // In this case, `getPost` will be re-run. `getPosts` *might*  rerun, if this id was under its results.
      invalidatesTags: (result, error, ) => [],
    }),
    deletePost: build.mutation<, number>(`,
          method: 'DELETE',
        }
      },
      // Invalidates all queries that subscribe to this Post `id` only.
      invalidatesTags: (result, error, id) => [],
    }),
  }),
})

export const  = postApi
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/app/services/posts.js

``` 
// Or from '@reduxjs/toolkit/query' if not using the auto-generated hooks
import  from '@reduxjs/toolkit/query/react'

export const postApi = createApi(),
  tagTypes: ['Posts'],
  endpoints: (build) => () => ()),
              ,
            ]
          : // an error occurred, but we still want to refetch this query when `` is invalidated
            [],
    }),
    addPost: build.mutation(
      },
      // Invalidates all Post-type queries providing the `LIST` id - after all, depending of the sort order,
      // that newly created post could show up in any lists.
      invalidatesTags: [],
    }),
    getPost: build.query(`,
      providesTags: (result, error, id) => [],
    }),
    updatePost: build.mutation( = data
        return `,
          method: 'PUT',
          body,
        }
      },
      // Invalidates all queries that subscribe to this Post `id` only.
      // In this case, `getPost` will be re-run. `getPosts` *might*  rerun, if this id was under its results.
      invalidatesTags: (result, error, ) => [],
    }),
    deletePost: build.mutation(`,
          method: 'DELETE',
        }
      },
      // Invalidates all queries that subscribe to this Post `id` only.
      invalidatesTags: (result, error, id) => [],
    }),
  }),
})

export const  = postApi
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
  endpoints: (build) => ( = data
        return `,
          method: 'PUT',
          body,
        }
      },
      responseSchema: postSchema,
    }),
    updatePostWithTransform: build.mutation<TransformedPost, Partial<Post>>( = data
        return `,
          method: 'PUT',
          body,
        }
      },
      rawResponseSchema: postSchema,
      transformResponse: (response) => (),
      // responseSchema can still be provided, to validate the transformed response
      responseSchema: transformedPost,
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/usage/mutations.mdx)

[Last updated on **Apr 12, 2025**]