# Source: https://redux-toolkit.js.org/rtk-query/usage/infinite-queries

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [Using RTK Query]
-   [Standard Usage]
-   [Infinite Queries]

On this page

 

<div>

# Infinite Queries

</div>

## Overview[​](#overview "Direct link to Overview") 

Rendering lists that can additively \"load more\" data onto an existing set of data or \"infinite scroll\" is a common UI pattern.

RTK Query supports this use case via \"infinite query\" endpoints. Infinite Query endpoints are similar to standard query endpoints, in that they fetch data and cache the results. However, infinite query endpoints have the ability to fetch \"next\" and \"previous\" pages, and contain all related fetched pages in a single cache entry.

## Infinite Query Concepts[​](#infinite-query-concepts "Direct link to Infinite Query Concepts") 

RTK Query\'s support for infinite queries is modeled after [React Query\'s infinite query API design](https://tanstack.com/query/latest/docs/framework/react/guides/infinite-queries).

### Query Args, Page Params, and Cache Structure[​](#query-args-page-params-and-cache-structure "Direct link to Query Args, Page Params, and Cache Structure") 

With standard query endpoints:

-   You specify the \"query arg\" value, which is passed to the `query` or `queryFn` function that will calculate the desired URL or do the actual fetching
-   The query arg is also serialized to generate the unique internal key for this specific cache entry
-   The single response value is directly stored as the `data` field in the cache entry

Infinite queries work similarly, but have a couple additional layers:

-   You still specify a \"query arg\", which is still used to generate the unique cache key for this specific cache entry
-   However, there is a separation between the \"query arg\" used for the cache key, and the \"page param\" used to fetch a specific page. Since both are useful for determining what to fetch, **your `query` and `queryFn` methods will receive a combined object with `` as the first argument, instead of just the `queryArg` by itself**.
-   The `data` field in the cache entry stores a `` structure that contains *all* of the fetched page results and their corresponding page params used to fetch them.

For example, a Pokemon API endpoint might have a string query arg like `"fire"`, but use a page number as the param to determine which page to fetch out of the results. For a query like `useGetPokemonInfiniteQuery('fire')`, the resulting cache data might look like this:

``` 

    }
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This structure allows flexibility in how your UI chooses to render the data (showing individual pages, flattening into a single list), enables limiting how many pages are kept in cache, and makes it possible to dynamically determine the next or previous page to fetch based on either the data or the page params.

## Defining Infinite Query Endpoints[​](#defining-infinite-query-endpoints "Direct link to Defining Infinite Query Endpoints") 

Infinite query endpoints are defined by returning an object inside the `endpoints` section of `createApi`, and defining the fields using the `build.infiniteQuery()` method. They are an extension of standard query endpoints - you can specify [the same options as standard queries](/rtk-query/usage/queries#defining-query-endpoints) (providing either `query` or `queryFn`, customizing with `transformResponse`, lifecycles with `onCacheEntryAdded` and `onQueryStarted`, defining tags, etc). However, they also require an additional `infiniteQueryOptions` field to specify the infinite query behavior.

With TypeScript, you must supply 3 generic arguments: `build.infiniteQuery<ResultType, QueryArg, PageParam>`, where `ResultType` is the contents of a single page, `QueryArg` is the type passed in as the cache key, and `PageParam` is the value used to request a specific page. If there is no argument, use `void` for the arg type instead.

### `infiniteQueryOptions`[​](#infinitequeryoptions "Direct link to infinitequeryoptions") 

The `infiniteQueryOptions` field includes:

-   `initialPageParam`: the default page param value used for the first request, if this was not specified at the usage site
-   `maxPages`: an optional limit to how many fetched pages will be kept in the cache entry at a time
-   `getNextPageParam`: a required callback you must provide to calculate the next page param, given the existing cached pages and page params
-   `getPreviousPageParam`: an optional callback that will be used to calculate the previous page param, if you try to fetch backwards.

Both `initialPageParam` and `getNextPageParam` are required, to ensure the infinite query can properly fetch the next page of data. Also, `initialPageParam` may be specified when using the endpoint, to override the default value for a first fetch. `maxPages` and `getPreviousPageParam` are both optional.

### Page Param Functions[​](#page-param-functions "Direct link to Page Param Functions") 

`getNextPageParam` and `getPreviousPageParam` are user-defined, giving you flexibility to determine how those values are calculated:

-   TypeScript
-   JavaScript

``` 
export type PageParamFunction<DataType, PageParam, QueryArg> = (
  currentPage: DataType,
  allPages: DataType[],
  currentPageParam: PageParam,
  allPageParams: PageParam[],
  queryArg: QueryArg,
) => PageParam | undefined | null
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

``` 
export 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A page param can be any value at all: numbers, strings, objects, arrays, etc. Since the existing page param values are stored in Redux state, you should still treat those immutably. For example, if you had a param structure like ``, incrementing the page would look like `return `.

Since both actual page contents and page params are passed in, you can calculate new page params based on any of those. This enables a number of possible infinite query use cases, including cursor-based and limit+offset-based queries.

The \"current\" arguments will be either the last page for `getNextPageParam`, or the first page for `getPreviousPageParam`.

The list of arguments is the same as with React Query, but with the addition of `queryArg` at the end. (This is because React Query always has access to the query arg when you pass the options to its `useQuery` hook, but with RTK Query the endpoints are defined separately, so this makes the query arg accessible if you need it to calculate the page params.)

If there is no possible page to fetch in that direction, the callback should return `undefined`.

### Infinite Query Definition Example[​](#infinite-query-definition-example "Direct link to Infinite Query Definition Example") 

A complete example of this for a fictional Pokemon API service might look like:

Infinite Query definition example

``` 
type Pokemon = 

const pokemonApi = createApi(),
  endpoints: (build) => (,
      },
      // The `query` function receives `` as its argument
      query() ?page=$`
      },
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Performing Infinite Queries with React Hooks[​](#performing-infinite-queries-with-react-hooks "Direct link to Performing Infinite Queries with React Hooks") 

[Similar to query endpoints](/rtk-query/usage/queries#performing-queries-with-react-hooks), RTK Query will automatically generate React hooks for infinite query endpoints based on the name of the endpoint. An endpoint field with `getPokemon: build.infiniteQuery()` will generate a hook named `useGetPokemonInfiniteQuery`, as well as a generically-named hook attached to the endpoint, like `api.endpoints.getPokemon.useInfiniteQuery`.

### Hook Types[​](#hook-types "Direct link to Hook Types") 

There are 3 infinite query-related hooks:

1.  [`useInfiniteQuery`](/rtk-query/api/created-api/hooks#useinfinitequery)
    -   Composes `useInfiniteQuerySubscription` and `useInfiniteQueryState`, and is the primary hook. Automatically triggers fetches of data from an endpoint, \'subscribes\' the component to the cached data, and reads the request status and cached data from the Redux store.
2.  [`useInfiniteQuerySubscription`](/rtk-query/api/created-api/hooks#useinfinitequerysubscription)
    -   Returns a `refetch` function and `fetchNext/PreviousPage` functions, and accepts all hooks options. Automatically triggers refetches of data from an endpoint, and \'subscribes\' the component to the cached data.
3.  [`useInfiniteQueryState`](/rtk-query/api/created-api/hooks#useinfinitequerystate)
    -   Returns the query state and accepts `skip` and `selectFromResult`. Reads the request status and cached data from the Redux store.

In practice, the standard `useInfiniteQuery`-based hooks such as `useGetPokemonInfiniteQuery` will be the primary hooks used in your application, but the other hooks are available for specific use cases.

### Query Hook Options[​](#query-hook-options "Direct link to Query Hook Options") 

The query hooks expect two parameters: `(queryArg?, queryOptions?)`.

The `queryOptions` object accepts [all the same parameters as `useQuery`](/rtk-query/usage/queries#query-hook-options), including `skip`, `selectFromResult`, and refetching/polling options.

Unlike normal query hooks, your `query` or `queryFn` callbacks will receive a \"page param\" value to generate the URL or make the request, instead of the \"query arg\" that was passed to the hook. By default, the `initialPageParam` value specified in the endpoint will be used to make the first request, and then your `getNext/PreviousPageParam` callbacks will be used to calculate further page params as you fetch forwards or backwards.

If you want to start from a different page param, you may override the `initialPageParam` by passing it as part of the hook options:

``` 
const  = useGetPokemonInfiniteQuery('fire', )
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The next and previous page params will still be calculated as needed.

### Frequently Used Query Hook Return Values[​](#frequently-used-query-hook-return-values "Direct link to Frequently Used Query Hook Return Values") 

Infinite query hooks return [the same result object as normal query hooks](/rtk-query/usage/queries#frequently-used-query-hook-return-values), but with [a few additional fields specific to infinite queries](/rtk-query/api/created-api/hooks#useinfinitequery-signature) and a different structure for `data` and `currentData`.

-   `data` / `currentData`: These contain the same \"latest successful\" and \"latest for current arg\" results as normal queries, but the value is the `` infinite query object with all fetched pages instead of a single response value.
-   `hasNextPage` / `hasPreviousPage`: When true, indicates that there *should* be another page available to fetch in that direction. This is calculated by calling `getNext/PreviousPageParam` with the latest fetched pages.
-   `isFetchingNext/PreviousPage`: When true, indicates that the current `isFetching` flag represents a fetch in that direction.
-   `isFetchNext/PreviousPageError`: When true, indicates that the current `isError` flag represents an error for a failed fetch in that direction
-   `fetchNext/PreviousPage`: methods that will trigger a fetch for another page in that direction.

In most cases, you will probably read `data` and either `isLoading` or `isFetching` in order to render your UI. You will also want to use the `fetchNext/PreviousPage` methods to trigger fetching additional pages.

### Displaying Infinite Query Data[​](#displaying-infinite-query-data "Direct link to Displaying Infinite Query Data") 

For infinite query hooks, the `data` field returned by the hook will be the `` structure containing all fetched pages, instead of just a single response value.

This gives you control over how the data is used for display. You can flatten all the page contents into a single array for infinite scrolling, use the individual page results for pagination, sort or reverse the entries, or any other logic you need for rendering the UI with this data.

As with any other Redux data, you should avoid mutating these arrays (including calling `array.sort/reverse()` directly on the existing references).

### Infinite Query Hook Usage Example[​](#infinite-query-hook-usage-example "Direct link to Infinite Query Hook Usage Example") 

Here is an example of a typical infinite query endpoint definition, and hook usage in a component:

``` 
type Pokemon = 

const pokemonApi = createApi(),
  endpoints: (build) => (,
      query() ?page=$`
      },
    }),
  }),
})

function PokemonList(: )  =
    pokemonApi.useGetPokemonInfiniteQuery(pokemonType)

  const handleNextPage = async () => 

  const handleRefetch = async () => 

  const allResults = data?.pages.flat() ?? []

  return (
    <div>
      <div>Type: </div>
      <div>
        ></div>
        ))}
      </div>
      <button onClick=>Fetch More</button>
      <button onClick=>Refetch</button>
    </div>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

In this example, the server returns an array of Pokemon as the response for each individual page. This component shows the results as a single list. Since the `data` field itself has a `pages` array of all responses, the component needs to flatten the pages into a single array to render that list. Alternately, it could map over the pages and show them in a paginated format.

Similarly, this example relies on manual user clicks on a \"Fetch More\" button to trigger fetching the next page, but could automatically call `fetchNextPage` based on things like an `IntersectionObserver`, a list component triggering some kind of \"end of the list\" event, or other similar indicators.

The endpoint itself only defines `getNextPageParam`, so this example doesn\'t support fetching backwards, but that can be provided in cases where backwards fetching makes sense. The page param here is a simple incremented number, but the page param

## Infinite Query Behaviors[​](#infinite-query-behaviors "Direct link to Infinite Query Behaviors") 

### Overlapping Page Fetches[​](#overlapping-page-fetches "Direct link to Overlapping Page Fetches") 

Since all pages are stored in a single cache entry, there can only be one request in progress at a time. RTK Query already has logic built in to bail out of running a new request if there is already a request in flight for that cache entry.

That means that if you call `fetchNextPage()` again while an existing request is in progress, the second call won\'t actually execute a request. Be sure to either await the previous `fetchNextPage()` promise result first or check the `isFetching` flag if you have concerns about a potential request already in progress.

The promise returned from `fetchNextPage()` does have [a `promise.abort()` method attached](/api/createAsyncThunk#canceling-while-running) that will force the earlier request to reject and not save the results. Note that this will mark the cache entry as errored, but the data will still exist. Since `promise.abort()` is synchronous, you would also need to await the previous promise to ensure the rejection is handled, and then trigger the new page fetch.

### Refetching[​](#refetching "Direct link to Refetching") 

When an infinite query endpoint is refetched (due to tag invalidation, polling, arg change configuration, or manual refetching), RTK Query\'s default behavior is **sequentially refetching *all* pages currently in the cache**. This ensures that the client is always working with the latest data, and avoids stale cursors or duplicate records.

If the cache entry is ever removed and then re-added, it will start with only fetching the initial page.

There may be cases when you want a refetch to *only* refetch the first page, and not any of the other pages in cache (ie, the refetch shrinks the cache from N pages to 1 page). This can be done via the `refetchCachedPages` option, which can be passed in several different places:

-   Defined on the endpoint as part of `infiniteQueryOptions`: applies to all attempted refetches
-   Passed as an option to a `useInfiniteQuery` hook: applies to all attempted refetches
-   Passed as an option to `endpoint.initiate()`, or the `refetch` method available on the `initiate` or hook result objects: applies only to the manually triggered refetch

Overall, the refetch logic defaults to refetching all pages, but will override that with the option provided to the endpoint or a manual refetch.

### Limiting Cache Entry Size[​](#limiting-cache-entry-size "Direct link to Limiting Cache Entry Size") 

All fetched pages for a given query arg are stored in the `pages` array in that cache entry. By default, there is no limit to the number of stored pages - if you call `fetchNextPage()` 1000 times, `data.pages` will have 1000 pages stored.

If you need to limit the number of stored pages (for reasons like memory usage), you can supply a `maxPages` option as part of the endpoint. If provided, fetching a page when already at the max will automatically drop the last page in the opposite direction. For example, with `maxPages: 3` and a cached page params of `[1, 2, 3]`, calling `fetchNextPage()` would result in page `1` being dropped and the new cached pages being `[2, 3, 4]`. From there, calling `fetchNextPage()` would result in `[3, 4, 5]`, or calling `fetchPreviousPage()` would go back to `[1, 2, 3]`.

## Common Infinite Query Patterns[​](#common-infinite-query-patterns "Direct link to Common Infinite Query Patterns") 

The `getNext/PreviousPageParam` callbacks offer flexibility in how you interact with the backend API.

Here are some examples of common infinite query patterns to show how you might approach different use cases.

For additional examples, and to see some of these patterns in action, see [the RTK Query \"infinite queries\" example app in the repo](https://github.com/reduxjs/redux-toolkit/tree/master/examples/query/react/infinite-queries).

### Basic Pagination[​](#basic-pagination "Direct link to Basic Pagination") 

For a simple API that just needs page numbers, you can calculate the previous and next page numbers based on the existing page params:

``` 
const pokemonApi = createApi(,
      },
      query() `
      },
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Pagination with Sizes[​](#pagination-with-sizes "Direct link to Pagination with Sizes") 

For an API that accepts values like page number and page size and includes total pages in the response, you can calculate whether there are more pages remaining:

``` 
type ProjectsResponse = 

type ProjectsInitialPageParam = 

const projectsApi = createApi(,
        getNextPageParam: (
          lastPage,
          allPages,
          lastPageParam,
          allPageParams,
        ) => 

          return 
        },
        getPreviousPageParam: (
          firstPage,
          allPages,
          firstPageParam,
          allPageParams,
        ) => 
        },
      },
      query: ( }) => &size=$`
      },
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Bidirectional Cursors[​](#bidirectional-cursors "Direct link to Bidirectional Cursors") 

If the server sends back cursor values in the response, you can use those as the page params for the next and previous requests:

``` 
type ProjectsCursorPaginated = 
}

type ProjectsInitialPageParam = 
type QueryParamLimit = number

const projectsApi = createApi(,
        getPreviousPageParam: (
          firstPage,
          allPages,
          firstPageParam,
          allPageParams,
        ) => 
          return 
        },
        getNextPageParam: (
          lastPage,
          allPages,
          lastPageParam,
          allPageParams,
        ) => 
          return 
        },
      },
      query: ( }) =>  else if (before != null)  else if (around != null) 

        return `https://example.com/api/projectsBidirectionalCursor?$`,
      },
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Limit and Offset[​](#limit-and-offset "Direct link to Limit and Offset") 

If the API expects a combination of limit and offset values, those can also be calculated based on the responses and page params.

``` 
export type ProjectsResponse = 

type ProjectsInitialPageParam = 

const projectsApi = createApi(,
        getNextPageParam: (
          lastPage,
          allPages,
          lastPageParam,
          allPageParams,
        ) => 

          return 
        },
        getPreviousPageParam: (
          firstPage,
          allPages,
          firstPageParam,
          allPageParams,
        ) => 
        },
      },
      query: ( }) => &limit=$`
      },
    }),
  }),
})
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

const pokemonSchema = v.object()
type Pokemon = v.InferOutput<typeof pokemonSchema>
const transformedPokemonSchema = v.object()
type TransformedPokemon = v.InferOutput<typeof transformedPokemonSchema>

const api = createApi(),
  endpoints: (build) => () => `type/$?page=$`,
      // argSchema for infinite queries must have both queryArg and pageParam
      argSchema: v.object(),
      responseSchema: v.array(pokemonSchema),
    }),
    getTransformedPokemon: build.infiniteQuery<
      TransformedPokemon[],
      string,
      number
    >() => `type/$?page=$`,
      argSchema: v.object(),
      rawResponseSchema: v.array(pokemonSchema),
      transformResponse: (response) =>
        response.map((pokemon) => ()),
      // responseSchema can still be provided, to validate the transformed response
      responseSchema: v.array(transformedPokemonSchema),
    }),
  }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/usage/infinite-queries.mdx)

[Last updated on **Nov 23, 2025**]