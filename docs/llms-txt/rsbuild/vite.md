# Source: https://rsbuild.dev/guide/migration/vite.md

# Vite

This guide explains how to migrate a Vite project to Rsbuild.

## Installing dependencies

First, replace Vite's npm dependencies with Rsbuild's equivalents.

import { PackageManagerTabs } from '@theme';

* Remove Vite dependencies:

<PackageManagerTabs command="remove vite" />

* Install Rsbuild dependencies:

<PackageManagerTabs command="add @rsbuild/core -D" />

## Updating npm scripts

Next, update the npm scripts in your package.json to run Rsbuild CLI commands.

```json title="package.json"
{
  "scripts": {
    "dev": "vite", // [!code --]
    "build": "vite build", // [!code --]
    "preview": "vite preview", // [!code --]
    "dev": "rsbuild dev", // [!code ++]
    "build": "rsbuild build", // [!code ++]
    "preview": "rsbuild preview" // [!code ++]
  }
}
```

## Create configuration file

Create an Rsbuild configuration file named `rsbuild.config.ts` alongside package.json, and add the following content:

```ts title="rsbuild.config.ts"
import { defineConfig } from '@rsbuild/core';

export default defineConfig({
  plugins: [],
});
```

## Build entry

The default build entry points for Rsbuild and Vite are different. Vite uses `index.html` as the default entry, while Rsbuild uses `src/index.js`.

When migrating from Vite to Rsbuild, use Rsbuild's [source.entry](/config/source/entry.md) to set the build entry and [html.template](/config/html/template.md) to set the template.

Using a newly created Vite project as an example, first delete the `<script>` tags from `index.html`:

```html title="index.html"
<!-- [!code --] -->
<script type="module" src="/src/main.ts"></script>
```

Then add the following configuration:

```ts title="rsbuild.config.ts"
export default {
  html: {
    template: './index.html',
  },
  source: {
    entry: {
      index: './src/main.ts',
    },
  },
};
```

Rsbuild automatically injects the `<script>` tags into the generated HTML files during the build.

## Migrating plugins

Most common Vite plugins can be easily migrated to Rsbuild plugins, such as:

| Vite                                                                                   | Rsbuild                                                                                        |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [@vitejs/plugin-react](https://npmjs.com/package/@vitejs/plugin-react)                 | [@rsbuild/plugin-react](/plugins/list/plugin-react.md)                                            |
| [@vitejs/plugin-react-swc](https://npmjs.com/package/@vitejs/plugin-react-swc)         | [@rsbuild/plugin-react](/plugins/list/plugin-react.md)                                            |
| [@vitejs/plugin-vue](https://npmjs.com/package/@vitejs/plugin-vue)                     | [@rsbuild/plugin-vue](/plugins/list/plugin-vue.md)                                                |
| [@vitejs/plugin-vue2](https://npmjs.com/package/@vitejs/plugin-vue2)                   | [@rsbuild/plugin-vue2](https://github.com/rstackjs/rsbuild-plugin-vue2)                        |
| [@vitejs/plugin-vue-jsx](https://npmjs.com/package/@vitejs/plugin-vue-jsx)             | [@rsbuild/plugin-vue-jsx](https://github.com/rstackjs/rsbuild-plugin-vue-jsx)                  |
| [@vitejs/plugin-vue2-jsx](https://npmjs.com/package/@vitejs/plugin-vue2-jsx)           | [@rsbuild/plugin-vue2-jsx](https://github.com/rstackjs/rsbuild-plugin-vue2-jsx)                |
| [@vitejs/plugin-basic-ssl](https://npmjs.com/package/@vitejs/plugin-basic-ssl)         | [@rsbuild/plugin-basic-ssl](https://github.com/rstackjs/rsbuild-plugin-basic-ssl)              |
| [@vitejs/plugin-legacy](https://npmjs.com/package/@vitejs/plugin-legacy)               | No need to use, see [Browser Compatibility](/guide/advanced/browser-compatibility.md) for details |
| [@sveltejs/vite-plugin-svelte](https://npmjs.com/package/@sveltejs/vite-plugin-svelte) | [@rsbuild/plugin-svelte](/plugins/list/plugin-svelte.md)                                          |
| [vite-plugin-svgr](https://npmjs.com/package/vite-plugin-svgr)                         | [@rsbuild/plugin-svgr](/plugins/list/plugin-svgr.md)                                              |
| [vite-plugin-checker](https://npmjs.com/package/vite-plugin-checker)                   | [@rsbuild/plugin-type-check](https://github.com/rstackjs/rsbuild-plugin-type-check)            |
| [vite-plugin-eslint](https://npmjs.com/package/vite-plugin-eslint)                     | [@rsbuild/plugin-eslint](https://github.com/rstackjs/rsbuild-plugin-eslint)                    |
| [vite-plugin-static-copy](https://npmjs.com/package/vite-plugin-static-copy)           | [output.copy](/config/output/copy.md)                                                             |
| [vite-plugin-node-polyfills](https://npmjs.com/package/vite-plugin-node-polyfills)     | [@rsbuild/plugin-node-polyfill](https://github.com/rstackjs/rsbuild-plugin-node-polyfill)      |
| [vite-plugin-solid](https://npmjs.com/package/vite-plugin-solid)                       | [@rsbuild/plugin-solid](/plugins/list/plugin-solid.md)                                            |
| [@preact/preset-vite](https://npmjs.com/package/@preact/preset-vite)                   | [@rsbuild/plugin-preact](/plugins/list/plugin-preact.md)                                          |

You can refer to [Plugin List](/plugins/list/index.md) to learn more about available plugins.

## Config migration

Here is the corresponding Rsbuild configuration for each Vite option:

| Vite                                  | Rsbuild                                                          |
| ------------------------------------- | ---------------------------------------------------------------- |
| root                                  | [root](/config/root.md)                                             |
| mode                                  | [mode](/config/mode.md)                                             |
| base                                  | [server.base](/config/server/base.md)                               |
| define                                | [source.define](/config/source/define.md)                           |
| plugins                               | [plugins](/config/plugins.md)                                       |
| appType                               | [server.historyApiFallback](/config/server/history-api-fallback.md) |
| envDir                                | [Env directory](/guide/advanced/env-vars.md#env-directory)          |
| logLevel                              | [logLevel](/config/log-level.md)                                    |
| cacheDir                              | [buildCache](/config/performance/build-cache.md)                    |
| publicDir                             | [server.publicDir](/config/server/public-dir.md)                    |
| customLogger                          | [Custom logger](/api/javascript-api/core.md#custom-logger)          |
| assetsInclude                         | [source.assetsInclude](/config/source/assets-include.md)            |
| resolve.alias                         | [resolve.alias](/config/resolve/alias.md)                           |
| resolve.dedupe                        | [resolve.dedupe](/config/resolve/dedupe.md)                         |
| resolve.extensions                    | [resolve.extensions](/config/resolve/extensions.md)                 |
| resolve.conditions                    | [resolve.conditionNames](/config/resolve/condition-names.md)        |
| resolve.mainFields                    | [resolve.mainFields](/config/resolve/main-fields.md)                |
| resolve.preserveSymlinks              | [tools.rspack.resolve.symlinks](/config/tools/rspack.md)            |
| html.cspNonce                         | [security.nonce](/config/security/nonce.md)                         |
| css.modules                           | [output.cssModules](/config/output/css-modules.md)                  |
| css.postcss                           | [tools.postcss](/config/tools/postcss.md)                           |
| css.preprocessorOptions.sass          | [pluginSass](/plugins/list/plugin-sass.md)                          |
| css.preprocessorOptions.less          | [pluginLess](/plugins/list/plugin-less.md)                          |
| css.preprocessorOptions.stylus        | [pluginStylus](/plugins/list/plugin-stylus.md)                      |
| css.devSourcemap                      | [output.sourceMap](/config/output/source-map.md)                    |
| css.lightningcss                      | [tools.lightningcssLoader](/config/tools/lightningcss-loader.md)    |
| server.host, preview.host             | [server.host](/config/server/host.md)                               |
| server.port, preview.port             | [server.port](/config/server/port.md)                               |
| server.cors, preview.cors             | [server.cors](/config/server/cors.md)                               |
| server.strictPort, preview.strictPort | [server.strictPort](/config/server/strict-port.md)                  |
| server.https, preview.https           | [server.https](/config/server/https.md)                             |
| server.open, preview.open             | [server.open](/config/server/open.md)                               |
| server.proxy, preview.proxy           | [server.proxy](/config/server/proxy.md)                             |
| server.headers, preview.headers       | [server.headers](/config/server/headers.md)                         |
| server.hmr                            | [dev.hmr](/config/dev/hmr.md), [dev.client](/config/dev/client.md)     |
| server.middlewareMode                 | [server.middlewareMode](/config/server/middleware-mode.md)          |
| build.target, build.cssTarget         | [Browserslist](/guide/advanced/browserslist.md)                     |
| build.outDir, build.assetsDir         | [output.distPath](/config/output/dist-path.md)                      |
| build.assetsInlineLimit               | [output.dataUriLimit](/config/output/data-uri-limit.md)             |
| build.cssMinify                       | [output.minify](/config/output/minify.md)                           |
| build.sourcemap                       | [output.sourceMap](/config/output/source-map.md)                    |
| build.lib                             | Use [Rslib](https://github.com/web-infra-dev/rslib)              |
| build.manifest                        | [output.manifest](/config/output/manifest.md)                       |
| build.ssrEmitAssets                   | [output.emitAssets](/config/output/emit-assets.md)                  |
| build.minify, build.terserOptions     | [output.minify](/config/output/minify.md)                           |
| build.emptyOutDir                     | [output.cleanDistPath](/config/output/clean-dist-path.md)           |
| build.copyPublicDir                   | [server.publicDir](/config/server/public-dir.md)                    |
| build.reportCompressedSize            | [performance.printFileSize](/config/performance/print-file-size.md) |
| ssr, worker                           | [environments](/config/environments.md)                             |

Notes:

* The table above doesn't cover every Vite option; feel free to add more.

## Environment variables

Vite injects environment variables starting with `VITE_` into the client code by default, while Rsbuild injects environment variables starting with `PUBLIC_` by default (see [public variables](/guide/advanced/env-vars.md#public-variables)).

To match Vite's behavior, you can manually call Rsbuild's [loadEnv](/api/javascript-api/core.md#loadenv) method to read environment variables starting with `VITE_`, and inject them into the client code through the [source.define](/config/source/define.md) config.

```ts title="rsbuild.config.ts"
import { defineConfig, loadEnv } from '@rsbuild/core';

const { publicVars } = loadEnv({ prefixes: ['VITE_'] });

export default defineConfig({
  source: {
    define: publicVars,
  },
});
```

Rsbuild injects the following [environment variables](/guide/advanced/env-vars.md) by default:

* `import.meta.env.MODE`
* `import.meta.env.BASE_URL`
* `import.meta.env.PROD`
* `import.meta.env.DEV`

For `import.meta.env.SSR`, you can set it through the [environments](/config/environments.md) and [source.define](/config/source/define.md) configuration options:

```ts title="rsbuild.config.ts"
export default defineConfig({
  environments: {
    web: {
      source: {
        define: {
          'import.meta.env.SSR': JSON.stringify(false),
        },
      },
    },
    node: {
      source: {
        define: {
          'import.meta.env.SSR': JSON.stringify(true),
        },
      },
      output: {
        target: 'node',
      },
    },
  },
});
```

## Preset types

Vite provides some preset type definitions through the `vite-env.d.ts` file. When migrating to Rsbuild, you can use the [preset types](/guide/basic/typescript.md#preset-types) provided by `@rsbuild/core`:

```ts title="src/env.d.ts"
// [!code --]
/// <reference types="vite/client" />
// [!code ++]
/// <reference types="@rsbuild/core/types" />
```

## Glob import

Vite provides `import.meta.glob()` for importing multiple modules.

When migrating to Rsbuild, you can use the [import.meta.webpackContext()](https://rspack.rs/api/runtime-api/module-variables#importmetawebpackcontext) function of Rspack instead:

* Vite:

```js
const modules = import.meta.glob('./dir/*.js');

for (const path in modules) {
  modules[path]().then((mod) => {
    console.log(path, mod);
  });
}
```

* Rsbuild:

```js
const context = import.meta.webpackContext('./dir', {
  // Whether to search subdirectories
  recursive: false,
  regExp: /\.js$/,
});

for (const path of context.keys()) {
  const mod = context(path);
  console.log(path, mod);
}
```

## vite-tsconfig-paths

Rsbuild supports TypeScript's `paths` option as alias out of the box, so you can remove the `vite-tsconfig-paths` dependency directly.

See [Path aliases](/guide/advanced/alias.md) for more details.

## Migrating Vite plugins

See [Vite plugin](/guide/migration/vite-plugin.md) to learn how to migrate Vite plugins.

## Validating results

After completing the steps above, the basic migration from Vite to Rsbuild is complete. You can now run the `npm run dev` command to try starting the dev server.

If you encounter issues during the build process, debug using the error log, or check the Vite configuration for any settings that haven't been migrated to Rsbuild.

## Contents supplement

This document covers only part of the migration process. If you have content to add, feel free to contribute via a pull request 🤝.

> The documentation for rsbuild can be found in the [rsbuild/website](https://github.com/web-infra-dev/rsbuild/tree/main/website) directory.
