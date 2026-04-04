# Source: https://rsbuild.dev/guide/migration/vue-cli.md

# Vue CLI

This chapter introduces how to migrate a [Vue CLI](https://github.com/vuejs/vue-cli) project to Rsbuild.

## Install dependencies

First, you need to replace the npm dependencies of Vue CLI with Rsbuild's dependencies.

import { PackageManagerTabs } from '@theme';

* Remove Vue CLI dependencies:

<PackageManagerTabs command="remove @vue/cli-service @vue/cli-plugin-babel @vue/cli-plugin-eslint core-js" />

* Install Rsbuild dependencies:

<PackageManagerTabs command="add @rsbuild/core @rsbuild/plugin-vue -D" />

:::tip
If your project is based on Vue 2, replace `@rsbuild/plugin-vue` with `@rsbuild/plugin-vue2`.
:::

## Update npm scripts

Next, you need to update the npm scripts in the package.json file to Rsbuild's CLI commands.

```json title="package.json"
{
  "scripts": {
    "serve": "vue-cli-service serve", // [!code --]
    "build": "vue-cli-service build", // [!code --]
    "serve": "rsbuild dev", // [!code ++]
    "build": "rsbuild build", // [!code ++]
    "preview": "rsbuild preview" // [!code ++]
  }
}
```

:::tip
Rsbuild does not integrate ESLint, so it does not provide a command to replace `vue-cli-service lint`. You can directly use ESLint's [CLI commands](https://eslint.org/docs/latest/use/command-line-interface) as an alternative.
:::

## Create configuration file

Create a Rsbuild configuration file `rsbuild.config.ts` in the same directory as package.json, and add the following content:

```ts title="rsbuild.config.ts"
import { defineConfig } from '@rsbuild/core';
import { pluginVue } from '@rsbuild/plugin-vue';

export default defineConfig({
  plugins: [pluginVue()],
  source: {
    // Specify the entry file
    entry: {
      index: './src/main.js',
    },
  },
});
```

:::tip
If your project is based on Vue 2, use `import { pluginVue2 } from '@rsbuild/plugin-vue2';`.
:::

## HTML template

Vue CLI uses the `public/index.html` file as the default HTML template. In Rsbuild, you can specify the HTML template through [html.template](/config/html/template.md):

```ts title="rsbuild.config.ts"
export default defineConfig({
  html: {
    template: './public/index.html',
  },
});
```

In the HTML template, if you are using the `BASE_URL` variable from Vue CLI, replace it with Rsbuild's [assetPrefix variable](/config/html/template-parameters.md) and use a forward slash for concatenation:

```html
<link rel="icon" href="<%= BASE_URL %>favicon.ico" />
<!-- [!code --] -->
<link rel="icon" href="<%= assetPrefix %>/favicon.ico" />
<!-- [!code ++] -->
```

This completes the basic migration from Vue CLI to Rsbuild. You can now run the `npm run serve` command to try starting the dev server.

## Config migration

Here is the corresponding Rsbuild configuration for Vue CLI configuration:

| Vue CLI                                                                                                                                 | Rsbuild                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [publicPath](https://cli.vuejs.org/config/#publicpath)                                                                                  | [dev.assetPrefix](/config/dev/asset-prefix.md) / [output.assetPrefix](/config/output/asset-prefix.md)                                                        |
| [outputDir](https://cli.vuejs.org/config/#outputdir) / [assetsDir](https://cli.vuejs.org/config/#assetsdir)                             | [output.distPath](/config/output/dist-path.md)                                                                                                            |
| [filenameHashing](https://cli.vuejs.org/config/#filenamehashing)                                                                        | [output.filenameHash](/config/output/filename-hash.md)                                                                                                    |
| [pages](https://cli.vuejs.org/config/#pages)                                                                                            | [source.entry](/config/source/entry.md) / [html.template](/config/html/template.md) / [html.title](/config/html/title.md)                                       |
| [transpileDependencies](https://cli.vuejs.org/config/#transpiledependencies)                                                            | [source.include](/config/source/include.md)                                                                                                               |
| [productionSourceMap](https://cli.vuejs.org/config/#productionsourcemap) / [css.sourceMap](https://cli.vuejs.org/config/#css-sourcemap) | [output.sourceMap](/config/output/source-map.md)                                                                                                          |
| [crossorigin](https://cli.vuejs.org/config/#crossorigin)                                                                                | [html.crossorigin](/config/html/crossorigin.md)                                                                                                           |
| [configureWebpack](https://cli.vuejs.org/config/#configurewebpack)                                                                      | [tools.rspack](/config/tools/rspack.md)                                                                                                                   |
| [chainWebpack](https://cli.vuejs.org/config/#chainwebpack)                                                                              | [tools.bundlerChain](/config/tools/bundler-chain.md)                                                                                                      |
| [css.extract](https://cli.vuejs.org/config/#css-extract)                                                                                | [output.injectStyles](/config/output/inject-styles.md)                                                                                                    |
| [css.loaderOptions](https://cli.vuejs.org/config/#css-loaderoptions)                                                                    | [tools.cssLoader](/config/tools/css-loader.md) / [less](/plugins/list/plugin-less.md) / [sass](/plugins/list/plugin-sass.md) / [postcss](/config/tools/postcss.md) |
| [devServer.proxy](https://cli.vuejs.org/config/#devserver-proxy)                                                                        | [server.proxy](/config/server/proxy.md)                                                                                                                   |

Notes:

* When migrating `configureWebpack`, note that most of the webpack and Rsbuild configs are the same, but there are also some differences or functionalities not implemented in Rsbuild.
* The above table does not cover all configurations of Vue CLI, feel free to add more.

## Environment variables

Vue CLI injects environment variables starting with `VUE_APP_` into the client code by default, while Rsbuild injects environment variables starting with `PUBLIC_` by default (see [public variables](/guide/advanced/env-vars.md#public-variables)).

To be compatible with Vue CLI's behavior, you can manually call Rsbuild's [loadEnv](/api/javascript-api/core.md#loadenv) method to read environment variables starting with `VUE_APP_`, and inject them into the client code through the [source.define](/config/source/define.md) config.

```ts title="rsbuild.config.ts"
import { defineConfig, loadEnv } from '@rsbuild/core';

const { publicVars } = loadEnv({ prefixes: ['VUE_APP_'] });

export default defineConfig({
  source: {
    define: publicVars,
  },
});
```

## Contents supplement

The current document only covers part of the migration process. If you find suitable content to add, feel free to contribute to the documentation via pull request 🤝.

> The documentation for rsbuild can be found in the [rsbuild/website](https://github.com/web-infra-dev/rsbuild/tree/main/website) directory.
