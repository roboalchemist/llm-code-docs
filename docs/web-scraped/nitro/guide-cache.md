# Source: https://nitro.build/guide/cache

-   [](/guide "Getting Started")

    ::: 
    []
    :::

    [Getting Started]
-   [](/deploy "Overview")

    ::: 
    []
    :::

    [Overview]
-   [](/config "Config")

    ::: 
    []
    :::

    [Config]

-   [[][Getting Started]](/guide)
-   [[][Server Utils]](/guide/utils)
-   [[][Tasks]](/guide/tasks)
-   [[][Server Routes]](/guide/routing)
-   [[][WebSocket]](/guide/websocket)
-   [[][KV Storage]](/guide/storage)
-   [[][SQL Database]](/guide/database)
-   [[][Cache]](/guide/cache)
-   [[][Fetch]](/guide/fetch)
-   [[][Assets]](/guide/assets)
-   [[][Plugins]](/guide/plugins)
-   [[][Configuration]](/guide/configuration)
-   [[][TypeScript]](/guide/typescript)
-   [[][Nightly Channel]](/guide/nightly)

<div>

# Cache 

Nitro provides a caching system built on top of the storage layer.

</div>

<div>

## [[[]]Cached event handlers](#cached-event-handlers) 

To cache an event handler, you simply need to use the `defineCachedEventHandler` method.

It works like [`defineEventHandler`](https://v1.h3.dev/guide/event-handler) but with an additional second [options](#options) parameter.

[][server/routes/cached.ts]

[]

``` 
// Cache an API handler
export default defineCachedEventHandler((event) => , );
```

With this example, the response will be cached for 1 hour and a stale value will be sent to the client while the cache is being updated in the background. If you want to immediately return the updated response set `swr: false`.

[]All incoming request headers are dropped when handling cached responses. If you define the `varies` option, only the specified headers will be considered when caching and serving the responses.

See the [options](#options) section for more details about the available options.

[]You can also use the `cachedEventHandler` method as alias of `defineCachedEventHandler`.

## [[[]]Cached functions](#cached-functions) 

You can also cache a function using the `defineCachedFunction` function. This is useful for caching the result of a function that is not an event handler, but is part of one, and reusing it in multiple handlers.

For example, you might want to cache the result of an API call for one hour:

[][server/utils/github.ts]

[][server/api/stars/\[\...repo\].ts]

[]

``` 
export const cachedGHStars = defineCachedFunction(async (repo: string) => `)

  return data.stargazers_count
}, )
```

[]

``` 
export default defineEventHandler(async (event) => 
})
```

The stars will be cached in development inside `.nitro/cache/functions/ghStars/<owner>/<repo>.json` with `value` being the number of stars.

[]

``` 

```

[]Because the cached data is serialized to JSON, it is important that the cached function does not return anything that cannot be serialized, such as Symbols, Maps, Sets...

[]You can also use the `cachedFunction` method as alias of `defineCachedFunction`.

### [[[]]Edge workers](#edge-workers) 

In edge workers, the instance is destroyed after each request. Nitro automatically uses `event.waitUntil` to keep the instance alive while the cache is being updated while the response is sent to the client.

To ensure that your cached functions work as expected in edge workers, you should always pass the `event` as the first argument to the function using `defineCachedFunction`.

[][server/utils/github.ts]

[][server/api/stars/\[\...repo\].ts]

[]

``` 
import type  from 'h3'

export const cachedGHStars = defineCachedFunction(async (event: H3Event, repo: string) => `)

  return data.stargazers_count
}, )
```

[]

``` 
export default defineEventHandler(async (event) => 
})
```

This way, the function will be able to keep the instance alive while the cache is being updated without slowing down the response to the client.

## [[[]]Caching route rules](#caching-route-rules) 

This feature enables you to add caching routes based on a glob pattern directly in the main configuration file. This is especially useful to have a global cache strategy for a part of your application.

Cache all the blog routes for 1 hour with `stale-while-revalidate` behavior:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig( },
  },
});
```

[]

``` 
export default defineNuxtConfig( },
  },
});
```

If we want to use a [custom storage](#customize-cache-storage) mount point, we can use the `base` option.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(,
  },
  routeRules:  },
  },
});
```

[]

``` 
export default defineNuxtConfig(,
    },
  },
  routeRules:  },
  },
});
```

## [[[]]Customize cache storage](#customize-cache-storage) 

Nitro stores the data in the `cache:` mount point.

-   In production, it will use the [memory driver](https://unstorage.unjs.io/drivers/memory) by default.
-   In development, it will use the [filesystem driver](https://unstorage.unjs.io/drivers/fs), writing to a temporary dir.

To overwrite the production storage, set the `cache` mount point using the `storage` option:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(
  }
})
```

[]

``` 
export default defineNuxtConfig(
    }
  }
})
```

In development, you can also overwrite the cache mount point using the `devStorage` option:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(
  }
})
```

[]

``` 
export default defineNuxtConfig(
    }
  }
})
```

## [[[]]Options](#options) 

The `cachedEventHandler` and `cachedFunction` functions accept the following options:

[base]

[string]

Name of the storage mountpoint to use for caching.\
Default to `cache`.

[name]

[string]

Guessed from function name if not provided, and falls back to `'_'` otherwise.

[group]

[string]

Defaults to `'nitro/handlers'` for handlers and `'nitro/functions'` for functions.

[getKey()]

[(\...args) =\> string]

A function that accepts the same arguments as the original function and returns a cache key (`String`).\
If not provided, a built-in hash function will be used to generate a key based on the function arguments.

[integrity]

[string]

A value that invalidates the cache when changed.\
By default, it is computed from **function code**, used in development to invalidate the cache when the function code changes.

[maxAge]

[number]

Maximum age that cache is valid, in seconds.\
Default to `1` (second).

[staleMaxAge]

[number]

Maximum age that a stale cache is valid, in seconds. If set to `-1` a stale value will still be sent to the client while the cache updates in the background.\
Defaults to `0` (disabled).

[swr]

[boolean]

Enable `stale-while-revalidate` behavior to serve a stale cached response while asynchronously revalidating it.\
Defaults to `true`.

[shouldInvalidateCache()]

[(..args) =\> boolean]

A function that returns a `boolean` to invalidate the current cache and create a new one.

[shouldBypassCache()]

[(..args) =\> boolean]

A function that returns a `boolean` to bypass the current cache without invalidating the existing entry.

[varies]

[string\[\]]

An array of request headers to be considered for the cache, [learn more](https://github.com/nitrojs/nitro/issues/1031). If utilizing in a multi-tenant environment, you may want to pass `['host', 'x-forwarded-host']` to ensure these headers are not discarded and that the cache is unique per tenant.

## [[[]]Cache keys and invalidation](#cache-keys-and-invalidation) 

When using the `defineCachedFunction` or `defineCachedEventHandler` functions, the cache key is generated using the following pattern:

[]

``` 
`$:$:$.json`
```

For example, the following function:

[]

``` 
const getAccessToken = defineCachedFunction(() => , )
```

Will generate the following cache key:

[]

``` 
nitro:functions:getAccessToken:default.json
```

You can invalidate the cached function entry with:

[]

``` 
await useStorage('cache').removeItem('nitro:functions:getAccessToken:default.json')
```

### [[[]]Normalizing Cache Keys](#normalizing-cache-keys) 

[]**Cache keys are automatically normalized** using an internal utility that removes non-alphanumeric characters such as `/` and `-`. This behavior helps ensure compatibility across various storage backends (e.g., `file systems`, `key-value` stores) that might have restrictions on characters in `keys`, and also prevents potential path traversal vulnerabilities.

For example:

[]

``` 
getKey: () => '/api/products/sale-items'
```

Would generate a key like:

[]

``` 
api/productssaleitems.json
```

This behavior may result in keys that look different from the original route or identifier.

[]To manually reproduce the same normalized key pattern used by Nitro (e.g., when invalidating cache entries), you can use the `escapeKey` utility function provided below:

[]

``` 
function escapeKey(key: string | string[]) 
```

It\'s recommended to use `escapeKey()` when invalidating manually using route paths or identifiers to ensure consistency with Nitro\'s internal key generation.

For example, if your `getKey` function is:

[]

``` 
getKey: (id: string) => `product/$/details`
```

And you want to invalidate `product/123/details`, you would do:

[]

``` 
const normalizedKey = escapeKey('product/123/details')
await useStorage('cache').removeItem(`nitro:functions:getProductDetails:$.json`)
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/6.cache.md)

[](/guide/database)

[]

SQL Database

Nitro provides a built-in and lightweight SQL database layer.

[](/guide/fetch)

[]

Fetch

Nitro provides a built-in fetch API that can be used to get data from server endpoints or from other sources. It\'s built on top of the ofetch.

[On this page][[]]

[On this page][[]]

-   [[Cached event handlers]](#cached-event-handlers)
-   [[Cached functions]](#cached-functions)
    -   [[Edge workers]](#edge-workers)
-   [[Caching route rules]](#caching-route-rules)
-   [[Customize cache storage]](#customize-cache-storage)
-   [[Options]](#options)
-   [[Cache keys and invalidation]](#cache-keys-and-invalidation)
    -   [[Normalizing Cache Keys]](#normalizing-cache-keys)