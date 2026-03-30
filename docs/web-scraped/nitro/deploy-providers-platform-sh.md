# Source: https://nitro.build/deploy/providers/platform-sh

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

# Platform.sh 

Deploy Nitro apps to platform.sh

</div>

<div>

**Preset:** `platform_sh`

[[]](https://platform.sh)[][] Read more in [platform.sh].

## [[[]]Setup](#setup) 

First, create a new project on platform.sh and link it to the repository you want to auto-deploy with.

Then in repository create `.platform.app.yaml` file:

[][.platform.app.yaml]

[]

``` 
name: nitro-app
type: 'nodejs:18'
disk: 128
web:
  commands:
    start: "node .output/server/index.mjs"
build:
  flavor: none
hooks:
  build: |
    corepack enable
    npx nypm install
    NITR_PRESET=platform_sh npm run build
mounts:
    '.data':
        source: local
        source_path: .data
```

[[]](https://docs.platform.sh/create-apps/app-reference.html)[][] Read more in [Complete list of all available properties].

[[]](https://unjs.io/blog/2023-08-25-nitro-2.6#default-persistent-data-storage)[][] Read more in [Complete list of all available properties].

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/platform-sh.md)

[](/deploy/providers/netlify)

[]

Netlify

Deploy Nitro apps to Netlify functions or edge.

[](/deploy/providers/render)

[]

Render.com

Deploy Nitro apps to Render.com.

[On this page][[]]

[On this page][[]]

-   [[Setup]](#setup)