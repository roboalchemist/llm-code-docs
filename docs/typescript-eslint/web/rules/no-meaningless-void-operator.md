# Source: https://typescript-eslint.io/rules/no-meaningless-void-operator

On this page# no-meaningless-void-operator
Disallow the `void` operator except when used to discard a value.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
`void` in TypeScript refers to a function return that is meant to be ignored.
The `void` operator is a useful tool to convey the programmer&#x27;s intent to discard a value.
For example, it is recommended as one way of suppressing [`@typescript-eslint/no-floating-promises`](/rules/no-floating-promises) instead of adding `.catch()` to a promise.
This rule helps an authors catch API changes where previously a value was being discarded at a call site, but the callee changed so it no longer returns a value.
When combined with [no-unused-expressions](https://eslint.org/docs/rules/no-unused-expressions), it also helps *readers* of the code by ensuring consistency: a statement that looks like `void foo();` is **always** discarding a return value, and a statement that looks like `foo();` is **never** discarding a return value.
This rule reports on any `void` operator whose argument is already of type `void` or `undefined`.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-meaningless-void-operator": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-meaningless-void-operator": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtEBDJswDmSZMloA3DpQAmtDqWh98HaOiiJo0VZHBgAviH1A)
## Examples[​](#examples)
## Examples[​](#examples-1)
- ❌ Incorrect- ✅ Correct```
void (() => {})();
function foo() {}
void foo();
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtEBDJswDmSZMloA3DpQAmtDqWh98HaOiiJo0VZHBgAviH1A&code=G4ewlgJgBAFDCUUC8A%2BKBvAvvBBuAUPgGYCuAdgMYAuYIZURIICGm%2BokDTeQA&fileType=.ts)```
(() => {})();
function foo() {}
foo(); // nothing to discard
function bar(x: number) {
void x; // discarding a number
return 2;
}
void bar(1); // discarding a number
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtEBDJswDmSZMloA3DpQAmtDqWh98HaOiiJo0VZHBgAviH1A&code=BTCUAIF4D5wbwL6jAbgFBoGYFcB2BjAFwEsB7XcTU0seBLa1cAemfF1MIAtjcBzcIVLgAJsQDO%2BAIYAnERhwES5cACNZwAB4AudtgC2qgKYyIcNOHAA3UsRHhNKFmzGTZY-uCl7DJi%2BBkjQmwZCgAmdHobOzUNAEZQJ1ZRCWk5XgFvXANjGSA&fileType=.ts)
## Options[​](#options)
This rule accepts the following options:
```
type Options = [
{
/** Whether to suggest removing `void` when the argument has type `never`. */
checkNever?: boolean;
},
];
const defaultOptions: Options = [{ checkNever: false }];
```
### `checkNever`[​](#checknever)
Whether to suggest removing `void` when the argument has type `never`. Default: `false`.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t mind extra `void`s in your project, you can avoid this rule.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-meaningless-void-operator.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-meaningless-void-operator.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-meaningless-void-operator.mdx)- [Examples](#examples)- [Examples](#examples-1)- [Options](#options)[`checkNever`](#checknever)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)