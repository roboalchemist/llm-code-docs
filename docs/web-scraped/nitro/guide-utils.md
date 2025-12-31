# Source: https://nitro.build/guide/utils

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

# Server Utils 

Enjoy auto-imported server utils and extend with your own utils.

</div>

<div>

## [[[]]Auto imports](#auto-imports) 

When reading the rest of the docs, you might notice that there are no `imports` in examples for using utilities. It is because Nitro uses [unimport](https://github.com/unjs/unimport) to auto import utilities when used with full tree-shaking support so you don\'t have to!

## [[[]]H3 utils](#h3-utils) 

Nitro enables all [h3 utils](https://v1.h3.dev/utils) as auto imports so you can use `defineEventHandler`, `readBody`, etc. without manually importing them.

[[]](https://v1.h3.dev/utils)[][] Read more in [H3 Docs].

### [[[]]`utils` directory](#utils-directory) 

You can add your application specific utils inside `server/utils/` directory and they will be auto-imported when used. Every export in the `utils` directory and its subdirectories will become available globally in your application.

**Example:** Create a `server/utils/sum.ts` file where a function `useSum` is exported:

[][server/utils/sum.ts]

[]

``` 
export function useSum(a: number, b: number) 
```

Use it in your `server/routes/index.ts` file without importing it:

[][server/routes/index.ts]

[]

``` 
export default defineEventHandler(() => 
})
```

## [[[]]Nitro utils](#nitro-utils) 

Nitro also exposes several built-in utils:

-   [`defineCachedFunction`][`(fn, options)`] / [`cachedFunction`][`(fn, options)`]
-   [`defineCachedEventHandler`][`(handler, options)`] / [`cachedEventHandler`][`(handler, options)`]
-   [`defineRenderHandler`][`(handler)`]
-   [`defineRouteMeta`][`(options)`] (experimental)
-   [`useRuntimeConfig`][`(event`][`?`][`)`]
-   [`useAppConfig`][`(event`][`?`][`)`]
-   [`useStorage`][`(base`][`?`][`)`]
-   [`useNitroApp`][`()`]
-   [`defineNitroPlugin`][`(plugin)`]
-   [`nitroPlugin`][`(plugin)`]
-   [`getRouteRules`][`(event)`]

[[]](https://github.com/nitrojs/nitro/blob/v2/src/core/config/resolvers/imports.ts#L58)[][]Check [the source code](https://github.com/nitrojs/nitro/blob/v2/src/core/config/resolvers/imports.ts#L58) for list of available Nitro auto imports.

[[]](/guide/typescript)[]The types are auto-generated for global auto-imports when running the `prepare` or `dev` command. See [TypeScript](/guide/typescript) guide, for IDE support.

## [[[]]Manual imports](#manual-imports) 

For some edge cases (IDE support and libraries in `node_modules`) it is impossible to rely on auto imports.

You can explicitly import them from virtual `#imports` file.

[] Manually importing from `#imports` still has benefits of tree-shaking.

[][server/plugins/test.ts]

[]

``` 
import  from '#imports'
```

## [[[]]Async Context (Experimental)](#async-context-experimental) 

Nitro (2.6+) enables a new server development experience in order to split application logic into smaller \"composable\" utilities that are fully decoupled from each other and can directly access a shared context (request event) without needing it to be passed along. This pattern is inspired from [Vue Composition API](https://vuejs.org/guide/extras/composition-api-faq.html#why-composition-api) and powered by [unctx](https://github.com/unjs/unctx).

[]This feature is currently supported for Node.js and Bun runtimes and also coming soon to other presets that support [`AsyncLocalStorage`](https://nodejs.org/api/async_context.html#class-asynclocalstorage) interface.

In order to enable async context feature, you have to enable `asyncContext` flag:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(
});
```

[]

``` 
export default defineNuxtConfig(
  }
})
```

After enabling this flag, you can use `useEvent()` (auto imported) in any utility or composable to access the request event without manually passing it along:

[with async context]

[without async context]

[]

``` 
// server/routes/index.ts
export default defineEventHandler(async () => )

// server/utils/auth.ts
export function useAuth() 
```

[]

``` 
// server/routes/index.ts
export default defineEventHandler(async (event) => )

// server/utils/auth.ts
export function useAuth(event) 
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/1.utils.md)

[](/guide)

[]

Getting Started

Create web servers with all necessary features and deploy them wherever you prefer.

[](/guide/tasks)

[]

Tasks

Nitro tasks allow on-off operations in runtime.

[On this page][[]]

[On this page][[]]

-   [[Auto imports]](#auto-imports)
-   [[H3 utils]](#h3-utils)
    -   [[utils directory]](#utils-directory)
-   [[Nitro utils]](#nitro-utils)
-   [[Manual imports]](#manual-imports)
-   [[Async Context (Experimental)]](#async-context-experimental)