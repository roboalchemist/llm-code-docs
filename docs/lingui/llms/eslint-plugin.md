# Source: https://lingui.dev/ref/eslint-plugin.md

# ESLint Plugin

Lingui provides an ESLint plugin to help you find common Lingui usage errors in your code.

[![npm-version](https://img.shields.io/npm/v/eslint-plugin-lingui?logo=npm\&cacheSeconds=1800)](https://www.npmjs.com/package/eslint-plugin-lingui) [![npm-downloads](https://img.shields.io/npm/dt/eslint-plugin-lingui?cacheSeconds=500)](https://www.npmjs.com/package/eslint-plugin-lingui)

## Installation[​](#installation "Direct link to Installation")

Install [ESLint](http://eslint.org):

* npm
* Yarn
* pnpm

```
npm install --save-dev eslint
```

```
yarn add --dev eslint
```

```
pnpm add --save-dev eslint
```

Next, install `eslint-plugin-lingui`:

* npm
* Yarn
* pnpm

```
npm install --save-dev eslint-plugin-lingui
```

```
yarn add --dev eslint-plugin-lingui
```

```
pnpm add --save-dev eslint-plugin-lingui
```

info

If you have installed ESLint globally (using the `-g` flag), you must also install `eslint-plugin-lingui` globally.

## Usage[​](#usage "Direct link to Usage")

### Flat Config (`eslint.config.js`)[​](#flat-config "Direct link to flat-config")

Version 8 of ESLint introduced a new configuration format called [Flat Config](https://eslint.org/docs/latest/use/configure/configuration-files). Flat config files represent plugins and parsers as JavaScript objects.

#### Recommended Setup[​](#recommended-setup "Direct link to Recommended Setup")

To enable all the recommended rules for the plugin, add the following config:

```
import pluginLingui from "eslint-plugin-lingui";

export default [
  pluginLingui.configs["flat/recommended"],
  // Any other config...
];
```

#### Custom Setup[​](#custom-setup "Direct link to Custom Setup")

Alternatively, you can load the plugin and configure only the rules you want to use:

```
import pluginLingui from "eslint-plugin-lingui";

export default [
  {
    plugins: {
      lingui: pluginLingui,
    },
    rules: {
      "lingui/t-call-in-function": "error",
    },
  },
  // Any other config...
];
```

### Legacy Config (`.eslintrc`)[​](#legacy-eslintrc "Direct link to legacy-eslintrc")

The legacy configuration format has been deprecated by ESLint, but it's still supported. If you're using the legacy format, you can use the following configuration.

#### Recommended Setup[​](#recommended-setup-1 "Direct link to Recommended Setup")

To enable all the recommended rules for the plugin, add `plugin:lingui/recommended` to the `extends` section:

```
{
  "extends": ["plugin:lingui/recommended"]
}
```

#### Custom Setup[​](#custom-setup-1 "Direct link to Custom Setup")

Alternatively, add `lingui` to the `plugins` section of your `.eslintrc` configuration file. You can omit the `eslint-plugin-` prefix:

```
{
  "plugins": ["lingui"]
}
```

In the rules section, configure the rules you want to use:

```
{
  "rules": {
    "lingui/no-unlocalized-strings": 2,
    "lingui/t-call-in-function": 2,
    "lingui/no-single-variables-to-translate": 2,
    "lingui/no-expression-in-message": 2,
    "lingui/no-single-tag-to-translate": 2,
    "lingui/no-trans-inside-trans": 2
  }
}
```

tip

See the [official repository](https://github.com/lingui/eslint-plugin) for more information about the rules.
