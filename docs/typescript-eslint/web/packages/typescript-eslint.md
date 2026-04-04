# Source: https://typescript-eslint.io/packages/typescript-eslint

On this page# `typescript-eslint`
[](https://npmjs.com/typescript-eslint)
Tooling which enables you to use TypeScript with ESLint
This package is the main entrypoint that you can use to consume our tooling with ESLint.
This package exports the following:
NameDescription`config` (deprecated)A utility function for creating type-safe flat configs -- see [`config(...)`](#config-deprecated)`configs`[Shared ESLint (flat) configs](/users/configs)`parser`A re-export of [`@typescript-eslint/parser`](/packages/parser)`plugin`A re-export of [`@typescript-eslint/eslint-plugin`](/packages/eslint-plugin)`FlatConfig`A re-export of the type from [`@typescript-eslint/utils`](/packages/utils)
## Installation[​](#installation)
- npm- Yarn- pnpm```
npm i typescript-eslint
``````
yarn add typescript-eslint
``````
pnpm add typescript-eslint
```
## Usage[​](#usage)
We recommend getting started by using the default ESLint setup with our shared configs.
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
This config file exports a flat config that enables both the [core ESLint recommended config](https://www.npmjs.com/package/@eslint/js) and [our recommended config](/users/configs#recommended).
### `config(...)` (deprecated)[​](#config-deprecated)
dangerThe `config(...)` utility function was deprecated in favor of ESLint core&#x27;s [`defineConfig(...)`](https://eslint.org/blog/2025/03/flat-config-extends-define-config-global-ignores/#introducing-defineConfig(...)-for-eslint) in [#10935](https://github.com/typescript-eslint/typescript-eslint/issues/10935).
See [the `defineConfig` migration guide later](#migrating-to-defineconfig) for more details.
The documentation here is preserved for historical reference and migration purposes.
`tseslint.config(...)` takes in any number of ESLint config objects, each of which may additionally include an `extends` array of configs to extend.
`tseslint.config(...)` returns the equivalent ESLint config of applying the rest of the settings for each extension.
By using this function you will get autocomplete and documentation for all config properties.
Additionally, if you provide invalid values, it can trigger informative TypeScript type errors.
- With helper- Without helpereslint.config.mjs```
// @ts-check
import eslint from &#x27;@eslint/js&#x27;;
import tseslint from &#x27;typescript-eslint&#x27;;
export default tseslint.config(
eslint.configs.recommended,
tseslint.configs.recommended,
{
/*... */
},
// ...
);
```eslint.config.mjs```
// @ts-check
import eslint from &#x27;@eslint/js&#x27;;
import tseslint from &#x27;typescript-eslint&#x27;;
/** @type {import(&#x27;@typescript-eslint/utils&#x27;).TSESLint.FlatConfig.ConfigFile} */
export default [
eslint.configs.recommended,
...tseslint.configs.recommended,
{
/*... */
},
// ...
];
```
noteWe ***strongly*** recommend using this utility to improve the config authoring experience — however it is entirely optional.
By choosing not to use it you lose editor autocomplete and type checking for config files.
Otherwise it *will not* impact your ability to use our tooling.
#### Flat config `extends`[​](#flat-config-extends)
The `tseslint.config(...)` utility function also adds handling for the `extends` property on flat config objects.
This allows you to more easily extend shared configs for specific file patterns whilst also overriding rules/options provided by those configs:
```
export default tseslint.config({
files: [&#x27;**/*.ts&#x27;],
extends: [
eslint.configs.recommended,
tseslint.configs.recommended,
],
rules: {
&#x27;@typescript-eslint/array-type&#x27;: &#x27;error&#x27;,
// ...
},
});
// is the same as writing
export default [
...[
eslint.configs.recommended,
...tseslint.configs.recommended,
].map(conf => ({
...conf,
files: [&#x27;**/*.ts&#x27;],
})),
{
files: [&#x27;**/*.ts&#x27;],
rules: {
&#x27;@typescript-eslint/array-type&#x27;: &#x27;error&#x27;,
// ...
},
},
];
```
We found that this is a common operation when writing ESLint configs which is why we provided this convenience property.
For example, in codebases with type-aware linting, a config object like the following is a common way to disable TypeScript-specific linting setups on JavaScript files:
```
export default tseslint.config({
files: [&#x27;**/*.js&#x27;],
extends: [tseslint.configs.disableTypeChecked],
rules: {
// turn off other type-aware rules
&#x27;other-plugin/typed-rule&#x27;: &#x27;off&#x27;,
// turn off rules that don&#x27;t apply to JS code
&#x27;@typescript-eslint/explicit-function-return-type&#x27;: &#x27;off&#x27;,
},
});
```
#### Migrating to `defineConfig(...)`[​](#migrating-to-defineconfig)
The core `defineConfig(...)` helper is a nearly exact clone of `tseslint.config(...)` that was [first released in ESLint v9.22.0](https://eslint.org/blog/2025/03/eslint-v9.22.0-released/).
See [the ESLint blog post](https://eslint.org/blog/2025/03/flat-config-extends-define-config-global-ignores/#support-for-older-eslint-versions) for info on how to use `defineConfig(...)` with older versions of ESLint.
At the time of writing there are a small number of known edge cases in which the two have different functionality.
-
Overriding `files` in `extends`.
When `files` is provided in both a base object and an extension, `tseslint.config(...)` *overrides* the `files` property in the extension, whereas `defineConfig(...)` semantically intersects the two provided `files` specifiers.
tseslint.config(...)- defineConfig(...)eslint.config.mjs```
import tseslint from &#x27;typescript-eslint&#x27;;
export default tseslint.config({
files: [&#x27;a.ts&#x27;],
extends: [
{
files: [&#x27;b.ts&#x27;],
rules: {
&#x27;some-rule&#x27;: &#x27;error&#x27;,
},
},
],
});
// is equivalent to
export default {
files: [&#x27;a.ts&#x27;],
rules: { &#x27;some-rule&#x27;: &#x27;error&#x27; },
};
```eslint.config.mjs```
import { defineConfig } from &#x27;eslint/config&#x27;;
export default defineConfig({
files: [&#x27;a.ts&#x27;],
extends: [
{
files: [&#x27;b.ts&#x27;],
rules: {
&#x27;some-rule&#x27;: &#x27;error&#x27;,
},
},
],
});
// is equivalent to
// The base config technically ensures that &#x27;a.ts&#x27; is still included in
// the lint run, but otherwise the config has no effect, due to the
// intersection of &#x27;a.ts&#x27; and &#x27;b.ts&#x27; being empty.
export default {
files: [&#x27;a.ts&#x27;],
};
```
-
Type declarations (only applies to users who typecheck their eslint configs).
There are slight differences in the way types are declared between the two functions, which may cause typechecking errors when you switch from `tseslint.config(...)` to `defineConfig(...)` in some cases (see [#10899](https://github.com/typescript-eslint/typescript-eslint/issues/10899) for an example that used to impact typescript-eslint&#x27;s own configs).
Type errors such as these do not indicate a runtime problem and can safely be ignored.
### Manual usage[​](#manual-usage)
[typescript-eslint&#x27;s recommended and stylistic configurations](/users/configs) specify typescript-eslint `parser` and `plugin` options for you, so there is no need to manually provide those.
However, in complex ESLint configurations, you may find yourself manually specifying those options yourself.
#### Manually configuring our plugin and parser[​](#manually-configuring-our-plugin-and-parser)
You can declare our plugin and parser in your config via this package, for example:
eslint.config.mjs```
// @ts-check
import eslint from &#x27;@eslint/js&#x27;;
import { defineConfig } from &#x27;eslint/config&#x27;;
import jestPlugin from &#x27;eslint-plugin-jest&#x27;;
import tseslint from &#x27;typescript-eslint&#x27;;
export default defineConfig({
plugins: {
&#x27;@typescript-eslint&#x27;: tseslint.plugin,
},
languageOptions: {
parser: tseslint.parser,
parserOptions: {
projectService: true,
},
},
rules: {
&#x27;@typescript-eslint/no-floating-promises&#x27;: &#x27;error&#x27;,
// ...
},
});
```
warningWe ***strongly*** recommend declaring our plugin with the namespace `@typescript-eslint` as shown above.
If you use our shared configs this is the namespace that they use.
This has been the standard namespace for our plugin for many years and is what users are most familiar with.
You may choose a different namespace - but note that currently [flat configs allow the same plugin to be registered, configured, and have duplicate reports under multiple namespaces](https://github.com/eslint/eslint/discussions/17766).
### Usage with other plugins[​](#usage-with-other-plugins)
Below is a more complex example of how you might use our tooling with flat configs.
This config:
- Ignores `build`/`dist` folders from being linted
- Enables our plugin, our parser, and type-aware linting with a few of our popular type-aware rules
- Disables type-aware linting on JS files
- Enables the recommended `eslint-plugin-jest` rules on test files only
eslint.config.mjs```
// @ts-check
import eslint from &#x27;@eslint/js&#x27;;
import { defineConfig } from &#x27;eslint/config&#x27;;
import jestPlugin from &#x27;eslint-plugin-jest&#x27;;
import tseslint from &#x27;typescript-eslint&#x27;;
export default defineConfig(
{
// config with just ignores is the replacement for `.eslintignore`
ignores: [&#x27;**/build/**&#x27;, &#x27;**/dist/**&#x27;, &#x27;src/some/file/to/ignore.ts&#x27;],
},
eslint.configs.recommended,
{
plugins: {
&#x27;@typescript-eslint&#x27;: tseslint.plugin,
jest: jestPlugin,
},
languageOptions: {
parser: tseslint.parser,
parserOptions: {
projectService: true,
},
},
rules: {
&#x27;@typescript-eslint/no-floating-promises&#x27;: &#x27;error&#x27;,
// ...
},
},
{
// disable type-aware linting on JS files
files: [&#x27;**/*.js&#x27;],
extends: [tseslint.configs.disableTypeChecked],
},
{
// enable jest rules on test files
files: [&#x27;test/**&#x27;],
extends: [jestPlugin.configs[&#x27;flat/recommended&#x27;]],
},
);
```
## Migrating from legacy `.eslintrc` configs[​](#migrating-from-legacy-eslintrc-configs)
If you&#x27;re migrating from a legacy `.eslintrc` configuration setup you likely have our plugin and parser installed separately.
This package includes these as dependencies so you can freely uninstall your local references:
- npm- Yarn- pnpm```
npm un @typescript-eslint/parser @typescript-eslint/eslint-plugin
``````
yarn remove @typescript-eslint/parser @typescript-eslint/eslint-plugin
``````
pnpm remove @typescript-eslint/parser @typescript-eslint/eslint-plugin
```
For more information on migrating from a "legacy" config setup, see [ESLint&#x27;s Configuration Migration Guide](https://eslint.org/docs/latest/use/configure/migration-guide).
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/packages/TypeScript_ESLint.mdx)- [Installation](#installation)- [Usage](#usage)[`config(...)` (deprecated)](#config-deprecated)[Flat config `extends`](#flat-config-extends)- [Migrating to `defineConfig(...)`](#migrating-to-defineconfig)- [Manual usage](#manual-usage)[Manually configuring our plugin and parser](#manually-configuring-our-plugin-and-parser)- [Usage with other plugins](#usage-with-other-plugins)- [Migrating from legacy `.eslintrc` configs](#migrating-from-legacy-eslintrc-configs)