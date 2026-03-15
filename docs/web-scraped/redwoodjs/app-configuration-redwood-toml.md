# Source: https://docs.redwoodjs.com/docs/app-configuration-redwood-toml

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [App Configuration]

[Version: 8.8]

On this page

<div>

# App Configuration: redwood.toml

</div>

One of the premier places you can configure your Redwood app is `redwood.toml`. By default, `redwood.toml` lists the following configuration options:

redwood.toml

``` 
[web]
  title = "Redwood App"
  port = 8910
  apiUrl = "/.redwood/functions"
  includeEnvironmentVariables = []
[api]
  port = 8911
[browser]
  open = true
[notifications]
  versionUpdates = ["latest"]
```

These are listed by default because they\'re the ones that you\'re most likely to configure, but there are plenty more available.

You can think of `redwood.toml` as a frontend for configuring Redwood\'s build tools. For certain options, instead of having to configure build tools directly, there\'s quick access via `redwood.toml`.

## \[web\][​](#web "Direct link to [web]") 

Key

Description

Default

`title`

Title of your Redwood app

`'Redwood App'`

`port`

Port for the web server to listen at

`8910`

`apiUrl`

URL to your api server. This can be a relative URL in which case it acts like a proxy, or a fully-qualified URL

`'/.redwood/functions'`

`includeEnvironmentVariables`

Environment variables made available to the web side during dev and build

`[]`

`host`

Hostname for the web server to listen at

Defaults to `'0.0.0.0'` in production and `'::'` in development

`apiGraphQLUrl`

URL to your GraphQL function

`'$/graphql'`

`apiDbAuthUrl`

URL to your dbAuth function

`'$/auth'`

`sourceMap`

Enable source maps for production builds

`false`

`a11y`

Enable storybook `addon-a11y` and `eslint-plugin-jsx-a11y`

`true`

### Customizing the GraphQL Endpoint[​](#customizing-the-graphql-endpoint "Direct link to Customizing the GraphQL Endpoint") 

By default, Redwood derives the GraphQL endpoint from `apiUrl` such that it\'s `$/graphql`, (with the default `apiUrl`, `./redwood/functions/graphql`). But sometimes you want to host your api side somewhere else. There\'s two ways you can do this:

1.  Change `apiUrl`:

redwood.toml

``` 
[web]
  apiUrl = "https://api.coolredwoodapp.com"
```

Now the GraphQL endpoint is at `https://api.coolredwoodapp.com/graphql`.

2.  Change `apiGraphQLUrl`:

redwood.toml

``` 
 [web]
   apiUrl = "/.redwood/functions"
+  apiGraphQLUrl = "https://api.coolredwoodapp.com/graphql"
```

### Customizing the dbAuth Endpoint[​](#customizing-the-dbauth-endpoint "Direct link to Customizing the dbAuth Endpoint") 

Similarly, if you\'re using dbAuth, you may decide to host it somewhere else. To do this without affecting your other endpoints, you can add `apiDbAuthUrl` to your `redwood.toml`:

redwood.toml

``` 
 [web]
   apiUrl = "/.redwood/functions"
+  apiDbAuthUrl = "https://api.coolredwoodapp.com/auth"
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

If you host your web and api sides at different domains and don\'t use a proxy, make sure you have [CORS](/docs/cors) configured. Otherwise browser security features may block client requests.

### includeEnvironmentVariables[​](#includeenvironmentvariables "Direct link to includeEnvironmentVariables") 

`includeEnvironmentVariables` is the set of environment variables that should be available to your web side during dev and build. Use it to include env vars like public keys for third-party services you\'ve defined in your `.env` file:

redwood.toml

``` 
[web]
  includeEnvironmentVariables = ["PUBLIC_KEY"]
```

.env

``` 
PUBLIC_KEY=...
```

Instead of including them in `includeEnvironmentVariables`, you can also prefix them with `REDWOOD_ENV_` (see [Environment Variables](/docs/environment-variables#web)).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]`includeEnvironmentVariables` isn\'t for secrets

Don\'t make secrets available to your web side. Everything in `includeEnvironmentVariables` is included in the bundle.

## \[api\][​](#api "Direct link to [api]") 

Key

Description

Default

`port`

Port for the api server to listen at

`8911`

`host`

Hostname for the api server to listen at

Defaults to `'0.0.0.0'` in production and `'::'` in development

`schemaPath`

The location of your Prisma schema. If you have [enabled Prisma multi file schemas](https://www.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema), then its value is the directory where your `schema.prisma` can be found, for example: `'./api/db/schema'`

Defaults to `'./api/db/schema.prisma'`

`debugPort`

Port for the debugger to listen at

`18911`

Additional server configuration can be done using [Server File](/docs/docker#using-the-server-file)

### Multi File Schema[​](#multi-file-schema "Direct link to Multi File Schema") 

Prisma\'s `prismaSchemaFolder` [feature](https://www.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema) allows you to define multiple files in a schema subdirectory of your prisma directory.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]Important

If you wish to [organize your Prisma Schema into multiple files](https://www.prisma.io/blog/organize-your-prisma-schema-with-multi-file-support), you will need [enable](https://www.prisma.io/docs/orm/prisma-schema/overview/location#multi-file-prisma-schema) that feature in Prisma, move your `schema.prisma` file into a new directory such as `./api/db/schema` and then set `schemaPath` in the api toml config.

For example:

redwood.toml

``` 
[api]
  port = 8911
  schemaPath = "./api/db/schema"
```

## \[browser\][​](#browser "Direct link to [browser]") 

redwood.toml

``` 
[browser]
  open = true
```

Setting `open` to `true` opens your browser to `http://$:$` (by default, `http://localhost:8910`) after the dev server starts. If you want your browser to stop opening when you run `yarn rw dev`, set this to `false`. (Or just remove it entirely.)

There\'s actually a lot more you can do here. For more, see Vite\'s docs on [`preview.open`](https://vitejs.dev/config/preview-options.html#preview-open).

## \[generate\][​](#generate "Direct link to [generate]") 

redwood.toml

``` 
[generate]
  tests = true
  stories = true
```

Many of Redwood\'s generators create Jest tests or Storybook stories. Understandably, this can be lot of files, and sometimes you don\'t want all of them, either because you don\'t plan on using Jest or Storybook, or are just getting started and don\'t want the overhead. These options allows you to disable the generation of test and story files.

## \[cli\][​](#cli "Direct link to [cli]") 

redwood.toml

``` 
[notifications]
  versionUpdates = ["latest"]
```

There are new versions of the framework all the time---a major every couple months, a minor every week or two, and patches when appropriate. And if you\'re on an experimental release line, like canary, there\'s new versions every day, multiple times.

If you\'d like to get notified (at most, once a day) when there\'s a new version, set `versionUpdates` to include the version tags you\'re interested in.

## Using Environment Variables in `redwood.toml`[​](#using-environment-variables-in-redwoodtoml "Direct link to using-environment-variables-in-redwoodtoml") 

You may find yourself wanting to change keys in `redwood.toml` based on the environment you\'re deploying to. For example, you may want to point to a different `apiUrl` in your staging environment.

You can do so with environment variables. Let\'s look at an example:

redwood.toml

``` 
[web]
  title = "App running on $"
  port = "$"
  apiUrl = "$"
  includeEnvironmentVariables = []
```

This `$` syntax does the following:

-   sets `title` by interpolating the env var `APP_TITLE`
-   sets `port` to the env var `PORT`, falling back to `8910`
-   sets `apiUrl` to the env var `API_URL`, falling back to `/.redwood/functions` (the default)

That\'s pretty much all there is to it. Just remember two things:

1.  fallback is always a string
2.  these values are interpolated at build time

## Running in a Container or VM[​](#running-in-a-container-or-vm "Direct link to Running in a Container or VM") 

To run a Redwood app in a container or VM, you\'ll want to set both the web and api\'s `host` to `0.0.0.0` to allow network connections to and from the host:

redwood.toml

``` 
[web]
  host = '0.0.0.0'
[api]
  host = '0.0.0.0'
```

You can also configure these values via `REDWOOD_WEB_HOST` and `REDWOOD_API_HOST`. And if you set `NODE_ENV` to production, these will be the defaults anyway.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/app-configuration-redwood-toml.md)