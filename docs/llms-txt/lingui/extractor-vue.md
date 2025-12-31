# Source: https://lingui.dev/ref/extractor-vue.md

# Vue.js Extractor

The `@lingui/extractor-vue` package provides a custom extractor that handles Vue.js files.

## Installation[​](#installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/extractor-vue
```

```
yarn add --dev @lingui/extractor-vue
```

```
pnpm add --save-dev @lingui/extractor-vue
```

## Usage[​](#usage "Direct link to Usage")

It is required that you use JavaScript or TypeScript for your Lingui configuration.

lingui.config.{js,ts}

```
import { defineConfig } from "@lingui/cli";
import { vueExtractor } from "@lingui/extractor-vue";
import babel from "@lingui/cli/api/extractors/babel";

export default defineConfig({
  locales: ["en", "nb"],
  sourceLocale: "en",
  catalogs: [
    {
      path: "<rootDir>/src/{locale}",
      include: ["<rootDir>/src"],
    },
  ],
  extractors: [babel, vueExtractor],
});
```

## See Also[​](#see-also "Direct link to See Also")

* [Message Extraction](/guides/message-extraction.md)
* [Custom Extractor](/guides/custom-extractor.md)
