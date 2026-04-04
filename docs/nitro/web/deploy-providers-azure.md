# Source: https://nitro.build/deploy/providers/azure

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

# Azure 

Deploy Nitro apps to Azure Static Web apps or functions.

</div>

<div>

## [[[]]Azure static web apps](#azure-static-web-apps) 

**Preset:** `azure`

[[]](https://azure.microsoft.com/en-us/products/app-service/static)[][] Read more in [Azure Static Web Apps].

[]Integration with this provider is possible with [zero configuration](/deploy/#zero-config-providers).

[Azure Static Web Apps](https://azure.microsoft.com/en-us/products/app-service/static) are designed to be deployed continuously in a [GitHub Actions workflow](https://docs.microsoft.com/en-us/azure/static-web-apps/github-actions-workflow). By default, Nitro will detect this deployment environment and enable the `azure` preset.

### [[[]]Local preview](#local-preview) 

Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local) if you want to test locally.

You can invoke a development environment to preview before deploying.

[]

``` 
NITRO_PRESET=azure npx nypm@latest run build
npx @azure/static-web-apps-cli start .output/public --api-location .output/server
```

### [[[]]Configuration](#configuration) 

Azure Static Web Apps are [configured](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration) using the `staticwebapp.config.json` file.

Nitro automatically generates this configuration file whenever the application is built with the `azure` preset.

Nitro will automatically add the following properties based on the following criteria:

  Property                                                                                                                                                                                                                                                                                                                                                                                   Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Default
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------
  **[platform.apiRuntime](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#platform)**                 Will automatically set to `node:16` or `node:14` depending on your package configuration.                                                                                                                                                                                                                                                                                                     `node:16`
  **[navigationFallback.rewrite](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#fallback-routes)**   Is always `/api/server`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     `/api/server`
  **[routes](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#routes)**                                All prerendered routes are added. Additionally, if you do not have an `index.html` file an empty one is created for you for compatibility purposes and also requests to `/index.html` are redirected to the root directory which is handled by `/api/server`.   `[]`

### [[[]]Custom configuration](#custom-configuration) 

You can alter the Nitro generated configuration using `azure.config` option.

Custom routes will be added and matched first. In the case of a conflict (determined if an object has the same route property), custom routes will override generated ones.

### [[[]]Deploy from CI/CD via GitHub actions](#deploy-from-cicd-via-github-actions) 

When you link your GitHub repository to Azure Static Web Apps, a workflow file is added to the repository.

When you are asked to select your framework, select custom and provide the following information:

  Input                 Value
  --------------------- --------------------
  **app_location**      \'/\'
  **api_location**      \'.output/server\'
  **output_location**   \'.output/public\'

If you miss this step, you can always find the build configuration section in your workflow and update the build configuration:

[][.github/workflows/azure-static-web-apps-\<RANDOM_NAME\>.yml]

[]

``` 
###### Repository/Build Configurations ######
app_location: '/'
api_location: '.output/server'
output_location: '.output/public'
###### End of Repository/Build Configurations ######
```

That\'s it! Now Azure Static Web Apps will automatically deploy your Nitro-powered application on push.

If you are using runtimeConfig, you will likely want to configure the corresponding [environment variables on Azure](https://docs.microsoft.com/en-us/azure/static-web-apps/application-settings).

## [[[]]Azure functions](#azure-functions) 

**Preset:** `azure_functions`

[]If you encounter any issues, please ensure you\'re using a Node.js 16+ runtime. You can find more information about [how to set the Node version in the Azure docs](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-node?tabs=v2#setting-the-node-version). Please see [nitrojs/nitro#2114](https://github.com/nitrojs/nitro/issues/2114) for some common issues.

### [[[]]Local preview](#local-preview-1) 

Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local) if you want to test locally.

You can invoke a development environment from the serverless directory.

[]

``` 
NITRO_PRESET=azure_functions npx nypm@latest run build
cd .output
func start
```

You can now visit `http://localhost:7071/` in your browser and browse your site running locally on Azure Functions.

### [[[]]Deploy from your local machine](#deploy-from-your-local-machine) 

To deploy, just run the following command:

[]

``` 
# To publish the bundled zip file
az functionapp deployment source config-zip -g <resource-group> -n <app-name> --src dist/deploy.zip
# Alternatively you can publish from source
cd dist && func azure functionapp publish --javascript <app-name>
```

### [[[]]Deploy from CI/CD via GitHub actions](#deploy-from-cicd-via-github-actions-1) 

First, obtain your Azure Functions Publish Profile and add it as a secret to your GitHub repository settings following [these instructions](https://github.com/Azure/functions-action#using-publish-profile-as-deployment-credential-recommended).

Then create the following file as a workflow:

[][.github/workflows/azure.yml]

[]

``` 
name: azure
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  deploy:
    runs-on: $}
    strategy:
      matrix:
        os: [ ubuntu-latest ]
        node: [ 14 ]
    steps:
      - uses: actions/setup-node@v2
        with:
          node-version: $}

      - name: Checkout
        uses: actions/checkout@master

      - name: Get yarn cache directory path
        id: yarn-cache-dir-path
        run: echo "::set-output name=dir::$(yarn cache dir)"

      - uses: actions/cache@v2
        id: yarn-cache
        with:
          path: $}
          key: $}-yarn-$}
          restore-keys: |
            $}-yarn-azure

      - name: Install Dependencies
        if: steps.cache.outputs.cache-hit != 'true'
        run: yarn

      - name: Build
        run: npm run build
        env:
          NITRO_PRESET: azure_functions

      - name: 'Deploy to Azure Functions'
        uses: Azure/functions-action@v1
        with:
          app-name: <your-app-name>
          package: .output/deploy.zip
          publish-profile: $}
```

### [[[]]Optimizing Azure functions](#optimizing-azure-functions) 

Consider [turning on immutable packages](https://docs.microsoft.com/en-us/azure/app-service/deploy-run-package) to support running your app from the zip file. This can speed up cold starts.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/azure.md)

[](/deploy/providers/aws-amplify)

[]

AWS Amplify

Deploy Nitro apps to AWS Amplify Hosting.

[](/deploy/providers/cleavr)

[]

Cleavr

Deploy Nitro apps to Cleavr.

[On this page][[]]

[On this page][[]]

-   [[Azure static web apps]](#azure-static-web-apps)
    -   [[Local preview]](#local-preview)
    -   [[Configuration]](#configuration)
    -   [[Custom configuration]](#custom-configuration)
    -   [[Deploy from CI/CD via GitHub actions]](#deploy-from-cicd-via-github-actions)
-   [[Azure functions]](#azure-functions)
    -   [[Local preview]](#local-preview-1)
    -   [[Deploy from your local machine]](#deploy-from-your-local-machine)
    -   [[Deploy from CI/CD via GitHub actions]](#deploy-from-cicd-via-github-actions-1)
    -   [[Optimizing Azure functions]](#optimizing-azure-functions)