# Source: https://nitro.build/guide/routing

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

# Server Routes 

Nitro supports filesystem routing to automatically map files to h3 routes.

</div>

<div>

## [[[]]Event handlers](#event-handlers) 

An [event handler](https://v1.h3.dev/guide/event-handler) is a function that will be bound to a route and executed when the route is matched by the router for an incoming request.

[[]](https://v1.h3.dev/guide/event-handler)[][] Read more in [v1.h3.dev/guide/event-handler].

## [[[]]Filesystem routing](#filesystem-routing) 

Nitro supports file-based routing for your API routes (files are automatically mapped to [h3 routes](https://v1.h3.dev/guide/router)). Defining a route is as simple as creating a file inside the `server/api/` or `server/routes/` directory.

You can only define one handler per files and you can [append the HTTP method](#specific-request-method) to the filename to define a specific request method.

[]

``` 
server/
  api/
    test.ts      <-- /api/test
  routes/
    hello.get.ts     <-- GET /hello
    hello.post.ts    <-- POST /hello
nitro.config.ts
```

You can nest routes by creating subdirectories.

[]

``` 
server/
  routes/
    communities/
      index.get.ts
      index.post.ts
      [id]/
        index.get.ts
        index.post.ts
    hello.get.ts
    hello.post.ts
```

### [[[]]Simple routes](#simple-routes) 

First, create a file in `server/routes/` or `server/api/` directory. The filename will be the route path.

Then, export a function wrapped in `defineEventHandler` that will be executed when the route is matched.

[][server/api/test.ts]

[]

``` 
export default defineEventHandler(() => 
})
```

### [[[]]Route with params](#route-with-params) 

#### [Single param](#single-param) 

To define a route with params, use the `[<param>]` syntax where `<param>` is the name of the param. The param will be available in the `event.context.params` object or using the `getRouterParam` utility from [h3](https://v1.h3.dev).

[][server/routes/hello/\[name\].ts]

[]

``` 
export default defineEventHandler(event => !`
})
```

Call the route with the param `/hello/nitro`, you will get:

[Response]

[]

``` 
Hello nitro!
```

#### [Multiple params](#multiple-params) 

You can define multiple params in a route using `[<param1>]/[<param2>]` syntax where each param is a folder. You **cannot** define multiple params in a single filename of folder.

[][server/routes/hello/\[name\]/\[age\].ts]

[]

``` 
export default defineEventHandler(event => ! You are $ years old.`
})
```

#### [Catch all params](#catch-all-params) 

You can capture all the remaining parts of a URL using `[...<param>]` syntax. This will include the `/` in the param.

[][server/routes/hello/\[\...name\].ts]

[]

``` 
export default defineEventHandler(event => !`
})
```

Call the route with the param `/hello/nitro/is/hot`, you will get:

[Response]

[]

``` 
Hello nitro/is/hot!
```

### [[[]]Specific request method](#specific-request-method) 

You can append the HTTP method to the filename to force the route to be matched only for a specific HTTP request method, for example `hello.get.ts` will only match for `GET` requests. You can use any HTTP method you want.

[GET]

[POST]

[]

``` 
// server/routes/users/[id].get.ts
export default defineEventHandler(async (event) => )
```

[]

``` 
// server/routes/users.post.ts
export default defineEventHandler(async event => 
})
```

### [[[]]Catch all route](#catch-all-route) 

You can create a special route that will match all routes that are not matched by any other route. This is useful for creating a default route.

To create a catch all route, create a file named `[...].ts` in the `server/routes/` or `server/api/` directory or in any subdirectory.

[][server/routes/\[\...\].ts]

[]

``` 
export default defineEventHandler(event => !`
})
```

### [[[]]Environment specific handlers](#environment-specific-handlers) 

You can specify for a route that will only be included in specific builds by adding a `.dev`, `.prod` or `.prerender` suffix to the file name, for example: `routes/test.get.dev.ts` or `routes/test.get.prod.ts`.

[] You can specify multiple environments or specify a preset name as environment using programmatic registration of routes via `handlers[]` config.

## [[[]]Middleware](#middleware) 

Nitro route middleware can hook into the request lifecycle.

[]A middleware can modify the request before it is processed, not after.

[[]](https://v1.h3.dev/guide/event-handler#middleware)[][] Read more in [v1.h3.dev/guide/event-handler#middleware].

Middleware are auto-registered within the `server/middleware/` directory.

[]

``` 
server/
  routes/
    hello.ts
  middleware/
    auth.ts
    logger.ts
    ...
nitro.config.ts
```

### [[[]]Simple middleware](#simple-middleware) 

Middleware are defined exactly like route handlers with the only exception that they should not return anything. Returning from middleware behaves like returning from a request - the value will be returned as a response and further code will not be ran.

[][server/middleware/auth.ts]

[]

``` 
export default defineEventHandler((event) => 
})
```

Middleware in `server/middleware/` directory are automatically registered for all routes. If you want to register a middleware for a specific route, see [Object Syntax Event Handler](https://v1.h3.dev/guide/event-handler#object-syntax).

[]Returning anything from a middleware will close the request and should be avoided! Any returned value from middleware will be the response and further code will not be executed however **this is not recommended to do!**

### [[[]]Route Meta](#route-meta) 

You can define route handler meta at build-time using `defineRouteMeta` macro in the event handler files.

[] 🚧 This feature is currently experimental.

[][server/api/test.ts]

[]

``` 
defineRouteMeta(],
  },
});

export default defineEventHandler(() => "OK");
```

[[]](https://swagger.io/specification/v3/)[][]This feature is currently usable to specify OpenAPI meta. See swagger specification for available OpenAPI options.

### [[[]]Execution order](#execution-order) 

Middleware are executed in directory listing order.

[]

``` 
server/
  middleware/
    auth.ts <-- First
    logger.ts <-- Second
    ... <-- Third
```

Prefix middleware with a number to control their execution order.

[]

``` 
server/
  middleware/
    1.logger.ts <-- First
    2.auth.ts <-- Second
    3.... <-- Third
```

[]Remember that file names are sorted as strings, thus for example if you have 3 files `1.filename.ts`, `2.filename.ts` and `10.filename.ts`, the `10.filename.ts` will come after the `1.filename.ts`. To avoid this, prefix `1-9` with a `0` like `01`, if you have more than 10 middleware in the same directory.

### [[[]]Request filtering](#request-filtering) 

Middleware are executed on every request.

Apply custom logic to scope them to specific conditions.

For example, you can use the URL to apply a middleware to a specific route:

[][server/middleware/auth.ts]

[]

``` 
export default defineEventHandler((event) => 
  }
})
```

## [[[]]Error handling](#error-handling) 

You can use the [utilities available in H3](https://v1.h3.dev/guide/event-handler#error-handling) to handle errors in both routes and middlewares.

The way errors are sent back to the client depends on the route\'s path. For most routes `Content-Type` is set to `text/html` by default and a simple html error page is delivered. If the route starts with `/api/` (either because it is placed in `api/` or `routes/api/`) the default will change to `application/json` and a JSON object will be sent.

This behaviour can be overridden by some request properties (e.g.: `Accept` or `User-Agent` headers).

## [[[]]Route Rules](#route-rules) 

Nitro allows you to add logic at the top-level for each route of your configuration. It can be used for redirecting, proxying, caching and adding headers to routes.

It is a map from route pattern (following [radix3](https://github.com/unjs/rou3/tree/radix3#route-matcher)) to route options.

When `cache` option is set, handlers matching pattern will be automatically wrapped with `defineCachedEventHandler`. See the [cache guide](/guide/cache) to learn more about this function.

[]`swr: true|number` is shortcut for `cache: `

You can set route rules in `nitro.config.ts` using the `routeRules` option.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(,
    '/blog/**': ,
    '/blog/**': ,
    '/blog/**':  },
    '/assets/**':  },
    '/api/v1/**':  },
    '/old-page': ,
    '/old-page/**': ,
    '/proxy/example': ,
    '/proxy/**': ,
  }
})
```

[]

``` 
export default defineNuxtConfig(,
    '/blog/**': ,
    '/blog/**': ,
    '/blog/**':  },
    '/assets/**':  },
    '/api/v1/**':  },
    '/old-page': ,
    '/old-page/**': ,
    '/proxy/example': ,
    '/proxy/**': ,
  }
})
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/2.routing.md)

[](/guide/tasks)

[]

Tasks

Nitro tasks allow on-off operations in runtime.

[](/guide/websocket)

[]

WebSocket

Nitro natively supports a cross platform WebSocket API

[On this page][[]]

[On this page][[]]

-   [[Event handlers]](#event-handlers)
-   [[Filesystem routing]](#filesystem-routing)
    -   [[Simple routes]](#simple-routes)
    -   [[Route with params]](#route-with-params)
    -   [[Specific request method]](#specific-request-method)
    -   [[Catch all route]](#catch-all-route)
    -   [[Environment specific handlers]](#environment-specific-handlers)
-   [[Middleware]](#middleware)
    -   [[Simple middleware]](#simple-middleware)
    -   [[Route Meta]](#route-meta)
    -   [[Execution order]](#execution-order)
    -   [[Request filtering]](#request-filtering)
-   [[Error handling]](#error-handling)
-   [[Route Rules]](#route-rules)