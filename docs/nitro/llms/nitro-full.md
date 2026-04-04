# Nitro Documentation

Source: https://nitro.build/llms-full.txt

---

# Getting Started

> Create web servers with all necessary features and deploy them wherever you prefer.

## Intro

Nitro is an open source framework to build web servers using [h3](https://v1.h3.dev){rel="&#x22;nofollow&#x22;"} and lots of built-in features.
Nitro automatically makes your code compatible with any [deployment](https://nitro.build/deploy) provider and runtime!

::note
Nitro can be used standalone or as the server engine of full-stack frameworks such as [Nuxt](https://nuxt.com){rel=""nofollow""}.
::

## Quick start

::tip
Instead of setting up a local development environment, you can use the [online playground](https://stackblitz.com/github/nitrojs/nitro/tree/main/examples/hello-world){rel=""nofollow""}.
::

::note
Make sure you have installed the recommended setup:

- Latest LTS version of either [Node.js](https://nodejs.org/en){rel=""nofollow""}, [Bun](https://bun.sh/){rel=""nofollow""}, or [Deno](https://deno.com/){rel=""nofollow""}.
- [Visual Studio Code](https://code.visualstudio.com/){rel=""nofollow""}
::

Create a new project using starter template:

:pm-x{command="giget@latest nitro nitro-app --install"}

```sh
cd nitro-app
```

Start the development server:

:pm-run{script="dev"}

Nitro is ready at `http://localhost:3000/`!

::tip
Check `.nitro/dev/index.mjs` if you want to know what is happening
::

Build your production-ready server:

:pm-run{script="build"}

Output is in the `.output` directory and ready to be deployed on almost any provider with no dependencies.

You can try it locally with:

:pm-run{script="preview"}

::read-more
You can find more examples in the Nitro repository: [nitrojs/nitro/examples](https://github.com/nitrojs/nitro/tree/main/examples){rel=""nofollow""}
::

## Directory structure

The starter template includes some important files to get you started.

### `server/routes/`

The `server/routes/` directory contains your application handlers. You can create subdirectories inside `server/routes/` dir to create nested handlers. The file name is the route path.

:read-more{to="https://nitro.build/guide/routing"}

### `server/api/`

The `server/api/` directory is similar to `server/routes/` with the only difference that routes inside it will be prefixed with `/api/` for convenience.

:read-more{to="https://nitro.build/guide/routing"}

### `server/utils/`

This directory contains your application utils with auto import support.

:read-more{to="https://nitro.build/guide/utils"}

### `server/plugins/`

This directory contains your custom nitro plugins.

:read-more{to="https://nitro.build/guide/plugins"}

### `nitro.config.ts`

The `nitro.config.ts` file contains the configuration for Nitro.

:read-more{to="https://nitro.build/guide/configuration"}

### `tsconfig.json`

The `tsconfig.json` file contains the TypeScript configuration for your project.

:read-more{to="https://nitro.build/guide/typescript"}

### `package.json`

The `package.json` file contains all the dependencies and scripts for your project.

# Server Utils

## Auto imports

When reading the rest of the docs, you might notice that there are no `imports` in examples for using utilities.
It is because Nitro uses [unimport](https://github.com/unjs/unimport){rel="&#x22;nofollow&#x22;"} to auto import utilities when used with full tree-shaking support so you don't have to!

## H3 utils

Nitro enables all [h3 utils](https://v1.h3.dev/utils){rel="&#x22;nofollow&#x22;"} as auto imports so you can use `defineEventHandler`, `readBody`, etc. without manually importing them.

:read-more{title="H3 Docs" to="https://v1.h3.dev/utils"}

### `utils` directory

You can add your application specific utils inside `server/utils/` directory and they will be auto-imported when used.
Every export in the `utils` directory and its subdirectories will become available globally in your application.

**Example:** Create a `server/utils/sum.ts` file where a function `useSum` is exported:

```ts [server/utils/sum.ts]
export function useSum(a: number, b: number) { return a + b }
```

Use it in your `server/routes/index.ts` file without importing it:

```ts [server/routes/index.ts]
export default defineEventHandler(() => {
  const sum = useSum(1, 2) // auto-imported
  return { sum }
})
```

## Nitro utils

Nitro also exposes several built-in utils:

- `defineCachedFunction(fn, options)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"} / `cachedFunction(fn, options)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `defineCachedEventHandler(handler, options)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"} / `cachedEventHandler(handler, options)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `defineRenderHandler(handler)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `defineRouteMeta(options)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"} (experimental)
- `useRuntimeConfig(event?)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `useAppConfig(event?)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `useStorage(base?)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `useNitroApp()`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `defineNitroPlugin(plugin)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `nitroPlugin(plugin)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- `getRouteRules(event)`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}

::read-more
---

to: https://github.com/nitrojs/nitro/blob/v2/src/core/config/resolvers/imports.ts#L58
---

Check [the source code](https://github.com/nitrojs/nitro/blob/v2/src/core/config/resolvers/imports.ts#L58){rel=""nofollow""} for list of available Nitro auto imports.
::

::read-more{to="https://nitro.build/guide/typescript"}
The types are auto-generated for global auto-imports when running the `prepare` or `dev` command. See [TypeScript](https://nitro.build/guide/typescript) guide, for IDE support.
::

## Manual imports

For some edge cases (IDE support and libraries in `node_modules`) it is impossible to rely on auto imports.

You can explicitly import them from virtual `#imports` file.

::tip
Manually importing from `#imports` still has benefits of tree-shaking.
::

```js [server/plugins/test.ts]
import { useStorage } from '#imports'
```

## Async Context (Experimental)

Nitro (2.6+) enables a new server development experience in order to split application logic into smaller "composable" utilities that are fully decoupled from each other and can directly access a shared context (request event) without needing it to be passed along. This pattern is inspired from [Vue Composition API](https://vuejs.org/guide/extras/composition-api-faq.html#why-composition-api){rel="&#x22;nofollow&#x22;"} and powered by [unctx](https://github.com/unjs/unctx){rel="&#x22;nofollow&#x22;"}.

::note
This feature is currently supported for Node.js and Bun runtimes and also coming soon to other presets that support [`AsyncLocalStorage`](https://nodejs.org/api/async_context.html#class-asynclocalstorage){rel=""nofollow""} interface.
::

In order to enable async context feature, you have to enable `asyncContext` flag:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  experimental: {
    asyncContext: true
  }
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    experimental: {
      asyncContext: true
    }
  }
})
```

::

After enabling this flag, you can use `useEvent()` (auto imported) in any utility or composable to access the request event without manually passing it along:

::code-group

```ts [with async context]
// server/routes/index.ts
export default defineEventHandler(async () => {
  const user = await useAuth()
})

// server/utils/auth.ts
export function useAuth() {
  return useSession(useEvent())
}
```

```ts [without async context]
// server/routes/index.ts
export default defineEventHandler(async (event) => {
  const user = await useAuth(event)
})

// server/utils/auth.ts
export function useAuth(event) {
  return useSession(event)
}
```

::

# Tasks

## Opt-in to the experimental feature

::important
Tasks support is currently experimental.
See [nitrojs/nitro#1974](https://github.com/nitrojs/nitro/issues/1974){rel=""nofollow""} for the relevant discussion.
::

In order to use the tasks API you need to enable experimental feature flag.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  experimental: {
    tasks: true
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    experimental: {
      tasks: true
    }
  }
})
```

::

## Define tasks

Tasks can be defined in `server/tasks/[name].ts` files.

Nested directories are supported. The task name will be joined with `:`. (Example: `server/tasks/db/migrate.ts`task name will be `db:migrate`)

**Example:**

```ts [server/tasks/db/migrate.ts]
export default defineTask({
  meta: {
    name: "db:migrate",
    description: "Run database migrations",
  },
  run({ payload, context }) {
    console.log("Running DB migration task...");
    return { result: "Success" };
  },
});
```

## Scheduled tasks

You can define scheduled tasks using Nitro configuration to automatically run after each period of time.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  scheduledTasks: {
    // Run `cms:update` task every minute
    '* * * * *': ['cms:update']
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    scheduledTasks: {
      // Run `cms:update` task every minute
      '* * * * *': ['cms:update']
    }
  }
})
```

::

::tip
You can use [crontab.guru](https://crontab.guru/){rel=""nofollow""} to easily generate and understand cron tab patterns.
::

### Platform support

- `dev`, `node-server`, `bun` and `deno-server` presets are supported with [croner](https://croner.56k.guru/){rel="&#x22;nofollow&#x22;"} engine.
- `cloudflare_module` preset have native integration with [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/){rel="&#x22;nofollow&#x22;"}. Make sure to configure wrangler to use exactly same patterns you define in `scheduledTasks` to be matched.
- More presets (with native primitives support) are planned to be supported!

## Programmatically run tasks

To manually run tasks, you can use `runTask(name, { payload? })` utility.

**Example:**

```ts [server/api/migrate.ts]
export default eventHandler(async (event) => {
  // IMPORTANT: Authenticate user and validate payload!
  const payload = { ...getQuery(event) };
  const { result } = await runTask("db:migrate", { payload });

  return { result };
});
```

## Run tasks with dev server

Nitro's built-in dev server exposes tasks to be easily executed without programmatic usage.

### Using API routes

#### `/_nitro/tasks`

This endpoint returns a list of available task names and their meta.

```json
// [GET] /_nitro/tasks
{
  "tasks": {
    "db:migrate": {
      "description": "Run database migrations"
    },
     "cms:update": {
      "description": "Update CMS content"
    }
  },
  "scheduledTasks": [
    {
      "cron": "* * * * *",
      "tasks": [
        "cms:update"
      ]
    }
  ]
}
```

#### `/_nitro/tasks/:name`

This endpoint executes a task. You can provide a payload using both query parameters and body JSON payload. The payload sent in the JSON body payload must be under the `"payload"` property.

::code-group

```ts [server/tasks/echo/payload.ts]
export default defineTask({
  meta: {
    name: "echo:payload",
    description: "Returns the provided payload",
  },
  run({ payload, context }) {
    console.log("Running echo task...");
    return { result: payload };
  },
});
```

```json [GET]
// [GET] /_nitro/tasks/echo:payload?field=value&array=1&array=2
{
  "field": "value",
  "array": ["1", "2"]
}
```

```json [POST]
/**
 * [POST] /_nitro/tasks/echo:payload?field=value
 * body: {
 *   "payload": {
 *     "answer": 42,
 *     "nested": {
 *       "value": true
 *     }
 *   }
 * }
 */
{
  "field": "value",
  "answer": 42,
  "nested": {
    "value": true
  }
}
```

::

::note
The JSON payload included in the body will overwrite the keys present in the query params.
::

### Using CLI

::important
It is only possible to run these commands while the **dev server is running**. You should run them in a second terminal.
::

#### List tasks

```sh
nitro task list
```

#### Run a task

```sh
nitro task run db:migrate --payload "{}"
```

## Notes

### Concurrency

Each task can have **one running instance**. Calling a task of same name multiple times in parallel, results in calling it once and all callers will get the same return value.

::note
Nitro tasks can be running multiple times and in parallel.
::

# Server Routes

## Event handlers

An [event handler](https://v1.h3.dev/guide/event-handler){rel="&#x22;nofollow&#x22;"} is a function that will be bound to a route and executed when the route is matched by the router for an incoming request.

:read-more{to="https://v1.h3.dev/guide/event-handler"}

## Filesystem routing

Nitro supports file-based routing for your API routes (files are automatically mapped to [h3 routes](https://v1.h3.dev/guide/router){rel="&#x22;nofollow&#x22;"}). Defining a route is as simple as creating a file inside the `server/api/` or `server/routes/` directory.

You can only define one handler per files and you can [append the HTTP method](https://nitro.build/#specific-request-method) to the filename to define a specific request method.

```md
server/
  api/
    test.ts      <-- /api/test
  routes/
    hello.get.ts     <-- GET /hello
    hello.post.ts    <-- POST /hello
nitro.config.ts
```

You can nest routes by creating subdirectories.

```md
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

### Simple routes

First, create a file in `server/routes/` or `server/api/` directory. The filename will be the route path.

Then, export a function wrapped in `defineEventHandler` that will be executed when the route is matched.

```ts [server/api/test.ts]
export default defineEventHandler(() => {
  return { hello: 'API' }
})
```

### Route with params

#### Single param

To define a route with params, use the `[<param>]` syntax where `<param>` is the name of the param. The param will be available in the `event.context.params` object or using the `getRouterParam` utility from [h3](https://v1.h3.dev){rel="&#x22;nofollow&#x22;"}.

```ts [server/routes/hello/[name\\].ts]
export default defineEventHandler(event => {
  const name = getRouterParam(event, 'name')

  return `Hello ${name}!`
})
```

Call the route with the param `/hello/nitro`, you will get:

```txt [Response]
Hello nitro!
```

#### Multiple params

You can define multiple params in a route using `[<param1>]/[<param2>]` syntax where each param is a folder. You **cannot** define multiple params in a single filename of folder.

```ts [server/routes/hello/[name\\]/[age\\].ts]
export default defineEventHandler(event => {
  const name = getRouterParam(event, 'name')
  const age = getRouterParam(event, 'age')

  return `Hello ${name}! You are ${age} years old.`
})
```

#### Catch all params

You can capture all the remaining parts of a URL using `[...<param>]` syntax. This will include the `/` in the param.

```ts [server/routes/hello/[...name\\].ts]
export default defineEventHandler(event => {
  const name = getRouterParam(event, 'name')

  return `Hello ${name}!`
})
```

Call the route with the param `/hello/nitro/is/hot`, you will get:

```txt [Response]
Hello nitro/is/hot!
```

### Specific request method

You can append the HTTP method to the filename to force the route to be matched only for a specific HTTP request method, for example `hello.get.ts` will only match for `GET` requests. You can use any HTTP method you want.

::code-group

```js [GET]
// server/routes/users/[id].get.ts
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')

  // Do something with id

  return `User profile!`
})
```

```js [POST]
// server/routes/users.post.ts
export default defineEventHandler(async event => {
  const body = await readBody(event)

  // Do something with body like saving it to a database

  return { updated: true }
})
```

::

### Catch all route

You can create a special route that will match all routes that are not matched by any other route. This is useful for creating a default route.

To create a catch all route, create a file named `[...].ts` in the `server/routes/` or `server/api/` directory or in any subdirectory.

```ts [server/routes/[...\\].ts]
export default defineEventHandler(event => {
  const url = getRequestURL(event)

  return `Hello ${url}!`
})
```

### Environment specific handlers

You can specify for a route that will only be included in specific builds by adding a `.dev`, `.prod` or `.prerender` suffix to the file name, for example: `routes/test.get.dev.ts` or `routes/test.get.prod.ts`.

::tip
You can specify multiple environments or specify a preset name as environment using programmatic registration of routes via `handlers[]` config.
::

## Middleware

Nitro route middleware can hook into the request lifecycle.

::tip
A middleware can modify the request before it is processed, not after.
::

:read-more{to="https://v1.h3.dev/guide/event-handler#middleware"}

Middleware are auto-registered within the `server/middleware/` directory.

```md
server/
  routes/
    hello.ts
  middleware/
    auth.ts
    logger.ts
    ...
nitro.config.ts
```

### Simple middleware

Middleware are defined exactly like route handlers with the only exception that they should not return anything.
Returning from middleware behaves like returning from a request - the value will be returned as a response and further code will not be ran.

```ts [server/middleware/auth.ts]
export default defineEventHandler((event) => {
  // Extends or modify the event
  event.context.user = { name: 'Nitro' }
})
```

Middleware in `server/middleware/` directory are automatically registered for all routes. If you want to register a middleware for a specific route, see [Object Syntax Event Handler](https://v1.h3.dev/guide/event-handler#object-syntax){rel="&#x22;nofollow&#x22;"}.

::note
Returning anything from a middleware will close the request and should be avoided! Any returned value from middleware will be the response and further code will not be executed however **this is not recommended to do!**
::

### Route Meta

You can define route handler meta at build-time using `defineRouteMeta` macro in the event handler files.

::important
🚧 This feature is currently experimental.
::

```ts [server/api/test.ts]
defineRouteMeta({
  openAPI: {
    tags: ["test"],
    description: "Test route description",
    parameters: [{ in: "query", name: "test", required: true }],
  },
});

export default defineEventHandler(() => "OK");
```

::read-more{to="https://swagger.io/specification/v3/"}
This feature is currently usable to specify OpenAPI meta. See swagger specification for available OpenAPI options.
::

### Execution order

Middleware are executed in directory listing order.

```md
server/
  middleware/
    auth.ts <-- First
    logger.ts <-- Second
    ... <-- Third
```

Prefix middleware with a number to control their execution order.

```md
server/
  middleware/
    1.logger.ts <-- First
    2.auth.ts <-- Second
    3.... <-- Third
```

::note
Remember that file names are sorted as strings, thus for example if you have 3 files `1.filename.ts`, `2.filename.ts` and `10.filename.ts`, the `10.filename.ts` will come after the `1.filename.ts`. To avoid this, prefix `1-9` with a `0` like `01`, if you have more than 10 middleware in the same directory.
::

### Request filtering

Middleware are executed on every request.

Apply custom logic to scope them to specific conditions.

For example, you can use the URL to apply a middleware to a specific route:

```ts [server/middleware/auth.ts]
export default defineEventHandler((event) => {
  // Will only execute for /auth route
  if (getRequestURL(event).pathname.startsWith('/auth')) {
    event.context.user = { name: 'Nitro' }
  }
})
```

## Error handling

You can use the [utilities available in H3](https://v1.h3.dev/guide/event-handler#error-handling){rel="&#x22;nofollow&#x22;"} to handle errors in both routes and middlewares.

The way errors are sent back to the client depends on the route's path. For most routes `Content-Type` is set to `text/html` by default and a simple html error page is delivered. If the route starts with `/api/` (either because it is placed in `api/` or `routes/api/`) the default will change to `application/json` and a JSON object will be sent.

This behaviour can be overridden by some request properties (e.g.: `Accept` or `User-Agent` headers).

## Route Rules

Nitro allows you to add logic at the top-level for each route of your configuration. It can be used for redirecting, proxying, caching and adding headers to routes.

It is a map from route pattern (following [radix3](https://github.com/unjs/rou3/tree/radix3#route-matcher){rel="&#x22;nofollow&#x22;"}) to route options.

When `cache` option is set, handlers matching pattern will be automatically wrapped with `defineCachedEventHandler`. See the [cache guide](https://nitro.build/guide/cache) to learn more about this function.

::note
`swr: true|number` is shortcut for `cache: { swr: true, maxAge: number }`
::

You can set route rules in `nitro.config.ts` using the `routeRules` option.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  routeRules: {
    '/blog/**': { swr: true },
    '/blog/**': { swr: 600 },
    '/blog/**': { static: true },
    '/blog/**': { cache: { /* cache options*/ } },
    '/assets/**': { headers: { 'cache-control': 's-maxage=0' } },
    '/api/v1/**': { cors: true, headers: { 'access-control-allow-methods': 'GET' } },
    '/old-page': { redirect: '/new-page' },
    '/old-page/**': { redirect: '/new-page/**' },
    '/proxy/example': { proxy: 'https://example.com' },
    '/proxy/**': { proxy: '/api/**' },
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  routeRules: {
    '/blog/**': { swr: true },
    '/blog/**': { swr: 600 },
    '/blog/**': { static: true },
    '/blog/**': { cache: { /* cache options*/ } },
    '/assets/**': { headers: { 'cache-control': 's-maxage=0' } },
    '/api/v1/**': { cors: true, headers: { 'access-control-allow-methods': 'GET' } },
    '/old-page': { redirect: '/new-page' },
    '/old-page/**': { redirect: '/new-page/**' },
    '/proxy/example': { proxy: 'https://example.com' },
    '/proxy/**': { proxy: '/api/**' },
  }
})
```

::

# WebSocket

Nitro natively supports runtime agnostic [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket){rel="&#x22;nofollow&#x22;"} API using [CrossWS](https://crossws.unjs.io/){rel="&#x22;nofollow&#x22;"} and [H3 WebSocket](https://v1.h3.dev/guide/websocket){rel="&#x22;nofollow&#x22;"}.

:read-more{title="WebSocket in MDN" to="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket"}

:read-more{title="CrossWS" to="https://crossws.unjs.io/"}

## Opt-in to the experimental feature

::important
WebSockets support is currently experimental. See [nitrojs/nitro#2171](https://github.com/nitrojs/nitro/issues/2171){rel=""nofollow""} for platform support status.
::

In order to enable websocket support you need to enable the experimental `websocket` feature flag.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  experimental: {
    websocket: true
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    experimental: {
      websocket: true
    }
  }
})
```

::

## Usage

Create a websocket handler in `server/routes/_ws.ts`.

::tip
You can use any route like `server/routes/chatroom.ts` to register upgrade handler on `/chatroom`.
::

```ts [server/routes/_ws.ts]
export default defineWebSocketHandler({
  open(peer) {
    console.log("[ws] open", peer);
  },

  message(peer, message) {
    console.log("[ws] message", peer, message);
    if (message.text().includes("ping")) {
      peer.send("pong");
    }
  },

  close(peer, event) {
    console.log("[ws] close", peer, event);
  },

  error(peer, error) {
    console.log("[ws] error", peer, error);
  },
});

```

::note
Nitro allows you defining multiple websocket handlers using same routing of event handlers.
::

Use a client to connect to server. Example: (`server/routes/websocket.ts`)

```ts [index.ts]
export default defineEventHandler(() => {
  return $fetch(
    "https://raw.githubusercontent.com/unjs/crossws/main/examples/h3/public/index.html"
  );
});

```

Now you can try it on `/websocket` route!

::tip
Check out our [chat demo](https://nuxt-chat.pi0.io/){rel=""nofollow""} using Nitro Websocket API.
::

## Server-Sent Events (SSE)

As an alternative to WebSockets, you can use [Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events){rel="&#x22;nofollow&#x22;"}

### Example

Create an SSE handler in `server/routes/sse.ts`.

```ts [server/routes/sse.ts]
export default defineEventHandler(async (event) => {
  const eventStream = createEventStream(event)

  const interval = setInterval(async () => {
    await eventStream.push(`Message @ ${new Date().toLocaleTimeString()}`)
  }, 1000)

  eventStream.onClosed(async () => {
    clearInterval(interval)
    await eventStream.close()
  })

  return eventStream.send()
})
```

Then connect to this SSE endpoint from the client

```ts
const eventSource = new EventSource('http://localhost:3000/sse')

eventSource.onmessage = (event) => {
  console.log(event.data)
}
```

:read-more{title="SSE guide in H3" to="https://v1.h3.dev/guide/websocket#server-sent-events-sse"}

# KV Storage

Nitro has built-in integration with [unstorage](https://unstorage.unjs.io){rel="&#x22;nofollow&#x22;"} to provide a runtime agnostic persistent layer.

## Usage

To use the storage layer, you can use the `useStorage()` and call `getItem(key)` to retrieve an item and `setItem(key, value)` to set an item.

```ts
// Default storage is in memory
await useStorage().setItem('test:foo', { hello: 'world' })
await useStorage().getItem('test:foo')

// You can also specify the base in useStorage(base)
await useStorage('test').setItem('foo', { hello: 'world' })

// You can use data storage to write data to default .data/kv directory
const dataStorage = useStorage('data')
await dataStorage.setItem('test', 'works')
await dataStorage.getItem('data:test') // Value persists

// You can use generics to define types
await useStorage<{ hello: string }>('test').getItem('foo')
await useStorage('test').getItem<{ hello: string }>('foo')
```

:read-more{to="https://unstorage.unjs.io"}

## Configuration

You can mount one or multiple custom storage drivers using the `storage` config.
The key is the mount point name, and the value is the driver name and configuration.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  storage: {
    redis: {
      driver: 'redis',
      /* redis connector options */
    },
    db: {
      driver: 'fs',
      base: './data/db'
    }
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    storage: {
      redis: {
        driver: 'redis',
        /* redis connector options */
      },
      db: {
        driver: 'fs',
        base: './.data/db'
      }
    }
  }
})
```

::

::read-more{to="https://unstorage.unjs.io/"}
You can find the driver list on [unstorage documentation](https://unstorage.unjs.io/){rel=""nofollow""} with their configuration.
::

### Runtime configuration

In scenarios where the mount point configuration is not known until runtime, Nitro can dynamically add mount points during startup using [plugins](https://nitro.build/guide/plugins).

::code-group

```ts [server/plugins/storage.ts]
import redisDriver from 'unstorage/drivers/redis'

export default defineNitroPlugin(() => {
  const storage = useStorage()

  // Dynamically pass in credentials from runtime configuration, or other sources
  const driver = redisDriver({
      base: 'redis',
      host: useRuntimeConfig().redis.host,
      port: useRuntimeConfig().redis.port,
      /* other redis connector options */
    })

  // Mount driver
  storage.mount('redis', driver)
})
```

```ts [nitro.config.ts]
export default defineNitroConfig({
  runtimeConfig: {
    redis: { // Default values
      host: '',
      port: 0,
      /* other redis connector options */
    }
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  runtimeConfig: {
    redis: { // Default values
      host: '',
      port: 0,
      /* other redis connector options */
    }
  }
})
```

::

::warning
This is a temporary workaround, with a better solution coming in the future! Keep a lookout on the GitHub issue [here](https://github.com/nitrojs/nitro/issues/1161#issuecomment-1511444675){rel=""nofollow""}.
::

### Development-only mount points

By default, Nitro will mount the project directory and some other dirs using the filesystem driver in development time.

```js
// Access to project root dir
const rootStorage = useStorage('root')

// Access to project src dir (same as root by default)
const srcStorage = useStorage('src')

// Access to server cache dir
const cacheStorage = useStorage('cache')

// Access to the temp build dir
const buildStorage = useStorage('build')
```

::tip
You also can use the `devStorage` key to overwrite the storage configuration during development. This is very useful when you use a database in production and want to use the filesystem in development.
::

In order to use the `devStorage` key, you need to use the `nitro dev` command and the key in the `storage` option must be the same as the production one.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  // Production
  storage: {
    db: {
      driver: 'redis',
      /* redis connector options */
    }
  },
  // Development
  devStorage: {
    db: {
      driver: 'fs',
      base: './data/db'
    }
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    // Production
    storage: {
      db: {
        driver: 'redis',
        /* redis connector options */
      }
    },
    // Development
    devStorage: {
      db: {
        driver: 'fs',
        base: './data/db'
      }
    }
  }
})
```

::

You will also be able to access to a `build` namespace in the storage layer only during development. It contains file generated by Nitro.

# SQL Database

The default database connection is **preconfigured** with [SQLite](https://db0.unjs.io/connectors/sqlite){rel="&#x22;nofollow&#x22;"} and works out of the box for development mode and any Node.js compatible production deployments. By default, data will be stored in `.data/db.sqlite3`.

::tip
You can change default connection or define more connections to any of the [supported databases](https://db0.unjs.io/connectors/sqlite){rel=""nofollow""}.
::

::tip
You can integrate database instance to any of the [supported ORMs](https://db0.unjs.io/integrations){rel=""nofollow""}.
::

:read-more{title="DB0 Documentation" to="https://db0.unjs.io"}

## Opt-in to the experimental feature

::important
Database support is currently experimental.
Refer to the [db0 issues](https://github.com/unjs/db0/issues){rel=""nofollow""} for status and bug report.
::

In order to enable database layer you need to enable experimental feature flag.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  experimental: {
    database: true
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    experimental: {
      database: true
    }
  }
})
```

::

## Usage

```ts [index.ts]
export default defineEventHandler(async () => {
  const db = useDatabase();

  // Create users table
  await db.sql`DROP TABLE IF EXISTS users`;
  await db.sql`CREATE TABLE IF NOT EXISTS users ("id" TEXT PRIMARY KEY, "firstName" TEXT, "lastName" TEXT, "email" TEXT)`;

  // Add a new user
  const userId = String(Math.round(Math.random() * 10_000));
  await db.sql`INSERT INTO users VALUES (${userId}, 'John', 'Doe', '')`;

  // Query for users
  const { rows } = await db.sql`SELECT * FROM users WHERE id = ${userId}`;

  return {
    rows,
  };
});
```

## Configuration

You can configure database connections using `database` config:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  database: {
    default: {
      connector: 'sqlite',
      options: { name: 'db' }
    },
    users: {
      connector: 'postgresql',
      options: {
        url: 'postgresql://username:password@hostname:port/database_name'
      }
    }
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    database: {
      default: {
        connector: 'sqlite',
        options: { name: 'db' }
      },
      users: {
        connector: 'postgresql',
        options: {
          url: 'postgresql://username:password@hostname:port/database_name'
        }
      }
    }
  }
})
```

::

::tip
You can use the `devDatabase` config to overwrite the database configuration only for development mode.
::

# Cache

## Cached event handlers

To cache an event handler, you simply need to use the `defineCachedEventHandler` method.

It works like [`defineEventHandler`](https://v1.h3.dev/guide/event-handler){rel="&#x22;nofollow&#x22;"} but with an additional second [options](https://nitro.build/#options) parameter.

```ts [server/routes/cached.ts]
// Cache an API handler
export default defineCachedEventHandler((event) => {
  // My event handler
}, { maxAge: 60 * 60 /* 1 hour */ });
```

With this example, the response will be cached for 1 hour and a stale value will be sent to the client while the cache is being updated in the background. If you want to immediately return the updated response set `swr: false`.

::important
All incoming request headers are dropped when handling cached responses. If you define the `varies` option, only the specified headers will be considered when caching and serving the responses.
::

See the [options](https://nitro.build/#options) section for more details about the available options.

::note
You can also use the `cachedEventHandler` method as alias of `defineCachedEventHandler`.
::

## Cached functions

You can also cache a function using the `defineCachedFunction` function. This is useful for caching the result of a function that is not an event handler, but is part of one, and reusing it in multiple handlers.

For example, you might want to cache the result of an API call for one hour:

::code-group

```ts [server/utils/github.ts]
export const cachedGHStars = defineCachedFunction(async (repo: string) => {
  const data: any = await $fetch(`https://api.github.com/repos/${repo}`)

  return data.stargazers_count
}, {
  maxAge: 60 * 60,
  name: 'ghStars',
  getKey: (repo: string) => repo
})
```

```ts [server/api/stars/[...repo\\].ts]
export default defineEventHandler(async (event) => {
  const repo = event.context.params.repo
  const stars = await cachedGHStars(repo).catch(() => 0)

  return { repo, stars }
})
```

::

The stars will be cached in development inside `.nitro/cache/functions/ghStars/<owner>/<repo>.json` with `value` being the number of stars.

```json
{"expires":1677851092249,"value":43991,"mtime":1677847492540,"integrity":"ZUHcsxCWEH"}
```

::important
Because the cached data is serialized to JSON, it is important that the cached function does not return anything that cannot be serialized, such as Symbols, Maps, Sets…
::

::note
You can also use the `cachedFunction` method as alias of `defineCachedFunction`.
::

### Edge workers

In edge workers, the instance is destroyed after each request. Nitro automatically uses `event.waitUntil` to keep the instance alive while the cache is being updated while the response is sent to the client.

To ensure that your cached functions work as expected in edge workers, you should always pass the `event` as the first argument to the function using `defineCachedFunction`.

::code-group

```ts [server/utils/github.ts]
import type { H3Event } from 'h3'

export const cachedGHStars = defineCachedFunction(async (event: H3Event, repo: string) => {
  const data: any = await $fetch(`https://api.github.com/repos/${repo}`)

  return data.stargazers_count
}, {
  maxAge: 60 * 60,
  name: 'ghStars',
  getKey: (event: H3Event, repo: string) => repo
})
```

```ts [server/api/stars/[...repo\\].ts]
export default defineEventHandler(async (event) => {
  const repo = event.context.params.repo
  const stars = await cachedGHStars(event, repo).catch(() => 0)

  return { repo, stars }
})
```

::

This way, the function will be able to keep the instance alive while the cache is being updated without slowing down the response to the client.

## Caching route rules

This feature enables you to add caching routes based on a glob pattern directly in the main configuration file. This is especially useful to have a global cache strategy for a part of your application.

Cache all the blog routes for 1 hour with `stale-while-revalidate` behavior:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  routeRules: {
    "/blog/**": { cache: { maxAge: 60 * 60 } },
  },
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  routeRules: {
    "/blog/**": { cache: { maxAge: 60 * 60 } },
  },
});
```

::

If we want to use a [custom storage](https://nitro.build/#customize-cache-storage) mount point, we can use the `base` option.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  storage: {
    redis: {
      driver: "redis",
      url: "redis://localhost:6379",
    },
  },
  routeRules: {
    "/blog/**": { cache: { maxAge: 60 * 60, base: "redis" } },
  },
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    storage: {
      redis: {
        driver: "redis",
        url: "redis://localhost:6379",
      },
    },
  },
  routeRules: {
    "/blog/**": { cache: { maxAge: 60 * 60, base: "redis" } },
  },
});
```

::

## Customize cache storage

Nitro stores the data in the `cache:` mount point.

- In production, it will use the [memory driver](https://unstorage.unjs.io/drivers/memory){rel="&#x22;nofollow&#x22;"} by default.
- In development, it will use the [filesystem driver](https://unstorage.unjs.io/drivers/fs){rel="&#x22;nofollow&#x22;"}, writing to a temporary dir.

To overwrite the production storage, set the `cache` mount point using the `storage` option:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  storage: {
    cache: {
      driver: 'redis',
      /* redis connector options */
    }
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    storage: {
      cache: {
        driver: 'redis',
        /* redis connector options */
      }
    }
  }
})
```

::

In development, you can also overwrite the cache mount point using the `devStorage` option:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  devStorage: {
    cache: {
      driver: 'redis',
      /* redis connector options */
    }
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    devStorage: {
      cache: {
        driver: 'redis',
        /* redis connector options */
      }
    }
  }
})
```

::

## Options

The `cachedEventHandler` and `cachedFunction` functions accept the following options:

::field-group
  :::field{name="base" type="string"}
  Name of the storage mountpoint to use for caching. :br
  Default to `cache`.
  :::

  :::field{name="name" type="string"}
  Guessed from function name if not provided, and falls back to `'_'` otherwise.
  :::

  :::field{name="group" type="string"}
  Defaults to `'nitro/handlers'` for handlers and `'nitro/functions'` for functions.
  :::

  :::field{name="getKey()" type="(...args) => string"}
  A function that accepts the same arguments as the original function and returns a cache key (`String`). :br
  If not provided, a built-in hash function will be used to generate a key based on the function arguments.
  :::

  :::field{name="integrity" type="string"}
  A value that invalidates the cache when changed. :br
  By default, it is computed from **function code**, used in development to invalidate the cache when the function code changes.
  :::

  :::field{name="maxAge" type="number"}
  Maximum age that cache is valid, in seconds. :br
  Default to `1` (second).
  :::

  :::field{name="staleMaxAge" type="number"}
  Maximum age that a stale cache is valid, in seconds. If set to `-1` a stale value will still be sent to the client while the cache updates in the background. :br
  Defaults to `0` (disabled).
  :::

  :::field{name="swr" type="boolean"}
  Enable `stale-while-revalidate` behavior to serve a stale cached response while asynchronously revalidating it. :br
  Defaults to `true`.
  :::

  :::field{name="shouldInvalidateCache()" type="(..args) => boolean"}
  A function that returns a `boolean` to invalidate the current cache and create a new one.
  :::

  :::field{name="shouldBypassCache()" type="(..args) => boolean"}
  A function that returns a `boolean` to bypass the current cache without invalidating the existing entry.
  :::

  :::field{name="varies" type="string[]"}
  An array of request headers to be considered for the cache, [learn more](https://github.com/nitrojs/nitro/issues/1031){rel=""nofollow""}. If utilizing in a multi-tenant environment, you may want to pass `['host', 'x-forwarded-host']` to ensure these headers are not discarded and that the cache is unique per tenant.
  :::
::

## Cache keys and invalidation

When using the `defineCachedFunction` or `defineCachedEventHandler` functions, the cache key is generated using the following pattern:

```ts
`${options.group}:${options.name}:${options.getKey(...args)}.json`
```

For example, the following function:

```ts
const getAccessToken = defineCachedFunction(() => {
  return String(Date.now())
}, {
  maxAge: 10,
  name: 'getAccessToken',
  getKey: () => 'default'
})
```

Will generate the following cache key:

```ts
nitro:functions:getAccessToken:default.json
```

You can invalidate the cached function entry with:

```ts
await useStorage('cache').removeItem('nitro:functions:getAccessToken:default.json')
```

### Normalizing Cache Keys

::important
**Cache keys are automatically normalized** using an internal utility that removes non-alphanumeric characters such as `/` and `-`. This behavior helps ensure compatibility across various storage backends (e.g., `file systems`, `key-value` stores) that might have restrictions on characters in `keys`, and also prevents potential path traversal vulnerabilities.
::

For example:

```ts
getKey: () => '/api/products/sale-items'
```

Would generate a key like:

```ts
api/productssaleitems.json
```

This behavior may result in keys that look different from the original route or identifier.

::tip
To manually reproduce the same normalized key pattern used by Nitro (e.g., when invalidating cache entries), you can use the `escapeKey` utility function provided below:
::

```ts
function escapeKey(key: string | string[]) {
  return String(key).replace(/\W/g, "");
}
```

It's recommended to use `escapeKey()` when invalidating manually using route paths or identifiers to ensure consistency with Nitro's internal key generation.

For example, if your `getKey` function is:

```ts
getKey: (id: string) => `product/${id}/details`
```

And you want to invalidate `product/123/details`, you would do:

```ts
const normalizedKey = escapeKey('product/123/details')
await useStorage('cache').removeItem(`nitro:functions:getProductDetails:${normalizedKey}.json`)
```

# Fetch

## Usage

In your handler, you just have to call the `$fetch` function to make a request. The response will be automatically parsed.

```ts [Router Handler]
export default defineEventHandler(async (event) => {
  const data = await $fetch('https://ungh.cc/orgs/unjs/repos')

  return data
})
```

You can pass a generic type to the `$fetch` function to get a better type inference.

```ts [Router Handler]
import { Repo } from '~/types'

export default defineEventHandler(async (event) => {
  const data = await $fetch<Repo[]>('https://ungh.cc/orgs/unjs/repos')

  return data
})
```

You can pass many options to the `$fetch` function like the method, headers, body, query, etc.

```ts [Router Handler]
import { Repo } from '~/types'

export default defineEventHandler(async (event) => {
  const data = await $fetch<Repo[]>('https://api.github.com/markdown', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: {
      text: 'Hello **world**!'
    }
  })

  return data
})
```

See more about the usage of the `$fetch` function in the [ofetch](https://ofetch.unjs.io){rel="&#x22;nofollow&#x22;"} documentation.

## In-Server fetch

You can also use the `$fetch` function to make internal requests to other handlers.

```ts [Router Handler]
export default defineEventHandler(async (event) => {
  const data = await $fetch('/api/users')

  return data
})
```

In reality, no fetch request is made and the handler is directly called, thanks to [unenv](https://unenv.unjs.io){rel="&#x22;nofollow&#x22;"}. This is useful to avoid making HTTP request overhead.

# Assets

## Public assets

Nitro handles assets via the `server/public/` directory.

All assets in `server/public/` directory will be automatically served. This means that you can access them directly from the browser without any special configuration.

```md
server/
  public/
    image.png     <-- /image.png
    video.mp4     <-- /video.mp4
    robots.txt    <-- /robots.txt
package.json
nitro.config.ts
```

### Production public assets

When building your Nitro app, the `server/public/` directory will be copied to `.output/public/` and a manifest with metadata will be created and embedded in the server bundle.

```json
{
  "/image.png": {
    "type": "image/png",
    "etag": "\"4a0c-6utWq0Kbk5OqDmksYCa9XV8irnM\"",
    "mtime": "2023-03-04T21:39:45.086Z",
    "size": 18956
  },
  "/robots.txt": {
    "type": "text/plain; charset=utf-8",
    "etag": "\"8-hMqyDrA8fJ0R904zgEPs3L55Jls\"",
    "mtime": "2023-03-04T21:39:45.086Z",
    "size": 8
  },
  "/video.mp4": {
    "type": "video/mp4",
    "etag": "\"9b943-4UwfQXKUjPCesGPr6J5j7GzNYGU\"",
    "mtime": "2023-03-04T21:39:45.085Z",
    "size": 637251
  }
}
```

This allows Nitro to know the public assets without scanning the directory, giving high performance with caching headers.

## Server assets

All assets in `server/assets/` directory will be added to the server bundle. After building your application, you can find them in the `.output/server/chunks/raw/` directory. Be careful with the size of your assets, as they will be bundled with the server bundle.

They can be addressed by the `assets:server` mount point using the [storage layer](https://nitro.build/guide/storage).

For example, you could store a json file in `server/assets/data.json` and retrieve it in your handler:

```js
export default defineEventHandler(async () => {
  const data = await useStorage('assets:server').getItem(`data.json`)
  return data
})
```

### Custom server assets

In order to add assets from a custom directory, you will need to define a path in your nitro config. This allows you to add assets from a directory outside of the `server/assets/` directory.

::code-group

```js [nitro.config.ts]
export default defineNitroConfig({
  serverAssets: [{
    baseName: 'my_directory',
    dir: './my_directory' // Relative to `srcDir`
  }]
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    serverAssets: [{
      baseName: 'my_directory',
      dir: './my_directory' // Relative to Nitro `srcDir`
    }]
  }
})
```

::

You could want to add a directory (`server/templates/`) with html templates for example.

::code-group

```js [nitro.config.ts]
export default defineNitroConfig({
  serverAssets: [{
    baseName: 'templates',
    dir: './templates' // Relative to `srcDir`
  }]
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    serverAssets: [{
      baseName: 'templates',
      dir: './templates' // Relative to Nitro `srcDir`
    }]
  }
})
```

::

Then you can use the `assets:templates` base to retrieve your assets.

```ts [handlers/success.ts]
export default defineEventHandler(async (event) => {
  const html = await useStorage('assets:templates').getItem(`success.html`)
  return html
})
```

# Plugins

Nitro plugins will be **executed once** during server startup in order to allow extending Nitro's runtime behavior.
They receive `nitroApp` context, which can be used to hook into Nitro lifecycle events.

Plugins are auto-registered from `plugins/` directory and run synchronously (by order of file name) on the first Nitro initialization.

**Example:**

```ts [server/plugins/test.ts]
export default defineNitroPlugin((nitroApp) => {
  console.log('Nitro plugin', nitroApp)
})
```

If you have plugins in another directory, you can use the `plugins` option:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  plugins: ['my-plugins/hello.ts']
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    plugins: ['my-plugins/hello.ts']
  }
})
```

::

## Nitro runtime hooks

You can use Nitro [hooks](https://github.com/unjs/hookable){rel="&#x22;nofollow&#x22;"} to extend the default runtime behaviour of Nitro by registering custom (async or sync) functions to the lifecycle events within plugins.

**Example:**

```ts
export default defineNitroPlugin((nitro) => {
  nitro.hooks.hook("close", async () => {
    // Will run when nitro is being closed
  });
})
```

### Available hooks

See the [source code](https://github.com/nitrojs/nitro/blob/v2/src/core/index.ts#L75){rel="&#x22;nofollow&#x22;"} for list of all available runtime hooks.

- `"close", () => {}`
- `"error", (error, { event? }) => {}`
- `"render:response", (response, { event }) => {}`
- `"request", (event) => {}`
- `"beforeResponse", (event, { body }) => {}`
- `"afterResponse", (event, { body }) => {}`

## Examples

### Capturing errors

You can use plugins to capture all application errors.

```ts
export default defineNitroPlugin((nitro) => {
  nitro.hooks.hook("error", async (error, { event }) => {
    console.error(`${event.path} Application error:`, error)
  });
})
```

### Graceful shutdown

You can use plugins to register a hook that resolves when Nitro is closed.

```ts
export default defineNitroPlugin((nitro) => {
  nitro.hooks.hookOnce("close", async () => {
    // Will run when nitro is closed
    console.log("Closing nitro server...")
    await new Promise((resolve) => setTimeout(resolve, 500));
    console.log("Task is done!");
  });
})
```

### Request and response lifecycle

You can use plugins to register a hook that can run on request lifecycle:

```ts
export default defineNitroPlugin((nitroApp) => {
  nitroApp.hooks.hook("request", (event) => {
    console.log("on request", event.path);
  });

  nitroApp.hooks.hook("beforeResponse", (event, { body }) => {
    console.log("on response", event.path, { body });
  });

  nitroApp.hooks.hook("afterResponse", (event, { body }) => {
    console.log("on after response", event.path, { body });
  });
});
```

### Renderer response

You can use plugins to register a hook that modifies the [`renderer`](https://nitro.build/config#renderer){rel="&#x22;nofollow&#x22;"} response.

::note
This **only works** for render handler defined with [`renderer`](https://nitro.build/config#renderer){rel=""nofollow""} and won't be called for other api/server routes.
In [Nuxt](https://nuxt.com/){rel=""nofollow""} this hook will be called for Server-side rendered pages
::

```ts
export default defineNitroPlugin((nitro) => {

  nitro.hooks.hook('render:response', (response, { event }) => {
    // Inspect or Modify the renderer response here
    console.log(response)
  })
})
```

# Configuration

::read-more{to="https://nitro.build/config"}
See [config reference](https://nitro.build/config) for available options.
::

You can customize your Nitro builder with a configuration file.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  // Nitro options
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    // Nitro options
  }
})
```

::

::important
If you are using [Nuxt](https://nuxt.com){rel=""nofollow""}, use the `nitro` option in your Nuxt config instead.
::

::tip
Nitro loads the configuration using [c12](https://github.com/unjs/c12){rel=""nofollow""}, giving more possibilities such as using `.nitrorc` file in current working directory or in the user's home directory.
::

## Runtime configuration

Nitro provides a runtime config API to expose configuration within your application, with the ability to update it at runtime by setting environment variables. This is useful when you want to expose different configuration values for different environments (e.g. development, staging, production). For example, you can use this to expose different API endpoints for different environments or to expose different feature flags.

First, you need to define the runtime config in your configuration file.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  runtimeConfig: {
    apiToken: "dev_token", // `dev_token` is the default value
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  runtimeConfig: {
    apiToken: "dev_token", // `dev_token` is the default value
  }
})
```

::

You can now access the runtime config using `useRuntimeConfig(event)`. Use `useRuntimeConfig(event)` within event handlers and utilities and **avoid** calling it in ambient global contexts. This could lead to unexpected behavior such as sharing the same runtime config across different requests.

```ts [server/api/example.get.ts]
export default defineEventHandler((event) => {
  return useRuntimeConfig(event).apiToken // Returns `dev_token`
});
```

### Local development

Finally, you can update the runtime config using environment variables. You can use a `.env` file in development and use platform variables in production (see below).

Create an `.env` file in your project root:

```bash [.env]
NITRO_API_TOKEN="123"
```

Re-start the development server, fetch the `/api/example` endpoint and you should see `123` as the response instead of `dev_token`.

Do not forget that you can still universally access environment variables using `import.meta.env` or `process.env` but avoid using them in ambiant global contexts to prevent unexpected behavior.

### Production

You can define variables in your production environment to update the runtime config. All variables must be prefixed with `NITRO_` to be applied to the runtime config. They will override the runtime config variables defined within your `nitro.config.ts` file.

::code-group

```bash [.env (nitro)]
NITRO_API_TOKEN="123"
```

```bash [.env (nuxt)]
NUXT_API_TOKEN="123"
```

::

In runtime config, define key using camelCase. In environment variables, define key using snake\_case and uppercase.

```ts
{
  helloWorld: "foo"
}
```

```bash
NITRO_HELLO_WORLD="foo"
```

# TypeScript

## `tsconfig.json`

To leverage type hints within your project, create a `tsconfig.json` file that extends auto-generated types.

::code-group

```json [tsconfig.json (nitro)]
{
  "extends": "./.nitro/types/tsconfig.json"
}
```

```json [server/tsconfig.json (nuxt)]
{
  "extends": "../.nuxt/tsconfig.server.json"
}
```

::

::tip
Starter templates have this file by default and usually you don't need to do anything. If this file does not exists, you can manually create it.
::

## Prepare types

You can use `prepare` command to auto generate the types.
This can be useful in a CI environment or as a `postinstall` command in your `package.json`.

:pm-x{command="nitro prepare"}

::tip
When using `nitro dev` command, types are also auto-generated!
::

::note
For [Nuxt](https://nuxt.com){rel=""nofollow""} you should use `nuxi generate`
::

# Nightly Channel

You can opt-in to the nightly release channel by updating your `package.json`:

::code-group

```diff [Nitro]
{
  "devDependencies": {
--    "nitropack": "^2.0.0"
++    "nitropack": "npm:nitropack-nightly@latest"
  }
}
```

```diff [Nuxt]
{
  "devDependencies": {
--    "nuxt": "^3.0.0"
++    "nuxt": "npm:nuxt-nightly@latest"
  }
}
```

::

::note
If you are using Nuxt, [use the Nuxt nightly channel](https://nuxt.com/docs/guide/going-further/nightly-release-channel#opting-in){rel=""nofollow""} as it already includes `nitropack-nightly`.
::

Remove the lockfile (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, or `bun.lockb`) and reinstall the dependencies.

# Overview

> Learn more about Nitro deploy providers.

Nitro can generate different output formats suitable for different hosting providers from the same code base.
Using built-in presets, you can easily configure Nitro to adjust its output format with almost no additional code or configuration!

## Default output

The default production output preset is [Node.js server](https://nitro.build/deploy/node).

When running Nitro in development mode, Nitro will always use a special preset called `nitro-dev` using Node.js with ESM in an isolated Worker environment with behavior as close as possible to the production environment.

## Zero-Config Providers

When deploying to production using CI/CD, Nitro tries to automatically detect the provider environment and set the right one without any additional configuration required. Currently, the providers below can be auto-detected with zero config.

- [aws amplify](https://nitro.build/deploy/providers/aws-amplify)
- [azure](https://nitro.build/deploy/providers/azure)
- [cloudflare](https://nitro.build/deploy/providers/cloudflare)
- [firebase app hosting](https://nitro.build/deploy/providers/firebase#firebase-app-hosting)
- [netlify](https://nitro.build/deploy/providers/netlify)
- [stormkit](https://nitro.build/deploy/providers/stormkit)
- [vercel](https://nitro.build/deploy/providers/vercel)
- [zeabur](https://nitro.build/deploy/providers/zeabur)

::warning
For Turborepo users, zero config detection will be interferenced by its Strict Environment Mode. You may need to allowing the variables explictly or use its Loose Environment Mode (with `--env-mode=loose` flag).
::

## Changing the deployment preset

If you need to build Nitro against a specific provider, you can target it by defining an environment variable named `NITRO_PRESET` or `SERVER_PRESET`, or by updating your Nitro [configuration](https://nitro.build/guide/configuration) or using `--preset` argument.

Using the environment variable approach is recommended for deployments depending on CI/CD.

**Example:** Defining a `NITRO_PRESET` environment variable

```bash
nitro build --preset cloudflare_pages
```

**Example:** Updating the `nitro.config.ts` file

```ts
export default defineNitroConfig({
  preset: 'cloudflare_pages'
})
```

## Compatibility date

Deployment providers regularly update their runtime behavior. Nitro presets are updated to support these new features.

To prevent breaking existing deployments, Nitro uses compatibility dates. These dates let you lock in behavior at the project creation time. You can also opt in to future updates when ready.

When you create a new project, the `compatibilityDate` is set to the current date. This setting is saved in your project's configuration.

You should update the compatibility date periodically. Always test your deployment thoroughly after updating. Below is a list of key dates and their effects.

| Compatibility date | Platform   | Description                                        |
| ------------------ | ---------- | -------------------------------------------------- |
| **≥ 2024-05-07**   | netlify    | Netlify functions v2                               |
| **≥ 2024-09-19**   | cloudflare | Static assets support for cloudflare-module preset |
| **≥ 2025-01-30**   | deno       | Deno v2 Node.js compatibility                      |

# Edge Workers

## Deploy to workers

Nitro provides out of the box support for deploying any Nitro app to different Edge Worker offerings as well as Service Workers.

- [Cloudflare](https://nitro.build/deploy/providers/cloudflare)
- [Deno Deploy](https://nitro.build/deploy/providers/deno-deploy)
- [Vercel](https://nitro.build/deploy/providers/vercel#vercel-edge-functions)
- [Netlify](https://nitro.build/deploy/providers/netlify#netlify-edge-functions)
- [Browser Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API){rel="&#x22;nofollow&#x22;"} (via experimental preset `service-worker`)

### Worker limitations

- No support for raw TCP/IP traffic
- Execution time is limited compared to classic serverless offerings (normally 15-30 seconds)
- No access to the filesystem (use the [nitro storage](https://nitro.build/guide/storage) layer)
- Bundle size is very limited (normally a few MBs)
- Limited access Node.js APIs (nitro provides compatibility layer via [unenv](https://github.com/unjs/unenv){rel="&#x22;nofollow&#x22;"})

### Incompatible libraries

::note
If you come across a library that you assume to be incompatible with edge workers, please open an issue on the [nitro repo](https://github.com/nitrojs/nitro/issues/new/choose){rel=""nofollow""} and help us keeping this list up to date.
::

The following libraries are known to be incompatible with edge workers because of one of the above mentioned limitations:

#### `mongodb`

> There are possible fixes for MongoDB, like using Realm and the [Realm SDK](https://www.mongodb.com/docs/realm/sdk/node/){rel="&#x22;nofollow&#x22;"} or
> using http interfaces (only available when self hosting MongoDB), but these are untested. You can find an example for using realm [here](https://github.com/albionstatus/albionstatus-backend/){rel="&#x22;nofollow&#x22;"}

#### `mysql`

> You can find an example with a modified MySQL driver [here](https://github.com/cloudflare/worker-template-mysql){rel="&#x22;nofollow&#x22;"}

- `rhea`
- `gremlin`
- `ioredis`
- `cassandra-driver`
- `kafkajs`

# Node.js

**Preset:** `node_server`

Node.js is the default nitro output preset for production builds and Nitro has native Node.js runtime support.

Build project using nitro CLI:

```bash
nitro build
```

When running `nitro build` with the Node server preset, the result will be an entry point that launches a ready-to-run Node server. To try output:

```bash
$ node .output/server/index.mjs
Listening on http://localhost:3000
```

You can now deploy fully standalone `.output` directory to the hosting of your choice.

### Environment Variables

You can customize server behavior using following environment variables:

- `NITRO_PORT` or `PORT` (defaults to `3000`)
- `NITRO_HOST` or `HOST`
- `NITRO_UNIX_SOCKET` - if provided (a path to the desired socket file) the service will be served over the provided UNIX socket.
- `NITRO_SSL_CERT` and `NITRO_SSL_KEY` - if both are present, this will launch the server in HTTPS mode. In the vast majority of cases, this should not be used other than for testing, and the Nitro server should be run behind a reverse proxy like nginx or Cloudflare which terminates SSL.
- `NITRO_SHUTDOWN_DISABLED` - Disables the graceful shutdown feature when set to `'true'`. If it's set to `'true'`, the graceful shutdown is bypassed to speed up the development process. Defaults to `'false'`.
- `NITRO_SHUTDOWN_SIGNALS` - Allows you to specify which signals should be handled. Each signal should be separated with a space. Defaults to `'SIGINT SIGTERM'`.
- `NITRO_SHUTDOWN_TIMEOUT` - Sets the amount of time (in milliseconds) before a forced shutdown occurs. Defaults to `'30000'` milliseconds.
- `NITRO_SHUTDOWN_FORCE` - When set to true, it triggers `process.exit()` at the end of the shutdown process. If it's set to `'false'`, the process will simply let the event loop clear. Defaults to `'true'`.

## Cluster mode

**Preset:** `node_cluster`

For more performance and leveraging multi-core handling, you can use cluster preset.

### Environment Variables

In addition to environment variables from the `node_server` preset, you can customize behavior:

- `NITRO_CLUSTER_WORKERS`: Number of cluster workers (default is Number of available cpu cores)

## Handler (advanced)

**Preset:** `node`

Nitro also has a more low-level preset that directly exports a function with `(req, res) => {}` signature usable for middleware and custom servers.

When running `nitro build` with the Node preset, the result will be an entry point exporting a function with the `(req, res) => {}` signature.

**Example:**

```js
import { createServer } from 'node:http'
import { listener } from './.output/server'

const server = createServer(listener)
server.listen(8080)
```

# WinterJS

**Preset:** `winterjs`

You can easily build Nitro powered applications to run with [wasmerio/winterjs](https://github.com/wasmerio/winterjs){rel="&#x22;nofollow&#x22;"} runtime.

[WinterJS](https://github.com/wasmerio/winterjs){rel="&#x22;nofollow&#x22;"} is a JavaScript Service Workers server written in Rust, that uses the SpiderMonkey runtime to execute JavaScript (the same runtime that Firefox uses) ([announcement](https://wasmer.io/posts/announcing-winterjs-service-workers){rel="&#x22;nofollow&#x22;"}).

::warning
🚧 WinterJS runtime is unstable and under heavy development. Follow [nitrojs/nitro#1861](https://github.com/nitrojs/nitro/issues/1861){rel=""nofollow""} for status and information.
::

In order to build for this runtime, use `NITRO_PRESET="winterjs"` environment variable:

```sh
NITRO_PRESET="winterjs" npm run build
```

Make sure you have `wasmer` installed locally ([install wasmer](https://docs.wasmer.io/install){rel="&#x22;nofollow&#x22;"})

Run locally:

```sh
wasmer run wasmer/winterjs --forward-host-env --net --mapdir app:.output app/server/index.mjs
```

# Bun

**Preset:** `bun`

Nitro output is compatible with Bun runtime. While using default [Node.js](https://nitro.build/deploy/runtimes/node) you can also run the output in bun, using `bun` preset has advantage of better optimizations.

After building with bun preset using `bun` as preset, you can run server in production using:

```bash
bun run ./.output/server/index.mjs
```

:read-more{to="https://bun.sh"}

## Environment Variables

You can use the `PORT` or `NITRO_PORT` and `HOST` or `NITRO_HOST` environment variables to set the server port.

Use the `NITRO_BUN_IDLE_TIMEOUT` environment variable to change the default [idleTimeout](https://bun.sh/docs/runtime/http/server#idletimeout){rel="&#x22;nofollow&#x22;"}.

# Deno

**Preset:** `deno_server`

You can build your Nitro server using Node.js to run within [Deno Runtime](https://deno.com/runtime){rel="&#x22;nofollow&#x22;"} in a custom server.

```bash
# Build with the deno NITRO preset
NITRO_PRESET=deno_server npm run build

# Start production server
deno run --unstable --allow-net --allow-read --allow-env .output/server/index.ts
```

To enabling Node.js compatibility, you need to upgrade to Deno v2, and a compatibility date set to `2025-01-30` or later in your nitro configuration file.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
    compatibilityDate: "2025-01-30",
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
    compatibilityDate: "2025-01-30",
})
```

::

## Deno Deploy

:read-more{to="https://nitro.build/deploy/providers/deno-deploy"}

# Custom Preset

Custom presets are local files that have a preset entry that defines builder configuration and a runtime entry point.

::warning
Custom local preset support is an experimental feature.
::

## Example

::note
Check [nitrojs/nitro-preset-starter](https://github.com/nitrojs/nitro-preset-starter){rel=""nofollow""} for a ready-to-use template.
::

First, we have to define our preset entry point in a local directory `preset/nitro.config.ts`

```ts [./preset/nitro.config.ts]
import type { NitroPreset } from "nitropack";
import { fileURLToPath } from "node:url"

export default <NitroPreset>{
  // extends: "node-server", // You can extend existing presets
  entry: fileURLToPath(new URL("./entry.ts", import.meta.url)),
  hooks: {
    compiled() {
      // ...
    },
  },
};
```

The entry point will be used by your server or provider, and you can fully customize its behavior.

::code-group

```ts [preset/entry.ts (Workers)]
import "#internal/nitro/virtual/polyfill";

const nitroApp = useNitroApp();

export default {
  fetch(request: Request) {
    const url = new URL(request.url);
    return nitroApp.localFetch(url.pathname + url.search, {
      context: {},
      host: url.hostname,
      protocol: url.protocol,
      method: request.method,
      headers: request.headers,
      body: undefined,
    });
  },
};
```

```ts [preset/entry.ts (Node.js)]
import "#internal/nitro/virtual/polyfill";
import { Server } from "node:http";
import { toNodeListener } from "h3";

const nitroApp = useNitroApp();
const server = new Server(toNodeListener(nitroApp.h3App));

// @ts-ignore
server.listen(3000, (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`Listening on http://localhost:3000 (custom preset)`);
});
```

::

Then in your nitro config file, you can use your custom preset.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  preset: "./preset",
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    preset: "./preset",
  }
});
```

::

Refer to the Nitro [source code](https://github.com/nitrojs/nitro/tree/main/src){rel="&#x22;nofollow&#x22;"} directly to have a better understanding of presets and entry points.

# Alwaysdata

**Preset:** `alwaysdata`

:read-more{to="https://alwaysdata.com"}

## Set up application

### Pre-requisites

::steps{level="4"}

#### [Register a new profile](https://www.alwaysdata.com/en/register/){rel=""nofollow""} on alwaysdata platform if you don't have one

#### Get a free 100Mb plan to host your app

::

::note
Keep in mind your *account name* will be used to provide you a default URL in the form of `account_name.alwaysdata.net`, so choose it wisely. You can also link your existing domains to your account later or register as many accounts under your profile as you need.
::

### Local deployment

::steps{level="4"}

#### Build your project locally with `npm run build -- preset alwaysdata`

#### [Upload your app](https://help.alwaysdata.com/en/remote-access/){rel=""nofollow""} to your account in its own directory (e.g. `$HOME/www/my-app`). You can use any protocol you prefer (SSH/FTP/WebDAV…) to do so

#### On your admin panel, [create a new site](https://admin.alwaysdata.com/site/add/){rel=""nofollow""} for your app with the following features:* *Addresses*: `[account_name].alwaysdata.net`
- *Type*: Node.js
- *Command*: `node ./output/server/index.mjs`
- *Working directory*: `www/my-app` (adapt it to your deployment path)
- *Environment*:

  ```ini
  NITRO_PRESET=alwaysdata
  ```
- *Node.js version*: `Default version` is fine; pick no less than `20.0.0` (you can also [set your Node.js version globally](https://help.alwaysdata.com/en/languages/nodejs/configuration/#supported-versions){rel=""nofollow""})
- *Hot restart*: `SIGHUP`:read-more{title="Get more information about alwaysdata Node.js sites type" to="https://help.alwaysdata.com/en/languages/nodejs"}

#### Your app is now live at `http(s)://[account_name].alwaysdata.net`

::

# AWS Lambda

**Preset:** `aws_lambda`

:read-more{title="AWS Lambda" to="https://aws.amazon.com/lambda/"}

Nitro provides a built-in preset to generate output format compatible with [AWS Lambda](https://aws.amazon.com/lambda/){rel="&#x22;nofollow&#x22;"}.
The output entrypoint in `.output/server/index.mjs` is compatible with [AWS Lambda format](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html){rel="&#x22;nofollow&#x22;"}.

It can be used programmatically or as part of a deployment.

```ts
import { handler } from './.output/server'

// Use programmatically
const { statusCode, headers, body } = handler({ rawPath: '/' })
```

## Inlining chunks

Nitro output, by default uses dynamic chunks for lazy loading code only when needed. However this sometimes can not be ideal for performance. (See discussions in [nitrojs/nitro#650](https://github.com/nitrojs/nitro/pull/650){rel="&#x22;nofollow&#x22;"}). You can enabling chunk inlining behavior using [`inlineDynamicImports`](https://nitro.build/config#inlinedynamicimports) config.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  inlineDynamicImports: true
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    inlineDynamicImports: true
  }
})
```

::

## Response streaming

:read-more{title="Introducing AWS Lambda response streaming" to="https://aws.amazon.com/blogs/compute/introducing-aws-lambda-response-streaming/"}

In order to enable response streaming, enable `awsLambda.streaming` flag:

```ts [nitro.config.ts]
export default defineNitroConfig({
  awsLambda: {
    streaming: true
  }
});
```

# AWS Amplify

**Preset:** `aws_amplify`

:read-more{title="AWS Amplify Hosting" to="https://aws.amazon.com/amplify"}

## Deploy to AWS Amplify Hosting

::tip
Integration with this provider is possible with [zero configuration](https://nitro.build/deploy/#zero-config-providers).
::

::steps{level="4"}

#### Login to the [AWS Amplify Hosting Console](https://console.aws.amazon.com/amplify/){rel=""nofollow""}

#### Click on "Get Started" > Amplify Hosting (Host your web app)

#### Select and authorize access to your Git repository provider and select the main branch

#### Choose a name for your app, make sure build settings are auto-detected and optionally set requirement environment variables under the advanced section

#### Optionally, select Enable SSR logging to enable server-side logging to your Amazon CloudWatch account

#### Confirm configuration and click on "Save and Deploy"

::

## Advanced Configuration

You can configure advanced options of this preset using `awsAmplify` option.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  awsAmplify: {
      // catchAllStaticFallback: true,
      // imageOptimization: { path: "/_image", cacheControl: "public, max-age=3600, immutable" },
      // imageSettings: { ... },
      // runtime: "nodejs18.x", // default: "nodejs18.x" | "nodejs16.x" | "nodejs20.x"
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    awsAmplify: {
      // catchAllStaticFallback: true,
      // imageOptimization: { "/_image", cacheControl: "public, max-age=3600, immutable" },
      // imageSettings: { ... },
      // runtime: "nodejs18.x", // default: "nodejs18.x" | "nodejs16.x" | "nodejs20.x"
    }
  }
})
```

::

### `amplify.yml`

You might need a custom `amplify.yml` file for advanced configuration. Here are two template examples:

::code-group

```yml [amplify.yml]
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - nvm use 18 && node --version
        - corepack enable && npx --yes nypm install
    build:
      commands:
        - pnpm build
  artifacts:
    baseDirectory: .amplify-hosting
    files:
      - "**/*"
```

```yml [amplify.yml (monorepo)]
version: 1
applications:
  - frontend:
      phases:
        preBuild:
          commands:
          - nvm use 18 && node --version
          - corepack enable && npx --yes nypm install
        build:
          commands:
            - pnpm --filter website1 build
      artifacts:
        baseDirectory: apps/website1/.amplify-hosting
        files:
          - '**/*'
      buildPath: /
    appRoot: apps/website1
```

::

# Azure

## Azure static web apps

**Preset:** `azure`

:read-more{title="Azure Static Web Apps" to="https://azure.microsoft.com/en-us/products/app-service/static"}

::note
Integration with this provider is possible with [zero configuration](https://nitro.build/deploy/#zero-config-providers).
::

[Azure Static Web Apps](https://azure.microsoft.com/en-us/products/app-service/static){rel="&#x22;nofollow&#x22;"} are designed to be deployed continuously in a [GitHub Actions workflow](https://docs.microsoft.com/en-us/azure/static-web-apps/github-actions-workflow){rel="&#x22;nofollow&#x22;"}. By default, Nitro will detect this deployment environment and enable the `azure` preset.

### Local preview

Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local){rel="&#x22;nofollow&#x22;"} if you want to test locally.

You can invoke a development environment to preview before deploying.

```bash
NITRO_PRESET=azure npx nypm@latest run build
npx @azure/static-web-apps-cli start .output/public --api-location .output/server
```

### Configuration

Azure Static Web Apps are [configured](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration){rel="&#x22;nofollow&#x22;"} using the `staticwebapp.config.json` file.

Nitro automatically generates this configuration file whenever the application is built with the `azure` preset.

Nitro will automatically add the following properties based on the following criteria:

| Property                                                                                                                                            | Criteria                                                                                                                                                                                                                                                      | Default       |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **[platform.apiRuntime](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#platform){rel="&#x22;nofollow&#x22;"}**               | Will automatically set to `node:16` or `node:14` depending on your package configuration.                                                                                                                                                                     | `node:16`     |
| **[navigationFallback.rewrite](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#fallback-routes){rel="&#x22;nofollow&#x22;"}** | Is always `/api/server`                                                                                                                                                                                                                                       | `/api/server` |
| **[routes](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#routes){rel="&#x22;nofollow&#x22;"}**                              | All prerendered routes are added. Additionally, if you do not have an `index.html` file an empty one is created for you for compatibility purposes and also requests to `/index.html` are redirected to the root directory which is handled by `/api/server`. | `[]`          |

### Custom configuration

You can alter the Nitro generated configuration using `azure.config` option.

Custom routes will be added and matched first. In the case of a conflict (determined if an object has the same route property), custom routes will override generated ones.

### Deploy from CI/CD via GitHub actions

When you link your GitHub repository to Azure Static Web Apps, a workflow file is added to the repository.

When you are asked to select your framework, select custom and provide the following information:

| Input                | Value            |
| -------------------- | ---------------- |
| **app\_location**    | '/'              |
| **api\_location**    | '.output/server' |
| **output\_location** | '.output/public' |

If you miss this step, you can always find the build configuration section in your workflow and update the build configuration:

```yaml [.github/workflows/azure-static-web-apps-<RANDOM_NAME>.yml]
###### Repository/Build Configurations ######
app_location: '/'
api_location: '.output/server'
output_location: '.output/public'
###### End of Repository/Build Configurations ######
```

That's it! Now Azure Static Web Apps will automatically deploy your Nitro-powered application on push.

If you are using runtimeConfig, you will likely want to configure the corresponding [environment variables on Azure](https://docs.microsoft.com/en-us/azure/static-web-apps/application-settings){rel="&#x22;nofollow&#x22;"}.

## Azure functions

**Preset:** `azure_functions`

::important
If you encounter any issues, please ensure you're using a Node.js 16+ runtime. You can find more information about [how to set the Node version in the Azure docs](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=v2#setting-the-node-version){rel=""nofollow""}.
Please see [nitrojs/nitro#2114](https://github.com/nitrojs/nitro/issues/2114){rel=""nofollow""} for some common issues.
::

### Local preview

Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local){rel="&#x22;nofollow&#x22;"} if you want to test locally.

You can invoke a development environment from the serverless directory.

```bash
NITRO_PRESET=azure_functions npx nypm@latest run build
cd .output
func start
```

You can now visit `http://localhost:7071/` in your browser and browse your site running locally on Azure Functions.

### Deploy from your local machine

To deploy, just run the following command:

```bash
# To publish the bundled zip file
az functionapp deployment source config-zip -g <resource-group> -n <app-name> --src dist/deploy.zip
# Alternatively you can publish from source
cd dist && func azure functionapp publish --javascript <app-name>
```

### Deploy from CI/CD via GitHub actions

First, obtain your Azure Functions Publish Profile and add it as a secret to your GitHub repository settings following [these instructions](https://github.com/Azure/functions-action#using-publish-profile-as-deployment-credential-recommended){rel="&#x22;nofollow&#x22;"}.

Then create the following file as a workflow:

```yaml [.github/workflows/azure.yml]
name: azure
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  deploy:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ ubuntu-latest ]
        node: [ 14 ]
    steps:
      - uses: actions/setup-node@v2
        with:
          node-version: ${{ matrix.node }}

      - name: Checkout
        uses: actions/checkout@master

      - name: Get yarn cache directory path
        id: yarn-cache-dir-path
        run: echo "::set-output name=dir::$(yarn cache dir)"

      - uses: actions/cache@v2
        id: yarn-cache
        with:
          path: ${{ steps.yarn-cache-dir-path.outputs.dir }}
          key: ${{ runner.os }}-yarn-${{ hashFiles('**/yarn.lock') }}
          restore-keys: |
            ${{ runner.os }}-yarn-azure

      - name: Install Dependencies
        if: steps.cache.outputs.cache-hit != 'true'
        run: yarn

      - name: Build
        run: npm run build
        env:
          NITRO_PRESET: azure_functions

      - name: 'Deploy to Azure Functions'
        uses: Azure/functions-action@v1
        with:
          app-name: <your-app-name>
          package: .output/deploy.zip
          publish-profile: ${{ secrets.AZURE_FUNCTIONAPP_PUBLISH_PROFILE }}
```

### Optimizing Azure functions

Consider [turning on immutable packages](https://docs.microsoft.com/en-us/azure/app-service/deploy-run-package){rel="&#x22;nofollow&#x22;"} to support running your app from the zip file. This can speed up cold starts.

# Cleavr

**Preset:** `cleavr`

:read-more{title="cleavr.io" to="https://cleavr.io"}

::note
Integration with this provider is possible with [zero configuration](https://nitro.build/deploy/#zero-config-providers).
::

## Set up your web app

In your project, set Nitro preset to `cleavr`.

```js
export default {
  nitro: {
    preset: 'cleavr'
  }
}
```

Push changes to your code repository.

**In your Cleavr panel:**

::steps{level="4"}

#### Provision a new server

#### Add a website, selecting **Nuxt 3** as the app type

#### In web app > settings > Code Repo, point to your project's code repository

::

You're now all set to deploy your project!

# Cloudflare

## Cloudflare Workers

**Preset:** `cloudflare_module`

:read-more{title="Cloudflare Workers" to="https://developers.cloudflare.com/workers/"}

::note
Integration with this provider is possible with [zero configuration](https://nitro.build/deploy#zero-config-providers) supporting [workers builds (beta)](https://developers.cloudflare.com/workers/ci-cd/builds/){rel=""nofollow""}.
::

::important
To use Workers with Static Assets, you need a Nitro compatibility date set to `2024-09-19` or later.
::

The following shows an example `nitro.config.ts` file for deploying a Nitro app to Cloudflare Workers.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
    compatibilityDate: "2024-09-19",
    preset: "cloudflare_module",
    cloudflare: {
      deployConfig: true,
      nodeCompat: true
    }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
    compatibilityDate: "2024-09-19",
    nitro: {
      preset: "cloudflare_module",
      cloudflare: {
        deployConfig: true,
        nodeCompat: true
      }
    }
})
```

::

By setting `deployConfig: true`, Nitro will automatically generate a `wrangler.json` for you with the correct configuration.
If you need to add [Cloudflare Workers configuration](https://developers.cloudflare.com/workers/wrangler/configuration/){rel="&#x22;nofollow&#x22;"}, such as [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/){rel="&#x22;nofollow&#x22;"}, you can either:

- Set these in your Nitro config under the `cloudflare: { wrangler : {} }`. This has the same type as `wrangler.json`.
- Provide your own `wrangler.json`. Nitro will merge your config with the appropriate settings, including pointing to the build output.

### Local Preview

You can use [Wrangler](https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler){rel="&#x22;nofollow&#x22;"} to preview your app locally:

:pm-run{script="build"}

:pm-x{command="wrangler dev"}

### Manual Deploy

After having built your application you can manually deploy it with Wrangler.

First make sure to be logged into your Cloudflare account:

:pm-x{command="wrangler login"}

Then you can deploy the application with:

:pm-x{command="wrangler deploy"}

### Runtime Hooks

You can use [runtime hooks](https://nitro.build/guide/plugins#nitro-runtime-hooks) below in order to extend [Worker handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/){rel="&#x22;nofollow&#x22;"}.

:read-more{to="https://nitro.build/guide/plugins#nitro-runtime-hooks"}

- [`cloudflare:scheduled`](https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/){rel="&#x22;nofollow&#x22;"}
- [`cloudflare:email`](https://developers.cloudflare.com/email-routing/email-workers/runtime-api/){rel="&#x22;nofollow&#x22;"}
- [`cloudflare:queue`](https://developers.cloudflare.com/queues/configuration/javascript-apis/#consumer){rel="&#x22;nofollow&#x22;"}
- [`cloudflare:tail`](https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/){rel="&#x22;nofollow&#x22;"}
- `cloudflare:trace`

## Cloudflare Pages

**Preset:** `cloudflare_pages`

:read-more{title="Cloudflare Pages" to="https://pages.cloudflare.com/"}

::note
Integration with this provider is possible with [zero configuration](https://nitro.build/deploy#zero-config-providers).
::

::warning
Cloudflare [Workers Module](https://nitro.build/#cloudflare-workers) is the new recommended preset for deployments. Please consider using the pages only if you need specific features.
::

The following shows an example `nitro.config.ts` file for deploying a Nitro app to Cloudflare Pages.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
    preset: "cloudflare_pages",
    cloudflare: {
      deployConfig: true,
      nodeCompat:true
    }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
    nitro: {
      preset: "cloudflare_pages",
      cloudflare: {
        deployConfig: true,
        nodeCompat:true
      }
    }
})
```

::

Nitro automatically generates a `_routes.json` file that controls which routes get served from files and which are served from the Worker script. The auto-generated routes file can be overridden with the config option `cloudflare.pages.routes` ([read more](https://developers.cloudflare.com/pages/platform/functions/routing/#functions-invocation-routes){rel="&#x22;nofollow&#x22;"}).

### Local Preview

You can use [Wrangler](https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler){rel="&#x22;nofollow&#x22;"} to preview your app locally:

:pm-run{script="build"}

:pm-x{command="wrangler pages dev"}

### Manual Deploy

After having built your application you can manually deploy it with Wrangler, in order to do so first make sure to be
logged into your Cloudflare account:

:pm-x{command="wrangler login"}

Then you can deploy the application with:

:pm-x{command="wrangler pages deploy"}

## Cloudflare Service Workers

**Preset:** `cloudflare`

::note
**Note:** This preset uses the [service worker syntax](https://developers.cloudflare.com/workers/learning/service-worker/){rel=""nofollow""} for deployment.
::

::warning
**Note:** This preset is deprecated.
::

The way this preset works is identical to that of the `cloudflare_module` one presented above, with the only difference being that such preset inherits all the [disadvantages](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/#advantages-of-migrating){rel="&#x22;nofollow&#x22;"} that such syntax brings.

## Deploy within CI/CD using GitHub Actions

Regardless on whether you're using Cloudflare Pages or Cloudflare Workers, you can use the [Wrangler GitHub actions](https://github.com/marketplace/actions/deploy-to-cloudflare-workers-with-wrangler){rel="&#x22;nofollow&#x22;"} to deploy your application.

::note
**Note:** Remember to [instruct Nitro to use the correct preset](https://nitro.build/deploy#changing-the-deployment-preset) (note that this is necessary for all presets including the `cloudflare_pages` one).
::

## Environment Variables

Nitro allows you to universally access environment variables using `process.env` or `import.meta.env` or the runtime config.

::note
Make sure to only access environment variables **within the event lifecycle** and not in global contexts since Cloudflare only makes them available during the request lifecycle and not before.
::

**Example:** If you have set the `SECRET` and `NITRO_HELLO_THERE` environment variables set you can access them in the following way:

```ts
console.log(process.env.SECRET) // note that this is in the global scope! so it doesn't actually work and the variable is undefined!

export default defineEventHandler((event) => {
  // note that all the below are valid ways of accessing the above mentioned variables
  useRuntimeConfig(event).helloThere
  useRuntimeConfig(event).secret
  process.env.NITRO_HELLO_THERE
  import.meta.env.SECRET
});
```

### Specify Variables in Development Mode

For development, you can use a `.env` file to specify environment variables:

```ini
NITRO_HELLO_THERE="captain"
SECRET="top-secret"
```

::note
**Note:** Make sure you add `.env` to the `.gitignore` file so that you don't commit it as it can contain sensitive information.
::

### Specify Variables for local previews

After build, when you try out your project locally with `wrangler dev` or `wrangler pages dev`, in order to have access to environment variables you will need to specify the in a `.dev.vars` file in the root of your project (as presented in the [Pages](https://developers.cloudflare.com/pages/functions/bindings/#interact-with-your-environment-variables-locally){rel="&#x22;nofollow&#x22;"} and [Workers](https://developers.cloudflare.com/workers/configuration/environment-variables/#interact-with-environment-variables-locally){rel="&#x22;nofollow&#x22;"} documentation).

If you are using a `.env` file while developing, your `.dev.vars` should be identical to it.

::note
**Note:** Make sure you add `.dev.vars` to the `.gitignore` file so that you don't commit it as it can contain sensitive information.
::

### Specify Variables for Production

For production, use the Cloudflare dashboard or the [`wrangler secret`](https://developers.cloudflare.com/workers/wrangler/commands/#secret){rel="&#x22;nofollow&#x22;"} command to set environment variables and secrets.

### Specify Variables using `wrangler.toml`/`wrangler.json`

You can specify a custom `wrangler.toml`/`wrangler.json` file and define vars inside.

::warning
Note that this isn't recommend for sensitive data like secrets.
::

**Example:**

```ini [wrangler.toml]
# Shared
[vars]
NITRO_HELLO_THERE="general"
SECRET="secret"

# Override values for `--env production` usage
[env.production.vars]
NITRO_HELLO_THERE="captain"
SECRET="top-secret"
```

## Direct access to Cloudflare bindings

Bindings are what allows you to interact with resources from the Cloudflare platform, examples of such resources are key-value data storages ([KVs](https://developers.cloudflare.com/kv/){rel="&#x22;nofollow&#x22;"}) and serverless SQL databases ([D1s](https://developers.cloudflare.com/d1/){rel="&#x22;nofollow&#x22;"}).

::read-more
For more details on Bindings and how to use them please refer to the Cloudflare [Pages](https://developers.cloudflare.com/pages/functions/bindings/){rel=""nofollow""} and [Workers](https://developers.cloudflare.com/workers/configuration/bindings/#bindings){rel=""nofollow""} documentation.
::

::tip
Nitro provides high level API to interact with primitives such as [KV Storage](https://nitro.build/guide/storage) and [Database](https://nitro.build/guide/database) and you are highly recommended to prefer using them instead of directly depending on low-level APIs for usage stability.
::

:read-more{title="Database Layer" to="https://nitro.build/guide/database"}

:read-more{title="KV Storage" to="https://nitro.build/guide/storage"}

In runtime, you can access bindings from the request event, by accessing its `context.cloudflare.env` field, this is for example how you can access a D1 bindings:

```ts
defineEventHandler(async (event) => {
  const { cloudflare } = event.context
  const stmt = await cloudflare.env.MY_D1.prepare('SELECT id FROM table')
  const { results } = await stmt.all()
})
```

## Dev Preset

Cloudflare preset can be enabled in development mode for production environment emulation and access to the bindings in local dev.

In order to enable dev preset, make sure using latest nitro version (>=2.12) and install [`wrangler`](https://npmjs.com/package/wrangler){rel="&#x22;nofollow&#x22;"} as a dependency.

:pm-install{name="-D wrangler"}

Then, update config:

::CodeGroup

```ts [nitro.config.ts]
export default defineNitroConfig({
    compatibilityDate: "2025-07-15", // or "latest"
    preset: "cloudflare-module" // or "cloudflare-pages"
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
    compatibilityDate: "2025-07-15", // or "latest"
    nitro: {
        preset: "cloudflare-module" // or "cloudflare-pages"
    }
})
```

::

In development terminal, you should see a message like this:

```sh
ℹ Using cloudflare-dev emulation in development mode.
```

In order to access bindings in dev mode we start by defining the bindings. You can do this in a `wrangler.toml`/`wrangler.jsonc` file, or directly in your Nitro config under `cloudflare.wrangler` (accepts the same type as `wrangler.json`).

For example to define a variable and a KV namespace in a `wrangler.toml`

```ini [wrangler.toml]
[vars]
MY_VARIABLE="my-value"

[[kv_namespaces]]
binding = "MY_KV"
id = "xxx"
```

Or in your Nitro config:

```js [nitro.config.js]
export default defineNitroConfig({
    cloudflare: {
      wrangler: {
        vars: {
          MY_VARIABLE: "my-value"
        },
        kv_namespaces: [
          {
            binding: "MY_KV",
            id: "xxx"
          }
        ]
      }
    }
});
```

::note
Only bindings in the default environment are recognized.
::

you will be able to access the `MY_VARIABLE` and `MY_KV` from the request event just as illustrated above.

# Deno Deploy

**Preset:** `deno_deploy`

:read-more{title="Deno Deploy" to="https://deno.com/deploy"}

## Deploy with the CLI

You can use [deployctl](https://deno.com/deploy/docs/deployctl){rel="&#x22;nofollow&#x22;"} to deploy your app.

Login to [Deno Deploy](https://dash.deno.com/account#access-tokens){rel="&#x22;nofollow&#x22;"} to obtain a `DENO_DEPLOY_TOKEN` access token, and set it as an environment variable.

```bash
# Build with the deno_deploy NITRO preset
NITRO_PRESET=deno_deploy npm run build

# Make sure to run the deployctl command from the output directory
cd .output
deployctl deploy --project=my-project server/index.ts
```

## Deploy within CI/CD using gitHub actions

You just need to include the deployctl GitHub Action as a step in your workflow.

You do not need to set up any secrets for this to work. You do need to link your GitHub repository to your Deno Deploy project and choose the "GitHub Actions" deployment mode. You can do this in your project settings on [Deno Deploy](https://dash.deno.com){rel="&#x22;nofollow&#x22;"}.

Create the following workflow file in your `.github/workflows` directory:

```yaml [.github/workflows/deno_deploy.yml]
name: deno-deploy

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  deploy:
    steps:
      - uses: actions/checkout@v3
      - run: corepack enable
      - uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: pnpm
      - run: pnpm install
      - run: pnpm build
        env:
          NITRO_PRESET: deno_deploy
      - name: Deploy to Deno Deploy
        uses: denoland/deployctl@v1
        with:
          project: my-project
          entrypoint: server/index.ts
          root: .output
```

## Deno runtime

:read-more{to="https://nitro.build/deploy/runtimes/deno"}

# DigitalOcean

**Preset:** `digital_ocean`

:read-more{title="Digital Ocean App Platform" to="https://docs.digitalocean.com/products/app-platform/"}

## Set up application

::steps{level="4"}

#### Create a new Digital Ocean app following the [guide](https://docs.digitalocean.com/products/app-platform/how-to/create-apps/){rel=""nofollow""}

#### Next, you'll need to configure environment variables. In your app settings, ensure the following app-level environment variables are set:```bash

NITRO_PRESET=digital_ocean

```:br[More information](https://docs.digitalocean.com/products/app-platform/how-to/use-environment-variables/){rel=""nofollow""}.

#### You will need to ensure you set an `engines.node` field in your app's `package.json` to ensure Digital Ocean uses a supported version of Node.js:```json
{
   "engines": {
      "node": "16.x"
   }
}
```:br[See more information](https://docs.digitalocean.com/products/app-platform/languages-frameworks/nodejs/#node-version){rel=""nofollow""}.

#### You'll also need to add a run command so Digital Ocean knows what command to run after a build. You can do so by adding a start script to your `package.json`:```json
{
   "scripts": {
      "start": "node .output/server/index.mjs"
   }
}
```

#### Finally, you'll need to add this start script to your Digital Ocean app's run command. Go to `Components > Settings > Commands`, click "Edit", then add `npm run start`

::

Your app should be live at a Digital Ocean generated URL and you can now follow [the rest of the Digital Ocean deployment guide](https://docs.digitalocean.com/products/app-platform/how-to/manage-deployments/){rel="&#x22;nofollow&#x22;"}.

# Edgio

::warning
This preset is deprecated and will be removed in v3.
::

# Firebase

::note
You will need to be on the [**Blaze plan**](https://firebase.google.com/pricing){rel=""nofollow""} (Pay as you go) to get started.
::

## Firebase app hosting

Preset: `firebase_app_hosting`

:read-more{title="Firebase App Hosting" to="https://firebase.google.com/docs/app-hosting"}

::tip
You can integrate with this provider using [zero configuration](https://nitro.build/deploy/#zero-config-providers).
::

### Project setup

::steps{level="4"}

#### Go to the Firebase [console](https://console.firebase.google.com/){rel=""nofollow""} and set up a new project

#### Select **Build > App Hosting** from the sidebar
- You may need to upgrade your billing plan at this step.

#### Click **Get Started**
- Choose a region.
- Import a GitHub repository (you’ll need to link your GitHub account).
- Configure deployment settings (project root directory and branch), and enable automatic rollouts.
- Choose a unique ID for your backend.

#### Click Finish & Deploy to create your first rollout

::

When you deploy with Firebase App Hosting, the App Hosting preset will be run automatically at build time.

## Firebase hosting (deprecated)

::important
This deployment method is deprecated and is not recommended. Firebase App Hosting is the recommended way to deploy Nitro apps on Firebase.
::

**Preset:** `firebase`

:read-more{title="Firebase Hosting" to="https://firebase.google.com/docs/hosting"}

::important
This preset will deploy to firebase functions 1st gen by default. If you want to deploy to firebase functions 2nd gen, see the [instructions below](https://nitro.build/#using-2nd-generation-firebase-functions).
::

### Project Setup

#### Using firebase CLI (recommended)

You may instead prefer to set up your project with the Firebase CLI, which will fetch your project ID for you, add required dependencies (see above) and even set up automated deployments via GitHub Actions (for hosting only). [Learn about installing the firebase CLI](https://firebase.google.com/docs/cli#windows-npm){rel="&#x22;nofollow&#x22;"}.

1. Install firebase CLI globally

Always try to use the latest version of the Firebase CLI.

```bash
npm install -g firebase-tools@latest
```

**Note**: You need to be on [^11.18.0](https://github.com/firebase/firebase-tools/releases/tag/v11.18.0){rel="&#x22;nofollow&#x22;"} to deploy a `nodejs18` function.

1. Initialize your firebase project

```bash
firebase login
firebase init hosting
```

When prompted, you can enter `.output/public` as the public directory. In the next step, **do not** configure your project as a single-page app.

Once complete, add the following to your `firebase.json` to enable server rendering in Cloud Functions:

```json [firebase.json]
{
  "functions": { "source": ".output/server" },
  "hosting": [
    {
      "site": "<your_project_id>",
      "public": ".output/public",
      "cleanUrls": true,
      "rewrites": [{ "source": "**", "function": "server" }]
    }
  ]
}
```

You can find more details in the [Firebase documentation](https://firebase.google.com/docs/hosting/quickstart){rel="&#x22;nofollow&#x22;"}.

#### Alternative method

If you don't already have a `firebase.json` in your root directory, Nitro will create one the first time you run it. In this file, you will need to replace `<your_project_id>` with the ID of your Firebase project. This file should then be committed to the git.

1. Create a `.firebaserc` file

It is recommended to create a `.firebaserc` file so you don't need to manually pass your project ID to your `firebase` commands (with `--project <your_project_id>`):

```json [.firebaserc]
{
  "projects": {
    "default": "<your_project_id>"
  }
}
```

This file is usually generated when you initialize your project with the Firebase CLI. But if you don't have one, you can create it manually.

1. Install firebase dependencies

Then, add Firebase dependencies to your project:

::pm-install
---

dev: true
name: firebase-admin firebase-functions firebase-functions-test
---

::

1. Log into the firebase CLI

Make sure you are authenticated with the firebase cli. Run this command and follow the prompts:

:pm-x{command="firebase-tools login"}

### Local preview

You can preview a local version of your site if you need to test things out without deploying.

```bash
NITRO_PRESET=firebase npm run build
firebase emulators:start
```

### Build and deploy

Deploy to Firebase Hosting by running a Nitro build and then running the `firebase deploy` command.

```bash
NITRO_PRESET=firebase npm run build
```

:pm-x{command="firebase-tools deploy"}

If you installed the Firebase CLI globally, you can also run:

```bash
firebase deploy
```

### Using 2nd generation firebase functions

- [Comparison between 1st and 2nd generation functions](https://firebase.google.com/docs/functions/version-comparison){rel="&#x22;nofollow&#x22;"}

To switch to the more recent and, recommended generation of firebase functions, set the `firebase.gen` option to `2`:

::code-group

```ts [nitro.config.ts] {3}
export default defineNitroConfig({
  firebase: {
    gen: 2
    // ...
  }
})
```

```ts [nuxt.config.ts] {4}
export default defineNuxtConfig({
  nitro: {
    firebase: {
      gen: 2
      // ...
    }
  }
})
```

::

::note
If you cannot use configuration for any reason, alternatively you can use `NITRO_FIREBASE_GEN` environment variable.
::

If you already have a deployed version of your website and want to upgrade to 2nd gen, [see the Migration process on Firebase docs](https://firebase.google.com/docs/functions/2nd-gen-upgrade){rel="&#x22;nofollow&#x22;"}. Namely, the CLI will ask you to delete your existing functions before deploying the new ones.

### Options

You can set options for the firebase functions in your `nitro.config.ts` file:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  firebase: {
    gen: 2,
    httpsOptions: {
      region: 'europe-west1',
      maxInstances: 3,
    },
  },
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    firebase: {
      gen: 2,
      httpsOptions: {
        region: 'europe-west1',
        maxInstances: 3,
      },
    },
  },
});
```

::

You can also set options for 1st generation Cloud Functions if the `gen` option is set to `1`. Note these are different from the options for 2nd generation Cloud Functions.

#### Runtime Node.js version

You can set custom Node.js version in configuration:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  firebase: {
    nodeVersion: "20" // Can be "16", "18", "20" or "22"
  },
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    firebase: {
      nodeVersion: "20" // Can be "16", "18", "20" or "22"
    },
  },
});
```

::

Firebase tools use the `engines.node` version in `package.json` to determine which node version to use for your functions. Nitro automatically writes to the `.output/server/package.json` with configured Node.js version.

You might also need to add a runtime key to your `firebase.json` file:

```json [firebase.json]
{
  "functions": {
    "source": ".output/server",
    "runtime": "nodejs20"
  }
}
```

You can read more about this in [Firebase Docs](https://firebase.google.com/docs/functions/manage-functions?gen=2nd#set_nodejs_version){rel="&#x22;nofollow&#x22;"}.

### If your firebase project has other cloud functions

You may be warned that other cloud functions will be deleted when you deploy your nitro project. This is because nitro will deploy your entire project to firebase functions. If you want to deploy only your nitro project, you can use the `--only` flag:

```bash
firebase deploy --only functions:server,hosting
```

### Advanced

#### Renaming function

When deploying multiple apps within the same Firebase project, you must give your server a unique name in order to avoid overwriting
your functions.

You can specify a new name for the deployed Firebase function in your configuration:

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
  firebase: {
    serverFunctionName: "<new_function_name>"
  }
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    firebase: {
      serverFunctionName: "<new_function_name>"
    }
  }
})
```

::

::important
`firebase.serverFunctionName` must be a valid JS variable name and cannot include dashes (`-`).
::

# Flightcontrol

**Preset:** `flightcontrol`

:read-more{title="flightcontrol.dev" to="https://flightcontrol.dev?ref=nitro"}

::note
Flightcontrol has zero config support for [Nuxt](https://nuxt.com/){rel=""nofollow""} projects.
::

## Set Up your flightcontrol account

On a high level, the steps you will need to follow to deploy a project for the first time are:

::steps{level="4"}

#### Create an account at [Flightcontrol](https://app.flightcontrol.dev/signup?ref=nitro){rel=""nofollow""}

#### Create an account at [AWS](https://portal.aws.amazon.com/billing/signup){rel=""nofollow""} (if you don't already have one)

#### Link your AWS account to the Flightcontrol

#### Authorize the Flightcontrol GitHub App to access your chosen repositories, public or private

#### Create a Flightcontrol project with configuration via the Dashboard or with configuration via `flightcontrol.json`

::

### Create a project with configuration via the dashboard

::steps{level="4"}

#### Create a Flightcontrol project from the Dashboard. Select a repository for the source

#### Select the `GUI` config type

#### Select the Nuxt preset. This preset will also work for any Nitro-based applications

#### Select your preferred AWS server size

#### Submit the new project form

::

### Create a project with configuration via `flightcontrol.json`

::steps{level="4"}

#### Create a Flightcontrol project from your dashboard. Select a repository for the source

#### Select the `flightcontrol.json` config type

#### Add a new file at the root of your repository called `flightcontrol.json`. Here is an example configuration that creates an AWS fargate service for your app

::

```json [flightcontrol.json]
{
  "$schema": "https://app.flightcontrol.dev/schema.json",
  "environments": [
    {
      "id": "production",
      "name": "Production",
      "region": "us-west-2",
      "source": {
        "branch": "main"
      },
      "services": [
        {
          "id": "nitro",
          "buildType": "nixpacks",
          "name": "My Nitro site",
          "type": "fargate",
          "domain": "www.yourdomain.com",
          "outputDirectory": ".output",
          "startCommand": "node .output/server/index.mjs",
          "cpu": 0.25,
          "memory": 0.5
        }
      ]
    }
  ]
}
```

1. Submit the new project form.

::read-more{to="https://www.flightcontrol.dev/docs?ref=nitro"}
Learn more about Flightcontrol's [configuration](https://www.flightcontrol.dev/docs?ref=nitro){rel=""nofollow""}.
::

# Genezio

**Preset:** `genezio`

:read-more{title="Genezio" to="https://genezio.com"}

::important
🚧 This preset is currently experimental.
::

## 1. Project Setup

Create `genezio.yaml` file:

```yaml
# The name of the project.
name: nitro-app
# The version of the Genezio YAML configuration to parse.
yamlVersion: 2
backend:
  # The root directory of the backend.
  path: .output/
  # Information about the backend's programming language.
  language:
      # The name of the programming language.
      name: js
      # The package manager used by the backend.
      packageManager: npm
  # Information about the backend's functions.
  functions:
      # The name (label) of the function.
      - name: nitroServer
      # The path to the function's code.
        path: server/
        # The name of the function handler
        handler: handler
        # The entry point for the function.
        entry: index.mjs
```

::read-more
---

to: https://genezio.com/docs/project-structure/genezio-configuration-file/
---

To further customize the file to your needs, you can consult the
[official documentation](https://genezio.com/docs/project-structure/genezio-configuration-file/){rel=""nofollow""}.
::

## 2. Deploy your project

Build with the genezio nitro preset:

```bash
NITRO_PRESET=genezio npm run build
```

Deploy with [`genezio`](https://npmjs.com/package/genezio){rel="&#x22;nofollow&#x22;"} cli:

:pm-x{command="genezio deploy"}

::read-more
---

title: Backend Environment Variables
to: https://genezio.com/docs/project-structure/backend-environment-variables
---

To set environment viarables, please check out [Genezio - Environment Variables](https://genezio.com/docs/project-structure/backend-environment-variables){rel=""nofollow""}.
::

## 3. Monitor your project

You can monitor and manage your application through the [Genezio App Dashboard](https://app.genez.io/dashboard){rel="&#x22;nofollow&#x22;"}. The dashboard URL, also provided after deployment, allows you to access comprehensive views of your project's status and logs.

# GitHub Pages

**Preset:** `github_pages`

:read-more{title="GitHub Pages" to="https://pages.github.com/"}

## Setup

Follow the steps to [create a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site){rel="&#x22;nofollow&#x22;"}.

## Deployment

Here is an example GitHub Actions workflow to deploy your site to GitHub Pages using the `github_pages` preset:

```yaml [.github/workflows/deploy.yml]
# https://github.com/actions/deploy-pages#usage
name: Deploy to GitHub Pages

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: corepack enable
      - uses: actions/setup-node@v3
        with:
          node-version: "18"

      - run: npx nypm install
      - run: npm run build
        env:
          NITRO_PRESET: github_pages

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: ./.output/public

  # Deployment job
  deploy:
    # Add a dependency to the build job
    needs: build

    # Grant GITHUB_TOKEN the permissions required to make a Pages deployment
    permissions:
      pages: write      # to deploy to Pages
      id-token: write   # to verify the deployment originates from an appropriate source

    # Deploy to the github_pages environment
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    # Specify runner + deployment step
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
```

# GitLab Pages

**Preset:** `gitlab_pages`

:read-more{title="GitLab Pages" to="https://pages.github.com/"}

## Setup

Follow the steps to [create a GitLab Pages site](https://docs.gitlab.com/ee/user/project/pages/#getting-started){rel="&#x22;nofollow&#x22;"}.

## Deployment

1. Here is an example GitLab Pages workflow to deploy your site to GitLab Pages:

```yaml [.gitlab-ci.yml]
image: node:lts
before_script:
  - npx nypm install
pages:
  cache:
    paths:
      - node_modules/
  variables:
    NITRO_PRESET: gitlab_pages
  script:
    - npm run build
  artifacts:
    paths:
      - .output/public
  publish: .output/public
  rules:
    # This ensures that only pushes to the default branch
    # will trigger a pages deploy
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

# Heroku

**Preset:** `heroku`

:read-more{title="heroku.com" to="https://heroku.com/"}

## Using the heroku CLI

::steps{level="4"}

#### Create a new Heroku app.```bash

heroku create myapp

```

#### Configure Heroku to use the nodejs buildpack.```bash
heroku buildpacks:set heroku/nodejs
```

#### Configure your app.```bash

heroku config:set NITRO_PRESET=heroku

```

#### Ensure you have `start` and `build` commands in your `package.json` file.```json5
"scripts": {
  "build": "nitro build", // or `nuxt build` if using nuxt
  "start": "node .output/server/index.mjs"
}
```

::

## With nginx

::steps{level="4"}

#### Add the heroku Nginx buildpack [here](https://github.com/heroku/heroku-buildpack-nginx.git){rel=""nofollow""}

#### Change to the 'node' preset in your `nuxt.config````json5

"nitro": {
   "preset":"node",
}

```

#### From the **Existing app** section of buildpack doc, 2 key steps are required to get things running :br Step 1: Listen on a socket at 'tmp/nginx.socket'
Step 2: Create a file '/tmp/app-initialized' when your app is ready to accept connections

#### Create custom app runner, eg: apprunner.mjs at the root of the project (or any other preferred location), in this file, create a server, using the listener generated by the node preset, then listen on the socket as detailed in the buildpack doc```ts
import { createServer } from 'node:http'
import { listener } from './.output/server/index.mjs'

const server = createServer(listener)

server.listen('/tmp/nginx.socket') //following the buildpack doc
```

#### To create the 'tmp/app-initialized' file, use a nitro plugin, create file 'initServer.ts' at the root of the project (or any other preferred location)```ts

import fs from "fs"

export default defineNitroPlugin((nitroApp) => {
   if((process.env.NODE_ENV || 'development') != 'development') {
      fs.openSync('/tmp/app-initialized', 'w')
   }
})

```

#### Finally, create file 'Procfile' at the root of the project, with the Procfile, we tell heroku to start nginx and use the custom apprunner.mjs to start the server :br web: bin/start-nginx node apprunner.mjs

#### Bonus: create file 'config/nginx.conf.erb' to customize your nginx config. With the node preset, by default, static files handlers will not be generated, you can use nginx to server static files, just add the right location rule to the server block(s), or, force the node preset to generate handlers for the static files by setting serveStatic to true.
::


# IIS

## Using [IISnode](https://github.com/Azure/iisnode){rel="&#x22;nofollow&#x22;"}

**Preset:** `iis_node`

::steps{level="4"}
#### Install the latest LTS version of [Node.js](https://nodejs.org/en/){rel=""nofollow""} on your Windows Server.

#### Install [IISnode](https://github.com/azure/iisnode/releases){rel=""nofollow""}

#### Install [IIS `URLRewrite` Module](https://www.iis.net/downloads/microsoft/url-rewrite){rel=""nofollow""}.

#### In IIS, add `.mjs` as a new mime type and set its content type to `application/javascript`.

#### Deploy the contents of your `.output` folder to your website in IIS.
::

## Using IIS handler

**Preset:** `iis_handler` / `iis`

You can use IIS http handler directly.

::steps{level="4"}
#### Install the latest LTS version of [Node.js](https://nodejs.org/en/){rel=""nofollow""} on your Windows Server.

#### Install [IIS `HttpPlatformHandler` Module](https://www.iis.net/downloads/microsoft/httpplatformhandler){rel=""nofollow""}

#### Copy your `.output` directory into the Windows Server, and create a website on IIS pointing to that exact directory.
::

## IIS config options

::code-group
```ts [nitro.config.ts]
export default defineNitroConfig({
  // IIS options default
  iis: {
    // merges in a pre-existing web.config file to the nitro default file
    mergeConfig: true,
    // overrides the default nitro web.config file all together
    overrideConfig: false,
  },
});
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    // IIS options default
    iis: {
      // merges in a pre-existing web.config file to the nitro default file
      mergeConfig: true,
      // overrides the default nitro web.config file all together
      overrideConfig: false,
    },
  },
});
```

::

# Koyeb

**Preset:** `koyeb`

:read-more{to="https://www.koyeb.com"}

## Using the control panel

::steps{level="4"}

#### In the [Koyeb control panel](https://app.koyeb.com/){rel=""nofollow""}, click **Create App**

#### Choose **GitHub** as your deployment method

#### Choose the GitHub **repository** and **branch** containing your application code

#### Name your Service

#### If you did not add a `start` command to your `package.json` file, under the **Build and deployment settings**, toggle the override switch associated with the run command field. In the **Run command** field, enter:```bash

node .output/server/index.mjs`

```

#### In the **Advanced** section, click **Add Variable** and add a `NITRO_PRESET` variable set to `koyeb`.

#### Name the App.

#### Click the **Deploy** button.
::

## Using the Koyeb CLI

::steps{level="4"}
#### Follow the instructions targeting your operating system to [install the Koyeb CLI client](https://www.koyeb.com/docs/cli/installation){rel=""nofollow""} with an installer. Alternatively, visit the [releases page on GitHub](https://github.com/koyeb/koyeb-cli/releases){rel=""nofollow""} to directly download required files.

#### Create a Koyeb API access token by visiting the [API settings for your organization](https://app.koyeb.com/settings/api){rel=""nofollow""} in the Koyeb control panel.

#### Log into your account with the Koyeb CLI by typing:```bash
koyeb login
```:br Paste your API credentials when prompted.

#### Deploy your Nitro application from a GitHub repository with the following command. Be sure to substitute your own values for `<APPLICATION_NAME>`, `<YOUR_GITHUB_USERNAME>`, and `<YOUR_REPOSITORY_NAME>`:```bash
koyeb app init <APPLICATION_NAME> \
   --git github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME> \
   --git-branch main \
   --git-run-command "node .output/server/index.mjs" \
   --ports 3000:http \
   --routes /:3000 \
   --env PORT=3000 \
   --env NITRO_PRESET=koyeb
```

::

## Using a docker container

::steps{level="4"}

#### Create a `.dockerignore` file in the root of your project and add the following lines:```text

Dockerfile
.dockerignore
node_modules
npm-debug.log
.nitro
.output
.git
dist
README.md

```

#### Add a `Dockerfile` to the root of your project:```text
FROM node:18-alpine AS base

FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build && npm cache clean --force

FROM base AS runner
WORKDIR /app
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nitro
COPY --from=builder /app .
USER nitro
EXPOSE 3000
ENV PORT 3000
CMD ["npm", "run", "start"]
```

::

The Dockerfile above provides the minimum requirements to run the Nitro application. You can easily extend it depending on your needs.
You will then need to push your Docker image to a registry. You can use [Docker Hub](https://hub.docker.com/){rel="&#x22;nofollow&#x22;"} or [GitHub Container Registry](https://docs.github.com/en/packages/guides/about-github-container-registry){rel="&#x22;nofollow&#x22;"} for example.
In the Koyeb control panel, use the image and the tag field to specify the image you want to deploy.
You can also use the [Koyeb CLI](https://www.koyeb.com/docs/build-and-deploy/cli/installation){rel="&#x22;nofollow&#x22;"}
Refer to the Koyeb [Docker documentation](https://www.koyeb.com/docs/build-and-deploy/prebuilt-docker-images){rel="&#x22;nofollow&#x22;"} for more information.

# Netlify

**Preset:** `netlify`

:read-more{title="Netlify Functions" to="https://www.netlify.com/platform/core/functions/"}

::note
Integration with this provider is possible with [zero configuration](https://nitro.build/deploy/#zero-config-providers).
::

Normally, the deployment to Netlify does not require any configuration.
Nitro will auto-detect that you are in a [Netlify](https://www.netlify.com){rel="&#x22;nofollow&#x22;"} build environment and build the correct version of your server.

To enabling Netlify Functions 2.0 and using its features (e.g. streaming responses and [Netlify Blobs](https://docs.netlify.com/blobs/overview/){rel="&#x22;nofollow&#x22;"}), you need a compatibility date set to `2024-05-07` or later in your nitro configuration file.

::code-group

```ts [nitro.config.ts]
export default defineNitroConfig({
    compatibilityDate: "2024-05-07",
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
    compatibilityDate: "2024-05-07",
})
```

::

For new sites, Netlify will detect that you are using Nitro and set the publish directory to `dist` and build command to `npm run build`.

If you are upgrading an existing site you should check these and update them if needed.

If you want to add custom redirects, you can do so with [`routeRules`](https://nitro.build/config#routerules) or by adding a [`_redirects`](https://docs.netlify.com/routing/redirects/#syntax-for-the-redirects-file){rel="&#x22;nofollow&#x22;"} file to your `public` directory.

For deployment, just push to your git repository [as you would normally do for Netlify](https://docs.netlify.com/configure-builds/get-started/){rel="&#x22;nofollow&#x22;"}.

::note{type="note"}
Make sure the publish directory is set to `dist` when creating a new project.
::

## Netlify edge functions

**Preset:** `netlify_edge`

Netlify Edge Functions use Deno and the powerful V8 JavaScript runtime to let you run globally distributed functions for the fastest possible response times.

:read-more{title="Netlify Edge functions" to="https://docs.netlify.com/edge-functions/overview/"}

Nitro output can directly run the server at the edge. Closer to your users.

::note{type="note"}
Make sure the publish directory is set to `dist` when creating a new project.
::

## On-demand builders

**Preset:** `netlify_builder`

::warning
**Note:** This preset is deprecated. Instead, use the `netlify` preset with the `isr` route rule.
::

On-demand Builders are serverless functions used to generate web content as needed that’s automatically cached on Netlify’s Edge CDN. They enable you to build pages for your site when a user visits them for the first time and then cache them at the edge for subsequent visits.

:read-more{title="Netlify On-demand Builders" to="https://docs.netlify.com/configure-builds/on-demand-builders/"}

## Custom deploy configuration

You can provide additional deploy configuration using the `netlify` key inside `nitro.config`. It will be merged with built-in auto-generated config. Currently the only supported value is `images.remote_images`, for [configuring Netlify Image CDN](https://docs.netlify.com/image-cdn/create-integration/){rel="&#x22;nofollow&#x22;"}.

# Platform.sh

**Preset:** `platform_sh`

:read-more{to="https://platform.sh"}

## Setup

First, create a new project on platform.sh and link it to the repository you want to auto-deploy with.

Then in repository create `.platform.app.yaml` file:

```yaml [.platform.app.yaml]
name: nitro-app
type: 'nodejs:18'
disk: 128
web:
  commands:
    start: "node .output/server/index.mjs"
build:
  flavor: none
hooks:
  build: |
    corepack enable
    npx nypm install
    NITR_PRESET=platform_sh npm run build
mounts:
    '.data':
        source: local
        source_path: .data
```

:read-more{title="Complete list of all available properties" to="https://docs.platform.sh/create-apps/app-reference.html"}

:read-more{title="Complete list of all available properties" to="https://unjs.io/blog/2023-08-25-nitro-2.6#default-persistent-data-storage"}

# Render.com

**Preset:** `render_com`

:read-more{title="render.com" to="https://render.com"}

## Set up application

::steps{level="4"}

#### [Create a new Web Service](https://dashboard.render.com/select-repo?type=web){rel=""nofollow""} and select the repository that contains your code

#### Ensure the 'Node' environment is selected

#### Update the start command to `node .output/server/index.mjs`

#### Click 'Advanced' and add an environment variable with `NITRO_PRESET` set to `render_com`. You may also need to add a `NODE_VERSION` environment variable set to `18` for the build to succeed ([docs](https://render.com/docs/node-version){rel=""nofollow""})

#### Click 'Create Web Service'

::

## Infrastructure as Code (IaC)

1. Create a file called `render.yaml` with following content at the root of your repository.

> This file followed by [Infrastructure as Code](https://render.com/docs/infrastructure-as-code){rel="&#x22;nofollow&#x22;"} on Render

```yaml
services:
  - type: web
    name: <PROJECTNAME>
    env: node
    branch: main
    startCommand: node .output/server/index.mjs
    buildCommand: npx nypm install && npm run build
    envVars:
    - key: NITRO_PRESET
      value: render_com
```

1. [Create a new Blueprint Instance](https://dashboard.render.com/select-repo?type=blueprint){rel="&#x22;nofollow&#x22;"} and select the repository containing your `render.yaml` file.

You should be good to go!

# StormKit

**Preset:** `stormkit`

:read-more{title="Stormkit" to="https://www.stormkit.io"}

::note
Integration with [Stormkit](https://www.stormkit.io/){rel=""nofollow""} is possible with [zero configuration](https://nitro.build/deploy#zero-config-providers).
::

## Setup

Follow the steps to [create a new app](https://app.stormkit.io/apps/new){rel="&#x22;nofollow&#x22;"} on Stormkit.

![Create a new app on Stormkit](https://nitro.build/images/stormkit-new-app.png)

## Deployment

By default, Stormkit will deploy your apps automatically when you push changes to your main branch. But to trigger a manual deploy (for example, you might do this for the very first deployment), you may click `Deploy now`.

![Trigger a manual deploy with Deploy Now](https://nitro.build/images/stormkit-deploy.png)

# Vercel

**Preset:** `vercel`

:read-more{title="Vercel Framework Support" to="https://vercel.com/docs/frameworks"}

::note
Integration with this provider is possible with [zero configuration](https://nitro.build/deploy/#zero-config-providers).
::

## Getting started

Deploying to Vercel comes with the following features:

- [Preview deployments](https://vercel.com/docs/deployments/environments){rel="&#x22;nofollow&#x22;"}
- [Fluid compute](https://vercel.com/docs/fluid-compute){rel="&#x22;nofollow&#x22;"}
- [Observability](https://vercel.com/docs/observability){rel="&#x22;nofollow&#x22;"}
- [Vercel Firewall](https://vercel.com/docs/vercel-firewall){rel="&#x22;nofollow&#x22;"}

And much more. Learn more in [the Vercel documentation](https://vercel.com/docs){rel="&#x22;nofollow&#x22;"}.

### Deploy with Git

Vercel supports Nitro with zero-configuration. [Deploy Nitro to Vercel now](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnitro){rel="&#x22;nofollow&#x22;"}.

## Observability

Nitro (>=2.12) generates routing hints for [functions observability insights](https://vercel.com/docs/observability/insights#vercel-functions){rel="&#x22;nofollow&#x22;"}, providing a detailed view of performance broken down by route.

To enable this feature, ensure you are using a compatibility date of `2025-07-15` or later.

::CodeGroup

```ts [nitro.config.ts]
export default defineNitroConfig({
    compatibilityDate: "2025-07-15", // or "latest"
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
    compatibilityDate: "2025-07-15", // or "latest"
})
```

::

Framework integrations can use the `ssrRoutes` configuration to declare SSR routes. For more information, see [#3475](https://github.com/nitrojs/nitro/pull/3475){rel="&#x22;nofollow&#x22;"}.

## Bun runtime

:read-more{title="Vercel" to="https://vercel.com/docs/functions/runtimes/bun"}

You can use [Bun](https://bun.com){rel="&#x22;nofollow&#x22;"} instead of Node.js by specifying the runtime using the `vercel.functions` key inside `nitro.config`:

```ts [nitro.config.ts]
export default defineNitroConfig({
  vercel: {
    functions: {
      runtime: "bun1.x"
    }
  }
})
```

Alternatively, Nitro also detects Bun automatically if you specify a `bunVersion` property in your `vercel.json`:

```json [vercel.json]
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "bunVersion": "1.x"
}
```

## Custom build output configuration

You can provide additional [build output configuration](https://vercel.com/docs/build-output-api/v3){rel="&#x22;nofollow&#x22;"} using `vercel.config` key inside `nitro.config`. It will be merged with built-in auto-generated config.

## On-Demand incremental static regeneration (ISR)

On-demand revalidation allows you to purge the cache for an ISR route whenever you want, foregoing the time interval required with background revalidation.

To revalidate a page on demand:

- Create an Environment Variable which will store a revalidation secret
  - You can use the command `openssl rand -base64 32` or [Generate a Secret](https://generate-secret.vercel.app/32){rel="&#x22;nofollow&#x22;"} to generate a random value.
- Update your configuration: :code-group[```ts \[nitro.config.ts\]
  export default defineNitroConfig({
    vercel: {
      config: {
        bypassToken: process.env.VERCEL_BYPASS_TOKEN
      }
    }
  })

  ``````ts \[nuxt.config.ts\]
  export default defineNuxtConfig({
    nitro: {
      vercel: {
        config: {
          bypassToken: process.env.VERCEL_BYPASS_TOKEN
        }
      }
    }
  })
  ```]
- To trigger "On-Demand Incremental Static Regeneration (ISR)" and revalidate a path to a Prerender Function, make a GET or HEAD request to that path with a header of x-prerender-revalidate: `bypassToken`. When that Prerender Function endpoint is accessed with this header set, the cache will be revalidated. The next request to that function should return a fresh response.

### Fine-grained ISR config via route rules

By default, query paramas are ignored by cache.

You can pass an options object to `isr` route rule to configure caching behavior.

- `expiration`: Expiration time (in seconds) before the cached asset will be re-generated by invoking the Serverless Function. Setting the value to `false` (or `isr: true` route rule) means it will never expire.
- `group`: Group number of the asset. Prerender assets with the same group number will all be re-validated at the same time.
- `allowQuery`: List of query string parameter names that will be cached independently.
  - If an empty array, query values are not considered for caching.
  - If `undefined` each unique query value is cached independently.
  - For wildcard `/**` route rules, `url` is always added
- `passQuery`: When `true`, the query string will be present on the `request` argument passed to the invoked function. The `allowQuery` filter still applies.
- `exposeErrBody`: When `true`, expose the response body regardless of status code including error status codes. (default `false`

```ts
export default defineNitroConfig({
  routeRules: {
    "/products/**": {
      isr: {
        allowQuery: ["q"],
        passQuery: true,
        exposeErrBody: true
      },
    },
  },
});
```

## Vercel edge functions

**Preset:** `vercel_edge` (deprecated)

We recommend migrating to the default Node.js runtime and enabling [Fluid compute](https://vercel.com/docs/functions/fluid-compute){rel="&#x22;nofollow&#x22;"}.

# Zeabur

**Preset:** `zeabur`

:read-more{title="Zeabur" to="https://zeabur.com"}

::note
Integration with this provider is possible with [zero configuration](https://nitro.build/deploy/#zero-config-providers).
::

## Deploy using git

::steps{level="4"}

#### Push your code to your git repository (Currently only GitHub supported)

#### [Import your project](https://zeabur.com/docs/get-started){rel=""nofollow""} into Zeabur

#### Zeabur will detect that you are using Nitro and will enable the correct settings for your deployment

#### Your application is deployed

::

# Zerops

**Preset:** `zerops`

:read-more{title="zerops.io" to="https://zerops.io"}

::important
🚧 This preset is currently experimental.
::

Zerops supports deploying both static and server-side rendered apps with a simple configuration file in your project root.

## Starter templates

If you want to quckly get started with zerops and nitro you can use repositories [`zeropsio/recipe-nitro-nodejs`](https://github.com/zeropsio/recipe-nitro-nodejs){rel="&#x22;nofollow&#x22;"} and [`zeropsio/recipe-nitro-static`](https://github.com/zeropsio/recipe-nitro-static){rel="&#x22;nofollow&#x22;"} starter templates.

## Project setup

Projects and services can be added either through [project add wizard](https://app.zerops.io/dashboard/project-add){rel="&#x22;nofollow&#x22;"} or imported using `zerops-project-import.yml`.

::code-group

```yml [zerops-project-import.yml (node.js)]
project:
  name: nitro-app

services:
  - hostname: app
    type: nodejs@20
```

```yml [zerops-project-import.yml (static)]
project:
  name: nitro-app

services:
  - hostname: app
    type: static
```

::

Then create a `zerops.yml` config in your project root:

::code-group

```yml [zerops.yml (node.js)]
zerops:
  - setup: app
    build:
      base: nodejs@20
      envVariables:
        SERVER_PRESET: zerops
      buildCommands:
        - pnpm i
        - pnpm run build
      deployFiles:
        - .output
        - package.json
        - node_modules
    run:
      base: nodejs@20
      ports:
        - port: 3000
          httpSupport: true
      start: node .output/server/index.mjs
```

```yml [zerops.yml (static)]
zerops:
  - setup: app
    build:
      base: nodejs@20
      envVariables:
        SERVER_PRESET: zerops-static
      buildCommands:
        - pnpm i
        - pnpm build
      deployFiles:
        - .zerops/output/static/~
    run:
      base: static
```

::

Now you can trigger the [build & deploy pipeline using the Zerops CLI](https://nitro.build/#building-deploying-your-app) or by connecting the app service with your [GitHub](https://docs.zerops.io/references/github-integration/){rel="&#x22;nofollow&#x22;"} / [GitLab](https://docs.zerops.io/references/gitlab-integration){rel="&#x22;nofollow&#x22;"} repository from inside the service detail.

## Build and deploy

Open [Settings > Access Token Management](https://app.zerops.io/settings/token-management){rel="&#x22;nofollow&#x22;"} in the Zerops app and generate a new access token.

Log in using your access token with the following command:

:pm-x{command="@zerops/zcli login <token>"}

Navigate to the root of your app (where `zerops.yml` is located) and run the following command to trigger the deploy:

:pm-x{command="@zerops/zcli push"}

Your code can be deployed automatically on each commit or a new tag by connecting the service with your [GitHub](https://docs.zerops.io/references/gitlab-integration){rel="&#x22;nofollow&#x22;"} / [GitLab](https://docs.zerops.io/references/gitlab-integration){rel="&#x22;nofollow&#x22;"} repository. This connection can be set up in the service detail.

:read-more{title="Zerops Documentation" to="https://docs.zerops.io/"}

# Config

:read-more{to="https://nitro.build/guide/configuration"}

## General

### `preset`

Use `preset` option `NITRO_PRESET` environment variable for custom **production** preset.

Preset for development mode is always `nitro_dev` and default `node_server` for production building a standalone Node.js server.

The preset will automatically be detected when the `preset` option is not set and running in known environments.

### `logLevel`

- Default: `3`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"} (`1`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"} when the testing environment is detected)

Log verbosity level. See [consola](https://github.com/unjs/consola?tab=readme-ov-file#log-level){rel="&#x22;nofollow&#x22;"} for more information.

### `runtimeConfig`

- Default: `{ nitro: { ... }, ...yourOptions }`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}

Server runtime configuration.

**Note:**: `nitro` namespace is reserved.

### `compatibilityDate`

Deployment providers introduce new features that Nitro presets can leverage, but some of them need to be explicitly opted into.

Set it to latest tested date in `YYYY-MM-DD` format to leverage latest preset features.

If this configuration is not provided, Nitro will continue using the current (v2.9) behavior for presets and show a warning.

## Features

### `experimental`

- Default: `{}`

Enable experimental features.

#### `openAPI`

Enable `/_scalar`, `/_swagger` and `/_openapi.json` endpoints.

- Default: `false`

To define the OpenAPI specification on your routes, take a look at [defineRouteMeta](https://nitro.build/guide/routing#route-meta)

You can pass an object on the root level to modify your OpenAPI specification:

```js
openAPI: {
  meta: {
    title: 'My Awesome Project',
    description: 'This might become the next big thing.',
    version: '1.0'
  }
}
```

These routes are disabled by default in production. To enable them, use the `production` key.
`"runtime"` allows middleware usage, and `"prerender"` is the most efficient because the JSON response is constant.

```js
openAPI: {
    // IMPORTANT: make sure to protect OpenAPI routes if necessary!
    production: "runtime", // or "prerender"
}
```

If you like to customize the Scalar integration, you can [pass a configuration object](https://github.com/scalar/scalar){rel="&#x22;nofollow&#x22;"} like this:

```js
openAPI: {
  ui: {
    scalar: {
      theme: 'purple'
    }
  }
}
```

Or if you want to customize the endpoints:

```js
openAPI: {
  route: "/_docs/openapi.json",
  ui: {
    scalar: {
      route: "/_docs/scalar"
    },
    swagger: {
      route: "/_docs/swagger"
    }
  }
}
```

#### `wasm`

Enable WASM support

#### `legacyExternals`

When enabled, legacy (unstable) experimental rollup externals algorithm will be used.

### `future`

- Default: `{}`

New features pending for a major version to avoid breaking changes.

#### `nativeSWR`

Uses built-in SWR functionality (using caching layer and storage) for Netlify and Vercel presets instead of falling back to ISR behavior.

### `storage`

- Default: `{}`

Storage configuration, read more in the [Storage Layer](https://nitro.build/guide/storage) section.

### `timing`

- Default: `false`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}

Enable timing information:

- Nitro startup time log
- `Server-Timing` header on HTTP responses

### `renderer`

Path to main render (file should export an event handler as default)

### `serveStatic`

- Type: `boolean` | `'node'`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"} | `'deno'`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}
- Default: depends of the deployment preset used.

Serve `public/` assets in production.

**Note:** It is highly recommended that your edge CDN (Nginx, Apache, Cloud) serves the `.output/public/` directory instead of enabling compression and higher lever caching.

### `noPublicDir`

- Default: `false`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}

If enabled, disabled `.output/public` directory creation. Skipping to copy `public/` dir and also disables pre-rendering.

### `publicAssets`

Public asset directories to serve in development and bundle in production.

If a `public/` directory is detected, it will be added by default, but you can add more by yourself too!

It's possible to set Cache-Control headers for assets using the `maxAge` option:

```ts
  publicAssets: [
    {
      baseURL: "images",
      dir: "public/images",
      maxAge: 60 * 60 * 24 * 7, // 7 days
    },
  ],
```

The config above generates the following header in the assets under `public/images/` folder:

`cache-control: public, max-age=604800, immutable`

The `dir` option is where your files live on your file system; the `baseURL` option is the folder they will be accessible from when served/bundled.

### `compressPublicAssets`

- Default: `{ gzip: false, brotli: false }`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}

If enabled, Nitro will generate a pre-compressed (gzip and/or brotli) version of supported types of public assets and prerendered routes
larger than 1024 bytes into the public directory. The best compression level is used. Using this option you can support zero overhead asset compression without using a CDN.

List of compressible MIME types:

- `application/dash+xml`
- `application/eot`
- `application/font`
- `application/font-sfnt`
- `application/javascript`
- `application/json`
- `application/opentype`
- `application/otf`
- `application/pdf`
- `application/pkcs7-mime`
- `application/protobuf`
- `application/rss+xml`
- `application/truetype`
- `application/ttf`
- `application/vnd.apple.mpegurl`
- `application/vnd.mapbox-vector-tile`
- `application/vnd.ms-fontobject`
- `application/wasm`
- `application/xhtml+xml`
- `application/xml`
- `application/x-font-opentype`
- `application/x-font-truetype`
- `application/x-font-ttf`
- `application/x-httpd-cgi`
- `application/x-javascript`
- `application/x-mpegurl`
- `application/x-opentype`
- `application/x-otf`
- `application/x-perl`
- `application/x-ttf`
- `font/eot`
- `font/opentype`
- `font/otf`
- `font/ttf`
- `image/svg+xml`
- `text/css`
- `text/csv`
- `text/html`
- `text/javascript`
- `text/js`
- `text/plain`
- `text/richtext`
- `text/tab-separated-values`
- `text/xml`
- `text/x-component`
- `text/x-java-source`
- `text/x-script`
- `vnd.apple.mpegurl`

### `serverAssets`

Assets can be accessed in server logic and bundled in production. [Read more](https://nitro.build/guide/assets#server-assets).

### `devServer`

- Default: `{ watch: [] }`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"}

Dev server options. You can use `watch` to make the dev server reload if any file changes in specified paths.

### `watchOptions`

Watch options for development mode. See [chokidar](https://github.com/paulmillr/chokidar){rel="&#x22;nofollow&#x22;"} for more information.

### `imports`

Auto import options. See [unimport](https://github.com/unjs/unimport){rel="&#x22;nofollow&#x22;"} for more information.

### `plugins`

- Default: `[]`

An array of paths to nitro plugins. They will be executed by order on the first initialization.

Note that Nitro auto-register the plugins in the `plugins/` directory, [learn more](https://nitro.build/guide/plugins).

### `virtual`

- Default: `{}`

A map from dynamic virtual import names to their contents or an (async) function that returns it.

## Routing

### `baseURL`

Default: `/`{.shiki,shiki-themes,github-light,github-dark,github-dark lang="ts"} (or `NITRO_APP_BASE_URL` environment variable if provided)

Server's main base URL.

### `apiBaseURL`

- Default : `/api`

Changes the default api base URL prefix.

### `handlers`

Server handlers and routes.

If `server/routes/`, `server/api/` or `server/middleware/` directories exist, they will be automatically added to the handlers array.

### `devHandlers`

Regular handlers refer to the path of handlers to be imported and transformed by rollup.

There are situations in that we directly want to provide a handler instance with programmatic usage.

We can use `devHandlers` but note that they are **only available in development mode** and **not in production build**.

For example:

```ts
import { defineEventHandler } from 'h3'

export default defineNitroConfig({
  devHandlers: [
    {
      route: '/',
      handler: defineEventHandler((event) => {
       console.log(event)
      })
    }
  ]
})
```

::note{type="info"}
Note that `defineEventHandler` is a helper function from [`h3`](https://v1.h3.dev){rel=""nofollow""} library.
::

### `devProxy`

Proxy configuration for development server.

You can use this option to override development server routes and proxy-pass requests.

```js
{
  devProxy: {
    '/proxy/test': 'http://localhost:3001',
    '/proxy/example': { target: 'https://example.com', changeOrigin: true }
  }
}
```

See [httpxy](https://github.com/unjs/httpxy){rel="&#x22;nofollow&#x22;"} for all available target options.

### `errorHandler`

Path to a custom runtime error handler. Replacing nitro's built-in error page.
The error handler is given an `H3Error` and `H3Event`. If the handler returns a promise it is awaited.
The handler is expected to send a response of its own.
Below is an example where a plain-text response is returned using h3's functions.

**Example:**

::CodeGroup

```js [nitro.config]
export default defineNitroConfig({
  errorHandler: "~/error",
});
```

```js [error.ts]
export default defineNitroErrorHandler((error, event) => {
  setResponseHeader(event, 'Content-Type', 'text/plain')
  return send(event, '[custom error handler] ' + error.stack)
});
```

::

### `routeRules`

**🧪 Experimental!**

Route options. It is a map from route pattern (following [radix3](https://github.com/unjs/rou3/tree/radix3#route-matcher){rel="&#x22;nofollow&#x22;"}) to route options.

When `cache` option is set, handlers matching pattern will be automatically wrapped with `defineCachedEventHandler`.

See the [Cache API](https://nitro.build/guide/cache) for all available cache options.

::note
`swr: true|number` is shortcut for `cache: { swr: true, maxAge: number }`
::

**Example:**

```js
routeRules: {
  '/blog/**': { swr: true },
  '/blog/**': { swr: 600 },
  '/blog/**': { static: true },
  '/blog/**': { cache: { /* cache options*/ } },
  '/assets/**': { headers: { 'cache-control': 's-maxage=0' } },
  '/api/v1/**': { cors: true, headers: { 'access-control-allow-methods': 'GET' } },
  '/old-page': { redirect: '/new-page' }, // uses status code 307 (Temporary Redirect)
  '/old-page2': { redirect: { to:'/new-page2', statusCode: 301 } },
  '/old-page/**': { redirect: '/new-page/**' },
  '/proxy/example': { proxy: 'https://example.com' },
  '/proxy/**': { proxy: '/api/**' },
}
```

### `prerender`

Default:

```ts
{
  autoSubfolderIndex: true,
  concurrency: 1,
  interval: 0,
  failOnError: false,
  crawlLinks: false,
  ignore: [],
  routes: [],
  retry: 3,
  retryDelay: 500
}
```

Prerendered options. Any route specified will be fetched during the build and copied to the `.output/public` directory as a static asset.

Any route (string) that starts with a prefix listed in `ignore` or matches a regular expression or function will be ignored.

If `crawlLinks` option is set to `true`, nitro starts with `/` by default (or all routes in `routes` array) and for HTML pages extracts `<a>` tags and prerender them as well.

You can set `failOnError` option to `true` to stop the CI when an error if Nitro could not prerender a route.

The `interval` and `concurrency` options lets you control the speed of pre-rendering, can be useful to avoid hitting some rate-limit if you call external APIs.

Set `autoSubfolderIndex` lets you control how to generate the files in the `.output/public` directory:

```bash
# autoSubfolderIndex: true (default)
/about -> .output/public/about/index.html
# autoSubfolderIndex: false
/about -> .output/public/about.html
```

This option is useful when your hosting provider does not give you an option regarding the trailing slash.

The prerenderer will attempt to render pages 3 times with a delay of 500ms. Use `retry` and `retryDelay` to change this behavior.

## Directories

### `workspaceDir`

Project workspace root directory.

The workspace (e.g. pnpm workspace) directory is automatically detected when the `workspaceDir` option is not set.

### `rootDir`

Project main directory.

### `srcDir`

- Default: (same as `rootDir`)

Project source directory. Same as `rootDir` unless specified.
Root directory for `api`, `routes`, `plugins`, `utils`, `public`, `middleware`, `assets`, and `tasks` folders.

### `scanDirs`

- Default: (source directory when empty array)

List of directories to scan and auto-register files, such as API routes.

### `apiDir`

- Default : `api`

Defines a different directory to scan for api route handlers.

### `routesDir`

- Default : `routes`

Defines a different directory to scan for route handlers.

### `buildDir`

- Default: `.nitro`

nitro's temporary working directory for generating build-related files.

### `output`

- Default: `{ dir: '.output', serverDir: '.output/server', publicDir: '.output/public' }`

Output directories for production bundle.

## Advanced

### `dev`

- Default: `true` for development and `false` for production.

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

### `typescript`

Default: `{ generateTsConfig: true }`

### `nodeModulesDirs`

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

Additional `node_modules` to search when resolving a module. By default user directory is added.

### `hooks`

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

nitro hooks. See [hookable](https://github.com/unjs/hookable){rel="&#x22;nofollow&#x22;"} for more information.

### `commands`

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

Preview and deploy command hints are usually filled by deployment presets.

### `devErrorHandler`

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

A custom error handler function for development errors.

## Rollup

### `rollupConfig`

Additional rollup configuration.

### `entry`

Rollup entry.

### `unenv`

Options for [unenv](https://github.com/unjs/unenv/){rel="&#x22;nofollow&#x22;"} preset.

### `alias`

Rollup aliases options.

### `minify`

- Default: `false`

Minify bundle.

### `inlineDynamicImports`

Avoid creating chunks.

### `sourceMap`

Enable source map generation. See [options](https://rollupjs.org/configuration-options/#output-sourcemap){rel="&#x22;nofollow&#x22;"}

- Default: `true`

### `node`

Specify whether the build is used for Node.js or not. If set to `false`, nitro tries to mock Node.js dependencies using [unenv](https://github.com/unjs/unenv){rel="&#x22;nofollow&#x22;"} and adjust its behavior.

### `analyze`

If enabled, will analyze server bundle after build using [rollup-plugin-visualizer](https://github.com/btd/rollup-plugin-visualizer){rel="&#x22;nofollow&#x22;"}. You can also pass your custom options.

### `moduleSideEffects`

Default: `['unenv/polyfill/', 'node-fetch-native/polyfill']`

Rollup specific option. Specifies module imports that have side-effects

### `replace`

Rollup specific option.

### `commonJS`

Rollup specific option. Specifies additional configuration for the rollup CommonJS plugin.

## Preset options

### `firebase`

The options for the firebase functions preset. See [Preset Docs](https://nitro.build/deploy/providers/firebase#options)

### `vercel`

The options for the vercel preset. See [Preset Docs](https://nitro.build/deploy/providers/vercel)

### `cloudflare`

The options for the cloudflare preset. See [Preset Docs](https://nitro.build/deploy/providers/cloudflare)
