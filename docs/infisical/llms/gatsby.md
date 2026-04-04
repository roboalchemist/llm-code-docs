# Source: https://infisical.com/docs/integrations/frameworks/gatsby.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gatsby

> How to use Infisical to inject environment variables and secrets into a Gatsby app.

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* [Install the CLI](/cli/overview)

## Initialize Infisical for your [Gatsby](https://www.gatsbyjs.com) app

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
infisical run -- npm run develop
```

<Note>
  Note that for environment variables to be exposed to the client, you'll have
  to prefix them with `GATSBY_`. Read more about that
  [here](https://www.gatsbyjs.com/docs/how-to/local-development/environment-variables/#accessing-environment-variables-in-the-browser).
</Note>
