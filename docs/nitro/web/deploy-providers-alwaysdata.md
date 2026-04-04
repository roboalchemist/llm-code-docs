# Source: https://nitro.build/deploy/providers/alwaysdata

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

# Alwaysdata 

Deploy Nitro apps to alwaysdata.

</div>

<div>

**Preset:** `alwaysdata`

[[]](https://alwaysdata.com)[][] Read more in [alwaysdata.com].

## [[[]]Set up application](#set-up-application) 

### [[[]]Pre-requisites](#pre-requisites) 

#### [Register a new profile](https://www.alwaysdata.com/en/register/) on alwaysdata platform if you don\'t have one. 

#### Get a free 100Mb plan to host your app. 

[] Keep in mind your *account name* will be used to provide you a default URL in the form of `account_name.alwaysdata.net`, so choose it wisely. You can also link your existing domains to your account later or register as many accounts under your profile as you need.

### [[[]]Local deployment](#local-deployment) 

#### Build your project locally with `npm run build -- preset alwaysdata` 

#### [Upload your app](https://help.alwaysdata.com/en/remote-access/) to your account in its own directory (e.g. `$HOME/www/my-app`). You can use any protocol you prefer (SSH/FTP/WebDAV...) to do so. 

#### On your admin panel, [create a new site](https://admin.alwaysdata.com/site/add/) for your app with the following features: 

-   *Addresses*: `[account_name].alwaysdata.net`
-   *Type*: Node.js
-   *Command*: `node ./output/server/index.mjs`
-   *Working directory*: `www/my-app` (adapt it to your deployment path)
-   *Environment*:

    ::: 
    []
    ``` 
    NITRO_PRESET=alwaysdata
    ```
    :::
-   *Node.js version*: `Default version` is fine; pick no less than `20.0.0` (you can also [set your Node.js version globally](https://help.alwaysdata.com/en/languages/nodejs/configuration/#supported-versions))
-   *Hot restart*: `SIGHUP`

[[]](https://help.alwaysdata.com/en/languages/nodejs)[][] Read more in [Get more information about alwaysdata Node.js sites type].

#### Your app is now live at `http(s)://[account_name].alwaysdata.net`. 

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/alwaysdata.md)

[](/deploy/custom-presets)

[]

Custom Preset

If you want to use a provider that Nitro doesn\'t support, or want to modify an existing one, you can create a local custom preset in your project.

[](/deploy/providers/aws)

[]

AWS Lambda

Deploy Nitro apps to AWS Lambda.

[On this page][[]]

[On this page][[]]

-   [[Set up application]](#set-up-application)
    -   [[Pre-requisites]](#pre-requisites)
    -   [[Local deployment]](#local-deployment)