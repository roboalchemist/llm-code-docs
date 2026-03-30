# Source: https://developers.webflow.com/cli/reference/webflow-cli.mdx

***

title: Introduction to the Webflow CLI
description: Introduction to the Webflow CLI
subtitle: Get started developing and deploying code with the Webflow CLI
------------------------------------------------------------------------

The [Webflow CLI](https://www.npmjs.com/package/@webflow/webflow-cli) brings Webflow development into your local environment, allowing you to use your own tools, workflows, and version control. Use the CLI to build and share code components, manage Webflow Cloud deployments, and sync code with your Webflow sites directly from the command line.

With the CLI, you can:

<CardGroup cols={2}>
  <Card
    title="Share Code Components"
    iconPosition="left"
    iconSize="12"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/ComponentsCode.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/ComponentsCode.svg" alt="" className="light-icon" />
    </>
  }
  >
    Create reusable React components and deploy them directly to the Webflow Designer.
  </Card>

  <Card
    title="Export components with DevLink"
    iconPosition="left"
    iconSize="12"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/DevLink.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/DevLink.svg" alt="" className="light-icon" />
    </>
  }
  >
    Export your Webflow Components as React components.
  </Card>

  <Card
    title="Deploy to Webflow Cloud"
    iconPosition="left"
    iconSize="12"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CloudHosting.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CloudHosting.svg" alt="" className="light-icon" />
    </>
  }
  >
    Host and manage full-stack applications with serverless functions, data storage, and dynamic routing.
  </Card>

  <Card
    title="Create Designer Extensions"
    iconPosition="left"
    iconSize="12"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Designer.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Designer.svg" alt="" className="light-icon" />
    </>
  }
  >
    Develop custom applications that run directly inside the Webflow Designer.
  </Card>
</CardGroup>

***

## Installation

Install the Webflow CLI globally using npm:

```bash
npm install -g @webflow/webflow-cli
```

Verify the installation:

```bash
webflow --version
```

***

## Authentication

Authentication connects your local environment to your Webflow account, enabling you to deploy and sync code with Webflow.

```bash
webflow auth login
```

This opens your browser to complete authentication for a single workspace, site, or multiple sites within a workspace. Once successful, your credentials are stored locally for future commands. For more information, see the [authentication documentation](/cli/authentication).

***

## Configuration

The `webflow.json` file is used to configure the CLI and should always be in the root of your project. Here you'll define your project type, and the configuration for each product you're using.

Below is an example of a `webflow.json` file for a project that uses Code Components, DevLink, and Webflow Cloud. To see more on configuration, see the [configuration documentation](/cli/configuration).

```json
{
  "cloud": {
    "projectId": "<Your Project ID>",
    "framework": "astro"
  },
  "devlink": {
    "rootDir": "./devlink",
    "cssModules": true,
    "fileExtensions": {
      "js": "jsx"
    }
  },
  "extensions": {
    "name": "<Your Extension Name>",
    "apiVersion": "2",
    "publicDir": "dist"
  },
  "library": {
    "name": "<Your Library Name>",
    "components": ["./src/**/*.webflow.@(js|jsx|mjs|ts|tsx)"],
    "bundleConfig": "./webpack.webflow.js"
  }
}
```

***

## Product-specific commands

The CLI is organized by product:

| Command             | Product                                                 |
| ------------------- | ------------------------------------------------------- |
| `webflow library`   | [Code Components](/code-components/reference/cli)       |
| `webflow devlink`   | [DevLink](/devlink/reference/cli)                       |
| `webflow cloud`     | [Webflow Cloud](/webflow-cloud)                         |
| `webflow extension` | [Designer Extensions](/designer/reference/introduction) |

Each command namespace includes additional commands specific to that product. Use `--help` with any command to see available options:

```bash
webflow library --help
```

For more information on each command, see the [command reference](/cli/command-reference).
