# Source: https://lingui.dev/ref/metro-transformer.md

# Metro Transformer

[Metro bundler](https://metrobundler.dev/) is a JavaScript bundler used in React Native apps. The `@lingui/metro-transformer` offers an alternative to the [`lingui compile`](/ref/cli.md#compile) command: a transformer that enables Metro to compile `.po` files on the fly.

The transformer enables you to `import` `.po` files directly, instead of running `lingui compile` and `import`ing the resulting JavaScript (or TypeScript) files.

## Installation[​](#installation "Direct link to Installation")

> Only Expo SDK 50 and React Native v0.73.0 or newer are supported.

Install `@lingui/metro-transformer` as a development dependency:

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/metro-transformer
```

```
yarn add --dev @lingui/metro-transformer
```

```
pnpm add --save-dev @lingui/metro-transformer
```

Set up the transformer in your `metro.config.js` by specifying [`babelTransformerPath`](https://metrobundler.dev/docs/configuration/#babeltransformerpath) and updating `sourceExts`.

If you need to combine multiple transformers, use [this approach](https://stackoverflow.com/a/57660231/2070942):

<!-- -->

* Expo
* Plain React Native

metro.config.js

```
// Learn more https://docs.expo.io/guides/customizing-metro
const { getDefaultConfig } = require("expo/metro-config");

const config = getDefaultConfig(__dirname);
const { transformer, resolver } = config;

config.transformer = {
  ...transformer,
  babelTransformerPath: require.resolve("@lingui/metro-transformer/expo"),
};
config.resolver = {
  ...resolver,
  sourceExts: [...resolver.sourceExts, "po", "pot"],
};

module.exports = config;
```

metro.config.js

```
const { getDefaultConfig, mergeConfig } = require("@react-native/metro-config");

const defaultConfig = getDefaultConfig(__dirname);
const { assetExts, sourceExts } = defaultConfig.resolver;

/**
 * Metro configuration
 * https://reactnative.dev/docs/metro
 *
 * @type {import('metro-config').MetroConfig}
 */
const config = {
  transformer: {
    babelTransformerPath: require.resolve("@lingui/metro-transformer/react-native"),
  },
  resolver: {
    sourceExts: [...sourceExts, "po", "pot"],
  },
};

module.exports = mergeConfig(defaultConfig, config);
```

## Usage[​](#usage "Direct link to Usage")

tip

Take a look at the [example app](https://github.com/lingui/js-lingui/tree/main/examples/react-native) that uses the transformer. The transformer only supports catalogs based on `po` and `pot` files.

The library is currently in beta. If you encounter any issues, please [report them](https://github.com/lingui/js-lingui/issues).

1. Import `.po` files directly in your code:

   ```
   -import { messages } from "./src/locales/en/messages.ts";
   +import { messages } from "./src/locales/en/messages.po";
   ```

2. If you are using TypeScript, you need to add `.po` file declaration so that TypeScript understands the file extension:

   src/po-types.d.ts

   ```
   declare module "*.po" {
     import type { Messages } from "@lingui/core";
     export const messages: Messages;
   }
   ```

3. Restart Metro bundler with `expo start -c` or `yarn start --reset-cache` to clear the transformer cache.

4. Profit! 🎉

danger

Whenever you make a change to the Lingui config file (this should not happen often), restart Metro bundler.

## See Also[​](#see-also "Direct link to See Also")

* [React Native i18n Tutorial](/tutorials/react-native.md)
* [Lingui React Native Example App](https://github.com/lingui/js-lingui/tree/main/examples/react-native)
