# Source: https://nitro.build/deploy/providers/render

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

# Render.com 

Deploy Nitro apps to Render.com.

</div>

<div>

**Preset:** `render_com`

[[]](https://render.com)[][] Read more in [render.com].

## [[[]]Set up application](#set-up-application) 

#### [Create a new Web Service](https://dashboard.render.com/select-repo?type=web) and select the repository that contains your code. 

#### Ensure the \'Node\' environment is selected. 

#### Update the start command to `node .output/server/index.mjs` 

#### Click \'Advanced\' and add an environment variable with `NITRO_PRESET` set to `render_com`. You may also need to add a `NODE_VERSION` environment variable set to `18` for the build to succeed ([docs](https://render.com/docs/node-version)). 

#### Click \'Create Web Service\'. 

## [[[]]Infrastructure as Code (IaC)](#infrastructure-as-code-iac) 

1.  Create a file called `render.yaml` with following content at the root of your repository.

> This file followed by [Infrastructure as Code](https://render.com/docs/infrastructure-as-code) on Render

[]

``` 
services:
  - type: web
    name: <PROJECTNAME>
    env: node
    branch: main
    startCommand: node .output/server/index.mjs
    buildCommand: npx nypm install && npm run build
    envVars:
    - key: NITRO_PRESET
      value: render_com
```

1.  [Create a new Blueprint Instance](https://dashboard.render.com/select-repo?type=blueprint) and select the repository containing your `render.yaml` file.

You should be good to go!

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/render.md)

[](/deploy/providers/platform-sh)

[]

Platform.sh

Deploy Nitro apps to platform.sh

[](/deploy/providers/stormkit)

[]

StormKit

Deploy Nitro apps to StormKit.

[On this page][[]]

[On this page][[]]

-   [[Set up application]](#set-up-application)
-   [[Infrastructure as Code (IaC)]](#infrastructure-as-code-iac)