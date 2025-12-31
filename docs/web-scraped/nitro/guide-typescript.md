# Source: https://nitro.build/guide/typescript

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

# TypeScript 

Nitro automatically generates the types for auto-imports and server routes ✨

</div>

<div>

## [[[]]`tsconfig.json`](#tsconfigjson) 

To leverage type hints within your project, create a `tsconfig.json` file that extends auto-generated types.

[][tsconfig.json (nitro)]

[][server/tsconfig.json (nuxt)]

[]

``` 

```

[]

``` 

```

[]Starter templates have this file by default and usually you don\'t need to do anything. If this file does not exists, you can manually create it.

## [[[]]Prepare types](#prepare-types) 

You can use `prepare` command to auto generate the types. This can be useful in a CI environment or as a `postinstall` command in your `package.json`.

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx nitro prepare
```

[]

``` 
yarn dlx nitro prepare
```

[]

``` 
pnpm dlx nitro prepare
```

[]

``` 
bunx nitro prepare
```

[]

``` 
deno run -A npm:nitro prepare
```

[]When using `nitro dev` command, types are also auto-generated!

[]For [Nuxt](https://nuxt.com) you should use `nuxi generate`

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/98.typescript.md)

[](/guide/configuration)

[]

Configuration

Customize and extend Nitro defaults.

[](/guide/nightly)

[]

Nightly Channel

Nitro has a nightly release channel that automatically releases for every commit to main branch to try latest changes.

[On this page][[]]

[On this page][[]]

-   [[tsconfig.json]](#tsconfigjson)
-   [[Prepare types]](#prepare-types)