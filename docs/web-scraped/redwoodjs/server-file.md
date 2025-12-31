# Source: https://docs.redwoodjs.com/docs/server-file

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Server File]

[Version: 8.8]

On this page

<div>

# Server File

</div>

Redwood v7 introduced a new entry point to Redwood\'s api server: the server file at `api/src/server.ts`.

It allows you to:

1.  have control over how the api server starts,
2.  customize the server as much as you want, and
3.  minimize the number of dependencies needed to start the api server process (all you need is Node.js!)

Get started by running the setup command:

``` 
yarn rw setup server-file
```

This should give you a new file at `api/src/server.ts`:

api/src/server.ts

``` 
import  from '@redwoodjs/api-server'

import  from 'src/lib/logger'

async function main() )

  await server.start()
}

main()
```

Without the server file, to start the api side, you\'d use binaries provided by `@redwoodjs/api-server` such as `yarn rw-server api` (you may also see this as `./node_modules/.bin/rw-server api`).

With the server file, there\'s no indirection. Just use `node`:

``` 
yarn node api/dist/server.js
```

### Building[​](#building "Direct link to Building") 

You can\'t run the server file directly with Node.js; it has to be built first:

``` 
yarn rw build api
```

The api serve stage in the Dockerfile pulls from the api build stage, so things are already in the right order there. Similarly, for `yarn rw dev`, the dev server will build and reload the server file for you.

### Command[​](#command "Direct link to Command") 

That means you will swap the `CMD` instruction in the api server stage:

``` 
  ENV NODE_ENV=production

- CMD [ "node_modules/.bin/rw-server", "api" ]
+ CMD [ "api/dist/server.js" ]
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]important

If you are using a [Server File](#using-the-server-file) then you must change the command that runs the `api_serve` service to `./api/dist/server.js` as shown above.

Not updating the command will not completely configure the GraphQL Server and not setup [Redwood Realtime](/docs/realtime), if you are using that.

### Configuring the server[​](#configuring-the-server "Direct link to Configuring the server") 

There are four ways you may wish to configure the server.

#### Underlying Fastify server[​](#underlying-fastify-server "Direct link to Underlying Fastify server") 

First, you can configure how the underlying Fastify server is instantiated via the`fastifyServerOptions` passed to the `createServer` function:

api/src/server.ts

``` 
const server = await createServer(,
})
```

For the complete list of options, see [Fastify\'s documentation](https://fastify.dev/docs/latest/Reference/Server/#factory).

#### Configure the redwood API plugin[​](#configure-the-redwood-api-plugin "Direct link to Configure the redwood API plugin") 

Second, you may want to alter the behavior of redwood\'s API plugin itself. To do this we provide a `configureApiServer(server)` option where you can do anything you wish to the fastify instance before the API plugin is registered. Two examples are given below.

##### Example: Compressing Payloads and Rate Limiting[​](#example-compressing-payloads-and-rate-limiting "Direct link to Example: Compressing Payloads and Rate Limiting") 

Let\'s say that we want to compress payloads and add rate limiting. We want to compress payloads only if they\'re larger than 1KB, preferring deflate to gzip, and we want to limit IP addresses to 100 requests in a five minute window. We can leverage two Fastify ecosystem plugins, [\@fastify/compress](https://github.com/fastify/fastify-compress) and [\@fastify/rate-limit](https://github.com/fastify/fastify-rate-limit) respectively.

First, you\'ll need to install these packages:

``` 
yarn workspace api add @fastify/compress @fastify/rate-limit
```

Then register them with the appropriate config:

api/src/server.ts

``` 
const server = await createServer()

    await server.register(import('@fastify/rate-limit'), )
  },
})
```

##### Example: Multipart POSTs[​](#example-multipart-posts "Direct link to Example: Multipart POSTs") 

If you try to POST file content to the api server such as images or PDFs, you may see the following error from Fastify:

``` 

```

This\'s because Fastify [only supports `application/json` and `text/plain` content types natively](https://www.fastify.io/docs/latest/Reference/ContentTypeParser/). While Redwood configures the api server to also accept `application/x-www-form-urlencoded` and `multipart/form-data`, if you want to support other content or MIME types (likes images or PDFs), you\'ll need to configure them here in the server file.

You can use Fastify\'s `addContentTypeParser` function to allow uploads of the content types your application needs. For example, to support image file uploads you\'d tell Fastify to allow `/^image\/.*/` content types:

api/src/server.ts

``` 
const server = await createServer()
    })
  },
})
```

The regular expression (`/^image\/.*/`) above allows all image content or MIME types because [they start with \"image\"](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types).

Now, when you POST those content types to a function served by the api server, you can access the file content on `event.body`.

Note that for the GraphQL endpoint, using Redwood\'s built-in [Uploads](/docs/uploads), multipart requests are already configured.

#### discoverFunctionsGlob[​](#discoverfunctionsglob "Direct link to discoverFunctionsGlob") 

Third, you can configure the discovery of the Redwood function files with `discoverFunctionsGlob` when the default value (`dist/functions/**/*.`) is not suitable.

The 3rd party library [fast-glob](https://github.com/mrmlnc/fast-glob) is used, which uses `https://github.com/micromatch/micromatch` under the covers. This allows configuring a single or multiple positive and negative matches.

##### Example[​](#example "Direct link to Example") 

Example usage after using a bundler that changes the directory structure, and generates extra support files when converting from ES modules to CJS:

``` 
const server = await createServer(,
  discoverFunctionsGlob: [
    'app/functions/**/*.js',
    // exclude all *.2.js files, e.g: exclude `app/functions/graphql/graphql2.js`, but keep `app/functions/graphql/graphql.js`
    '!app/functions/**/*2.js',
  ],
})
```

#### Additional Fastify plugins[​](#additional-fastify-plugins "Direct link to Additional Fastify plugins") 

Finally, you can register additional Fastify plugins on the server instance:

api/src/server.ts

``` 
const server = await createServer()

server.register(myFastifyPlugin)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]Fastify encapsulation

Fastify is built around the concept of [encapsulation](https://fastify.dev/docs/latest/Reference/Encapsulation/). It is important to note that redwood\'s API plugin cannot be mutated after it is registered, see [here](https://fastify.dev/docs/latest/Reference/Plugins/#asyncawait). This is why you must use the `configureApiServer` option to do as shown above.

### The `start` method[​](#the-start-method "Direct link to the-start-method") 

Since there\'s a few different ways to configure the host and port the server listens at, the server instance returned by `createServer` has a special `start` method:

api/src/server.ts

``` 
await server.start()
```

`start` is a thin wrapper around [`listen`](https://fastify.dev/docs/latest/Reference/Server/#listen). It takes the same arguments as `listen`, except for host and port. It computes those in the following way, in order of precedence:

1.  `--apiHost` or `--apiPort` flags:

``` 
yarn node api/dist/server.js --apiHost 0.0.0.0 --apiPort 8913
```

2.  `REDWOOD_API_HOST` or `REDWOOD_API_PORT` env vars:

``` 
export REDWOOD_API_HOST='0.0.0.0'
export REDWOOD_API_PORT='8913'
yarn node api/dist/server.js
```

3.  `[api].host` and `[api].port` in `redwood.toml`:

redwood.toml

``` 
[api]
  host = '0.0.0.0'
  port = 8913
```

If you\'d rather not have `createServer` parsing `process.argv`, you can disable it via `parseArgv`:

api/src/server.ts

``` 
await createServer()
```

And if you\'d rather it do none of this, just change `start` to `listen` and specify the host and port inline:

api/src/server.ts

``` 
await server.listen()
```

If you don\'t specify a host, `createServer` uses `NODE_ENV` to set it. If `NODE_ENV` is production, it defaults to `'0.0.0.0'` and `'::'` otherwise. The Dockerfile sets `NODE_ENV` to production so that things work out of the box.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/server-file.md)