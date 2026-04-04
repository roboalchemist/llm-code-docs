# Source: https://typescript-eslint.io/rules/no-redeclare

On this page# no-redeclare
Disallow variable redeclaration.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
dangerThe code problem checked by this ESLint rule is automatically checked by the TypeScript compiler. Thus, it is not recommended to turn on this rule in new TypeScript projects. You only need to enable this rule if you prefer the ESLint error messages over the TypeScript compiler error messages.
This rule extends the base [`no-redeclare`](https://eslint.org/docs/latest/rules/no-redeclare) rule from ESLint core. It adds support for TypeScript function overloads, and declaration merging.
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"no-redeclare": "off",
"@typescript-eslint/no-redeclare": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"no-redeclare": "off",
"@typescript-eslint/no-redeclare": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaaRAE0QGN4BDE9KfAM0cgBpxtIABAFwE8ADigrQAlgJ6EU8Ubh4B6AsTKUadDJETRo%2BaJA4BfEAaA)
## Options[​](#options)
See [`eslint/no-redeclare`&#x27;s options](https://eslint.org/docs/rules/no-redeclare#options).
This rule adds the following options:
```
interface Options extends BaseNoRedeclareOptions {
ignoreDeclarationMerge?: boolean;
}
const defaultOptions: Options = {
...baseNoRedeclareDefaultOptions,
ignoreDeclarationMerge: true,
};
```
### `ignoreDeclarationMerge`[​](#ignoredeclarationmerge)
Whether to ignore declaration merges between certain TypeScript declaration types. Default: `true`.
The following sets will be ignored when this option is enabled:
- interface + interface
- namespace + namespace
- class + interface
- class + namespace
- class + interface + namespace
- function + namespace
- enum + namespace
Examples of **correct** code with `{ ignoreDeclarationMerge: true }`:
```
interface A {
prop1: 1;
}
interface A {
prop2: 2;
}
namespace Foo {
export const a = 1;
}
namespace Foo {
export const b = 2;
}
class Bar {}
namespace Bar {}
function Baz() {}
namespace Baz {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaaRAE0QGN4BDE9KfAM0cgBpxtIABAFwE8ADigrQAlgJ6EU8Ubh4B6AsTKUadDAG0O2KImjR80NtuxYdnUQHMCJACKra1HqPy4AsnsuJ6POIhMQAL4mALocwYFAA&code=JYOwLgpgTgZghgYwgAgILIN4ChnIA5QD2eAjAFzIkDcWAvlqJLIiutrgcQEwVc31YQcALYQAznhbIAYoUKYcyCAA88hKGGQJCIMZrjIAvJX6CR4yUhlyFuFWo1ade5ACMjyPnSxYEAGzgxMWQAITgoTHohUQkpMIiMARgAVxAEMGAdULgALwAKAEpIsxjLFDCcyKA&fileType=.ts)
**Note:** Even with this option set to true, this rule will report if you name a type and a variable the same name. ***This is intentional***.
Declaring a variable and a type the same is usually an accident, and it can lead to hard-to-understand code.
If you have a rare case where you&#x27;re intentionally naming a type the same name as a variable, use a disable comment. For example:
```
type something = string;
// eslint-disable-next-line @typescript-eslint/no-redeclare -- intentionally naming the variable the same as the type
const something = 2;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaaRAE0QGN4BDE9KfAM0cgBpxtIABAFwE8ADigrQAlgJ6EU8Ubh4B6AsTKUadDAG0O2KImjR80NtuxYdnUQHMCJACKra1HqPy4AsnsuJ6POIhMQAL4mALocwYFAA&code=C4TwDgpgBAzg9gWwsAFgSwHYHMoF5bABOmWA3AFAD0lUEMANpsALQAmaMAhgEb0TMYIADxaNBUAAKhIMAMbEwLOmOCUMcZoQisIs%2Bpy1RmzKEwgZgaOBk716IKDYQkoqaADcDaHn1cpoXEhQnDB%2B0NIQ5LLWMMCwiMjo2HhQAEykQA&fileType=.ts)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-redeclare.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-redeclare.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/no-redeclare.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-redeclare.mdx)- [How to Use](#how-to-use)- [Options](#options)[`ignoreDeclarationMerge`](#ignoredeclarationmerge)- [Resources](#resources)