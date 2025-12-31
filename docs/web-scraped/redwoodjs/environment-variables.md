# Source: https://docs.redwoodjs.com/docs/environment-variables

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Environment Variables]

[Version: 8.8]

On this page

<div>

# Environment Variables

</div>

You can provide environment variables to each side of your Redwood app in different ways, depending on each Side\'s target, and whether you\'re in development or production.

> Right now, Redwood apps have two fixed Sides, API and Web, that each have a single target, nodejs and browser respectively.

## Generally[​](#generally "Direct link to Generally") 

Redwood apps use [dotenv](https://github.com/motdotla/dotenv) to load vars from your `.env` file into `process.env`. For a reference on dotenv syntax, see the dotenv README\'s [Rules](https://github.com/motdotla/dotenv#rules) section.

> Technically, we use [dotenv-defaults](https://github.com/mrsteele/dotenv-defaults), which is how we also supply and load `.env.defaults`.

Redwood also configures Vite, so that all references to `process.env` vars on the Web side will be replaced with the variable\'s actual value at build-time. More on this in [Web](#Web).

## Web[​](#web "Direct link to Web") 

### Including environment variables[​](#including-environment-variables "Direct link to Including environment variables") 

> **Heads Up:** for Web to access environment variables in production, you *must* configure one of the options below.
>
> Redwood recommends **Option 1: `redwood.toml`** as it is the most robust.

In production, you can get environment variables to the Web Side either by

1.  adding to `redwood.toml` via the `includeEnvironmentVariables` array, or
2.  prefixing with `REDWOOD_ENV_`

Just like for the API Side, you\'ll also have to set them up with your provider. Some hosting providers distinguish between build and runtime environments for configuring environment variables. Environment variables for the web side should in those cases be configured as build-time variables.

#### Option 1: includeEnvironmentVariables in redwood.toml[​](#option-1-includeenvironmentvariables-in-redwoodtoml "Direct link to Option 1: includeEnvironmentVariables in redwood.toml") 

For Example:

redwood.toml

``` 
[web]
  includeEnvironmentVariables = ['SECRET_API_KEY', 'ANOTHER_ONE']
```

By adding environment variables to this array, they\'ll be available to Web in production via `process.env.SECRET_API_KEY`. This means that if you have an environment variable like `process.env.SECRET_API_KEY` Redwood removes and replaces it with its *actual* value.

Note: if someone inspects your site\'s source, *they could see your `REDWOOD_ENV_SECRET_API_KEY` in plain text.* This is a limitation of delivering static JS and HTML to the browser.

#### Option 2: Prefixing with REDWOOD_ENV\_[​](#option-2-prefixing-with-redwood_env_ "Direct link to Option 2: Prefixing with REDWOOD_ENV_") 

In `.env`, if you prefix your environment variables with `REDWOOD_ENV_`, they\'ll be available via `process.env.REDWOOD_ENV_MY_VAR_NAME`, and will be dynamically replaced at build-time.

Like the option above, these are also removed and replaced with the *actual value* during build in order to be available in production.

### Accessing API URLs[​](#accessing-api-urls "Direct link to Accessing API URLs") 

Redwood automatically makes your API URL configurations from the web section of your `redwood.toml` available globally. They\'re accessible via the `window` or `global` objects. For example, `global.RWJS_API_GRAPHQL_URL` gives you the URL for your graphql endpoint.

The toml values are mapped as follows:

`redwood.toml` key

Available globally as

Description

`apiUrl`

`global.RWJS_API_URL`

URL or absolute path to your api-server

`apiGraphQLUrl`

`global.RWJS_API_GRAPHQL_URL`

URL or absolute path to GraphQL function

See the [redwood.toml reference](/docs/app-configuration-redwood-toml#api-paths) for more details.

## Development Fatal Error Page[​](#development-fatal-error-page "Direct link to Development Fatal Error Page") 

.env

``` 
REDWOOD_ENV_EDITOR=vscode
```

Redwood comes with a `FatalErrorPage` that displays helpful information---like the stack trace and the request---when something breaks.

> `FatalErrorPage` isn\'t bundled when deploying to production

As part of the stack trace, there are links to the original source files so that they can be quickly opened in your editor. The page defaults to VSCode, but you can override the editor by setting the environment variable `REDWOOD_ENV_EDITOR`.

## API[​](#api "Direct link to API") 

### Development[​](#development "Direct link to Development") 

You can access environment variables defined in `.env` and `.env.defaults` as `process.env.VAR_NAME`. For example, if we define the environment variable `HELLO_ENV` in `.env`:

``` 
HELLO_ENV=hello world
```

and make a hello Function (`yarn rw generate function hello`) and reference `HELLO_ENV` in the body of our response:

./api/src/functions/hello.js

``` 
export const handler = async (event, context) => `,
  }
}
```

Navigating to [http://localhost:8911/hello](http://localhost:8911/hello) shows that the Function successfully accesses the environment variable:

![rw-envVars-api](https://user-images.githubusercontent.com/32992335/86520528-47112100-bdfa-11ea-8d7e-1c0d502805b2.png)

### Production[​](#production "Direct link to Production") 

Whichever platform you deploy to, they\'ll have some specific way of making environment variables available to the serverless environment where your Functions run. For example, if you deploy to Netlify, you set your environment variables in **Settings** \> **Build & Deploy** \> **Environment**. You\'ll just have to read your provider\'s documentation. Some hosting providers distinguish between build and runtime environments for configuring environment variables. Environment variables for the api side should in those cases be configured as runtime variables.

## Keeping Sensitive Information Safe[​](#keeping-sensitive-information-safe "Direct link to Keeping Sensitive Information Safe") 

Since it usually contains sensitive information, you should [never commit your `.env` file](https://github.com/motdotla/dotenv#should-i-commit-my-env-file). Note that you\'d actually have to go out of your way to do this as, by default, a Redwood app\'s `.gitignore` explicitly ignores `.env`:

``` 
.DS_Store
.env
.netlify
dev.db
dist
dist-babel
node_modules
yarn-error.log
```

## Where Does Redwood Load My Environment Variables?[​](#where-does-redwood-load-my-environment-variables "Direct link to Where Does Redwood Load My Environment Variables?") 

For all the variables in your `.env` and `.env.defaults` files to make their way to `process.env`, there has to be a call to `dotenv`\'s `config` function somewhere. So where is it?

It\'s in [the CLI](https://github.com/redwoodjs/redwood/blob/main/packages/cli/src/index.js#L6-L12)---every time you run a `yarn rw` command:

packages/cli/src/index.js

``` 
import  from 'dotenv-defaults'

config()
```

Remember, if `yarn rw dev` is already running, your local app won\'t reflect any changes you make to your `.env` file until you stop and re-run `yarn rw dev`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/environment-variables.md)