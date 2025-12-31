# Source: https://nitro.build/deploy/providers/genezio

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

# Genezio 

Deploy Nitro apps to Genezio.

</div>

<div>

**Preset:** `genezio`

[[]](https://genezio.com)[][] Read more in [Genezio].

[] 🚧 This preset is currently experimental.

## [[[]]1. Project Setup](#_1-project-setup) 

Create `genezio.yaml` file:

[]

``` 
# The name of the project.
name: nitro-app
# The version of the Genezio YAML configuration to parse.
yamlVersion: 2
backend:
  # The root directory of the backend.
  path: .output/
  # Information about the backend's programming language.
  language:
      # The name of the programming language.
      name: js
      # The package manager used by the backend.
      packageManager: npm
  # Information about the backend's functions.
  functions:
      # The name (label) of the function.
      - name: nitroServer
      # The path to the function's code.
        path: server/
        # The name of the function handler
        handler: handler
        # The entry point for the function.
        entry: index.mjs
```

[[]](https://genezio.com/docs/project-structure/genezio-configuration-file/)[][]To further customize the file to your needs, you can consult the [official documentation](https://genezio.com/docs/project-structure/genezio-configuration-file/).

## [[[]]2. Deploy your project](#_2-deploy-your-project) 

Build with the genezio nitro preset:

[]

``` 
NITRO_PRESET=genezio npm run build
```

Deploy with [`genezio`](https://npmjs.com/package/genezio) cli:

[][npm]

[][yarn]

[][pnpm]

[][bun]

[][deno]

[]

``` 
npx genezio deploy
```

[]

``` 
yarn dlx genezio deploy
```

[]

``` 
pnpm dlx genezio deploy
```

[]

``` 
bunx genezio deploy
```

[]

``` 
deno run -A npm:genezio deploy
```

[[]](https://genezio.com/docs/project-structure/backend-environment-variables)[][]To set environment viarables, please check out [Genezio - Environment Variables](https://genezio.com/docs/project-structure/backend-environment-variables).

## [[[]]3. Monitor your project](#_3-monitor-your-project) 

You can monitor and manage your application through the [Genezio App Dashboard](https://app.genez.io/dashboard). The dashboard URL, also provided after deployment, allows you to access comprehensive views of your project\'s status and logs.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/genezio.md)

[](/deploy/providers/flightcontrol)

[]

Flightcontrol

Deploy Nitro apps to AWS via Flightcontrol.

[](/deploy/providers/github-pages)

[]

GitHub Pages

Deploy Nitro apps to GitHub Pages.

[On this page][[]]

[On this page][[]]

-   [[1. Project Setup]](#_1-project-setup)
-   [[2. Deploy your project]](#_2-deploy-your-project)
-   [[3. Monitor your project]](#_3-monitor-your-project)