# Source: https://typescript-eslint.io/rules/consistent-return

On this page# consistent-return
Require `return` statements to either always or never specify values.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
This rule extends the base [`consistent-return`](https://eslint.org/docs/latest/rules/consistent-return) rule from ESLint core. It adds support for functions that return `void` or `Promise<void>`.
warningIf possible, it is recommended to use tsconfig&#x27;s [`noImplicitReturns`](https://www.typescriptlang.org/tsconfig/#noImplicitReturns) option rather than this rule. `noImplicitReturns` is powered by TS&#x27;s type information and control-flow analysis so it has better coverage than this rule.
- ❌ Incorrect- ✅ Correct```
function foo(): undefined {}
function bar(flag: boolean): undefined {
if (flag) return foo();
return;
}
async function baz(flag: boolean): Promise<undefined> {
if (flag) return;
return foo();
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQMYHsA7ZAS2QBdFDyBaaRc2aQ9KfAM3cgBpxtIAAuQCeABxS5oJUbRTwS1APQFiZStToMmLDJETRo%2BaJD4BfEKaA&code=GYVwdgxgLglg9mABMOcAUBKAXI8ATAU2BjAL0QG8BfAKFElgUQCMBDAJzWABtWBzHM1TcCrMNlxhCxUuQo1EiGMERdefDInYEoIdkhToMAbgVadesKdo1WAZwCekZOGjwkbAF5r%2Bg4aPEcAAV2OABbGDsCAB58IhIyAD5KM2VVHn5NbV19U0Vsy2RUTGsgA&fileType=.ts)```
function foo(): void {}
function bar(flag: boolean): void {
if (flag) return foo();
return;
}
async function baz(flag: boolean): Promise<void | number> {
if (flag) return 42;
return;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQMYHsA7ZAS2QBdFDyBaaRc2aQ9KfAM3cgBpxtIAAuQCeABxS5oJUbRTwS1APQFiZStToMmLDJETRo%2BaJD4BfEKaA&code=GYVwdgxgLglg9mABMOcAUBKAXIgbnGAE0QG8BfAKFElgUQCMBDAJzWABtGBzHe1dgKaMw2PAWIkKiRDGCI2nLhkTMBUEMyQp0GANxSVajWH2UKjAM4BPSMnDR4SJgC8F3XvyEicABWZwAWxgLAQAefCJEAB9EMBAA%2BgFmAD5SA1l5Dm5lVXVNRAAWACZ9aVzjUyA&fileType=.ts)
## Options[​](#options)
See [`eslint/consistent-return`&#x27;s options](https://eslint.org/docs/rules/consistent-return#options).
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"consistent-return": "off",
"@typescript-eslint/consistent-return": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"consistent-return": "off",
"@typescript-eslint/consistent-return": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQMYHsA7ZAS2QBdFDyBaaRc2aQ9KfAM3cgBpxtIAAuQCeABxS5oJUbRTwS1APQFiZStToMmLDJETRo%2BaJD4BfEKaA)
## When Not To Use It[​](#when-not-to-use-it)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/consistent-return.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/consistent-return.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/consistent-return.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/consistent-return.mdx)- [Options](#options)- [How to Use](#how-to-use)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)