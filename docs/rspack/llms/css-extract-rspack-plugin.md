# Source: https://rspack.dev/plugins/rspack/css-extract-rspack-plugin.md

# CssExtractRspackPlugin

Rspack only
Rspack is currently incompatible with [mini-css-extract-plugin](https://github.com/webpack/mini-css-extract-plugin), but you can use the CssExtractRspackPlugin as a replacement. It can be used with css-loader to extract CSS into separate files.

> If your project does not depend on on css-loader and mini-css-extract-plugin, it is recommended to use Rspack's built-in CSS solution, which offers better performance.

## Example

When using CssExtractRspackPlugin, you need to register the plugin in the `plugins` section and register `CssExtractRspackPlugin.loader` in [module.rules](/config/module.md#modulerules).

```ts title="rspack.config.mjs"
import { rspack } from '@rspack/core';

export default {
  plugins: [new rspack.CssExtractRspackPlugin({})],
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [rspack.CssExtractRspackPlugin.loader, 'css-loader'],
        type: 'javascript/auto',
      },
    ],
  },
};
```

## Plugin options

Options for `CssExtractRspackPlugin`.

- **Types:**

```ts
interface PluginOptions {
  filename?: string | ((pathData: PathData, assetInfo?: AssetInfo) => string);
  chunkFilename?:
    | string
    | ((pathData: PathData, assetInfo?: AssetInfo) => string);
  ignoreOrder?: boolean;
  insert?: string | ((linkTag: HTMLLinkElement) => void);
  attributes?: Record<string, string>;
  linkType?: string | 'text/css' | false;
  runtime?: boolean;
  pathinfo?: boolean;
  enforceRelative?: boolean;
}
```

| Name | Type | Default Value | Description |
| --- | --- | --- | --- |
| `filename` | `string` | "[name].css" | The name of each CSS output file, please refer to `output.filename` |
| `chunkFilename` | `string` | "[name].css" | The name of the asynchronously loaded CSS files. If not set, it will use `filename`; please refer to `output.chunkFilename` |
| `ignoreOrder` | `boolean` | false | Whether to issue a warning if there are conflicts in the order of some CSS in different chunks. For example, entryA introduces a.css and b.css, entryB introduces b.css and a.css, and the order of a.css and b.css cannot be determined |
| `insert` | `string | ((linkTag: HTMLLinkElement) => void)` | undefined | Decide how the link tag is inserted into the page. If passed as a string type, it will be regarded as DOM selector, and the link tag will be inserted after element corresponding to that selector. If passed as function type, the function will be converted into a string at runtime for invocation, with link tag as parameter |
| `attributes` | `Record<string, string>` | undefined | Adds custom attributes to the `link` tag for async CSS chunks |
| `linkType` | `string | 'text/css' | false` | "text/css" | Set the `type` attribute value for link tags to load async CSS chunks |
| `runtime` | `boolean` | true | Whether to inject runtime code for CSS loading. If disabled, CSS will be still extracted and can be used for a custom loading methods |
| `pathinfo` | `boolean` | false | Whether to include comments in CSS bundles with more detailed path information |
| `enforceRelative` | `boolean` | false | Whether to preserve "./" when generated CSS `url()` is relative |


## Loader options

Options for `CssExtractRspackPlugin.loader`.

- **Types:**

```ts
interface LoaderOptions {
  publicPath?: string | ((resourcePath: string, context: string) => string);
  emit?: boolean;
  esModule?: boolean;
}
```

| Name | Type | Default Value | Description |
| --- | --- | --- | --- |
| `publicPath` | `string | ((resourcePath: string, context: string) => string)` | output.publicPath | Specifies a custom public path for the external resources like images, files, etc inside CSS |
| `emit` | `boolean` | true | If true, emits CSS files. If false, the plugin will extract the CSS but will not emit files |
| `esModule` | `boolean` | true | whether to use ES modules syntax for CSS Modules class name exports in the generated JavaScript module |


## Note

Please note that if you want to use this plugin and css together, it's recommended to explicitly set type to `javascript/auto`.

For example:

```ts title="rspack.config.mjs"
import { rspack } from '@rspack/core';

export default {
  plugins: [new rspack.CssExtractRspackPlugin({})],
  module: {
    rules: [
      {
        test: /src\/legacy-project\/.*\.css$/,
        type: 'javascript/auto', // Cover the default CSS module type and treat it as a regular JS file.
        use: [rspack.CssExtractRspackPlugin.loader, 'css-loader'],
      },
      {
        test: /src\/new-project\/.*\.css$/,
        type: 'css/auto', // Handle with built-in CSS
      },
    ],
  },
};
```
