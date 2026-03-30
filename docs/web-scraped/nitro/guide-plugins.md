# Source: https://nitro.build/guide/plugins

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

# Plugins 

Use plugins to extend Nitro\'s runtime behavior.

</div>

<div>

Nitro plugins will be **executed once** during server startup in order to allow extending Nitro\'s runtime behavior. They receive `nitroApp` context, which can be used to hook into Nitro lifecycle events.

Plugins are auto-registered from `plugins/` directory and run synchronously (by order of file name) on the first Nitro initialization.

**Example:**

[][server/plugins/test.ts]

[]

``` 
export default defineNitroPlugin((nitroApp) => )
```

If you have plugins in another directory, you can use the `plugins` option:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig()
```

[]

``` 
export default defineNuxtConfig(
})
```

## [[[]]Nitro runtime hooks](#nitro-runtime-hooks) 

You can use Nitro [hooks](https://github.com/unjs/hookable) to extend the default runtime behaviour of Nitro by registering custom (async or sync) functions to the lifecycle events within plugins.

**Example:**

[]

``` 
export default defineNitroPlugin((nitro) => );
})
```

### [[[]]Available hooks](#available-hooks) 

See the [source code](https://github.com/nitrojs/nitro/blob/v2/src/core/index.ts#L75) for list of all available runtime hooks.

-   `"close", () => `
-   `"error", (error, ) => `
-   `"render:response", (response, ) => `
-   `"request", (event) => `
-   `"beforeResponse", (event, ) => `
-   `"afterResponse", (event, ) => `

## [[[]]Examples](#examples) 

### [[[]]Capturing errors](#capturing-errors) 

You can use plugins to capture all application errors.

[]

``` 
export default defineNitroPlugin((nitro) => ) =>  Application error:`, error)
  });
})
```

### [[[]]Graceful shutdown](#graceful-shutdown) 

You can use plugins to register a hook that resolves when Nitro is closed.

[]

``` 
export default defineNitroPlugin((nitro) => );
})
```

### [[[]]Request and response lifecycle](#request-and-response-lifecycle) 

You can use plugins to register a hook that can run on request lifecycle:

[]

``` 
export default defineNitroPlugin((nitroApp) => );

  nitroApp.hooks.hook("beforeResponse", (event, ) => );
  });

  nitroApp.hooks.hook("afterResponse", (event, ) => );
  });
});
```

### [[[]]Renderer response](#renderer-response) 

You can use plugins to register a hook that modifies the [`renderer`](https://nitro.build/config#renderer) response.

[]This **only works** for render handler defined with [`renderer`](https://nitro.build/config#renderer) and won\'t be called for other api/server routes. In [Nuxt](https://nuxt.com/) this hook will be called for Server-side rendered pages

[]

``` 
export default defineNitroPlugin((nitro) => ) => )
})
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/9.plugins.md)

[](/guide/assets)

[]

Assets

[](/guide/configuration)

[]

Configuration

Customize and extend Nitro defaults.

[On this page][[]]

[On this page][[]]

-   [[Nitro runtime hooks]](#nitro-runtime-hooks)
    -   [[Available hooks]](#available-hooks)
-   [[Examples]](#examples)
    -   [[Capturing errors]](#capturing-errors)
    -   [[Graceful shutdown]](#graceful-shutdown)
    -   [[Request and response lifecycle]](#request-and-response-lifecycle)
    -   [[Renderer response]](#renderer-response)