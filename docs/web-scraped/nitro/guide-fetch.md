# Source: https://nitro.build/guide/fetch

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

# Fetch 

Nitro provides a built-in fetch API that can be used to get data from server endpoints or from other sources. It\'s built on top of the ofetch.

</div>

<div>

## [[[]]Usage](#usage) 

In your handler, you just have to call the `$fetch` function to make a request. The response will be automatically parsed.

[Router Handler]

[]

``` 
export default defineEventHandler(async (event) => )
```

You can pass a generic type to the `$fetch` function to get a better type inference.

[Router Handler]

[]

``` 
import  from '~/types'

export default defineEventHandler(async (event) => )
```

You can pass many options to the `$fetch` function like the method, headers, body, query, etc.

[Router Handler]

[]

``` 
import  from '~/types'

export default defineEventHandler(async (event) => ,
    body: 
  })

  return data
})
```

See more about the usage of the `$fetch` function in the [ofetch](https://ofetch.unjs.io) documentation.

## [[[]]In-Server fetch](#in-server-fetch) 

You can also use the `$fetch` function to make internal requests to other handlers.

[Router Handler]

[]

``` 
export default defineEventHandler(async (event) => )
```

In reality, no fetch request is made and the handler is directly called, thanks to [unenv](https://unenv.unjs.io). This is useful to avoid making HTTP request overhead.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/7.fetch.md)

[](/guide/cache)

[]

Cache

Nitro provides a caching system built on top of the storage layer.

[](/guide/assets)

[]

Assets

[On this page][[]]

[On this page][[]]

-   [[Usage]](#usage)
-   [[In-Server fetch]](#in-server-fetch)