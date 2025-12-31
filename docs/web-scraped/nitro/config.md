# Source: https://nitro.build/config

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

```
<!-- -->
```

<div>

# Config 

</div>

<div>

[[]](/guide/configuration)[] Read more in [Guide \> Configuration].

## [[[]]General](#general) 

### [[[]]`preset`](#preset) 

Use `preset` option `NITRO_PRESET` environment variable for custom **production** preset.

Preset for development mode is always `nitro_dev` and default `node_server` for production building a standalone Node.js server.

The preset will automatically be detected when the `preset` option is not set and running in known environments.

### [[[]]`logLevel`](#loglevel) 

-   Default: [`3`] ([`1`] when the testing environment is detected)

Log verbosity level. See [consola](https://github.com/unjs/consola?tab=readme-ov-file#log-level) for more information.

### [[[]]`runtimeConfig`](#runtimeconfig) 

-   Default: [`][`nitro`][`: ][`...`][` }, `][`...`][`yourOptions }`]

Server runtime configuration.

**Note:**: `nitro` namespace is reserved.

### [[[]]`compatibilityDate`](#compatibilitydate) 

Deployment providers introduce new features that Nitro presets can leverage, but some of them need to be explicitly opted into.

Set it to latest tested date in `YYYY-MM-DD` format to leverage latest preset features.

If this configuration is not provided, Nitro will continue using the current (v2.9) behavior for presets and show a warning.

## [[[]]Features](#features) 

### [[[]]`experimental`](#experimental) 

-   Default: ``

Enable experimental features.

#### [`openAPI`](#openapi) 

Enable `/_scalar`, `/_swagger` and `/_openapi.json` endpoints.

-   Default: `false`

To define the OpenAPI specification on your routes, take a look at [defineRouteMeta](/guide/routing#route-meta)

You can pass an object on the root level to modify your OpenAPI specification:

[]

``` 
openAPI: 
}
```

These routes are disabled by default in production. To enable them, use the `production` key. `"runtime"` allows middleware usage, and `"prerender"` is the most efficient because the JSON response is constant.

[]

``` 
openAPI: 
```

If you like to customize the Scalar integration, you can [pass a configuration object](https://github.com/scalar/scalar) like this:

[]

``` 
openAPI: 
  }
}
```

Or if you want to customize the endpoints:

[]

``` 
openAPI: ,
    swagger: 
  }
}
```

#### [`wasm`](#wasm) 

Enable WASM support

#### [`legacyExternals`](#legacyexternals) 

When enabled, legacy (unstable) experimental rollup externals algorithm will be used.

### [[[]]`future`](#future) 

-   Default: ``

New features pending for a major version to avoid breaking changes.

#### [`nativeSWR`](#nativeswr) 

Uses built-in SWR functionality (using caching layer and storage) for Netlify and Vercel presets instead of falling back to ISR behavior.

### [[[]]`storage`](#storage) 

-   Default: ``

Storage configuration, read more in the [Storage Layer](/guide/storage) section.

### [[[]]`timing`](#timing) 

-   Default: [`false`]

Enable timing information:

-   Nitro startup time log
-   `Server-Timing` header on HTTP responses

### [[[]]`renderer`](#renderer) 

Path to main render (file should export an event handler as default)

### [[[]]`serveStatic`](#servestatic) 

-   Type: `boolean` \| [`'node'`] \| [`'deno'`]
-   Default: depends of the deployment preset used.

Serve `public/` assets in production.

**Note:** It is highly recommended that your edge CDN (Nginx, Apache, Cloud) serves the `.output/public/` directory instead of enabling compression and higher lever caching.

### [[[]]`noPublicDir`](#nopublicdir) 

-   Default: [`false`]

If enabled, disabled `.output/public` directory creation. Skipping to copy `public/` dir and also disables pre-rendering.

### [[[]]`publicAssets`](#publicassets) 

Public asset directories to serve in development and bundle in production.

If a `public/` directory is detected, it will be added by default, but you can add more by yourself too!

It\'s possible to set Cache-Control headers for assets using the `maxAge` option:

[]

``` 
  publicAssets: [
    ,
  ],
```

The config above generates the following header in the assets under `public/images/` folder:

`cache-control: public, max-age=604800, immutable`

The `dir` option is where your files live on your file system; the `baseURL` option is the folder they will be accessible from when served/bundled.

### [[[]]`compressPublicAssets`](#compresspublicassets) 

-   Default: [`][`gzip`][`: `][`false`][`, `][`brotli`][`: `][`false`][` }`]

If enabled, Nitro will generate a pre-compressed (gzip and/or brotli) version of supported types of public assets and prerendered routes larger than 1024 bytes into the public directory. The best compression level is used. Using this option you can support zero overhead asset compression without using a CDN.

List of compressible MIME types:

-   `application/dash+xml`
-   `application/eot`
-   `application/font`
-   `application/font-sfnt`
-   `application/javascript`
-   `application/json`
-   `application/opentype`
-   `application/otf`
-   `application/pdf`
-   `application/pkcs7-mime`
-   `application/protobuf`
-   `application/rss+xml`
-   `application/truetype`
-   `application/ttf`
-   `application/vnd.apple.mpegurl`
-   `application/vnd.mapbox-vector-tile`
-   `application/vnd.ms-fontobject`
-   `application/wasm`
-   `application/xhtml+xml`
-   `application/xml`
-   `application/x-font-opentype`
-   `application/x-font-truetype`
-   `application/x-font-ttf`
-   `application/x-httpd-cgi`
-   `application/x-javascript`
-   `application/x-mpegurl`
-   `application/x-opentype`
-   `application/x-otf`
-   `application/x-perl`
-   `application/x-ttf`
-   `font/eot`
-   `font/opentype`
-   `font/otf`
-   `font/ttf`
-   `image/svg+xml`
-   `text/css`
-   `text/csv`
-   `text/html`
-   `text/javascript`
-   `text/js`
-   `text/plain`
-   `text/richtext`
-   `text/tab-separated-values`
-   `text/xml`
-   `text/x-component`
-   `text/x-java-source`
-   `text/x-script`
-   `vnd.apple.mpegurl`

### [[[]]`serverAssets`](#serverassets) 

Assets can be accessed in server logic and bundled in production. [Read more](/guide/assets#server-assets).

### [[[]]`devServer`](#devserver) 

-   Default: [`][`watch`][`: [] }`]

Dev server options. You can use `watch` to make the dev server reload if any file changes in specified paths.

### [[[]]`watchOptions`](#watchoptions) 

Watch options for development mode. See [chokidar](https://github.com/paulmillr/chokidar) for more information.

### [[[]]`imports`](#imports) 

Auto import options. See [unimport](https://github.com/unjs/unimport) for more information.

### [[[]]`plugins`](#plugins) 

-   Default: `[]`

An array of paths to nitro plugins. They will be executed by order on the first initialization.

Note that Nitro auto-register the plugins in the `plugins/` directory, [learn more](/guide/plugins).

### [[[]]`virtual`](#virtual) 

-   Default: ``

A map from dynamic virtual import names to their contents or an (async) function that returns it.

## [[[]]Routing](#routing) 

### [[[]]`baseURL`](#baseurl) 

Default: [`/`] (or `NITRO_APP_BASE_URL` environment variable if provided)

Server\'s main base URL.

### [[[]]`apiBaseURL`](#apibaseurl) 

-   Default : `/api`

Changes the default api base URL prefix.

### [[[]]`handlers`](#handlers) 

Server handlers and routes.

If `server/routes/`, `server/api/` or `server/middleware/` directories exist, they will be automatically added to the handlers array.

### [[[]]`devHandlers`](#devhandlers) 

Regular handlers refer to the path of handlers to be imported and transformed by rollup.

There are situations in that we directly want to provide a handler instance with programmatic usage.

We can use `devHandlers` but note that they are **only available in development mode** and **not in production build**.

For example:

[]

``` 
import  from 'h3'

export default defineNitroConfig()
    }
  ]
})
```

[]Note that `defineEventHandler` is a helper function from [`h3`](https://v1.h3.dev) library.

### [[[]]`devProxy`](#devproxy) 

Proxy configuration for development server.

You can use this option to override development server routes and proxy-pass requests.

[]

``` 

  }
}
```

See [httpxy](https://github.com/unjs/httpxy) for all available target options.

### [[[]]`errorHandler`](#errorhandler) 

Path to a custom runtime error handler. Replacing nitro\'s built-in error page. The error handler is given an `H3Error` and `H3Event`. If the handler returns a promise it is awaited. The handler is expected to send a response of its own. Below is an example where a plain-text response is returned using h3\'s functions.

**Example:**

[][nitro.config]

[][error.ts]

[]

``` 
export default defineNitroConfig();
```

[]

``` 
export default defineNitroErrorHandler((error, event) => );
```

### [[[]]`routeRules`](#routerules) 

**🧪 Experimental!**

Route options. It is a map from route pattern (following [radix3](https://github.com/unjs/rou3/tree/radix3#route-matcher)) to route options.

When `cache` option is set, handlers matching pattern will be automatically wrapped with `defineCachedEventHandler`.

See the [Cache API](/guide/cache) for all available cache options.

[]`swr: true|number` is shortcut for `cache: `

**Example:**

[]

``` 
routeRules: ,
  '/blog/**': ,
  '/blog/**': ,
  '/blog/**':  },
  '/assets/**':  },
  '/api/v1/**':  },
  '/old-page': , // uses status code 307 (Temporary Redirect)
  '/old-page2':  },
  '/old-page/**': ,
  '/proxy/example': ,
  '/proxy/**': ,
}
```

### [[[]]`prerender`](#prerender) 

Default:

[]

``` 

```

Prerendered options. Any route specified will be fetched during the build and copied to the `.output/public` directory as a static asset.

Any route (string) that starts with a prefix listed in `ignore` or matches a regular expression or function will be ignored.

If `crawlLinks` option is set to `true`, nitro starts with `/` by default (or all routes in `routes` array) and for HTML pages extracts `<a>` tags and prerender them as well.

You can set `failOnError` option to `true` to stop the CI when an error if Nitro could not prerender a route.

The `interval` and `concurrency` options lets you control the speed of pre-rendering, can be useful to avoid hitting some rate-limit if you call external APIs.

Set `autoSubfolderIndex` lets you control how to generate the files in the `.output/public` directory:

[]

``` 
# autoSubfolderIndex: true (default)
/about -> .output/public/about/index.html
# autoSubfolderIndex: false
/about -> .output/public/about.html
```

This option is useful when your hosting provider does not give you an option regarding the trailing slash.

The prerenderer will attempt to render pages 3 times with a delay of 500ms. Use `retry` and `retryDelay` to change this behavior.

## [[[]]Directories](#directories) 

### [[[]]`workspaceDir`](#workspacedir) 

Project workspace root directory.

The workspace (e.g. pnpm workspace) directory is automatically detected when the `workspaceDir` option is not set.

### [[[]]`rootDir`](#rootdir) 

Project main directory.

### [[[]]`srcDir`](#srcdir) 

-   Default: (same as `rootDir`)

Project source directory. Same as `rootDir` unless specified. Root directory for `api`, `routes`, `plugins`, `utils`, `public`, `middleware`, `assets`, and `tasks` folders.

### [[[]]`scanDirs`](#scandirs) 

-   Default: (source directory when empty array)

List of directories to scan and auto-register files, such as API routes.

### [[[]]`apiDir`](#apidir) 

-   Default : `api`

Defines a different directory to scan for api route handlers.

### [[[]]`routesDir`](#routesdir) 

-   Default : `routes`

Defines a different directory to scan for route handlers.

### [[[]]`buildDir`](#builddir) 

-   Default: `.nitro`

nitro\'s temporary working directory for generating build-related files.

### [[[]]`output`](#output) 

-   Default: ``

Output directories for production bundle.

## [[[]]Advanced](#advanced) 

### [[[]]`dev`](#dev) 

-   Default: `true` for development and `false` for production.

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

### [[[]]`typescript`](#typescript) 

Default: ``

### [[[]]`nodeModulesDirs`](#nodemodulesdirs) 

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

Additional `node_modules` to search when resolving a module. By default user directory is added.

### [[[]]`hooks`](#hooks) 

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

nitro hooks. See [hookable](https://github.com/unjs/hookable) for more information.

### [[[]]`commands`](#commands) 

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

Preview and deploy command hints are usually filled by deployment presets.

### [[[]]`devErrorHandler`](#deverrorhandler) 

**⚠️ Caution! This is an advanced configuration. Things can go wrong if misconfigured.**

A custom error handler function for development errors.

## [[[]]Rollup](#rollup) 

### [[[]]`rollupConfig`](#rollupconfig) 

Additional rollup configuration.

### [[[]]`entry`](#entry) 

Rollup entry.

### [[[]]`unenv`](#unenv) 

Options for [unenv](https://github.com/unjs/unenv/) preset.

### [[[]]`alias`](#alias) 

Rollup aliases options.

### [[[]]`minify`](#minify) 

-   Default: `false`

Minify bundle.

### [[[]]`inlineDynamicImports`](#inlinedynamicimports) 

Avoid creating chunks.

### [[[]]`sourceMap`](#sourcemap) 

Enable source map generation. See [options](https://rollupjs.org/configuration-options/#output-sourcemap)

-   Default: `true`

### [[[]]`node`](#node) 

Specify whether the build is used for Node.js or not. If set to `false`, nitro tries to mock Node.js dependencies using [unenv](https://github.com/unjs/unenv) and adjust its behavior.

### [[[]]`analyze`](#analyze) 

If enabled, will analyze server bundle after build using [rollup-plugin-visualizer](https://github.com/btd/rollup-plugin-visualizer). You can also pass your custom options.

### [[[]]`moduleSideEffects`](#modulesideeffects) 

Default: `['unenv/polyfill/', 'node-fetch-native/polyfill']`

Rollup specific option. Specifies module imports that have side-effects

### [[[]]`replace`](#replace) 

Rollup specific option.

### [[[]]`commonJS`](#commonjs) 

Rollup specific option. Specifies additional configuration for the rollup CommonJS plugin.

## [[[]]Preset options](#preset-options) 

### [[[]]`firebase`](#firebase) 

The options for the firebase functions preset. See [Preset Docs](/deploy/providers/firebase#options)

### [[[]]`vercel`](#vercel) 

The options for the vercel preset. See [Preset Docs](/deploy/providers/vercel)

### [[[]]`cloudflare`](#cloudflare) 

The options for the cloudflare preset. See [Preset Docs](/deploy/providers/cloudflare)

</div>

-   [[][Edit this page []]](https://github.com/nitrojs/nitro/edit/nitrobuild-git-v2-nitrojs.vercel.app/docs/3.config/0.index.md)

[](/deploy/providers/zerops)

[]

Zerops

Deploy Nitro apps to Zerops.

[ ]

[On this page][[]]

[On this page][[]]

-   [[General]](#general)
    -   [[preset]](#preset)
    -   [[logLevel]](#loglevel)
    -   [[runtimeConfig]](#runtimeconfig)
    -   [[compatibilityDate]](#compatibilitydate)
-   [[Features]](#features)
    -   [[experimental]](#experimental)
    -   [[future]](#future)
    -   [[storage]](#storage)
    -   [[timing]](#timing)
    -   [[renderer]](#renderer)
    -   [[serveStatic]](#servestatic)
    -   [[noPublicDir]](#nopublicdir)
    -   [[publicAssets]](#publicassets)
    -   [[compressPublicAssets]](#compresspublicassets)
    -   [[serverAssets]](#serverassets)
    -   [[devServer]](#devserver)
    -   [[watchOptions]](#watchoptions)
    -   [[imports]](#imports)
    -   [[plugins]](#plugins)
    -   [[virtual]](#virtual)
-   [[Routing]](#routing)
    -   [[baseURL]](#baseurl)
    -   [[apiBaseURL]](#apibaseurl)
    -   [[handlers]](#handlers)
    -   [[devHandlers]](#devhandlers)
    -   [[devProxy]](#devproxy)
    -   [[errorHandler]](#errorhandler)
    -   [[routeRules]](#routerules)
    -   [[prerender]](#prerender)
-   [[Directories]](#directories)
    -   [[workspaceDir]](#workspacedir)
    -   [[rootDir]](#rootdir)
    -   [[srcDir]](#srcdir)
    -   [[scanDirs]](#scandirs)
    -   [[apiDir]](#apidir)
    -   [[routesDir]](#routesdir)
    -   [[buildDir]](#builddir)
    -   [[output]](#output)
-   [[Advanced]](#advanced)
    -   [[dev]](#dev)
    -   [[typescript]](#typescript)
    -   [[nodeModulesDirs]](#nodemodulesdirs)
    -   [[hooks]](#hooks)
    -   [[commands]](#commands)
    -   [[devErrorHandler]](#deverrorhandler)
-   [[Rollup]](#rollup)
    -   [[rollupConfig]](#rollupconfig)
    -   [[entry]](#entry)
    -   [[unenv]](#unenv)
    -   [[alias]](#alias)
    -   [[minify]](#minify)
    -   [[inlineDynamicImports]](#inlinedynamicimports)
    -   [[sourceMap]](#sourcemap)
    -   [[node]](#node)
    -   [[analyze]](#analyze)
    -   [[moduleSideEffects]](#modulesideeffects)
    -   [[replace]](#replace)
    -   [[commonJS]](#commonjs)
-   [[Preset options]](#preset-options)
    -   [[firebase]](#firebase)
    -   [[vercel]](#vercel)
    -   [[cloudflare]](#cloudflare)