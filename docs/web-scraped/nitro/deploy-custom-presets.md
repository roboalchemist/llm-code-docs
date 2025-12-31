# Source: https://nitro.build/deploy/custom-presets

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

<div>

# Custom Preset 

If you want to use a provider that Nitro doesn\'t support, or want to modify an existing one, you can create a local custom preset in your project.

</div>

<div>

Custom presets are local files that have a preset entry that defines builder configuration and a runtime entry point.

[]Custom local preset support is an experimental feature.

## [[[]]Example](#example) 

[]Check [nitrojs/nitro-preset-starter](https://github.com/nitrojs/nitro-preset-starter) for a ready-to-use template.

First, we have to define our preset entry point in a local directory `preset/nitro.config.ts`

[][./preset/nitro.config.ts]

[]

``` 
import type  from "nitropack";
import  from "node:url"

export default <NitroPreset>,
  },
};
```

The entry point will be used by your server or provider, and you can fully customize its behavior.

[][preset/entry.ts (Workers)]

[][preset/entry.ts (Node.js)]

[]

``` 
import "#internal/nitro/virtual/polyfill";

const nitroApp = useNitroApp();

export default ,
      host: url.hostname,
      protocol: url.protocol,
      method: request.method,
      headers: request.headers,
      body: undefined,
    });
  },
};
```

[]

``` 
import "#internal/nitro/virtual/polyfill";
import  from "node:http";
import  from "h3";

const nitroApp = useNitroApp();
const server = new Server(toNodeListener(nitroApp.h3App));

// @ts-ignore
server.listen(3000, (err) => 
  console.log(`Listening on http://localhost:3000 (custom preset)`);
});
```

Then in your nitro config file, you can use your custom preset.

[][nitro.config.ts]

[][nuxt.config.ts]

[]

``` 
export default defineNitroConfig();
```

[]

``` 
export default defineNuxtConfig(
});
```

Refer to the Nitro [source code](https://github.com/nitrojs/nitro/tree/main/src) directly to have a better understanding of presets and entry points.

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/2.custom-presets.md)

[](/deploy/runtimes/deno)

[]

Deno

Run Nitro apps with Deno runtime.

[](/deploy/providers/alwaysdata)

[]

Alwaysdata

Deploy Nitro apps to alwaysdata.

[On this page][[]]

[On this page][[]]

-   [[Example]](#example)