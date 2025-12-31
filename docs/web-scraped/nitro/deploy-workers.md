# Source: https://nitro.build/deploy/workers

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

# Edge Workers 

Nitro provides out of the box support for deploying to Edge Workers.

</div>

<div>

## [[[]]Deploy to workers](#deploy-to-workers) 

Nitro provides out of the box support for deploying any Nitro app to different Edge Worker offerings as well as Service Workers.

-   [Cloudflare](/deploy/providers/cloudflare)
-   [Deno Deploy](/deploy/providers/deno-deploy)
-   [Vercel](/deploy/providers/vercel#vercel-edge-functions)
-   [Netlify](/deploy/providers/netlify#netlify-edge-functions)
-   [Browser Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) (via experimental preset `service-worker`)

### [[[]]Worker limitations](#worker-limitations) 

-   No support for raw TCP/IP traffic
-   Execution time is limited compared to classic serverless offerings (normally 15-30 seconds)
-   No access to the filesystem (use the [nitro storage](/guide/storage) layer)
-   Bundle size is very limited (normally a few MBs)
-   Limited access Node.js APIs (nitro provides compatibility layer via [unenv](https://github.com/unjs/unenv))

### [[[]]Incompatible libraries](#incompatible-libraries) 

[]If you come across a library that you assume to be incompatible with edge workers, please open an issue on the [nitro repo](https://github.com/nitrojs/nitro/issues/new/choose) and help us keeping this list up to date.

The following libraries are known to be incompatible with edge workers because of one of the above mentioned limitations:

#### [`mongodb`](#mongodb) 

> There are possible fixes for MongoDB, like using Realm and the [Realm SDK](https://www.mongodb.com/docs/realm/sdk/node/) or using http interfaces (only available when self hosting MongoDB), but these are untested. You can find an example for using realm [here](https://github.com/albionstatus/albionstatus-backend/)

#### [`mysql`](#mysql) 

> You can find an example with a modified MySQL driver [here](https://github.com/cloudflare/worker-template-mysql)

-   `rhea`
-   `gremlin`
-   `ioredis`
-   `cassandra-driver`
-   `kafkajs`

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/1.workers.md)

[](/deploy)

[]

Overview

Learn more about Nitro deploy providers.

[](/deploy/runtimes/node)

[]

Node.js

Run Nitro apps with Node.js runtime.

[On this page][[]]

[On this page][[]]

-   [[Deploy to workers]](#deploy-to-workers)
    -   [[Worker limitations]](#worker-limitations)
    -   [[Incompatible libraries]](#incompatible-libraries)