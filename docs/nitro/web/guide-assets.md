# Source: https://nitro.build/guide/assets

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

# Assets 

</div>

<div>

## [[[]]Public assets](#public-assets) 

Nitro handles assets via the `server/public/` directory.

All assets in `server/public/` directory will be automatically served. This means that you can access them directly from the browser without any special configuration.

[]

``` 
server/
  public/
    image.png     <-- /image.png
    video.mp4     <-- /video.mp4
    robots.txt    <-- /robots.txt
package.json
nitro.config.ts
```

### [[[]]Production public assets](#production-public-assets) 

When building your Nitro app, the `server/public/` directory will be copied to `.output/public/` and a manifest with metadata will be created and embedded in the server bundle.

[]

``` 
,
  "/robots.txt": ,
  "/video.mp4": 
}
```

This allows Nitro to know the public assets without scanning the directory, giving high performance with caching headers.

## [[[]]Server assets](#server-assets) 

All assets in `server/assets/` directory will be added to the server bundle. After building your application, you can find them in the `.output/server/chunks/raw/` directory. Be careful with the size of your assets, as they will be bundled with the server bundle.

They can be addressed by the `assets:server` mount point using the [storage layer](/guide/storage).

For example, you could store a json file in `server/assets/data.json` and retrieve it in your handler:

[]

``` 
export default defineEventHandler(async () => )
```

### [[[]]Custom server assets](#custom-server-assets) 

In order to add assets from a custom directory, you will need to define a path in your nitro config. This allows you to add assets from a directory outside of the `server/assets/` directory.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(]
})
```

[]

``` 
export default defineNuxtConfig(]
  }
})
```

You could want to add a directory (`server/templates/`) with html templates for example.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(]
})
```

[]

``` 
export default defineNuxtConfig(]
  }
})
```

Then you can use the `assets:templates` base to retrieve your assets.

[][handlers/success.ts]

[]

``` 
export default defineEventHandler(async (event) => )
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/1.guide/8.assets.md)

[](/guide/fetch)

[]

Fetch

Nitro provides a built-in fetch API that can be used to get data from server endpoints or from other sources. It\'s built on top of the ofetch.

[](/guide/plugins)

[]

Plugins

Use plugins to extend Nitro\'s runtime behavior.

[On this page][[]]

[On this page][[]]

-   [[Public assets]](#public-assets)
    -   [[Production public assets]](#production-public-assets)
-   [[Server assets]](#server-assets)
    -   [[Custom server assets]](#custom-server-assets)