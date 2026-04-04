# Source: https://rspack.dev/plugins/webpack/banner-plugin.md

# BannerPlugin

```js
new rspack.BannerPlugin(options);
```

Adds a banner to the top or bottom of each generated chunk.

## Options

- **Type:**

```ts
type BannerFunction = (args: {
  hash: string;
  chunk: Chunk;
  filename: string;
}) => string;
type BannerContent = string | BannerFunction;
type BannerPluginOptions = {
  banner: BannerContent;
  entryOnly?: boolean;
  footer?: boolean;
  raw?: boolean;
  stage?: number;
  test?: BannerRules;
  include?: BannerRules;
  exclude?: BannerRules;
};
type BannerPluginArgument = BannerContent | BannerPluginOptions;
```

- **Default:** `undefined`

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `banner` | `BannerFunction|string` | undefined | Specifies the banner, it will be wrapped in a comment. |
| `entryOnly` | `boolean|undefined` | undefined | If true, the banner will only be added to the entry chunks. |
| `footer` | `boolean|undefined` | undefined | If true, banner will be placed at the end of the output. |
| `raw` | `boolean|undefined` | undefined | If true, banner will not be wrapped in a comment. |
| `stage` | `number|undefined` | `PROCESS_ASSETS_STAGE_ADDITIONS`(-100) | The stage of the compilation in which the banner should be injected. |
| `test` | `BannerRules|undefined` | undefined | Include all modules that pass test assertion. |
| `include` | `BannerRules|undefined` | undefined | Include all modules matching any of these conditions. |
| `exclude` | `BannerRules|undefined` | undefined | Exclude all modules matching any of these conditions. |


## Examples

Add a banner to the bottom of each chunk file.

```js title="rspack.config.mjs"
import { rspack } from '@rspack/core';

export default {
  plugins: [
    new rspack.BannerPlugin({
      banner: 'hello world',
      footer: true,
    }),
  ],
};
```
