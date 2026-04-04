# Source: https://typescript-eslint.io/developers/eslint-plugins

On this page# ESLint PluginsimportantThis page describes how to write your own custom ESLint plugins using typescript-eslint.
You should be familiar with [ESLint&#x27;s plugins guide](https://eslint.org/docs/latest/extend/plugins) and [typescript-eslint Custom Rules](/developers/custom-rules) before writing custom plugins.
Custom plugins that support TypeScript code and typed linting look very similar to any other ESLint plugin.
Follow the same general steps as [ESLint&#x27;s plugins guide > *Creating a plugin*](https://eslint.org/docs/latest/extend/plugins#creating-a-plugin) to set up your plugin.
The required differences are noted on this page.
tipSee [**`eslint-plugin-example-typed-linting`**](https://github.com/typescript-eslint/examples/tree/main/packages/eslint-plugin-example-typed-linting) for an example plugin that supports typed linting.
## Package Dependencies[​](#package-dependencies)
Your plugin should have the following `package.json` entries.
For all `@typescript-eslint` and `typescript-eslint` packages, keep them at the same semver versions.
As an example, you might set each of them to `^8.1.2` or `^7.12.0 || ^8.0.0`.
### `dependencies`[​](#dependencies)
[`@typescript-eslint/utils`](/packages/utils) is required for the [`RuleCreator` factory to create rules](#rulecreator-usage).
### `devDependencies`[​](#devdependencies)
[`@typescript-eslint/rule-tester`](/packages/rule-tester) is strongly recommended to be able to [test rules with our `RuleTester`](/developers/custom-rules).
### `peerDependencies`[​](#peerdependencies)
Include the following to enforce the version range allowed without making users&#x27; package managers install them:
- `@typescript-eslint/parser` and any other parsers users are expected to be using
- `eslint`
- `typescript`
Those are all packages consumers are expected to be using already.
You don&#x27;t need to declare any dependencies on `typescript-eslint` or `@typescript-eslint/eslint-plugin`.
Our setup guide ensures that the parser is automatically registered when configuring ESLint.
## `RuleCreator` Usage[​](#rulecreator-usage)
We recommend including at least the following three properties in your plugin&#x27;s [`RuleCreator` extra rule docs types](/developers/custom-rules#extra-rule-docs-types):
- `description: string`: a succinct description of what the rule does
- `recommended?: boolean`: whether the rule exists in your plugin&#x27;s shared *"`recommended`"* config
- `requiresTypeChecking?: boolean`: whether the rule will use type information, for documentation generators such as [`eslint-doc-generator`](https://github.com/bmish/eslint-doc-generator)
For example, from [`eslint-plugin-example-typed-linting`&#x27;s `utils.ts`](https://github.com/typescript-eslint/examples/blob/main/packages/eslint-plugin-example-typed-linting/src/utils.ts):
```
import { ESLintUtils } from &#x27;@typescript-eslint/utils&#x27;;
export interface ExamplePluginDocs {
description: string;
recommended?: boolean;
requiresTypeChecking?: boolean;
}
export const createRule = ESLintUtils.RuleCreator<ExamplePluginDocs>(
name =>
`https://github.com/your/eslint-plugin-example/tree/main/docs/${name}.md`,
);
```
## Type Checking and Configs[​](#type-checking-and-configs)
Most ESLint plugins export a *"`recommended`"* [ESLint shared config](https://eslint.org/docs/latest/extend/shareable-configs).
Many ESLint users assume enabling a plugin&#x27;s `recommended` config is enough to enable all its relevant rules.
However, at the same time, not all users want to or are able to enabled typed linting.
If your plugin&#x27;s rules heavily use type information, it might be difficult to enable those in a `recommended` config.
You have roughly two options:
- Have your plugin&#x27;s `recommended` config require enabling type information
- Have a separate config with a name like `recommendedTypeChecked`
Either way, explicitly mention the strategy taken in your docs.
infoPer [*Custom Rules* > *Conditional Type Information*](/developers/custom-rules#conditional-type-information), we recommend not changing rule logic based on whether type information is available.
tipSee [**`eslint-plugin-example-typed-linting`**](https://github.com/typescript-eslint/examples/tree/main/packages/eslint-plugin-example-typed-linting) for an example plugin that supports typed linting.
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/developers/ESLint_Plugins.mdx)- [Package Dependencies](#package-dependencies)[`dependencies`](#dependencies)- [`devDependencies`](#devdependencies)- [`peerDependencies`](#peerdependencies)- [`RuleCreator` Usage](#rulecreator-usage)- [Type Checking and Configs](#type-checking-and-configs)