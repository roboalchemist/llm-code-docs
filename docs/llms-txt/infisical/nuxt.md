# Source: https://infisical.com/docs/integrations/frameworks/nuxt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Nuxt

> How to use Infisical to inject environment variables and secrets into a Nuxt app.

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* [Install the CLI](/cli/overview)

## Initialize Infisical for your [Nuxt](https://nuxtjs.org) app

```bash  theme={"dark"}
# navigate to the root of your of your project 
cd /path/to/project

# then initialize infisical
infisical init
```

## Start your application as usual but with Infisical

```bash  theme={"dark"}
infisical run -- <your application start command>

# Example
infisical run -- npm run dev
```
