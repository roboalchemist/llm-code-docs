# Source: https://nitro.build/deploy/providers/aws-amplify

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

# AWS Amplify 

Deploy Nitro apps to AWS Amplify Hosting.

</div>

<div>

**Preset:** `aws_amplify`

[[]](https://aws.amazon.com/amplify)[][] Read more in [AWS Amplify Hosting].

## [[[]]Deploy to AWS Amplify Hosting](#deploy-to-aws-amplify-hosting) 

[]Integration with this provider is possible with [zero configuration](/deploy/#zero-config-providers).

#### Login to the [AWS Amplify Hosting Console](https://console.aws.amazon.com/amplify/) 

#### Click on \"Get Started\" \> Amplify Hosting (Host your web app) 

#### Select and authorize access to your Git repository provider and select the main branch 

#### Choose a name for your app, make sure build settings are auto-detected and optionally set requirement environment variables under the advanced section 

#### Optionally, select Enable SSR logging to enable server-side logging to your Amazon CloudWatch account 

#### Confirm configuration and click on \"Save and Deploy\" 

## [[[]]Advanced Configuration](#advanced-configuration) 

You can configure advanced options of this preset using `awsAmplify` option.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig(,
      // imageSettings: ,
      // runtime: "nodejs18.x", // default: "nodejs18.x" | "nodejs16.x" | "nodejs20.x"
  }
})
```

[]

``` 
export default defineNuxtConfig(,
      // imageSettings: ,
      // runtime: "nodejs18.x", // default: "nodejs18.x" | "nodejs16.x" | "nodejs20.x"
    }
  }
})
```

### [[[]]`amplify.yml`](#amplifyyml) 

You might need a custom `amplify.yml` file for advanced configuration. Here are two template examples:

[][amplify.yml]

[][amplify.yml (monorepo)]

[]

``` 
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - nvm use 18 && node --version
        - corepack enable && npx --yes nypm install
    build:
      commands:
        - pnpm build
  artifacts:
    baseDirectory: .amplify-hosting
    files:
      - "**/*"
```

[]

``` 
version: 1
applications:
  - frontend:
      phases:
        preBuild:
          commands:
          - nvm use 18 && node --version
          - corepack enable && npx --yes nypm install
        build:
          commands:
            - pnpm --filter website1 build
      artifacts:
        baseDirectory: apps/website1/.amplify-hosting
        files:
          - '**/*'
      buildPath: /
    appRoot: apps/website1
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/aws-amplify.md)

[](/deploy/providers/aws)

[]

AWS Lambda

Deploy Nitro apps to AWS Lambda.

[](/deploy/providers/azure)

[]

Azure

Deploy Nitro apps to Azure Static Web apps or functions.

[On this page][[]]

[On this page][[]]

-   [[Deploy to AWS Amplify Hosting]](#deploy-to-aws-amplify-hosting)
-   [[Advanced Configuration]](#advanced-configuration)
    -   [[amplify.yml]](#amplifyyml)