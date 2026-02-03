# Source: https://infisical.com/docs/integrations/frameworks/vite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vite

> How to use Infisical to inject environment variables and secrets into a Vite app.

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* [Install the CLI](/cli/overview)

## Initialize Infisical for your [Vite](https://vitejs.dev) app

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

<Note>
  Note that for environment variables to be exposed to the client, you'll have
  to prefix them with `VITE_` and export them from the `vite.config.js` file.
  Read more about that [here](https://vitejs.dev/guide/env-and-mode.html) and
  [here](https://main.vitejs.dev/config).
</Note>
