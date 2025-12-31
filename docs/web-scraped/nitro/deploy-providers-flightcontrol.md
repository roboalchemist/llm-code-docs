# Source: https://nitro.build/deploy/providers/flightcontrol

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

# Flightcontrol 

Deploy Nitro apps to AWS via Flightcontrol.

</div>

<div>

**Preset:** `flightcontrol`

[[]](https://flightcontrol.dev?ref=nitro)[][] Read more in [flightcontrol.dev].

[]Flightcontrol has zero config support for [Nuxt](https://nuxt.com/) projects.

## [[[]]Set Up your flightcontrol account](#set-up-your-flightcontrol-account) 

On a high level, the steps you will need to follow to deploy a project for the first time are:

#### Create an account at [Flightcontrol](https://app.flightcontrol.dev/signup?ref=nitro) 

#### Create an account at [AWS](https://portal.aws.amazon.com/billing/signup) (if you don\'t already have one) 

#### Link your AWS account to the Flightcontrol 

#### Authorize the Flightcontrol GitHub App to access your chosen repositories, public or private. 

#### Create a Flightcontrol project with configuration via the Dashboard or with configuration via `flightcontrol.json`. 

### [[[]]Create a project with configuration via the dashboard](#create-a-project-with-configuration-via-the-dashboard) 

#### Create a Flightcontrol project from the Dashboard. Select a repository for the source. 

#### Select the `GUI` config type. 

#### Select the Nuxt preset. This preset will also work for any Nitro-based applications. 

#### Select your preferred AWS server size. 

#### Submit the new project form. 

### [[[]]Create a project with configuration via `flightcontrol.json`](#create-a-project-with-configuration-via-flightcontroljson) 

#### Create a Flightcontrol project from your dashboard. Select a repository for the source. 

#### Select the `flightcontrol.json` config type. 

#### Add a new file at the root of your repository called `flightcontrol.json`. Here is an example configuration that creates an AWS fargate service for your app: 

[][flightcontrol.json]

[]

``` 
,
      "services": [
        
      ]
    }
  ]
}
```

4.  Submit the new project form.

[[]](https://www.flightcontrol.dev/docs?ref=nitro)[][]Learn more about Flightcontrol\'s [configuration](https://www.flightcontrol.dev/docs?ref=nitro).

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/flightcontrol.md)

[](/deploy/providers/firebase)

[]

Firebase

Deploy Nitro apps to Firebase.

[](/deploy/providers/genezio)

[]

Genezio

Deploy Nitro apps to Genezio.

[On this page][[]]

[On this page][[]]

-   [[Set Up your flightcontrol account]](#set-up-your-flightcontrol-account)
    -   [[Create a project with configuration via the dashboard]](#create-a-project-with-configuration-via-the-dashboard)
    -   [[Create a project with configuration via flightcontrol.json]](#create-a-project-with-configuration-via-flightcontroljson)