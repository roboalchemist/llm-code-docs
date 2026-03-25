# Source: https://nitro.build/deploy/providers/digitalocean

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

# DigitalOcean 

Deploy Nitro apps to DigitalOcean.

</div>

<div>

**Preset:** `digital_ocean`

[[]](https://docs.digitalocean.com/products/app-platform/)[][] Read more in [Digital Ocean App Platform].

## [[[]]Set up application](#set-up-application) 

#### Create a new Digital Ocean app following the [guide](https://docs.digitalocean.com/products/app-platform/how-to/create-apps/). 

#### Next, you\'ll need to configure environment variables. In your app settings, ensure the following app-level environment variables are set: 

[]

``` 
NITRO_PRESET=digital_ocean
```

\
[More information](https://docs.digitalocean.com/products/app-platform/how-to/use-environment-variables/).

#### You will need to ensure you set an `engines.node` field in your app\'s `package.json` to ensure Digital Ocean uses a supported version of Node.js: 

[]

``` 

}
```

\
[See more information](https://docs.digitalocean.com/products/app-platform/languages-frameworks/nodejs/#node-version).

#### You\'ll also need to add a run command so Digital Ocean knows what command to run after a build. You can do so by adding a start script to your `package.json`: 

[]

``` 

}
```

#### Finally, you\'ll need to add this start script to your Digital Ocean app\'s run command. Go to `Components > Settings > Commands`, click \"Edit\", then add `npm run start` 

Your app should be live at a Digital Ocean generated URL and you can now follow [the rest of the Digital Ocean deployment guide](https://docs.digitalocean.com/products/app-platform/how-to/manage-deployments/).

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/20.providers/digitalocean.md)

[](/deploy/providers/deno-deploy)

[]

Deno Deploy

Deploy Nitro apps to Deno Deploy.

[](/deploy/providers/edgio)

[]

Edgio

Deploy Nitro apps to Edgio.

[On this page][[]]

[On this page][[]]

-   [[Set up application]](#set-up-application)