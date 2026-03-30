# Source: https://developers.webflow.com/code-components/installation.mdx

***

title: Installation
slug: installation
description: Learn how to configure your Component Library for code components.
hidden: false
subtitle: Learn how to configure your React project for code components.
canonical-url: '[https://developers.webflow.com/code-components/installation](https://developers.webflow.com/code-components/installation)'
-------------------------------------------------------------------------------------------------------------------------------------------

This reference describes the configuration requirements to setup DevLink in a React project for component imports.

## Setup requirements

### Webflow CLI

Install the Webflow CLI and the necessary dependencies to import React components into Webflow:

```bash
npm i --save-dev @webflow/webflow-cli @webflow/data-types @webflow/react
```

**What you get:**

* `@webflow/webflow-cli` - CLI used to publish components to Webflow
* `@webflow/data-types` - TypeScript definitions for Webflow props
* `@webflow/react` - React utilities for code components

See the [CLI reference](/code-components/reference/cli) for publishing commands.

### `webflow.json`

The `webflow.json` file is used to configure DevLink for component imports. Use this file to define the name of your library and the components that should be included in the library. Additionally, you can specify a custom webpack configuration file to use for [bundling your components.](/code-components/bundling-and-import)

Create or update `webflow.json` in the root of your project with the following configuration:

```json title={"webflow.json"}
{
    "library": {
        "name": "<Your Library Name>",
        "components": ["./src/**/*.webflow.@(js|jsx|mjs|ts|tsx)"],
        "bundleConfig": "./webpack.webflow.js",
        "globals": "./src/globals.webflow.ts"
    }
}

```

| Field                  | Description                                                                                        | Required |
| ---------------------- | -------------------------------------------------------------------------------------------------- | -------- |
| `library.name`         | The name of your component library as it appears in Webflow                                        | Yes      |
| `library.components`   | Glob pattern matching your component files                                                         | Yes      |
| `library.bundleConfig` | Path to a [custom webpack configuration](/code-components/webpack-configuration-overrides) file    | No       |
| `library.globals`      | Path to a [Component Decorators](/code-components/define-code-component#component-decorators) file | No       |

## Authentication

When importing your component library to Webflow using the `npx webflow library share` command, the Webflow CLI will prompt you to authenticate with Webflow. Once authenticated, DevLink will save the token to your `.env` file.

### Manual authentication

To manually authenticate with Webflow, run the `webflow library share` command with the `--api-token` option and include a [Workspace API token](#workspace-api-token) in the command. This is useful when sharing your component library to a different workspace.

```bash
npx webflow library share --api-token <your-api-token>
```

### Workspace API token

DevLink publishes your component library to a Webflow workspace. To publish to the correct workspace, you must provide a [workspace API token](/data/reference/authentication/workspace-token) for authentication.

<Warning title="Workspace admin required">
  You must be a Workspace Admin to create a Workspace token.
</Warning>

To get your workspace API token:

1. Open your workspace and navigate to **Apps & Integrations.**
2. In the left sidebar. Click **Manage**
3. Scroll to the bottom section labeled **Workspace API Access**
4. Click **Generate API Token** and copy the token.
5. Add the token to your `.env` file.

<Warning title="Security best practices">
  Never commit your `.env` file to version control. Be sure to add `.env` to your `.gitignore` file.
</Warning>

## Next steps

After configuration, you can:

* [Define a code component](/code-components/define-code-component)
* [Publish your library](/code-components/reference/cli)

## Related topics

* [Getting started with code components](/code-components/introduction/quick-start)
* [Webflow CLI reference](/code-components/reference/cli)
* [Workspace API token](/data/reference/authentication/workspace-token)
