# Source: https://nitro.build/guide

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

# Getting Started 

Create web servers with all necessary features and deploy them wherever you prefer.

</div>

<div>

## [[[]]Intro](#intro) 

Nitro is an open source framework to build web servers using [h3](https://v1.h3.dev) and lots of built-in features. Nitro automatically makes your code compatible with any [deployment](/deploy) provider and runtime!

[] Nitro can be used standalone or as the server engine of full-stack frameworks such as [Nuxt](https://nuxt.com).

## [[[]]Quick start](#quick-start) 

[] Instead of setting up a local development environment, you can use the [online playground](https://stackblitz.com/github/nitrojs/nitro/tree/main/examples/hello-world).

[]Make sure you have installed the recommended setup:

-   Latest LTS version of either [Node.js](https://nodejs.org/en), [Bun](https://bun.sh/), or [Deno](https://deno.com/).
-   [Visual Studio Code](https://code.visualstudio.com/)

Create a new project using starter template:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx giget@latest nitro nitro-app --install
```

[]

``` 
yarn dlx giget@latest nitro nitro-app --install
```

[]

``` 
pnpm dlx giget@latest nitro nitro-app --install
```

[]

``` 
bunx giget@latest nitro nitro-app --install
```

[]

``` 
deno run -A npm:giget@latest nitro nitro-app --install
```

[]

``` 
cd nitro-app
```

Start the development server:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npm run dev
```

[]

``` 
yarn dev
```

[]

``` 
pnpm dev
```

[]

``` 
bun run dev
```

[]

``` 
deno run dev
```

Nitro is ready at `http://localhost:3000/`!

[]Check `.nitro/dev/index.mjs` if you want to know what is happening

Build your production-ready server:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npm run build
```

[]

``` 
yarn build
```

[]

``` 
pnpm build
```

[]

``` 
bun run build
```

[]

``` 
deno run build
```

Output is in the `.output` directory and ready to be deployed on almost any provider with no dependencies.

You can try it locally with:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npm run preview
```

[]

``` 
yarn preview
```

[]

``` 
pnpm preview
```

[]

``` 
bun run preview
```

[]

``` 
deno run preview
```

[]You can find more examples in the Nitro repository: [nitrojs/nitro/examples](https://github.com/nitrojs/nitro/tree/main/examples)

## [[[]]Directory structure](#directory-structure) 

The starter template includes some important files to get you started.

### [[[]]`server/routes/`](#serverroutes) 

The `server/routes/` directory contains your application handlers. You can create subdirectories inside `server/routes/` dir to create nested handlers. The file name is the route path.

[[]](/guide/routing)[] Read more in [Guide \> Routing].

### [[[]]`server/api/`](#serverapi) 

The `server/api/` directory is similar to `server/routes/` with the only difference that routes inside it will be prefixed with `/api/` for convenience.

[[]](/guide/routing)[] Read more in [Guide \> Routing].

### [[[]]`server/utils/`](#serverutils) 

This directory contains your application utils with auto import support.

[[]](/guide/utils)[] Read more in [Guide \> Utils].

### [[[]]`server/plugins/`](#serverplugins) 

This directory contains your custom nitro plugins.

[[]](/guide/plugins)[] Read more in [Guide \> Plugins].

### [[[]]`nitro.config.ts`](#nitroconfigts) 

The `nitro.config.ts` file contains the configuration for Nitro.

[[]](/guide/configuration)[] Read more in [Guide \> Configuration].

### [[[]]`tsconfig.json`](#tsconfigjson) 

The `tsconfig.json` file contains the TypeScript configuration for your project.

[[]](/guide/typescript)[] Read more in [Guide \> Typescript].

### [[[]]`package.json`](#packagejson) 

The `package.json` file contains all the dependencies and scripts for your project.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/0.index.md)

[ ][](/guide/utils)

[]

Server Utils

Enjoy auto-imported server utils and extend with your own utils.

[On this page][[]]

[On this page][[]]

-   [[Intro]](#intro)
-   [[Quick start]](#quick-start)
-   [[Directory structure]](#directory-structure)
    -   [[server/routes/]](#serverroutes)
    -   [[server/api/]](#serverapi)
    -   [[server/utils/]](#serverutils)
    -   [[server/plugins/]](#serverplugins)
    -   [[nitro.config.ts]](#nitroconfigts)
    -   [[tsconfig.json]](#tsconfigjson)
    -   [[package.json]](#packagejson)