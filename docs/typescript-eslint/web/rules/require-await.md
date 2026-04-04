# Source: https://typescript-eslint.io/rules/require-await

On this page# require-await
Disallow async functions which do not return promises and have no `await` expression.
✅Extending [`"plugin:@typescript-eslint/recommended-type-checked"`](/users/configs#recommended-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
This rule extends the base [`require-await`](https://eslint.org/docs/latest/rules/require-await) rule from ESLint core. It uses type information to allow promise-returning functions to be marked as `async` without containing an `await` expression.
note`yield` expressions in [async generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*) behave differently from sync generator functions (they unwrap promises), so the base rule never checks async generator functions. On the other hand, our rule uses type information and can detect async generator functions that both never use `await` and always yield non-promise values.
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
async function returnNumber() {
return 1;
}
async function* asyncGenerator() {
yield 1;
}
const num = returnNumber();
const callAsyncGenerator = () => asyncGenerator();
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEI0QR1gEtpEBaAQwHdzCAXdKAewDNnIAacbSAAVoE8ADigDG0QoNqkU8QgDtaAehIFiZKjXoZIiaNEbRIXAL4hjQA&code=IYZwngdgxgBAZgV2gFwJYHsIwE4FNkLYQByCAtgEa7YAUAlDAN4BQMO%2BhWAjANzMC%2BzZqEixEKDBABUMEdADiuCNWDJ0tBizZhUuADYATGLwFComEMhgRyMALzsCRUpWr0%2B5iJZhRgevQCC4ApKKmrY9jD09gB8ssFQisrYquruQA&fileType=.ts)```
function returnNumber() {
return 1;
}
function* syncGenerator() {
yield 1;
}
const num = returnNumber();
const callSyncGenerator = () => syncGenerator();
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEI0QR1gEtpEBaAQwHdzCAXdKAewDNnIAacbSAAVoE8ADigDG0QoNqkU8QgDtaAehIFiZKjXoZIiaNEbRIXAL4hjQA&code=GYVwdgxgLglg9mABAJwKZRMsA5EBbAI1WQAoBKRAbwChEV1MkBGAbmoF9rrRJYEAqRAGcAnpADiqMMQCGUOKQo06ImKgA2AE0SsOXCAiFREYfIgC89DFlyFi5NgbBHEEGevUBlMREnTkcgoWiOQWAHzCPn6y8oosQA&fileType=.ts)
## Options[​](#options)
See [`eslint/require-await`&#x27;s options](https://eslint.org/docs/rules/require-await#options).
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"require-await": "off",
"@typescript-eslint/require-await": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"require-await": "off",
"@typescript-eslint/require-await": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEI0QR1gEtpEBaAQwHdzCAXdKAewDNnIAacbSAAVoE8ADigDG0QoNqkU8QgDtaAehIFiZKjXoZIiaNEbRIXAL4hjQA)
## When Not To Use It[​](#when-not-to-use-it)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/require-await.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/require-await.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/require-await.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/require-await.mdx)- [Examples](#examples)- [Options](#options)- [How to Use](#how-to-use)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)