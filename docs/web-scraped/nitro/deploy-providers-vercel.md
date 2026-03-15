# Source: https://nitro.build/deploy/providers/vercel

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

1.  [[Providers]]

<div>

# Vercel 

Deploy Nitro apps to Vercel.

</div>

<div>

**Preset:** `vercel`

[[]](https://vercel.com/docs/frameworks)[][] Read more in [Vercel Framework Support].

[]Integration with this provider is possible with [zero configuration](/deploy/#zero-config-providers).

## [[[]]Getting started](#getting-started) 

Deploying to Vercel comes with the following features:

-   [Preview deployments](https://vercel.com/docs/deployments/environments)
-   [Fluid compute](https://vercel.com/docs/fluid-compute)
-   [Observability](https://vercel.com/docs/observability)
-   [Vercel Firewall](https://vercel.com/docs/vercel-firewall)

And much more. Learn more in [the Vercel documentation](https://vercel.com/docs).

### [[[]]Deploy with Git](#deploy-with-git) 

Vercel supports Nitro with zero-configuration. [Deploy Nitro to Vercel now](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnitro).

## [[[]]Observability](#observability) 

Nitro (\>=2.12) generates routing hints for [functions observability insights](https://vercel.com/docs/observability/insights#vercel-functions), providing a detailed view of performance broken down by route.

To enable this feature, ensure you are using a compatibility date of `2025-07-15` or later.

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

Framework integrations can use the `ssrRoutes` configuration to declare SSR routes. For more information, see [#3475](https://github.com/nitrojs/nitro/pull/3475).

## [[[]]Bun runtime](#bun-runtime) 

[[]](https://vercel.com/docs/functions/runtimes/bun)[][] Read more in [Vercel].

You can use [Bun](https://bun.com) instead of Node.js by specifying the runtime using the `vercel.functions` key inside `nitro.config`:

[][nitro.config.ts]

[]

``` 
export default defineNitroConfig(
  }
})
```

Alternatively, Nitro also detects Bun automatically if you specify a `bunVersion` property in your `vercel.json`:

[][vercel.json]

[]

``` 

```

## [[[]]Custom build output configuration](#custom-build-output-configuration) 

You can provide additional [build output configuration](https://vercel.com/docs/build-output-api/v3) using `vercel.config` key inside `nitro.config`. It will be merged with built-in auto-generated config.

## [[[]]On-Demand incremental static regeneration (ISR)](#on-demand-incremental-static-regeneration-isr) 

On-demand revalidation allows you to purge the cache for an ISR route whenever you want, foregoing the time interval required with background revalidation.

To revalidate a page on demand:

-   Create an Environment Variable which will store a revalidation secret
    -   You can use the command `openssl rand -base64 32` or [Generate a Secret](https://generate-secret.vercel.app/32) to generate a random value.
-   Update your configuration:

    ::: 
    ::: 
    [][nitro.config.ts]
    [][nuxt.config.ts]
    :::

    ::: 
    []
    ``` 
    export default defineNitroConfig(
      }
    })
    ```
    :::

    ::: 
    []
    ``` 
    export default defineNuxtConfig(
        }
      }
    })
    ```
    :::
    :::
-   To trigger \"On-Demand Incremental Static Regeneration (ISR)\" and revalidate a path to a Prerender Function, make a GET or HEAD request to that path with a header of x-prerender-revalidate: `bypassToken`. When that Prerender Function endpoint is accessed with this header set, the cache will be revalidated. The next request to that function should return a fresh response.

### [[[]]Fine-grained ISR config via route rules](#fine-grained-isr-config-via-route-rules) 

By default, query paramas are ignored by cache.

You can pass an options object to `isr` route rule to configure caching behavior.

-   `expiration`: Expiration time (in seconds) before the cached asset will be re-generated by invoking the Serverless Function. Setting the value to `false` (or `isr: true` route rule) means it will never expire.
-   `group`: Group number of the asset. Prerender assets with the same group number will all be re-validated at the same time.
-   `allowQuery`: List of query string parameter names that will be cached independently.
    -   If an empty array, query values are not considered for caching.
    -   If `undefined` each unique query value is cached independently.
    -   For wildcard `/**` route rules, `url` is always added
-   `passQuery`: When `true`, the query string will be present on the `request` argument passed to the invoked function. The `allowQuery` filter still applies.

[]

``` 
export default defineNitroConfig(,
    },
  },
});
```

## [[[]]Vercel edge functions](#vercel-edge-functions) 

**Preset:** `vercel_edge` (deprecated)

We recommend migrating to the default Node.js runtime and enabling [Fluid compute](https://vercel.com/docs/functions/fluid-compute).

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/vercel.md)

[](/deploy/providers/stormkit)

[]

StormKit

Deploy Nitro apps to StormKit.

[](/deploy/providers/zeabur)

[]

Zeabur

Deploy Nitro apps to Zeabur.

[On this page][[]]

[On this page][[]]

-   [[Getting started]](#getting-started)
    -   [[Deploy with Git]](#deploy-with-git)
-   [[Observability]](#observability)
-   [[Bun runtime]](#bun-runtime)
-   [[Custom build output configuration]](#custom-build-output-configuration)
-   [[On-Demand incremental static regeneration (ISR)]](#on-demand-incremental-static-regeneration-isr)
    -   [[Fine-grained ISR config via route rules]](#fine-grained-isr-config-via-route-rules)
-   [[Vercel edge functions]](#vercel-edge-functions)