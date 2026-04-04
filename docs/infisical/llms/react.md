# Source: https://infisical.com/docs/integrations/frameworks/react.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# React

> How to use Infisical to inject environment variables and secrets into a React app.

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* [Install the CLI](/cli/overview)

## Initialize Infisical for your [Create React App](https://create-react-app.dev)

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

<Info>
  React environment variables must be prefixed with `REACT_APP_` to show up within the application
</Info>
