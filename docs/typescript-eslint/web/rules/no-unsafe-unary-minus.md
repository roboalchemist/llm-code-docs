# Source: https://typescript-eslint.io/rules/no-unsafe-unary-minus

On this page# no-unsafe-unary-minus
Require unary negation to take a number.
✅Extending [`"plugin:@typescript-eslint/recommended-type-checked"`](/users/configs#recommended-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
TypeScript does not prevent you from putting a minus sign before things other than numbers:
```
const s = &#x27;hello&#x27;;
const x = -s; // x is NaN
```
This rule restricts the unary `-` operator to `number | bigint`.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unsafe-unary-minus": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unsafe-unary-minus": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZom5M%2B0QrQC2zWKgyRE0aB2iRwYAL4gNQA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
declare const a: string;
-a;
declare const b: {};
-b;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZom5M%2B0QrQC2zWKgyRE0aB2iRwYAL4gNQA&code=CYUwxgNghgTiAEYD2A7AzgF3lAXPTMAligOYDcAUALRSUWiSwLLpYBGeA3gL6VVtkgA&fileType=.ts)```
-42;
-42n;
declare const a: number;
-a;
declare const b: number;
-b;
declare const c: number | bigint;
-c;
declare const d: any;
-d;
declare const e: 1 | 2;
-e;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZom5M%2B0QrQC2zWKgyRE0aB2iRwYAL4gNQA&code=LQFgTA3AUKYHbSgEwKYGMA2BDATigBGgPZwDOALvlgFz5wCuAtgEYo7TBaKqa4HFlKzWgxZsOzbumx5CJCoRFNWOfAB98zAJYBzLXHIc0U3rIEKktLHACeHJCZn95lFLQCM6-JBgoIQA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unsafe-unary-minus.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unsafe-unary-minus.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unsafe-unary-minus.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)