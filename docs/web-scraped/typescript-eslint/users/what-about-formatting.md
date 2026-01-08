# Source: https://typescript-eslint.io/users/what-about-formatting

On this page# What About Formatting?We recommend against using ESLint for formatting.
We recommend using [Prettier](https://prettier.io), [dprint](https://dprint.dev), or an equivalent instead.
## Formatters vs. Linters[​](#formatters-vs-linters)
**Formatters** are tools that verify and correct whitespace issues in code, such as spacing and newlines.
Formatters typically run very quickly because they are only concerned with changing whitespace, not code logic or naming.
**Linters** are tools that verify and correct logical and non-whitespace style issues in code, such as naming consistency and bug detection.
Linters often take seconds or more to run because they apply many logical rules to code.
### Problems with Using Linters as Formatters[​](#problems-with-using-linters-as-formatters)
Linters are designed to run in a parse, check, report, fix cycle. This means that there is a lot of intermediate work that needs to be done before a linter can fix a formatting issue with your code.
Additionally linters typically run each rule isolated from one another. This has several problems with it such as:
- any two lint rules can&#x27;t share config, meaning one lint rule&#x27;s fixer might introduce a violation of another lint rule&#x27;s fixer (eg one lint rule might use the incorrect indentation character).
- lint rule fixers can conflict (apply to the same code range), forcing the linter to perform an additional cycle to attempt to apply a fixer to a clean set of code.
These problems cause a linter to be much slower - which can be much more of a problem in projects that enable [typed linting](/getting-started/typed-linting).
Formatting with a linter is also much less consistent and less able to handle edge-cases than a purpose-built formatter.
The maintenance cost of formatting-related lint rules is typically very high as a result.
Modern formatters such as Prettier are architected in a way that applies formatting to all code regardless of original formatting.
This design allows formatters to be much more comprehensive and consistent at much lower maintenance cost than linters.
### Suggested Usage - Prettier[​](#suggested-usage---prettier)
Neither typescript-eslint nor ESLint core enable any formatting-related rules in any recommended presets.
However, some third party plugin configurations may still enable that bad practice.
If you see formatting rules enabled in your ESLint configuration, we recommend using [`eslint-config-prettier`](https://github.com/prettier/eslint-config-prettier) to disable formatting rules in your ESLint configuration.
You can then configure your formatter separately from ESLint.
Using this config by adding it to the end of your `extends`:
- Flat Config- Legacy Configeslint.config.mjs```
// @ts-check
import eslint from &#x27;@eslint/js&#x27;;
import { defineConfig } from &#x27;eslint/config&#x27;;
import someOtherConfig from &#x27;eslint-config-other-configuration-that-enables-formatting-rules&#x27;;
import prettierConfig from &#x27;eslint-config-prettier&#x27;;
import tseslint from &#x27;typescript-eslint&#x27;;
export default defineConfig(
eslint.configs.recommended,
tseslint.configs.recommended,
someOtherConfig,
prettierConfig,
);
```.eslintrc.js```
/* eslint-env node */
module.exports = {
extends: [
&#x27;eslint:recommended&#x27;,
&#x27;plugin:@typescript-eslint/recommended&#x27;,
&#x27;other-configuration-that-enables-formatting-rules&#x27;,
&#x27;prettier&#x27;,
],
parser: &#x27;@typescript-eslint/parser&#x27;,
plugins: [&#x27;@typescript-eslint&#x27;],
root: true,
};
```
Note that even if you use a formatter other than `prettier`, you can use `eslint-config-prettier` as it exclusively turns **off** all formatting rules.
#### `eslint-plugin-prettier`[​](#eslint-plugin-prettier)
`eslint-config-prettier` is not the same as [`eslint-plugin-prettier`](https://github.com/prettier/eslint-plugin-prettier).
- The *config* only disables rules from core and other plugins.
- The *plugin* loads and runs Prettier inside ESLint.
Running Prettier inside ESLint can be slow: see [Performance Troubleshooting > `eslint-plugin-prettier`](/troubleshooting/typed-linting/performance#eslint-plugin-prettier).
However, because it doesn&#x27;t re-implement Prettier&#x27;s logic in ESLint, the caveats mentioned about using linters for formatting don&#x27;t apply to `eslint-plugin-prettier` either.
## ESLint Core and Formatting[​](#eslint-core-and-formatting)
Most lint rules fall into one of two to three categories:
- **Logical**: Rules that care about the logic in runtime behavior of code (such as missing `await`s or invalid logical checks).
- **Stylistic**: Rules that care about style concerns which do impact runtime behavior of code, but generally not logic. These are mostly around naming or which roughly-equivalent syntax constructs to use (such as function declarations vs. arrow functions).
**Formatting**: Stylistic rules that care only about trivia (semicolons, whitespace, etc.) without impacting the runtime behavior of the code. These rules conflict with dedicated formatters such as Prettier.
Per [ESLint&#x27;s 2020 Changes to Rule Policies blog post](https://eslint.org/blog/2020/05/changes-to-rules-policies#what-are-the-changes), ESLint itself has moved away from *stylistic* rules, including *formatting* rules:
Stylistic rules are frozen - we won&#x27;t be adding any more options to stylistic rules.
We&#x27;ve learned that there&#x27;s no way to satisfy everyone&#x27;s personal preferences, and most of the rules already have a lot of difficult-to-understand options.
Stylistic rules are those related to spacing, conventions, and generally anything that does not highlight an error or a better way to do something.
We mirror the ESLint team&#x27;s move away from *formatting* and *stylistic* rules.
With the exception of bug fixes, no new formatting- or stylistic-related pull requests will be accepted into typescript-eslint.
noteThe [`stylistic` configurations](/users/configs#stylistic) are not deprecated or recommended-against.
We&#x27;ll continue to include those configs and their rules to help enforce TypeScript-related stylistic consistency for the foreseeable future.
## `eslint-stylistic`[​](#eslint-stylistic)
The downside of using a comprehensive formatter for formatting is that it will strictly apply opinions to code.
Although you can [ignore code in Prettier](https://prettier.io/docs/en/ignore.html) and other formatters, including inline such as with [`// prettier-ignore` comments](https://prettier.io/docs/en/ignore.html#javascript), formatters are much more opinionated than lint rules.
The [`eslint-stylistic`](https://eslint.style) project provides an ESLint plugin containing *formatting* and *stylistic* rules.
That plugin can serve as your formatter if you strongly prefer not to use a dedicated formatter.
See [ESLint Stylistic > Why?](https://eslint.style/guide/why) for more details on that project&#x27;s motivation, and [ESLint Stylistic > Getting Started](https://eslint.style/guide/getting-started) for how to set it up.
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/users/What_About_Formatting.mdx)- [Formatters vs. Linters](#formatters-vs-linters)[Problems with Using Linters as Formatters](#problems-with-using-linters-as-formatters)- [Suggested Usage - Prettier](#suggested-usage---prettier)[`eslint-plugin-prettier`](#eslint-plugin-prettier)- [ESLint Core and Formatting](#eslint-core-and-formatting)- [`eslint-stylistic`](#eslint-stylistic)