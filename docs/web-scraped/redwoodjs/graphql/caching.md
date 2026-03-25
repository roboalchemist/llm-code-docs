# Source: https://docs.redwoodjs.com/docs/graphql/caching

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [GraphQL](/docs/graphql/index)
-   [Caching]

[Version: 8.8]

On this page

<div>

# GraphQL Caching

</div>

## Client Caching[​](#client-caching "Direct link to Client Caching") 

Apollo Client stores the results of your GraphQL queries in a local, normalized, in-memory cache.

Redwood provides a custom hook called `useCache` that makes it more convenience to access and use the cache object.

Please refer to Apollo\'s documentation for complete information about [Caching in Apollo Client](https://www.apollographql.com/docs/react/caching/overview).

### useCache Hook[​](#usecache-hook "Direct link to useCache Hook") 

`useCache` is a custom hook that returns the cache object and some useful methods to interact with the cache.

Example of useCache() hook

``` 
import  from '@redwoodjs/web/apollo'

const CacheExample = () =>  =
    useCache()

  // ...
}
```

### Helper Methods[​](#helper-methods "Direct link to Helper Methods") 

#### cache[​](#cache "Direct link to cache") 

The cache object itself.

With `cache` you can access methods on the cache not exposed as helpers here, such as `readQuery` or `gc` for garbage collections. See Apollo\'s [caching interaction](https://www.apollographql.com/docs/react/caching/cache-interaction) documentation.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

To help understand the structure of your cached data, you can install the [Apollo Client Devtools](https://www.apollographql.com/docs/react/development-testing/developer-tooling/#apollo-client-devtools).

This browser extension includes an inspector that enables you to view all of the normalized objects contained in your cache.

Alternatively, see [extract](#extract) to get a normalized cache object you can inspect.

#### evict[​](#evict "Direct link to evict") 

Either removes a normalized object from the cache or removes a specific field from a normalized object in the cache.

Example of evict

``` 
import  from '@redwoodjs/web/apollo'

const CacheExample = () =>  = useCache()

  // You can remove any normalized object from the cache using the evict method:
  evict()

  // You can also remove a single field from a cached object by providing the name of the field to remove
  evict()
}
```

#### extract[​](#extract "Direct link to extract") 

Returns a serialized representation of the cache\'s current contents

Example of extract

``` 
import  from '@redwoodjs/web/apollo'

const CacheExample = () =>  = useCache()

  console.log(extract())
}
```

#### identify[​](#identify "Direct link to identify") 

If a type in your cache uses a custom cache ID (or even if it doesn\'t), you can use the `cache.identify` method to obtain the cache ID for an object of that type.

This method takes an object and computes its ID based on both its `__typename` and its identifier field(s).

This means you don\'t have to keep track of which fields make up each type\'s cache ID.

Example of identify

``` 
import  from '@redwoodjs/web/apollo'

const CacheExample = () =>  = useCache()

  const id = identify()

  console.log(id)
}
```

#### modify[​](#modify "Direct link to modify") 

Modifies one or more field values of a cached object.

You must provide a modifier function for each field to modify. A modifier function takes a cached field\'s current value and returns the value that should replace it.

Returns `true` if the cache was modified successfully and `false` otherwise.

Example of modify

``` 
import  from '@redwoodjs/web/apollo'

const CacheExample = () =>  = useCache()

  const id = identify()

  modify(id, )
}
```

#### resetStore[​](#resetstore "Direct link to resetStore") 

Reset the cache entirely, such as when a user logs out.

See Apollo\'s [Resetting the Cache](https://www.apollographql.com/docs/react/caching/advanced-topics#resetting-the-cache) for more details.

Example of resetStore

``` 
import  from '@redwoodjs/web/apollo'

const Logout = () =>  = useCache()

  return (
    <button onClick=>
      Log out
    </button>
  )
}
```

#### clearStore[​](#clearstore "Direct link to clearStore") 

To reset the cache without refetching active queries, use `clearStore`.

See Apollo\'s documentation on [Resetting the Cache](https://www.apollographql.com/docs/react/caching/advanced-topics#resetting-the-cache) for more details.

Example of clearStore

``` 
import  from '@redwoodjs/web/apollo'

const Logout = () =>  = useCache()

  return (
    <button onClick=>
      Log out
    </button>
  )
}
```

### Persisting Cache[​](#persisting-cache "Direct link to Persisting Cache") 

Apollo Client allows you [persist and rehydrate](https://www.apollographql.com/docs/react/caching/advanced-topics/#persisting-the-cache) the `InMemoryCache` from a storage provider like `AsyncStorage` or `localStorage`. To do so, use the `apollo3-cache-persist` package. This package works with a variety of storage providers.

To get started, pass your `cache` from the `useCache` hook and a storage provider to `persistCache`. By default, the contents of your cache are immediately restored asynchronously, and they\'re persisted on every write to the cache with a short, configurable debounce interval.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

The persistCache method is async and returns a Promise.

Example of persisting cache

``` 
import  from 'apollo3-cache-persist'

import  from '@redwoodjs/web/apollo'

const PersistCacheExample = async () =>  = useCache()

  await persistCache()

  // ...
}
```

## Response Caching[​](#response-caching "Direct link to Response Caching") 

[Response caching](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching) is a technique for reducing server load by caching GraphQL query operation results. For incoming GraphQL Query operations with the same variable values, the same response is returned from a cache instead of executed again.

Redwood\'s GraphQL Server offers response caching via the `useResponseCache` [GraphQL Yoga plugin](https://github.com/dotansimha/graphql-yoga/tree/main/packages/plugins/response-cache).

### Setup[​](#setup "Direct link to Setup") 

To setup response caching, first install `@graphql-yoga/plugin-response-cache`:

``` 
yarn workspace api add @graphql-yoga/plugin-response-cache
```

And then modify your `api/src/functions/graphql.ts` function to add (and configure) the `useResponseCache` plugin to the handler\'s `extraPlugins`:

Example of GraphQL Response Caching

``` 
import  from '@graphql-yoga/plugin-response-cache'

import  from '@redwoodjs/graphql-server'

import directives from 'src/directives/**/*.'
import sdls from 'src/graphql/**/*.sdl.'
import services from 'src/services/**/*.'

import  from 'src/lib/db'
import  from 'src/lib/logger'

export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
  extraPlugins: [
    useResponseCache(,
    }),
  ],
  onException: () => ,
})
```

### In-Memory vs External Caching[​](#in-memory-vs-external-caching "Direct link to In-Memory vs External Caching") 

By default, the response cache stores all the cached query results in memory. That means if you have deployed to a serverless hosting platform, the cache only lives per-request.

In this case you would want to use an [External Cache](https://the-guild.dev/graphql/yoga-server/docs/features/response-caching#external-cache) like Redis.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/graphql/caching.md)