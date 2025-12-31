# Source: https://nitro.build/guide/tasks

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

# Tasks 

Nitro tasks allow on-off operations in runtime.

</div>

<div>

## [[[]]Opt-in to the experimental feature](#opt-in-to-the-experimental-feature) 

[] Tasks support is currently experimental. See [nitrojs/nitro#1974](https://github.com/nitrojs/nitro/issues/1974) for the relevant discussion.

In order to use the tasks API you need to enable experimental feature flag.

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
  }
})
```

## [[[]]Define tasks](#define-tasks) 

Tasks can be defined in `server/tasks/[name].ts` files.

Nested directories are supported. The task name will be joined with `:`. (Example: `server/tasks/db/migrate.ts`task name will be `db:migrate`)

**Example:**

[][server/tasks/db/migrate.ts]

[]

``` 
export default defineTask(,
  run() ;
  },
});
```

## [[[]]Scheduled tasks](#scheduled-tasks) 

You can define scheduled tasks using Nitro configuration to automatically run after each period of time.

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
  }
})
```

[] You can use [crontab.guru](https://crontab.guru/) to easily generate and understand cron tab patterns.

### [[[]]Platform support](#platform-support) 

-   `dev`, `node-server`, `bun` and `deno-server` presets are supported with [croner](https://croner.56k.guru/) engine.
-   `cloudflare_module` preset have native integration with [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/). Make sure to configure wrangler to use exactly same patterns you define in `scheduledTasks` to be matched.
-   More presets (with native primitives support) are planned to be supported!

## [[[]]Programmatically run tasks](#programmatically-run-tasks) 

To manually run tasks, you can use `runTask(name, )` utility.

**Example:**

[][server/api/migrate.ts]

[]

``` 
export default eventHandler(async (event) => ;
  const  = await runTask("db:migrate", );

  return ;
});
```

## [[[]]Run tasks with dev server](#run-tasks-with-dev-server) 

Nitro\'s built-in dev server exposes tasks to be easily executed without programmatic usage.

### [[[]]Using API routes](#using-api-routes) 

#### [`/_nitro/tasks`](#_nitrotasks) 

This endpoint returns a list of available task names and their meta.

[]

``` 
// [GET] /_nitro/tasks
,
     "cms:update": 
  },
  "scheduledTasks": [
    
  ]
}
```

#### [`/_nitro/tasks/:name`](#_nitrotasksname) 

This endpoint executes a task. You can provide a payload using both query parameters and body JSON payload. The payload sent in the JSON body payload must be under the `"payload"` property.

[][server/tasks/echo/payload.ts]

[GET]

[POST]

[]

``` 
export default defineTask(,
  run() ;
  },
});
```

[]

``` 
// [GET] /_nitro/tasks/echo:payload?field=value&array=1&array=2

```

[]

``` 
/**
 * [POST] /_nitro/tasks/echo:payload?field=value
 * body: 
 *   }
 * }
 */

}
```

[] The JSON payload included in the body will overwrite the keys present in the query params.

### [[[]]Using CLI](#using-cli) 

[] It is only possible to run these commands while the **dev server is running**. You should run them in a second terminal.

#### [List tasks](#list-tasks) 

[]

``` 
nitro task list
```

#### [Run a task](#run-a-task) 

[]

``` 
nitro task run db:migrate --payload ""
```

## [[[]]Notes](#notes) 

### [[[]]Concurrency](#concurrency) 

Each task can have **one running instance**. Calling a task of same name multiple times in parallel, results in calling it once and all callers will get the same return value.

[] Nitro tasks can be running multiple times and in parallel.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/10.tasks.md)

[](/guide/utils)

[]

Server Utils

Enjoy auto-imported server utils and extend with your own utils.

[](/guide/routing)

[]

Server Routes

Nitro supports filesystem routing to automatically map files to h3 routes.

[On this page][[]]

[On this page][[]]

-   [[Opt-in to the experimental feature]](#opt-in-to-the-experimental-feature)
-   [[Define tasks]](#define-tasks)
-   [[Scheduled tasks]](#scheduled-tasks)
    -   [[Platform support]](#platform-support)
-   [[Programmatically run tasks]](#programmatically-run-tasks)
-   [[Run tasks with dev server]](#run-tasks-with-dev-server)
    -   [[Using API routes]](#using-api-routes)
    -   [[Using CLI]](#using-cli)
-   [[Notes]](#notes)
    -   [[Concurrency]](#concurrency)