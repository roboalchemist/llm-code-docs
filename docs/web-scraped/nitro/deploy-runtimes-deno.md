# Source: https://nitro.build/deploy/runtimes/deno

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

-   [[][Overview]](/deploy)
-   [[][Edge Workers]](/deploy/workers)
-   [Runtimes]

    ::: 
    -   [[][Node.js]](/deploy/runtimes/node)
    -   [[][WinterJS]](/deploy/runtimes/_winterjs)
    -   [[][Bun]](/deploy/runtimes/bun)
    -   [[][Deno]](/deploy/runtimes/deno)
    :::
-   [[][Custom Preset]](/deploy/custom-presets)
-   [Providers]

    ::: 
    -   [[Alwaysdata]](/deploy/providers/alwaysdata)
    -   [[AWS Lambda]](/deploy/providers/aws)
    -   [[AWS Amplify]](/deploy/providers/aws-amplify)
    -   [[Azure]](/deploy/providers/azure)
    -   [[Cleavr]](/deploy/providers/cleavr)
    -   [[Cloudflare]](/deploy/providers/cloudflare)
    -   [[Deno Deploy]](/deploy/providers/deno-deploy)
    -   [[DigitalOcean]](/deploy/providers/digitalocean)
    -   [[Edgio]](/deploy/providers/edgio)
    -   [[Firebase]](/deploy/providers/firebase)
    -   [[Flightcontrol]](/deploy/providers/flightcontrol)
    -   [[Genezio]](/deploy/providers/genezio)
    -   [[GitHub Pages]](/deploy/providers/github-pages)
    -   [[GitLab Pages]](/deploy/providers/gitlab-pages)
    -   [[Heroku]](/deploy/providers/heroku)
    -   [[IIS]](/deploy/providers/iis)
    -   [[Koyeb]](/deploy/providers/koyeb)
    -   [[Netlify]](/deploy/providers/netlify)
    -   [[Platform.sh]](/deploy/providers/platform-sh)
    -   [[Render.com]](/deploy/providers/render)
    -   [[StormKit]](/deploy/providers/stormkit)
    -   [[Vercel]](/deploy/providers/vercel)
    -   [[Zeabur]](/deploy/providers/zeabur)
    -   [[Zerops]](/deploy/providers/zerops)
    :::

1.  [[Runtimes]]

<div>

# Deno 

Run Nitro apps with Deno runtime.

</div>

<div>

**Preset:** `deno_server`

You can build your Nitro server using Node.js to run within [Deno Runtime](https://deno.com/runtime) in a custom server.

[]

``` 
# Build with the deno NITRO preset
NITRO_PRESET=deno_server npm run build

# Start production server
deno run --unstable --allow-net --allow-read --allow-env .output/server/index.ts
```

To enabling Node.js compatibility, you need to upgrade to Deno v2, and a compatibility date set to `2025-01-30` or later in your nitro configuration file.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig()
```

[]

``` 
export default defineNuxtConfig()
```

## [[[]]Deno Deploy](#deno-deploy) 

[[]](/deploy/providers/deno-deploy)[] Read more in [Deploy \> Providers \> Deno Deploy].

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/10.runtimes/deno.md)

[](/deploy/runtimes/bun)

[]

Bun

Run Nitro apps with Bun runtime.

[](/deploy/custom-presets)

[]

Custom Preset

If you want to use a provider that Nitro doesn\'t support, or want to modify an existing one, you can create a local custom preset in your project.

[On this page][[]]

[On this page][[]]

-   [[Deno Deploy]](#deno-deploy)