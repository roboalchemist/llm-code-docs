# Source: https://nitro.build/guide/database

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

# SQL Database 

Nitro provides a built-in and lightweight SQL database layer.

</div>

<div>

The default database connection is **preconfigured** with [SQLite](https://db0.unjs.io/connectors/sqlite) and works out of the box for development mode and any Node.js compatible production deployments. By default, data will be stored in `.data/db.sqlite3`.

[] You can change default connection or define more connections to any of the [supported databases](https://db0.unjs.io/connectors/sqlite).

[] You can integrate database instance to any of the [supported ORMs](https://db0.unjs.io/integrations).

[[]](https://db0.unjs.io)[][] Read more in [DB0 Documentation].

## [[[]]Opt-in to the experimental feature](#opt-in-to-the-experimental-feature) 

[] Database support is currently experimental. Refer to the [db0 issues](https://github.com/unjs/db0/issues) for status and bug report.

In order to enable database layer you need to enable experimental feature flag.

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

## [[[]]Usage](#usage) 

[][index.ts]

[]

``` 
export default defineEventHandler(async () => , 'John', 'Doe', '')`;

  // Query for users
  const  = await db.sql`SELECT * FROM users WHERE id = $`;

  return ;
});
```

## [[[]]Configuration](#configuration) 

You can configure database connections using `database` config:

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(
    },
    users: 
    }
  }
})
```

[]

``` 
export default defineNuxtConfig(
      },
      users: 
      }
    }
  }
})
```

[] You can use the `devDatabase` config to overwrite the database configuration only for development mode.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/5.database.md)

[](/guide/storage)

[]

KV Storage

Nitro provides a built-in storage layer that can abstract filesystem or database or any other data source.

[](/guide/cache)

[]

Cache

Nitro provides a caching system built on top of the storage layer.

[On this page][[]]

[On this page][[]]

-   [[Opt-in to the experimental feature]](#opt-in-to-the-experimental-feature)
-   [[Usage]](#usage)
-   [[Configuration]](#configuration)