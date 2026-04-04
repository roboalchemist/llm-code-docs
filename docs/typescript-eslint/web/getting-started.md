# Source: https://typescript-eslint.io/getting-started

On this page# Getting Started## Quickstart[​](#quickstart)
This page is a quick-start for [ESLint&#x27;s new "flat" config format](https://eslint.org/docs/latest/use/configure/configuration-files-new) to go from zero to linting with our recommended rules on your TypeScript code as quickly as possible.
note
- For the same guide but for [ESLint&#x27;s legacy format](https://eslint.org/docs/latest/use/configure/configuration-files-deprecated) — see [Legacy ESLint Setup](/getting-started/legacy-eslint-setup).
- For quickstart information on linting with type information — see [Typed Linting](/getting-started/typed-linting).
### Step 1: Installation[​](#step-1-installation)
First, install the required packages for [ESLint](https://eslint.org), [TypeScript](https://typescriptlang.org), and [our tooling](/packages/typescript-eslint):
- npm- Yarn- pnpm```
npm install --save-dev eslint @eslint/js typescript typescript-eslint
``````
yarn add --dev eslint @eslint/js typescript typescript-eslint
``````
pnpm add --save-dev eslint @eslint/js typescript typescript-eslint
```
### Step 2: Configuration[​](#step-2-configuration)
Next, create an `eslint.config.mjs` config file in the root of your project, and populate it with the following:
eslint.config.mjs```
// @ts-check
import eslint from &#x27;@eslint/js&#x27;;
import { defineConfig } from &#x27;eslint/config&#x27;;
import tseslint from &#x27;typescript-eslint&#x27;;
export default defineConfig(
eslint.configs.recommended,
tseslint.configs.recommended,
);
```
This code will enable our [recommended configuration](/users/configs) for linting.
#### Details[​](#details)
- `defineConfig(...)` is an optional helper function built in to current versions of ESLint. See [the ESLint configuration docs](https://eslint.org/docs/latest/use/configure/configuration-files) for more detail.
- `&#x27;@eslint/js&#x27;` / `eslint.configs.recommended` turns on [eslint&#x27;s recommended config](https://www.npmjs.com/package/@eslint/js).
- `tseslint.configs.recommended` turns on [our recommended config](/users/configs#recommended).
Aside on file extensionsThe `.mjs` extension makes the file use the [ES modules (ESM)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) format. Node interprets `.js` files in the [CommonJS (CJS)](https://nodejs.org/api/modules.html) format by default, but if you have `"type": "module"` in your `package.json`, you can also use `eslint.config.js`.
### Step 3: Running ESLint[​](#step-3-running-eslint)
Open a terminal to the root of your project and run the following command:
- npm- Yarn- pnpm```
npx eslint .
``````
yarn eslint .
``````
pnpm eslint .
```
ESLint will lint all TypeScript compatible files within the current folder, and will output the results to your terminal.
## Next Steps[​](#next-steps)
If you&#x27;re having problems getting this working, please have a look at our [Troubleshooting & FAQs](/troubleshooting/faqs/general).
### Additional Configs[​](#additional-configs)
We recommend you consider enabling the following two configs:
- [`strict`](/users/configs#strict): a superset of `recommended` that includes more opinionated rules which may also catch bugs.
- [`stylistic`](/users/configs#stylistic): additional rules that enforce consistent styling without significantly catching bugs or changing logic.
eslint.config.mjs```
export default defineConfig(
eslint.configs.recommended,
tseslint.configs.recommended,
tseslint.configs.strict,
tseslint.configs.stylistic,
);
```
You can read more about these in our [shared configurations docs](/users/configs).
### Typed Linting[​](#typed-linting)
We also provide a plethora of powerful rules that utilize the power of TypeScript&#x27;s type information.
[Visit the next page for a typed rules setup guide](/getting-started/typed-linting).
## Documentation Resources[​](#documentation-resources)
- You can read more about configuring ESLint [in their documentation on configuration](https://eslint.org/docs/user-guide/configuring).
- You can read more about the rules provided by ESLint [in their documentation on their rules](https://eslint.org/docs/rules/).
- You can read more about the rules provided by typescript-eslint in our [rules documentation](/rules).
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/getting-started/Quickstart.mdx)- [Quickstart](#quickstart)[Step 1: Installation](#step-1-installation)- [Step 2: Configuration](#step-2-configuration)[Details](#details)- [Step 3: Running ESLint](#step-3-running-eslint)- [Next Steps](#next-steps)[Additional Configs](#additional-configs)- [Typed Linting](#typed-linting)- [Documentation Resources](#documentation-resources)