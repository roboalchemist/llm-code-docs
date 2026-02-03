# Source: https://infisical.com/docs/integrations/frameworks/express.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Express, Fastify, Koa

> How to use Infisical to inject environment variables and secrets into an Express app.

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* [Install the CLI](/cli/overview)

The steps apply to the following non-exhaustive list of frameworks:

* [Express](https://expressjs.com)
* [Fastify](https://www.fastify.io)
* [Koa](https://koajs.com)

## Initialize Infisical for your app

```bash  theme={"dark"}
# navigate to the root of your of your project 
cd /path/to/project

# then initialize Infisical
infisical init
```

## Start your application as usual but with Infisical

```bash  theme={"dark"}
infisical run -- <your application start command>

# Example
infisical run -- npm run dev
```
