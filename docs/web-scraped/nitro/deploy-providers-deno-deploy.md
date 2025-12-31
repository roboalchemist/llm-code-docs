# Source: https://nitro.build/deploy/providers/deno-deploy

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

# Deno Deploy 

Deploy Nitro apps to Deno Deploy.

</div>

<div>

**Preset:** `deno_deploy`

[[]](https://deno.com/deploy)[][] Read more in [Deno Deploy].

## [[[]]Deploy with the CLI](#deploy-with-the-cli) 

You can use [deployctl](https://deno.com/deploy/docs/deployctl) to deploy your app.

Login to [Deno Deploy](https://dash.deno.com/account#access-tokens) to obtain a `DENO_DEPLOY_TOKEN` access token, and set it as an environment variable.

[]

``` 
# Build with the deno_deploy NITRO preset
NITRO_PRESET=deno_deploy npm run build

# Make sure to run the deployctl command from the output directory
cd .output
deployctl deploy --project=my-project server/index.ts
```

## [[[]]Deploy within CI/CD using gitHub actions](#deploy-within-cicd-using-github-actions) 

You just need to include the deployctl GitHub Action as a step in your workflow.

You do not need to set up any secrets for this to work. You do need to link your GitHub repository to your Deno Deploy project and choose the \"GitHub Actions\" deployment mode. You can do this in your project settings on [Deno Deploy](https://dash.deno.com).

Create the following workflow file in your `.github/workflows` directory:

[][.github/workflows/deno_deploy.yml]

[]

``` 
name: deno-deploy

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  deploy:
    steps:
      - uses: actions/checkout@v3
      - run: corepack enable
      - uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: pnpm
      - run: pnpm install
      - run: pnpm build
        env:
          NITRO_PRESET: deno_deploy
      - name: Deploy to Deno Deploy
        uses: denoland/deployctl@v1
        with:
          project: my-project
          entrypoint: server/index.ts
          root: .output
```

## [[[]]Deno runtime](#deno-runtime) 

[[]](/deploy/runtimes/deno)[] Read more in [Deploy \> Runtimes \> Deno].

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/deno-deploy.md)

[](/deploy/providers/cloudflare)

[]

Cloudflare

Deploy Nitro apps to Cloudflare.

[](/deploy/providers/digitalocean)

[]

DigitalOcean

Deploy Nitro apps to DigitalOcean.

[On this page][[]]

[On this page][[]]

-   [[Deploy with the CLI]](#deploy-with-the-cli)
-   [[Deploy within CI/CD using gitHub actions]](#deploy-within-cicd-using-github-actions)
-   [[Deno runtime]](#deno-runtime)