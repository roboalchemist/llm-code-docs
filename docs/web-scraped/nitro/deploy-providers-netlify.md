# Source: https://nitro.build/deploy/providers/netlify

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

# Netlify 

Deploy Nitro apps to Netlify functions or edge.

</div>

<div>

**Preset:** `netlify`

[[]](https://www.netlify.com/platform/core/functions/)[][] Read more in [Netlify Functions].

[]Integration with this provider is possible with [zero configuration](/deploy/#zero-config-providers).

Normally, the deployment to Netlify does not require any configuration. Nitro will auto-detect that you are in a [Netlify](https://www.netlify.com) build environment and build the correct version of your server.

To enabling Netlify Functions 2.0 and using its features (e.g. streaming responses and [Netlify Blobs](https://docs.netlify.com/blobs/overview/)), you need a compatibility date set to `2024-05-07` or later in your nitro configuration file.

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

For new sites, Netlify will detect that you are using Nitro and set the publish directory to `dist` and build command to `npm run build`.

If you are upgrading an existing site you should check these and update them if needed.

If you want to add custom redirects, you can do so with [`routeRules`](/config#routerules) or by adding a [`_redirects`](https://docs.netlify.com/routing/redirects/#syntax-for-the-redirects-file) file to your `public` directory.

For deployment, just push to your git repository [as you would normally do for Netlify](https://docs.netlify.com/configure-builds/get-started/).

[]Make sure the publish directory is set to `dist` when creating a new project.

## [[[]]Netlify edge functions](#netlify-edge-functions) 

**Preset:** `netlify_edge`

Netlify Edge Functions use Deno and the powerful V8 JavaScript runtime to let you run globally distributed functions for the fastest possible response times.

[[]](https://docs.netlify.com/edge-functions/overview/)[][] Read more in [Netlify Edge functions].

Nitro output can directly run the server at the edge. Closer to your users.

[]Make sure the publish directory is set to `dist` when creating a new project.

## [[[]]On-demand builders](#on-demand-builders) 

**Preset:** `netlify_builder`

[]**Note:** This preset is deprecated. Instead, use the `netlify` preset with the `isr` route rule.

On-demand Builders are serverless functions used to generate web content as needed that's automatically cached on Netlify's Edge CDN. They enable you to build pages for your site when a user visits them for the first time and then cache them at the edge for subsequent visits.

[[]](https://docs.netlify.com/configure-builds/on-demand-builders/)[][] Read more in [Netlify On-demand Builders].

## [[[]]Custom deploy configuration](#custom-deploy-configuration) 

You can provide additional deploy configuration using the `netlify` key inside `nitro.config`. It will be merged with built-in auto-generated config. Currently the only supported value is `images.remote_images`, for [configuring Netlify Image CDN](https://docs.netlify.com/image-cdn/create-integration/).

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/netlify.md)

[](/deploy/providers/koyeb)

[]

Koyeb

Deploy Nitro apps to Koyeb.

[](/deploy/providers/platform-sh)

[]

Platform.sh

Deploy Nitro apps to platform.sh

[On this page][[]]

[On this page][[]]

-   [[Netlify edge functions]](#netlify-edge-functions)
-   [[On-demand builders]](#on-demand-builders)
-   [[Custom deploy configuration]](#custom-deploy-configuration)