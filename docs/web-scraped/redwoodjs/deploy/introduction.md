# Source: https://docs.redwoodjs.com/docs/deploy/introduction

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Deployment](/docs/deployment/index)
-   [Introduction]

[Version: 8.8]

On this page

<div>

# Introduction to Deployment

</div>

Redwood is designed for both serverless and traditional infrastructure deployments, offering a unique continuous deployment process in both cases:

1.  code is committed to a repository on GitHub, GitLab, or Bitbucket, which triggers the deployment
2.  the Redwood API Side and Web Side are individually prepared via a build process
3.  during the build process, any database related actions are run (e.g. migrations)
4.  the hosting provider deploys the built Web static assets to a CDN and the API code to a serverless backend (e.g. AWS Lambdas)

Currently, these are the officially supported deploy targets:

-   Baremetal (physical server that you have SSH access to)
-   [Coherence](https://www.withcoherence.com/)
-   [Flightcontrol.dev](https://www.flightcontrol.dev?ref=redwood)
-   [Edg.io](https://edg.io)
-   [Netlify.com](https://www.netlify.com/)
-   [Render.com](https://render.com)
-   [Serverless.com](https://serverless.com)
-   [Vercel.com](https://vercel.com)

Redwood has a CLI generator that adds the code and configuration required by the specified provider (see the [CLI Doc](/docs/cli-commands#deploy-config) for more information):

``` 
yarn rw setup deploy <provider>
```

There are examples of deploying Redwood on other providers such as Google Cloud and direct to AWS. You can find more information by searching the [GitHub Issues](https://github.com/redwoodjs/redwood/issues) and [Forums](https://community.redwoodjs.com).

## General Deployment Setup[​](#general-deployment-setup "Direct link to General Deployment Setup") 

Deploying Redwood requires setup for the following four categories.

### 1. Host Specific Configuration[​](#1-host-specific-configuration "Direct link to 1. Host Specific Configuration") 

Each hosting provider has different requirements for how (and where) the deployment is configured. Sometimes you\'ll need to add code to your repository, configure settings in a dashboard, or both. You\'ll need to read the provider specific documentation.

The most important Redwood configuration is to set the `apiUrl` in your `redwood.toml` This sets the API path for your serverless functions specific to your hosting provider.

### 2. Build Command[​](#2-build-command "Direct link to 2. Build Command") 

The build command is used to prepare the Web and API for deployment. Additionally, other actions can be run during build such as database migrations. The Redwood build command must specify one of the supported hosting providers (aka `target`):

``` 
yarn rw deploy <target>
```

For example:

``` 
# Build command for Netlify deploy target
yarn rw deploy netlify
```

``` 
# Build command for Vercel deploy target
yarn rw deploy vercel
```

``` 
# Build command for AWS Lambdas using the https://serverless.com framework
yarn rw deploy serverless --side api
```

``` 
# Build command for Edgio deploy target
yarn rw deploy edgio
```

``` 
# Build command for baremetal deploy target
yarn rw deploy baremetal [--first-run]
```

### 3. Prisma and Database[​](#3-prisma-and-database "Direct link to 3. Prisma and Database") 

Redwood uses Prisma for managing database access and migrations. The settings in `api/prisma/schema.prisma` must include the correct deployment database, e.g. postgresql, and the database connection string.

To use PostgreSQL in production, include this in your `schema.prisma`:

``` 
datasource db 
```

The `url` setting above accesses the database connection string via an environment variable, `DATABASE_URL`. Using env vars is the recommended method for both ease of development process as well as security best practices.

Whenever you make changes to your `schema.prisma`, you must run the following command:

``` 
yarn rw prisma migrate dev # creates and applies a new Prisma DB migration
```

> Note: when setting your production DATABASE_URL env var, be sure to also set any connection-pooling or sslmode parameters. For example, if using Supabase Postgres with pooling, then you would use a connection string similar to `postgresql://postgres:mydb.supabase.co:6432/postgres?sslmode=require&pgbouncer=true` that uses a specific 6432 port, informs Prisma to consider pgBouncer, and also to use SSL. See: [Connection Pooling](/docs/connection-pooling) for more info.

### 4. Environment Variables[​](#4-environment-variables "Direct link to 4. Environment Variables") 

Any environment variables used locally, e.g. in your `env.defaults` or `.env`, must also be added to your hosting provider settings. (See documentation specific to your provider.)

Additionally, if your application uses env vars on the Web Side, you must configure Redwood\'s build process to make them available in production. See the [Redwood Environment Variables doc](/docs/environment-variables) for instructions.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/deploy/introduction.md)