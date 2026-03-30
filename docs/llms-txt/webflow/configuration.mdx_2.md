# Source: https://developers.webflow.com/cli/configuration.mdx

***

title: Configure your Webflow project
slug: configuration
description: Learn how to configure your Webflow project with the Webflow CLI.
hidden: false
subtitle: Learn how to configure your Webflow project with the Webflow CLI.
---------------------------------------------------------------------------

The `webflow.json` file configures your Webflow project, defining how the CLI builds and deploys your code for each product. This file is created automatically when you run `init` commands, but you can modify it to customize behavior.

## File location

Place `webflow.json` in your the root of your project:

<Files>
  <Folder name="my-webflow-project" defaultOpen>
    <Folder name="src">
      <File name="components/Button.webflow.tsx" />
    </Folder>

    <File name="webflow.json" highlighted />

    <File name="package.json" />
  </Folder>
</Files>

## Schema

The `webflow.json` supports configuration for:

* Code Components
* DevLink
* Webflow Cloud
* Designer Extensions

Each product has its own set of configuration options. See below for the configuration options for each product.

### Code Components

```json title="webflow.json"
{
    "library": {
        "name": "<Your Library Name>",
        "components": ["./src/**/*.webflow.@(js|jsx|mjs|ts|tsx)"],
        "bundleConfig": "./webpack.webflow.js"
    }
}
```

| Field          | Description                                                                                                                    | Required |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `name`         | The name of your component library as it appears in Webflow                                                                    | Yes      |
| `components`   | Glob pattern matching your component files. To target a specific folder, use a path like `src/my-components/**/*.webflow.tsx`. | Yes      |
| `bundleConfig` | Path to a [custom webpack configuration](/code-components/webpack-configuration-overrides) file                                | No       |

***

### DevLink

```json
{
  "devlink": {
    "rootDir": "./devlink",
    "cssModules": true,
    "fileExtensions": {
      "js": "jsx"
    }
  }
}
```

### Configuration options

| Option             | Description                                           | Default                              | Required |
| :----------------- | :---------------------------------------------------- | :----------------------------------- | :------- |
| `host`             | Webflow API host URL                                  | `https://api.webflow.com`            | No       |
| `rootDir`          | Directory to export components into                   | `./devlink`                          | Yes      |
| `siteId`           | Webflow site ID                                       | `process.env.WEBFLOW_SITE_ID`        | No       |
| `authToken`        | Webflow API authentication token                      | `process.env.WEBFLOW_SITE_API_TOKEN` | No       |
| `cssModules`       | Enable CSS modules for component styles               | `true`                               | No       |
| `allowTelemetry`   | Allow anonymous usage analytics                       | `true`                               | No       |
| `envVariables`     | Inject environment variables into exported components | `{}`                                 | No       |
| `components`       | Regex pattern to match components to export           | `.*`                                 | No       |
| `overwriteModule`  | Whether to overwrite the module file                  | `true`                               | No       |
| `fileExtensions`   | File extensions for exported components               | `{ js: ".js", css: ".css" }`         | No       |
| `skipTagSelectors` | Exclude tag/ID/attribute selectors from global CSS    | `false`                              | No       |
| `relativeHrefRoot` | Control how relative `href` attributes are resolved   | `/`                                  | No       |

While DevLink will try to assume reasonable defaults for most of the settings, you can specify certain options to customize the behavior of DevLink management and setup. See the [DevLink documentation](/devlink/docs/component-export/installation#configuration-options) for more details.

***

### Webflow Cloud

```json
{
  "cloud": {
    "projectId": "<Your Project ID>",
    "framework": "astro"
  }
}
```

| Field       | Description                                                                                                 | Required |
| ----------- | ----------------------------------------------------------------------------------------------------------- | -------- |
| `projectId` | Cloud project identifier. This is automatically set by the Webflow CLI when you run `webflow cloud deploy`. | Yes      |
| `framework` | Framework preset either `nextjs` or `astro`                                                                 | Yes      |

***

### Designer Extensions

```json
{
  "name": "<Your Extension Name>",
  "apiVersion": "2",
  "publicDir": "dist",
  "appIntents": {
    "image": ["manage"],
    "form": ["manage"]
  },
  "appConnections": [
    "myAppImageConnection",
    "myAppFormConnection"
  ]
}
```

| Field            | Description                                                     | Default | Required |
| :--------------- | :-------------------------------------------------------------- | :------ | :------- |
| `name`           | The name of your extension as it appears in Webflow             | -       | Yes      |
| `apiVersion`     | The API version to use for your extension                       | `2`     | Yes      |
| `publicDir`      | The directory to build and serve the extension from             | `dist`  | Yes      |
| `appIntents`     | The element types that can create connections to your extension | `{}`    | No       |
| `appConnections` | The element types that can create connections to your extension | `[]`    | No       |
