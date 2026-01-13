# Source: https://typescript-eslint.io/rules/method-signature-style

On this page# method-signature-style
Enforce using a particular method signature syntax.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
TypeScript provides two ways to define an object/interface function property:
```
interface Example {
// method shorthand syntax
func(arg: string): number;
// regular property with function type
func: (arg: string) => number;
}
```
The two are very similar; most of the time it doesn&#x27;t matter which one you use.
A good practice is to use the TypeScript&#x27;s `strict` option (which implies `strictFunctionTypes`) which enables correct typechecking for function properties only (method signatures get old behavior).
TypeScript FAQ:
A method and a function property of the same type behave differently.
Methods are always bivariant in their argument, while function properties are contravariant in their argument under `strictFunctionTypes`.
See the reasoning behind that in the [TypeScript PR for the compiler option](https://github.com/microsoft/TypeScript/pull/18654).
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/method-signature-style": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/method-signature-style": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6AW0XwAsB7AE1rJKAcyYBDfLGiIhRJOiiJo0XtEjgwAXxBagA)
## Options[​](#options)
This rule accepts the following options:
```
type Options = [
/** The method signature style to enforce using. */
| &#x27;method&#x27;
/** The method signature style to enforce using. */
| &#x27;property&#x27;,
];
const defaultOptions: Options = [&#x27;property&#x27;];
```
This rule accepts one string option:
- `"property"`: Enforce using property signature for functions. Use this to enforce maximum correctness together with TypeScript&#x27;s strict mode.
- `"method"`: Enforce using method signature for functions. Use this if you aren&#x27;t using TypeScript&#x27;s strict mode and prefer this style.
### `property`[​](#property)
Examples of code with `property` option.
- ❌ Incorrect- ✅ Correct```
interface T1 {
func(arg: string): number;
}
type T2 = {
func(arg: boolean): void;
};
interface T3 {
func(arg: number): void;
func(arg: string): void;
func(arg: boolean): void;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6AW0XwAsB7AE1rJKAcyYBDfLGiIhRJOjABtcNhyJo0XtEgAaVWsjEtpaEUgGwAXVUBfELaA&code=JYOwLgpgTgZghgYwgAgCoEZkG8BQzkwCuICAFHFAOYBcyAzmFKJQJS0iEC2ARtANw4AvjjABPAA4pUAJmQBebHgLEyFGsm4B7TQBsIcEG2QA3TcAAmAwQNCRYiKQGZF%2BIiXJV2XXlCOmLAq4qHuoMTCCstP6WSm6qnhraegZ%2BZjGCQA&fileType=.ts)```
interface T1 {
func: (arg: string) => number;
}
type T2 = {
func: (arg: boolean) => void;
};
// this is equivalent to the overload
interface T3 {
func: ((arg: number) => void) &
((arg: string) => void) &
((arg: boolean) => void);
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6AW0XwAsB7AE1rJKAcyYBDfLGiIhRJOjABtcNhyJo0XtEgAaVWsjEtpaEUgGwAXVUBfELaA&code=JYOwLgpgTgZghgYwgAgCoEZkG8BQzkwCuICAXMgBRxQDm5AzmFKDQJTIC8AfMiIQLYAjaAG4cAXxxgAngAcUqAEydseAsTKVqdZIID2egDYQ4Idt2QA3PcAAmY8WID0T5GAAWwesi-IIAR0JgSzhjcDc9N3cUPUtoQz04WxxQSFhEBQBmVXwiEnIKKlpyPiFocx5rO3YAMjV8Qu0GJhYKqxtbWvrKIp19IxMzTkqO1gcgA&fileType=.ts)
### `method`[​](#method)
Examples of code with `method` option.
- ❌ Incorrect- ✅ Correct```
interface T1 {
func: (arg: string) => number;
}
type T2 = {
func: (arg: boolean) => void;
};
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6AW0XwAsB7AE1rJKAcyYBDfLGiIhRJOjABtcNhyJo0XtEgAaVWsiceAyAbABdVQF8Q1oA&code=JYOwLgpgTgZghgYwgAgCoEZkG8BQzkwCuICAXMgBRxQDm5AzmFKDQJTIC8AfMiIQLYAjaAG4cAXxxgAngAcUqAEydseAsTKVqdZIID2egDYQ4Idt2QA3PcAAmY8SKA&fileType=.ts)```
interface T1 {
func(arg: string): number;
}
type T2 = {
func(arg: boolean): void;
};
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6AW0XwAsB7AE1rJKAcyYBDfLGiIhRJOjABtcNhyJo0XtEgAaVWsiceAyAbABdVQF8Q1oA&code=JYOwLgpgTgZghgYwgAgCoEZkG8BQzkwCuICAFHFAOYBcyAzmFKJQJS0iEC2ARtANw4AvjjABPAA4pUAJmQBebHgLEyFGsm4B7TQBsIcEG2QA3TcAAmAwXyA&fileType=.ts)
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t want to enforce a particular style for object/interface function types, and/or if you don&#x27;t use `strictFunctionTypes`, then you don&#x27;t need this rule.
However, keep in mind that inconsistent style can harm readability in a project.
We recommend picking a single option for this rule that works best for your project.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/method-signature-style.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/method-signature-style.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/method-signature-style.mdx)- [Options](#options)[`property`](#property)- [`method`](#method)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)