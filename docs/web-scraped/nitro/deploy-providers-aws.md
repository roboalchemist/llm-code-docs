# Source: https://nitro.build/deploy/providers/aws

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

# AWS Lambda 

Deploy Nitro apps to AWS Lambda.

</div>

<div>

**Preset:** `aws_lambda`

[[]](https://aws.amazon.com/lambda/)[][] Read more in [AWS Lambda].

Nitro provides a built-in preset to generate output format compatible with [AWS Lambda](https://aws.amazon.com/lambda/). The output entrypoint in `.output/server/index.mjs` is compatible with [AWS Lambda format](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html).

It can be used programmatically or as part of a deployment.

[]

``` 
import  from './.output/server'

// Use programmatically
const  = handler()
```

## [[[]]Inlining chunks](#inlining-chunks) 

Nitro output, by default uses dynamic chunks for lazy loading code only when needed. However this sometimes can not be ideal for performance. (See discussions in [nitrojs/nitro#650](https://github.com/nitrojs/nitro/pull/650)). You can enabling chunk inlining behavior using [`inlineDynamicImports`](/config#inlinedynamicimports) config.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig();
```

[]

``` 
export default defineNuxtConfig(
})
```

## [[[]]Response streaming](#response-streaming) 

[[]](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-response-streaming/)[][] Read more in [Introducing AWS Lambda response streaming].

In order to enable response streaming, enable `awsLambda.streaming` flag:

[][nitro.config.ts]

[]

``` 
export default defineNitroConfig(
});
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/aws.md)

[](/deploy/providers/alwaysdata)

[]

Alwaysdata

Deploy Nitro apps to alwaysdata.

[](/deploy/providers/aws-amplify)

[]

AWS Amplify

Deploy Nitro apps to AWS Amplify Hosting.

[On this page][[]]

[On this page][[]]

-   [[Inlining chunks]](#inlining-chunks)
-   [[Response streaming]](#response-streaming)