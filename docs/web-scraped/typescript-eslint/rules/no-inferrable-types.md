# Source: https://typescript-eslint.io/rules/no-inferrable-types

On this page# no-inferrable-types
Disallow explicit type declarations for variables or parameters initialized to a number, string, or boolean.
🎨Extending [`"plugin:@typescript-eslint/stylistic"`](/users/configs#stylistic) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
TypeScript is able to infer the types of parameters, properties, and variables from their default or initial values.
There is no need to use an explicit `:` type annotation on one of those constructs initialized to a boolean, number, or string.
Doing so adds unnecessary verbosity to code -making it harder to read- and in some cases can prevent TypeScript from inferring a more specific literal type (e.g. `10`) instead of the more general primitive type (e.g. `number`)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-inferrable-types": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-inferrable-types": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1uYDNFpoAQwBGSWkVKoMkftA7RI4MAF8QyoA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
const a: bigint = 10n;
const a: bigint = BigInt(10);
const a: boolean = !0;
const a: boolean = Boolean(null);
const a: boolean = true;
const a: null = null;
const a: number = 10;
const a: number = Infinity;
const a: number = NaN;
const a: number = Number(&#x27;1&#x27;);
const a: RegExp = /a/;
const a: RegExp = new RegExp(&#x27;a&#x27;);
const a: string = `str`;
const a: string = String(1);
const a: symbol = Symbol(&#x27;a&#x27;);
const a: undefined = undefined;
const a: undefined = void someValue;
class Foo {
prop: number = 5;
}
function fn(a: number = 5, b: boolean = true) {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1uYDNFpoAQwBGSWkVKoMkftA7RI4MAF8QyoA&code=MYewdgzgLgBAhgLhgIwJYHNVlgXhgRgAYwBuAKFElkRQy1xgCEMBJbACiIEpzLp4kyECAA2AUzhgYeAISFe4fjSGiJUvI2HjJ7MAFcRInhUXVBWtdJhQATnrEKqAmPsNXXIx0qT6AtsjEbKyIvMxc9f0CrNgAzLFQoAE9Q5z8AoLwAOThMlJo0qKyI9PYAcnxS4z4wgCUxdABRAA8ABysAejh2vKQ6xtb3MQB3GD7mlrK4Sp6YaBssdCsAAzmlmbmFqwBlWwXOKtNnCET-UW2ToRFJ6ZMnGj0wABMxOLAxR6sH59f3ma%2BXrDvKwANxAqA%2BEBAvjEADU4CJ7OQKCI4BAIDAAGLCGAAbzIMBgLRsIBaPmKhRgAFZyABfMhkGIPYBQVDgGAxMDsfLkjJUgA0KHMqkkVls9i4uJpQA&fileType=.ts)```
const a = 10n;
const a = BigInt(10);
const a = !0;
const a = Boolean(null);
const a = true;
const a = null;
const a = 10;
const a = Infinity;
const a = NaN;
const a = Number(&#x27;1&#x27;);
const a = /a/;
const a = new RegExp(&#x27;a&#x27;);
const a = `str`;
const a = String(1);
const a = Symbol(&#x27;a&#x27;);
const a = undefined;
const a = void someValue;
class Foo {
prop = 5;
}
function fn(a = 5, b = true) {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1uYDNFpoAQwBGSWkVKoMkftA7RI4MAF8QyoA&code=MYewdgzgLgBAhjAvDAjABjAbgFCkrBZAIQEsBzASTCgAp0BKHPaeJGAQjSfBcJiJAgANgFM4YGmACuQoY1w8CbKACcpI7vlbJpszbzbp9S5FQBmJMCSgBPY9pgA5OI-t9HUgLYAjESpoA5CgB8swmMAD0cBFubGAiAO4wAEoiZACiAB4ADoFwIbHIAAbQKkWFMADKqpZkdKGKDpU2PsJ5BQpafFJgACYiFvG9FQBuICS9MBAgniIAanBC6ji4QnAQEDAAYoIwAN7YMDDZKiDZbACsOAC%2B2NhmPcBQJOAwZhJ8FwA0MN7KaiJ6PtrkA&fileType=.ts)
## Options[​](#options)
This rule accepts the following options:
```
type Options = [
{
/** Whether to ignore function parameters. */
ignoreParameters?: boolean;
/** Whether to ignore class properties. */
ignoreProperties?: boolean;
},
];
const defaultOptions: Options = [
{ ignoreParameters: false, ignoreProperties: false },
];
```
### `ignoreParameters`[​](#ignoreparameters)
Whether to ignore function parameters. Default: `false`.
When set to true, the following pattern is considered valid:
```
function foo(a: number = 5, b: boolean = true) {
// ...
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1uYDNFpoAQwBGSWkVKoMAbXDYc-aB2iQANHPlZ52SJQDmnaIgAKgoQFtE%2BflLD44iDdgC%2BTgLpzXzoA&code=GYVwdgxgLglg9mABMOcAUBDAXIsIC2ARgKYBOiAvIgKwA0ihOhqANsRklVKSMQJSIA3gChEiAPTjEAOlnCAvkA&fileType=.ts)
### `ignoreProperties`[​](#ignoreproperties)
Whether to ignore class properties. Default: `false`.
When set to true, the following pattern is considered valid:
```
class Foo {
prop: number = 5;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1uYDNFpoAQwBGSWkVKoMAbXDYc-aB2iQANHPlZ52SJQDmnaIgAKS0tHyUU6MPjiIN2AL6OAunJdOgA&code=MYGwhgzhAEBiD29oG8BQ1oAcBO9MC5oA7AVwFsAjAU22gF5oBWAblQF8g&fileType=.ts)
## When Not To Use It[​](#when-not-to-use-it)
If you strongly prefer to have explicit types regardless of whether they can be inferred, this rule may not be for you.
If you use the `--isolatedDeclarations` compiler option, this rule is incompatible.
## Further Reading[​](#further-reading)
- [TypeScript Inference](https://www.typescriptlang.org/docs/handbook/type-inference.html)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-inferrable-types.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-inferrable-types.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-inferrable-types.mdx)- [Examples](#examples)- [Options](#options)[`ignoreParameters`](#ignoreparameters)- [`ignoreProperties`](#ignoreproperties)- [When Not To Use It](#when-not-to-use-it)- [Further Reading](#further-reading)- [Resources](#resources)