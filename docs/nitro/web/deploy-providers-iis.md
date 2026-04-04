# Source: https://nitro.build/deploy/providers/iis

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

# IIS 

Deploy Nitro apps to IIS.

</div>

<div>

## [[[]]Using](#using-iisnode) [IISnode](https://github.com/Azure/iisnode) 

**Preset:** `iis_node`

#### Install the latest LTS version of [Node.js](https://nodejs.org/en/) on your Windows Server. 

#### Install [IISnode](https://github.com/azure/iisnode/releases) 

#### Install [IIS `URLRewrite` Module](https://www.iis.net/downloads/microsoft/url-rewrite). 

#### In IIS, add `.mjs` as a new mime type and set its content type to `application/javascript`. 

#### Deploy the contents of your `.output` folder to your website in IIS. 

## [[[]]Using IIS handler](#using-iis-handler) 

**Preset:** `iis_handler` / `iis`

You can use IIS http handler directly.

#### Install the latest LTS version of [Node.js](https://nodejs.org/en/) on your Windows Server. 

#### Install [IIS `HttpPlatformHandler` Module](https://www.iis.net/downloads/microsoft/httpplatformhandler) 

#### Copy your `.output` directory into the Windows Server, and create a website on IIS pointing to that exact directory. 

## [[[]]IIS config options](#iis-config-options) 

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(,
});
```

[]

``` 
export default defineNuxtConfig(,
  },
});
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/iis.md)

[](/deploy/providers/heroku)

[]

Heroku

Deploy Nitro apps to Heroku.

[](/deploy/providers/koyeb)

[]

Koyeb

Deploy Nitro apps to Koyeb.

[On this page][[]]

[On this page][[]]

-   [[Using IISnode]](#using-iisnode)
-   [[Using IIS handler]](#using-iis-handler)
-   [[IIS config options]](#iis-config-options)