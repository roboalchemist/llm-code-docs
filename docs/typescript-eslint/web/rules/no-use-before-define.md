# Source: https://typescript-eslint.io/rules/no-use-before-define

On this page# no-use-before-define
Disallow the use of variables before they are defined.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
This rule extends the base [`no-use-before-define`](https://eslint.org/docs/latest/rules/no-use-before-define) rule from ESLint core. It adds support for `type`, `interface` and `enum` declarations.
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"no-use-before-define": "off",
"@typescript-eslint/no-use-before-define": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"no-use-before-define": "off",
"@typescript-eslint/no-use-before-define": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaWZRQgI0QDN9oyATagS10XSnyqsgBpxtIAAQAuATwAOKAMbQm44YRTwWwgPQFipCtVoNmrdpETRotSPwC%2BIC0A)
## Options[​](#options)
See [`eslint/no-use-before-define`&#x27;s options](https://eslint.org/docs/rules/no-use-before-define#options).
This rule adds the following options:
```
interface Options extends BaseNoUseBeforeDefineOptions {
enums?: boolean;
typedefs?: boolean;
ignoreTypeReferences?: boolean;
}
const defaultOptions: Options = {
...baseNoUseBeforeDefineDefaultOptions,
enums: true,
typedefs: true,
ignoreTypeReferences: true,
};
```
### `enums`[​](#enums)
Whether to check references to enums. Default: `true`.
If this is `true`, this rule warns every reference to a enum before the enum declaration.
If this is `false`, this rule will ignore references to enums, when the reference is in a child scope.
Examples of code for the `{ "enums": true }` option:
- ❌ Incorrect- ✅ Correct```
const x = Foo.FOO;
enum Foo {
FOO,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaWZRQgI0QDN9oyATagS10XSnyqsgBpxtIAAQAuATwAOKAMbQm44YRTwWwgPQFipCtVoNmrdgG1%2B2KImjRavE9iymBiXLAC2qDMLiIbEAL42Auvx%2BPkA&code=MYewdgzgLgBAHjAvDAYiEA6FB5bBuAKAIFMwBXAW1XRgG8CZVcAaAgXyA&fileType=.ts)```
function foo() {
return Foo.FOO;
}
enum Foo {
FOO,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaWZRQgI0QDN9oyATagS10XSnyqsgBpxtIAAQAuATwAOKAMbQm44YRTwWwgPQFipCtVoNmrdgG1%2B2KImjRavE9iymBiXLAC2qDFQCG8UjYgBfGwBdfgC-IA&code=GYVwdgxgLglg9mABMOcAUBKRBvAUIxAJwFMoRCkAxVAOkoHl6BuXAX112LBAFtFq4OfP0YAaNkA&fileType=.ts)
### `typedefs`[​](#typedefs)
Whether to check references to types. Default: `true`.
If this is `true`, this rule warns every reference to a type before the type declaration.
If this is `false`, this rule will ignore references to types.
Examples of **correct** code for the `{ "typedefs": false }` option:
```
let myVar: StringOrNumber;
type StringOrNumber = string | number;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaWZRQgI0QDN9oyATagS10XSnyqsgBpxtIAAQAuATwAOKAMbQm44YRTwWwgPQFipCtVoNmrdgG1%2B2KImjRavE9iymBYyYyqoMVAIbxSNiAF8bALr8-r5AA&code=DYUwLgBAtgngagQwE4C4IGUxIJYDsDmA8kgHICuUARiEgNwBQYMADiBlnkaRdUhALwQAzhwIQAPhFw8atIA&fileType=.ts)
### `ignoreTypeReferences`[​](#ignoretypereferences)
Whether to ignore type references, such as in type annotations and assertions. Default: `true`.
If this is `true`, this rule ignores all type references.
If this is `false`, this will check all type references.
Examples of **correct** code for the `{ "ignoreTypeReferences": true }` option:
```
let var1: StringOrNumber;
type StringOrNumber = string | number;
let var2: Enum;
enum Enum {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaWZRQgI0QDN9oyATagS10XSnyqsgBpxtIAAQAuATwAOKAMbQm44YRTwWwgPQFipCtVoNmrdgG1%2B2KImjRavE9iymBTAOYE6AFQmIAStXOJcUlHZhOEQbCABfGwBdfkjwoA&code=DYUwLgBAbghgTgRgFwQMpjgSwHYHMDycAcgK4C2ARiHANwBQYAngA4hoY4HHlVwQC8EAM4c8EAD4RsPavTqhIsOACYUAUWll6ITRA3kIAbwC%2BQA&fileType=.ts)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-use-before-define.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-use-before-define.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/no-use-before-define.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-use-before-define.mdx)- [How to Use](#how-to-use)- [Options](#options)[`enums`](#enums)- [`typedefs`](#typedefs)- [`ignoreTypeReferences`](#ignoretypereferences)- [Resources](#resources)