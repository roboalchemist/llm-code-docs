# Source: https://nitro.build/guide/configuration

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

# Configuration 

Customize and extend Nitro defaults.

</div>

<div>

[[]](/config)[]See [config reference](/config) for available options.

You can customize your Nitro builder with a configuration file.

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

[] If you are using [Nuxt](https://nuxt.com), use the `nitro` option in your Nuxt config instead.

[] Nitro loads the configuration using [c12](https://github.com/unjs/c12), giving more possibilities such as using `.nitrorc` file in current working directory or in the user\'s home directory.

## [[[]]Runtime configuration](#runtime-configuration) 

Nitro provides a runtime config API to expose configuration within your application, with the ability to update it at runtime by setting environment variables. This is useful when you want to expose different configuration values for different environments (e.g. development, staging, production). For example, you can use this to expose different API endpoints for different environments or to expose different feature flags.

First, you need to define the runtime config in your configuration file.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(
})
```

[]

``` 
export default defineNuxtConfig(
})
```

You can now access the runtime config using `useRuntimeConfig(event)`. Use `useRuntimeConfig(event)` within event handlers and utilities and **avoid** calling it in ambient global contexts. This could lead to unexpected behavior such as sharing the same runtime config across different requests.

[][server/api/example.get.ts]

[]

``` 
export default defineEventHandler((event) => );
```

### [[[]]Local development](#local-development) 

Finally, you can update the runtime config using environment variables. You can use a `.env` file in development and use platform variables in production (see below).

Create an `.env` file in your project root:

[][.env]

[]

``` 
NITRO_API_TOKEN="123"
```

Re-start the development server, fetch the `/api/example` endpoint and you should see `123` as the response instead of `dev_token`.

Do not forget that you can still universally access environment variables using `import.meta.env` or `process.env` but avoid using them in ambiant global contexts to prevent unexpected behavior.

### [[[]]Production](#production) 

You can define variables in your production environment to update the runtime config. All variables must be prefixed with `NITRO_` to be applied to the runtime config. They will override the runtime config variables defined within your `nitro.config.ts` file.

[][.env (nitro)]

[][.env (nuxt)]

[]

``` 
NITRO_API_TOKEN="123"
```

[]

``` 
NUXT_API_TOKEN="123"
```

In runtime config, define key using camelCase. In environment variables, define key using snake_case and uppercase.

[]

``` 

```

[]

``` 
NITRO_HELLO_WORLD="foo"
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/97.configuration.md)

[](/guide/plugins)

[]

Plugins

Use plugins to extend Nitro\'s runtime behavior.

[](/guide/typescript)

[]

TypeScript

Nitro automatically generates the types for auto-imports and server routes ✨

[On this page][[]]

[On this page][[]]

-   [[Runtime configuration]](#runtime-configuration)
    -   [[Local development]](#local-development)
    -   [[Production]](#production)