# Source: https://nitro.build/deploy/node

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

1.  [[Runtimes]]

<div>

# Node.js 

Run Nitro apps with Node.js runtime.

</div>

<div>

**Preset:** `node_server`

Node.js is the default nitro output preset for production builds and Nitro has native Node.js runtime support.

Build project using nitro CLI:

[]

``` 
nitro build
```

When running `nitro build` with the Node server preset, the result will be an entry point that launches a ready-to-run Node server. To try output:

[]

``` 
$ node .output/server/index.mjs
Listening on http://localhost:3000
```

You can now deploy fully standalone `.output` directory to the hosting of your choice.

### [[[]]Environment Variables](#environment-variables) 

You can customize server behavior using following environment variables:

-   `NITRO_PORT` or `PORT` (defaults to `3000`)
-   `NITRO_HOST` or `HOST`
-   `NITRO_UNIX_SOCKET` - if provided (a path to the desired socket file) the service will be served over the provided UNIX socket.
-   `NITRO_SSL_CERT` and `NITRO_SSL_KEY` - if both are present, this will launch the server in HTTPS mode. In the vast majority of cases, this should not be used other than for testing, and the Nitro server should be run behind a reverse proxy like nginx or Cloudflare which terminates SSL.
-   `NITRO_SHUTDOWN_DISABLED` - Disables the graceful shutdown feature when set to `'true'`. If it\'s set to `'true'`, the graceful shutdown is bypassed to speed up the development process. Defaults to `'false'`.
-   `NITRO_SHUTDOWN_SIGNALS` - Allows you to specify which signals should be handled. Each signal should be separated with a space. Defaults to `'SIGINT SIGTERM'`.
-   `NITRO_SHUTDOWN_TIMEOUT` - Sets the amount of time (in milliseconds) before a forced shutdown occurs. Defaults to `'30000'` milliseconds.
-   `NITRO_SHUTDOWN_FORCE` - When set to true, it triggers `process.exit()` at the end of the shutdown process. If it\'s set to `'false'`, the process will simply let the event loop clear. Defaults to `'true'`.

## [[[]]Cluster mode](#cluster-mode) 

**Preset:** `node_cluster`

For more performance and leveraging multi-core handling, you can use cluster preset.

### [[[]]Environment Variables](#environment-variables-1) 

In addition to environment variables from the `node_server` preset, you can customize behavior:

-   `NITRO_CLUSTER_WORKERS`: Number of cluster workers (default is Number of available cpu cores)

## [[[]]Handler (advanced)](#handler-advanced) 

**Preset:** `node`

Nitro also has a more low-level preset that directly exports a function with `(req, res) => ` signature usable for middleware and custom servers.

When running `nitro build` with the Node preset, the result will be an entry point exporting a function with the `(req, res) => ` signature.

**Example:**

[]

``` 
import  from 'node:http'
import  from './.output/server'

const server = createServer(listener)
server.listen(8080)
```

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/2.deploy/10.runtimes/1.node.md)

[](/deploy/workers)

[]

Edge Workers

Nitro provides out of the box support for deploying to Edge Workers.

[](/deploy/runtimes/_winterjs)

[]

WinterJS

[On this page][[]]

[On this page][[]]

-   [[Environment Variables]](#environment-variables)
-   [[Cluster mode]](#cluster-mode)
    -   [[Environment Variables]](#environment-variables-1)
-   [[Handler (advanced)]](#handler-advanced)