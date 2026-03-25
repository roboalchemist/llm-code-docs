# Source: https://nitro.build/deploy

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

<div>

# Overview 

Learn more about Nitro deploy providers.

</div>

<div>

Nitro can generate different output formats suitable for different hosting providers from the same code base. Using built-in presets, you can easily configure Nitro to adjust its output format with almost no additional code or configuration!

## [[[]]Default output](#default-output) 

The default production output preset is [Node.js server](/deploy/node).

When running Nitro in development mode, Nitro will always use a special preset called `nitro-dev` using Node.js with ESM in an isolated Worker environment with behavior as close as possible to the production environment.

## [[[]]Zero-Config Providers](#zero-config-providers) 

When deploying to production using CI/CD, Nitro tries to automatically detect the provider environment and set the right one without any additional configuration required. Currently, the providers below can be auto-detected with zero config.

-   [aws amplify](/deploy/providers/aws-amplify)
-   [azure](/deploy/providers/azure)
-   [cloudflare](/deploy/providers/cloudflare)
-   [firebase app hosting](/deploy/providers/firebase#firebase-app-hosting)
-   [netlify](/deploy/providers/netlify)
-   [stormkit](/deploy/providers/stormkit)
-   [vercel](/deploy/providers/vercel)
-   [zeabur](/deploy/providers/zeabur)

[]For Turborepo users, zero config detection will be interferenced by its Strict Environment Mode. You may need to allowing the variables explictly or use its Loose Environment Mode (with `--env-mode=loose` flag).

## [[[]]Changing the deployment preset](#changing-the-deployment-preset) 

If you need to build Nitro against a specific provider, you can target it by defining an environment variable named `NITRO_PRESET` or `SERVER_PRESET`, or by updating your Nitro [configuration](/guide/configuration) or using `--preset` argument.

Using the environment variable approach is recommended for deployments depending on CI/CD.

**Example:** Defining a `NITRO_PRESET` environment variable

[]

``` 
nitro build --preset cloudflare_pages
```

**Example:** Updating the `nitro.config.ts` file

[]

``` 
export default defineNitroConfig()
```

## [[[]]Compatibility date](#compatibility-date) 

Deployment providers regularly update their runtime behavior. Nitro presets are updated to support these new features.

To prevent breaking existing deployments, Nitro uses compatibility dates. These dates let you lock in behavior at the project creation time. You can also opt in to future updates when ready.

When you create a new project, the `compatibilityDate` is set to the current date. This setting is saved in your project\'s configuration.

You should update the compatibility date periodically. Always test your deployment thoroughly after updating. Below is a list of key dates and their effects.

  Compatibility date   Platform     Description
  -------------------- ------------ ----------------------------------------------------
  **≥ 2024-05-07**     netlify      Netlify functions v2
  **≥ 2024-09-19**     cloudflare   Static assets support for cloudflare-module preset
  **≥ 2025-01-30**     deno         Deno v2 Node.js compatibility

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/0.index.md)

[](/guide/nightly)

[]

Nightly Channel

Nitro has a nightly release channel that automatically releases for every commit to main branch to try latest changes.

[](/deploy/workers)

[]

Edge Workers

Nitro provides out of the box support for deploying to Edge Workers.

[On this page][[]]

[On this page][[]]

-   [[Default output]](#default-output)
-   [[Zero-Config Providers]](#zero-config-providers)
-   [[Changing the deployment preset]](#changing-the-deployment-preset)
-   [[Compatibility date]](#compatibility-date)