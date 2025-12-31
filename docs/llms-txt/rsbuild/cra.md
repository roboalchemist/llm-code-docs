# Source: https://rsbuild.dev/guide/migration/cra.md

# Create React App

This chapter introduces how to migrate a [Create React App](https://github.com/facebook/create-react-app) (CRA) or [CRACO](https://craco.js.org/) project to Rsbuild.

:::tip CRA eject
If your project has already run the CRA `eject` command, then most of the content in this document will no longer be applicable.

After ejecting a CRA project, it becomes more like a project directly using webpack, so you can refer to the [webpack migration guide](/guide/migration/webpack.md).

:::

## Installing dependencies

First, you need to replace the npm dependencies of CRA with Rsbuild's dependencies.

import { PackageManagerTabs } from '@theme';

* Remove CRA dependencies:

<PackageManagerTabs command="remove react-scripts" />

> For projects using CRACO, you can also remove the @craco/craco dependency.

* Install Rsbuild dependencies:

<PackageManagerTabs command="add @rsbuild/core @rsbuild/plugin-react -D" />

## Updating npm scripts

Next, you need to update the npm scripts in package.json to Rsbuild's CLI commands.

```json title="package.json"
{
  "scripts": {
    "start": "react-scripts start", // [!code --]
    "build": "react-scripts build", // [!code --]
    "eject": "react-scripts eject", // [!code --]
    "start": "rsbuild dev", // [!code ++]
    "build": "rsbuild build", // [!code ++]
    "preview": "rsbuild preview" // [!code ++]
  }
}
```

:::tip
Rsbuild doesn't include built-in testing frameworks, so it does not provide a command to replace `react-scripts test`. You can directly use testing frameworks such as [Rstest](https://github.com/web-infra-dev/rstest), Jest or Vitest. Check the [Testing](/guide/advanced/testing.md) section for more details.
:::

## Creating configuration file

Create a Rsbuild configuration file `rsbuild.config.ts` in the same directory as package.json and add the following content:

```ts title="rsbuild.config.ts"
import { defineConfig } from '@rsbuild/core';
import { pluginReact } from '@rsbuild/plugin-react';

export default defineConfig({
  plugins: [pluginReact()],
});
```

## HTML template

CRA uses the `public/index.html` file as the default HTML template. In Rsbuild, you can specify the HTML template through [html.template](/config/html/template.md):

```ts title="rsbuild.config.ts"
export default defineConfig({
  html: {
    template: './public/index.html',
  },
});
```

In the HTML template, if you are using the `%PUBLIC_URL%` variable from CRA, replace it with Rsbuild's [assetPrefix variable](/config/html/template-parameters.md) and use a forward slash for concatenation:

```html
<!-- [!code --] -->
<link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
<!-- [!code ++] -->
<link rel="icon" href="<%= assetPrefix %>/favicon.ico" />
```

This completes the basic migration from CRA to Rsbuild. You can now run the `npm run start` command to try starting the dev server.

## Output directory

By default, CRA outputs to the `build` directory, while Rsbuild's default output directory is `dist`.

You can configure Rsbuild's [output.distPath.root](/config/output/dist-path.md) option to change the directory to `build`, in line with CRA:

```ts title="rsbuild.config.ts"
export default {
  output: {
    distPath: {
      root: 'build',
    },
  },
};
```

> For more details, please refer to the [Output Files](/guide/basic/output-files.md) section.

## Using CSS preprocessors

Rsbuild supports CSS preprocessors such as Sass and Less through plugins. Please refer to:

* [Sass Plugin](/plugins/list/plugin-sass.md)
* [Less Plugin](/plugins/list/plugin-less.md)
* [Stylus Plugin](/plugins/list/plugin-stylus.md)

## Using SVGR

If you are using the "SVG to React Component" feature of CRA (i.e., [SVGR](https://react-svgr.com/)), you also need to install the SVGR plugin for Rsbuild.

For example, if you are using the following usage:

```jsx
import { ReactComponent as Logo } from './logo.svg';

const App = () => (
  <div>
    <Logo />
  </div>
);
```

You only need to install and register `@rsbuild/plugin-svgr`:

```ts title="rsbuild.config.ts"
import { pluginSvgr } from '@rsbuild/plugin-svgr';

export default {
  plugins: [pluginSvgr({ mixedImport: true })],
};
```

Please refer to the [SVGR plugin](/plugins/list/plugin-svgr.md) documentation to learn how to use SVGR in Rsbuild.

## Config migration

Here is the corresponding Rsbuild configuration for [CRA configuration](https://create-react-app.dev/docs/advanced-configuration/):

| CRA                     | Rsbuild                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------- |
| HOST                    | [server.host](/config/server/host.md)                                                              |
| PORT                    | [server.port](/config/server/port.md)                                                              |
| HTTPS                   | [server.https](/config/server/https.md)                                                            |
| WDS\_SOCKET\_HOST         | [dev.client.host](/config/dev/client.md)                                                           |
| WDS\_SOCKET\_PATH         | [dev.client.path](/config/dev/client.md)                                                           |
| WDS\_SOCKET\_PORT         | [dev.client.port](/config/dev/client.md)                                                           |
| PUBLIC\_URL              | [dev.assetPrefix](/config/dev/asset-prefix.md) / [output.assetPrefix](/config/output/asset-prefix.md) |
| BUILD\_PATH              | [output.distPath](/config/output/dist-path.md)                                                     |
| GENERATE\_SOURCEMAP      | [output.sourceMap](/config/output/source-map.md)                                                   |
| IMAGE\_INLINE\_SIZE\_LIMIT | [output.dataUriLimit](/config/output/data-uri-limit.md)                                            |
| FAST\_REFRESH            | [dev.hmr](/config/dev/hmr.md)                                                                      |
| TSC\_COMPILE\_ON\_ERROR    | [@rsbuild/plugin-type-check](https://github.com/rstackjs/rsbuild-plugin-type-check)             |

Notes:

* The above table does not cover all configurations of CRA, feel free to add more.

## Compile node\_modules

By default, CRA uses Babel to compile dependencies in node\_modules, but Rsbuild does not, to avoid the performance overhead and potential compilation errors caused by secondary compilation.

To handle syntax compatibility issues caused by dependencies in node\_modules, you can use the [source.include](/config/source/include.md#compile-node_modules) config to compile node\_modules.

```ts title="rsbuild.config.ts"
export default {
  source: {
    // Compile all JS files and exclude core-js
    include: [{ not: /[\\/]core-js[\\/]/ }],
  },
};
```

## Environment variables

CRA injects environment variables starting with `REACT_APP_` into the client code by default, while Rsbuild injects environment variables starting with `PUBLIC_` by default (see [public variables](/guide/advanced/env-vars.md#public-variables)).

To be compatible with CRA's behavior, you can manually call Rsbuild's [loadEnv](/api/javascript-api/core.md#loadenv) method to read environment variables starting with `REACT_APP_`, and inject them into the client code through the [source.define](/config/source/define.md) config.

```ts title="rsbuild.config.ts"
import { defineConfig, loadEnv } from '@rsbuild/core';

const { publicVars } = loadEnv({ prefixes: ['REACT_APP_'] });

export default defineConfig({
  source: {
    define: publicVars,
  },
});
```

Note that CRA allows access to the full `process.env` object in the code and also allows destructuring of `process.env`. However, Rsbuild does not define the `process.env` object due to bundle size and security concerns.

```ts title="src/index.js"
// In CRA, you can access it like this
const { PUBLIC_URL } = process.env;
console.log(PUBLIC_URL);
console.log(process.env);
```

In Rsbuild, you can use the [source.define](/config/source/define.md) config to set `process.env` and read the `rawPublicVars` returned by the `loadEnv` method to allow the above usage:

```ts title="rsbuild.config.ts"
import { defineConfig, loadEnv } from '@rsbuild/core';

const { publicVars, rawPublicVars } = loadEnv({ prefixes: ['REACT_APP_'] });

export default defineConfig({
  source: {
    define: {
      ...publicVars,
      'process.env': JSON.stringify(rawPublicVars),
    },
  },
});
```

## Import unknown assets

In CRA, if you import an asset that the build tool cannot recognize, CRA will by default output the file to the `build/static/media` directory, for example, the `document.pdf` file:

```js title="index.js"
import document from './document.pdf';
```

In Rsbuild, when you import unrecognized assets, Rsbuild will output error logs:

```
You may need an appropriate loader to handle this file type.
```

To resolve this error, you can use the following methods:

* Configure a suitable loader to handle this type of asset via [tools.rspack](/config/tools/rspack.md).
* Configure [asset modules](https://rspack.rs/guide/features/asset-module) rule to handle this type of asset via [tools.rspack](/config/tools/rspack.md).

For example, you can add the following asset modules config to get the same output result as CRA:

```ts title="rsbuild.config.ts"
export default {
  tools: {
    rspack: {
      module: {
        rules: [
          {
            // Match .png asset
            // You can change this regular expression to match different types of files
            test: /\.png$/,
            type: 'asset/resource',
            generator: {
              filename: 'static/media/[name].[hash][ext]',
            },
          },
        ],
      },
    },
  },
};
```

## Remove react-app-polyfill

CRA provides [react-app-polyfill](https://npmjs.com/package/react-app-polyfill) to manually inject polyfill code.

In the Rsbuild project, you can remove the dependency and code related to react-app-polyfill, as Rsbuild will automatically read the browserslist config and allow you to enable polyfill injection through the [output.polyfill](/config/output/polyfill.md) config.

1. Remove the `react-app-polyfill` reference:

```ts title="src/index.js"
import 'react-app-polyfill/ie11'; // [!code --]
import 'react-app-polyfill/stable'; // [!code --]
```

2. Configure [output.polyfill](/config/output/polyfill.md):

```ts title="rsbuild.config.ts"
export default {
  output: {
    polyfill: 'usage',
  },
};
```

> Read [Browser compatibility](/guide/advanced/browser-compatibility.md) to understand how Rsbuild handles polyfills.

## Setup ESLint

CRA uses ESLint to lint the code by default. Rsbuild does not include linting by default, but you can add a separate npm script to run ESLint in `package.json`.

First, install [eslint](https://eslint.org/) and [eslint-config-react-app](https://npmjs.com/package/eslint-config-react-app), you need to install ESLint v8 to keep consistent with CRA:

<PackageManagerTabs command="add eslint@8 eslint-config-react-app -D" />

Then, add the `lint` command in `package.json`, and confirm that the project contains an `eslintConfig` configuration or an independent ESLint configuration file:

```json title="package.json"
{
  "scripts": {
    "lint": "eslint src"
  },
  "eslintConfig": {
    "extends": ["react-app", "react-app/jest"]
  }
}
```

Then, you can use the `npm run lint` command to run ESLint.

### Run ESLint during the build

In addition to adding the `lint` command in `package.json`, you can also add the [@rsbuild/plugin-eslint](https://github.com/rstackjs/rsbuild-plugin-eslint) plugin to maintain the same behavior as CRA.

`@rsbuild/plugin-eslint` allows you to run ESLint during the build process.

```ts title="rsbuild.config.ts"
import { pluginEslint } from '@rsbuild/plugin-eslint';

export default {
  plugins: [pluginEslint()],
};
```

After registering the plugin, ESLint will run automatically during development (`npm run dev`) and production builds (`npm run build`). The plugin will display ESLint warnings and errors in the console output.

:::warning
We do not recommend using the `@rsbuild/plugin-eslint` plugin, as running ESLint during the build process will significantly increase the build time. Instead, we recommend using a separate `lint` command to run ESLint checks.
:::

## Reading jsconfig.json

In non-TypeScript projects, CRA supports reading the `paths` field in jsconfig.json as the path alias.

To use this feature in Rsbuild, refer to the [Path Alias - jsconfig.json](/guide/advanced/alias.md#jsconfigjson).

## CRACO migration

If your project is using [CRACO](https://craco.js.org) to override CRA configuration, you can refer to the table below for migration:

| CRACO                                                                                           | Rsbuild                                                                             |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [webpack.configure](https://craco.js.org/docs/configuration/webpack/#webpackconfigure)          | [tools.rspack](/config/tools/rspack.md)                                                |
| [webpack.alias](https://craco.js.org/docs/configuration/webpack/#webpackalias)                  | [resolve.alias](/config/resolve/alias.md)                                              |
| [webpack.plugins.add](https://craco.js.org/docs/configuration/webpack/#webpackplugins)          | [appendPlugins of tools.rspack](/config/tools/rspack.md#appendplugins)                 |
| [webpack.plugins.remove](https://craco.js.org/docs/configuration/webpack/#webpackpluginsremove) | [removePlugin of tools.rspack](/config/tools/rspack.md#removeplugin)                   |
| [style.modules](https://craco.js.org/docs/configuration/style/#stylemodules)                    | [output.cssModules](/config/output/css-modules.md)                                     |
| [style.css](https://craco.js.org/docs/configuration/style/#stylecss)                            | [tools.cssLoader](/config/tools/css-loader.md)                                         |
| [style.sass](https://craco.js.org/docs/configuration/style/#stylesass)                          | [Sass Plugin](/plugins/list/plugin-sass.md)                                            |
| [style.postcss](https://craco.js.org/docs/configuration/style/#stylepostcss)                    | [tools.postcss](/config/tools/postcss.md)                                              |
| [babel](https://craco.js.org/docs/configuration/babel/)                                         | [Babel Plugin](/plugins/list/plugin-babel.md)                                          |
| [typescript](https://craco.js.org/docs/configuration/typescript/)                               | [@rsbuild/plugin-type-check](https://github.com/rstackjs/rsbuild-plugin-type-check) |
| [devServer](https://craco.js.org/docs/configuration/devserver/)                                 | [server configs](/config/index.md)                                                     |

### Example

Here is an example of migrating from `webpack.configure` to `tools.rspack`:

* Before migration:

```js title="craco.config.js"
const { whenDev } = require('@craco/craco');

module.exports = {
  webpack: {
    configure: {
      resolve: {
        mainFields: ['browser', 'module', 'main'],
      },
    },
    plugins: [...whenDev(() => [new MyWebpackPlugin()], [])],
  },
};
```

* After migration:

```ts title="rsbuild.config.ts"
export default {
  tools: {
    rspack: {
      resolve: {
        mainFields: ['browser', 'module', 'main'],
      },
      plugins:
        process.env.NODE_ENV === 'development' ? [new MyWebpackPlugin()] : [],
    },
  },
};
```

## Contents supplement

The current document only covers part of the migration process. If you find suitable content to add, feel free to contribute to the documentation via pull request 🤝.

> The documentation for rsbuild can be found in the [rsbuild/website](https://github.com/web-infra-dev/rsbuild/tree/main/website) directory.
