# Source: https://lingui.dev/ref/vite-plugin.md

# Vite Plugin

Vite is a blazing fast frontend build tool powering the next generation of web applications.

The `@lingui/vite-plugin` is a Vite plugin that compiles Lingui catalogs on the fly and provides the necessary configuration for seamless integration with Vite.

[![npm-version](https://img.shields.io/npm/v/@lingui/vite-plugin?logo=npm\&cacheSeconds=1800)](https://www.npmjs.com/package/@lingui/vite-plugin) [![npm-downloads](https://img.shields.io/npm/dt/@lingui/vite-plugin?cacheSeconds=500)](https://www.npmjs.com/package/@lingui/vite-plugin)

## Installation[​](#installation "Direct link to Installation")

Install `@lingui/vite-plugin` as a development dependency:

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/vite-plugin
```

```
yarn add --dev @lingui/vite-plugin
```

```
pnpm add --save-dev @lingui/vite-plugin
```

For a complete installation guide, see [Installation and Setup](/installation.md#vite).

## Usage[​](#usage "Direct link to Usage")

To integrate Lingui with Vite, add the `@lingui/vite-plugin` inside your `vite.config.ts` as follows:

vite.config.ts

```
import { UserConfig } from "vite";
import { lingui } from "@lingui/vite-plugin";

const config: UserConfig = {
  plugins: [lingui()],
};
```

Then use [dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#dynamic_imports) in your code to load only necessary catalog:

```
export async function dynamicActivate(locale: string) {
  const { messages } = await import(`./locales/${locale}.po`);

  i18n.load(locale, messages);
  i18n.activate(locale);
}
```

Remember that the file extension is mandatory.

tip

If you are using a format that has a different extension than `*.po`, you need to specify the `?lingui` suffix:

```
const { messages } = await import(`./locales/${language}.json?lingui`);
```

## See Also[​](#see-also "Direct link to See Also")

* [Dynamic Loading](/guides/dynamic-loading-catalogs.md)
* [Dynamic Import in Vite](https://vitejs.dev/guide/features.html#dynamic-import)
