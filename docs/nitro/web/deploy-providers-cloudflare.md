# Source: https://nitro.build/deploy/providers/cloudflare

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

# Cloudflare 

Deploy Nitro apps to Cloudflare.

</div>

<div>

## [[[]]Cloudflare Workers](#cloudflare-workers) 

**Preset:** `cloudflare_module`

[[]](https://developers.cloudflare.com/workers/)[][] Read more in [Cloudflare Workers].

[]Integration with this provider is possible with [zero configuration](/deploy#zero-config-providers) supporting [workers builds (beta)](https://developers.cloudflare.com/workers/ci-cd/builds/).

[]To use Workers with Static Assets, you need a Nitro compatibility date set to `2024-09-19` or later.

The following shows an example `nitro.config.ts` file for deploying a Nitro app to Cloudflare Workers.

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

By setting `deployConfig: true`, Nitro will automatically generate a `wrangler.json` for you with the correct configuration. If you need to add [Cloudflare Workers configuration](https://developers.cloudflare.com/workers/wrangler/configuration/), such as [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/), you can either:

-   Set these in your Nitro config under the `cloudflare:  }`. This has the same type as `wrangler.json`.
-   Provide your own `wrangler.json`. Nitro will merge your config with the appropriate settings, including pointing to the build output.

### [[[]]Local Preview](#local-preview) 

You can use [Wrangler](https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler) to preview your app locally:

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

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx wrangler dev
```

[]

``` 
yarn dlx wrangler dev
```

[]

``` 
pnpm dlx wrangler dev
```

[]

``` 
bunx wrangler dev
```

[]

``` 
deno run -A npm:wrangler dev
```

### [[[]]Manual Deploy](#manual-deploy) 

After having built your application you can manually deploy it with Wrangler.

First make sure to be logged into your Cloudflare account:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx wrangler login
```

[]

``` 
yarn dlx wrangler login
```

[]

``` 
pnpm dlx wrangler login
```

[]

``` 
bunx wrangler login
```

[]

``` 
deno run -A npm:wrangler login
```

Then you can deploy the application with:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx wrangler deploy
```

[]

``` 
yarn dlx wrangler deploy
```

[]

``` 
pnpm dlx wrangler deploy
```

[]

``` 
bunx wrangler deploy
```

[]

``` 
deno run -A npm:wrangler deploy
```

### [[[]]Runtime Hooks](#runtime-hooks) 

You can use [runtime hooks](/guide/plugins#nitro-runtime-hooks) below in order to extend [Worker handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/).

[[]](/guide/plugins#nitro-runtime-hooks)[] Read more in [Guide \> Plugins#nitro Runtime Hooks].

-   [`cloudflare:scheduled`](https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/)
-   [`cloudflare:email`](https://developers.cloudflare.com/email-routing/email-workers/runtime-api/)
-   [`cloudflare:queue`](https://developers.cloudflare.com/queues/configuration/javascript-apis/#consumer)
-   [`cloudflare:tail`](https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/)
-   `cloudflare:trace`

## [[[]]Cloudflare Pages](#cloudflare-pages) 

**Preset:** `cloudflare_pages`

[[]](https://pages.cloudflare.com/)[][] Read more in [Cloudflare Pages].

[]Integration with this provider is possible with [zero configuration](/deploy#zero-config-providers).

[]Cloudflare [Workers Module](#cloudflare-workers) is the new recommended preset for deployments. Please consider using the pages only if you need specific features.

The following shows an example `nitro.config.ts` file for deploying a Nitro app to Cloudflare Pages.

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

Nitro automatically generates a `_routes.json` file that controls which routes get served from files and which are served from the Worker script. The auto-generated routes file can be overridden with the config option `cloudflare.pages.routes` ([read more](https://developers.cloudflare.com/pages/platform/functions/routing/#functions-invocation-routes)).

### [[[]]Local Preview](#local-preview-1) 

You can use [Wrangler](https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler) to preview your app locally:

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

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx wrangler pages dev
```

[]

``` 
yarn dlx wrangler pages dev
```

[]

``` 
pnpm dlx wrangler pages dev
```

[]

``` 
bunx wrangler pages dev
```

[]

``` 
deno run -A npm:wrangler pages dev
```

### [[[]]Manual Deploy](#manual-deploy-1) 

After having built your application you can manually deploy it with Wrangler, in order to do so first make sure to be logged into your Cloudflare account:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx wrangler login
```

[]

``` 
yarn dlx wrangler login
```

[]

``` 
pnpm dlx wrangler login
```

[]

``` 
bunx wrangler login
```

[]

``` 
deno run -A npm:wrangler login
```

Then you can deploy the application with:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx wrangler pages deploy
```

[]

``` 
yarn dlx wrangler pages deploy
```

[]

``` 
pnpm dlx wrangler pages deploy
```

[]

``` 
bunx wrangler pages deploy
```

[]

``` 
deno run -A npm:wrangler pages deploy
```

## [[[]]Cloudflare Service Workers](#cloudflare-service-workers) 

**Preset:** `cloudflare`

[]**Note:** This preset uses the [service worker syntax](https://developers.cloudflare.com/workers/learning/service-worker/) for deployment.

[]**Note:** This preset is deprecated.

The way this preset works is identical to that of the `cloudflare_module` one presented above, with the only difference being that such preset inherits all the [disadvantages](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/#advantages-of-migrating) that such syntax brings.

## [[[]]Deploy within CI/CD using GitHub Actions](#deploy-within-cicd-using-github-actions) 

Regardless on whether you\'re using Cloudflare Pages or Cloudflare Workers, you can use the [Wrangler GitHub actions](https://github.com/marketplace/actions/deploy-to-cloudflare-workers-with-wrangler) to deploy your application.

[]**Note:** Remember to [instruct Nitro to use the correct preset](/deploy#changing-the-deployment-preset) (note that this is necessary for all presets including the `cloudflare_pages` one).

## [[[]]Environment Variables](#environment-variables) 

Nitro allows you to universally access environment variables using `process.env` or `import.meta.env` or the runtime config.

[]Make sure to only access environment variables **within the event lifecycle** and not in global contexts since Cloudflare only makes them available during the request lifecycle and not before.

**Example:** If you have set the `SECRET` and `NITRO_HELLO_THERE` environment variables set you can access them in the following way:

[]

``` 
console.log(process.env.SECRET) // note that this is in the global scope! so it doesn't actually work and the variable is undefined!

export default defineEventHandler((event) => );
```

### [[[]]Specify Variables in Development Mode](#specify-variables-in-development-mode) 

For development, you can use a `.env` file to specify environment variables:

[]

``` 
NITRO_HELLO_THERE="captain"
SECRET="top-secret"
```

[]**Note:** Make sure you add `.env` to the `.gitignore` file so that you don\'t commit it as it can contain sensitive information.

### [[[]]Specify Variables for local previews](#specify-variables-for-local-previews) 

After build, when you try out your project locally with `wrangler dev` or `wrangler pages dev`, in order to have access to environment variables you will need to specify the in a `.dev.vars` file in the root of your project (as presented in the [Pages](https://developers.cloudflare.com/pages/functions/bindings/#interact-with-your-environment-variables-locally) and [Workers](https://developers.cloudflare.com/workers/configuration/environment-variables/#interact-with-environment-variables-locally) documentation).

If you are using a `.env` file while developing, your `.dev.vars` should be identical to it.

[]**Note:** Make sure you add `.dev.vars` to the `.gitignore` file so that you don\'t commit it as it can contain sensitive information.

### [[[]]Specify Variables for Production](#specify-variables-for-production) 

For production, use the Cloudflare dashboard or the [`wrangler secret`](https://developers.cloudflare.com/workers/wrangler/commands/#secret) command to set environment variables and secrets.

### [[[]]Specify Variables using `wrangler.toml`/`wrangler.json`](#specify-variables-using-wranglertomlwranglerjson) 

You can specify a custom `wrangler.toml`/`wrangler.json` file and define vars inside.

[]Note that this isn\'t recommend for sensitive data like secrets.

**Example:**

[][wrangler.toml]

[]

``` 
# Shared
[vars]
NITRO_HELLO_THERE="general"
SECRET="secret"

# Override values for `--env production` usage
[env.production.vars]
NITRO_HELLO_THERE="captain"
SECRET="top-secret"
```

## [[[]]Direct access to Cloudflare bindings](#direct-access-to-cloudflare-bindings) 

Bindings are what allows you to interact with resources from the Cloudflare platform, examples of such resources are key-value data storages ([KVs](https://developers.cloudflare.com/kv/)) and serverless SQL databases ([D1s](https://developers.cloudflare.com/d1/)).

[]For more details on Bindings and how to use them please refer to the Cloudflare [Pages](https://developers.cloudflare.com/pages/functions/bindings/) and [Workers](https://developers.cloudflare.com/workers/configuration/bindings/#bindings) documentation.

[] Nitro provides high level API to interact with primitives such as [KV Storage](/guide/storage) and [Database](/guide/database) and you are highly recommended to prefer using them instead of directly depending on low-level APIs for usage stability.

[[]](/guide/database)[] Read more in [Database Layer].

[[]](/guide/storage)[] Read more in [KV Storage].

In runtime, you can access bindings from the request event, by accessing its `context.cloudflare.env` field, this is for example how you can access a D1 bindings:

[]

``` 
defineEventHandler(async (event) =>  = event.context
  const stmt = await cloudflare.env.MY_D1.prepare('SELECT id FROM table')
  const  = await stmt.all()
})
```

## [[[]]Dev Preset](#dev-preset) 

Cloudflare preset can be enabled in development mode for production environment emulation and access to the bindings in local dev.

In order to enable dev preset, make sure using latest nitro version (\>=2.12) and install [`wrangler`](https://npmjs.com/package/wrangler) as a dependency.

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npm i -D wrangler
```

[]

``` 
yarn add -D wrangler
```

[]

``` 
pnpm i -D wrangler
```

[]

``` 
bun i -D wrangler
```

[]

``` 
deno i npm:-D wrangler
```

Then, update config:

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

In development terminal, you should see a message like this:

[]

``` 
ℹ Using cloudflare-dev emulation in development mode.
```

In order to access bindings in dev mode we start by defining the bindings. You can do this in a `wrangler.toml`/`wrangler.jsonc` file, or directly in your Nitro config under `cloudflare.wrangler` (accepts the same type as `wrangler.json`).

For example to define a variable and a KV namespace in a `wrangler.toml`

[][wrangler.toml]

[]

``` 
[vars]
MY_VARIABLE="my-value"

[[kv_namespaces]]
binding = "MY_KV"
id = "xxx"
```

Or in your Nitro config:

[][nitro.config.js]

[]

``` 
export default defineNitroConfig(,
        kv_namespaces: [
          
        ]
      }
    }
});
```

[] Only bindings in the default environment are recognized.

you will be able to access the `MY_VARIABLE` and `MY_KV` from the request event just as illustrated above.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/cloudflare.md)

[](/deploy/providers/cleavr)

[]

Cleavr

Deploy Nitro apps to Cleavr.

[](/deploy/providers/deno-deploy)

[]

Deno Deploy

Deploy Nitro apps to Deno Deploy.

[On this page][[]]

[On this page][[]]

-   [[Cloudflare Workers]](#cloudflare-workers)
    -   [[Local Preview]](#local-preview)
    -   [[Manual Deploy]](#manual-deploy)
    -   [[Runtime Hooks]](#runtime-hooks)
-   [[Cloudflare Pages]](#cloudflare-pages)
    -   [[Local Preview]](#local-preview-1)
    -   [[Manual Deploy]](#manual-deploy-1)
-   [[Cloudflare Service Workers]](#cloudflare-service-workers)
-   [[Deploy within CI/CD using GitHub Actions]](#deploy-within-cicd-using-github-actions)
-   [[Environment Variables]](#environment-variables)
    -   [[Specify Variables in Development Mode]](#specify-variables-in-development-mode)
    -   [[Specify Variables for local previews]](#specify-variables-for-local-previews)
    -   [[Specify Variables for Production]](#specify-variables-for-production)
    -   [[Specify Variables using wrangler.toml/wrangler.json]](#specify-variables-using-wranglertomlwranglerjson)
-   [[Direct access to Cloudflare bindings]](#direct-access-to-cloudflare-bindings)
-   [[Dev Preset]](#dev-preset)