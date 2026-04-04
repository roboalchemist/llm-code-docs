# Source: https://nitro.build/deploy/providers/zerops

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

# Zerops 

Deploy Nitro apps to Zerops.

</div>

<div>

**Preset:** `zerops`

[[]](https://zerops.io)[][] Read more in [zerops.io].

[] 🚧 This preset is currently experimental.

Zerops supports deploying both static and server-side rendered apps with a simple configuration file in your project root.

## [[[]]Starter templates](#starter-templates) 

If you want to quckly get started with zerops and nitro you can use repositories [`zeropsio/recipe-nitro-nodejs`](https://github.com/zeropsio/recipe-nitro-nodejs) and [`zeropsio/recipe-nitro-static`](https://github.com/zeropsio/recipe-nitro-static) starter templates.

## [[[]]Project setup](#project-setup) 

Projects and services can be added either through [project add wizard](https://app.zerops.io/dashboard/project-add) or imported using `zerops-project-import.yml`.

[][zerops-project-import.yml (node.js)]

[][zerops-project-import.yml (static)]

[]

``` 
project:
  name: nitro-app

services:
  - hostname: app
    type: nodejs@20
```

[]

``` 
project:
  name: nitro-app

services:
  - hostname: app
    type: static
```

Then create a `zerops.yml` config in your project root:

[][zerops.yml (node.js)]

[][zerops.yml (static)]

[]

``` 
zerops:
  - setup: app
    build:
      base: nodejs@20
      envVariables:
        SERVER_PRESET: zerops
      buildCommands:
        - pnpm i
        - pnpm run build
      deployFiles:
        - .output
        - package.json
        - node_modules
    run:
      base: nodejs@20
      ports:
        - port: 3000
          httpSupport: true
      start: node .output/server/index.mjs
```

[]

``` 
zerops:
  - setup: app
    build:
      base: nodejs@20
      envVariables:
        SERVER_PRESET: zerops-static
      buildCommands:
        - pnpm i
        - pnpm build
      deployFiles:
        - .zerops/output/static/~
    run:
      base: static
```

Now you can trigger the [build & deploy pipeline using the Zerops CLI](#building-deploying-your-app) or by connecting the app service with your [GitHub](https://docs.zerops.io/references/github-integration/) / [GitLab](https://docs.zerops.io/references/gitlab-integration) repository from inside the service detail.

## [[[]]Build and deploy](#build-and-deploy) 

Open [Settings \> Access Token Management](https://app.zerops.io/settings/token-management) in the Zerops app and generate a new access token.

Log in using your access token with the following command:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx @zerops/zcli login <token>
```

[]

``` 
yarn dlx @zerops/zcli login <token>
```

[]

``` 
pnpm dlx @zerops/zcli login <token>
```

[]

``` 
bunx @zerops/zcli login <token>
```

[]

``` 
deno run -A npm:@zerops/zcli login <token>
```

Navigate to the root of your app (where `zerops.yml` is located) and run the following command to trigger the deploy:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx @zerops/zcli push
```

[]

``` 
yarn dlx @zerops/zcli push
```

[]

``` 
pnpm dlx @zerops/zcli push
```

[]

``` 
bunx @zerops/zcli push
```

[]

``` 
deno run -A npm:@zerops/zcli push
```

Your code can be deployed automatically on each commit or a new tag by connecting the service with your [GitHub](https://docs.zerops.io/references/gitlab-integration) / [GitLab](https://docs.zerops.io/references/gitlab-integration) repository. This connection can be set up in the service detail.

[[]](https://docs.zerops.io/)[][] Read more in [Zerops Documentation].

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/zerops.md)

[](/deploy/providers/zeabur)

[]

Zeabur

Deploy Nitro apps to Zeabur.

[](/config)

[]

Config

[On this page][[]]

[On this page][[]]

-   [[Starter templates]](#starter-templates)
-   [[Project setup]](#project-setup)
-   [[Build and deploy]](#build-and-deploy)