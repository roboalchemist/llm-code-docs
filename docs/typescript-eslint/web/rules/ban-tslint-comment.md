# Source: https://typescript-eslint.io/rules/ban-tslint-comment

On this page# ban-tslint-comment
Disallow `// tslint:<rule-flag>` comments.
🎨Extending [`"plugin:@typescript-eslint/stylistic"`](/users/configs#stylistic) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
Useful when migrating from TSLint to ESLint. Once TSLint has been removed, this rule helps locate TSLint annotations (e.g. `// tslint:disable`).
See the [TSLint rule flags docs](https://palantir.github.io/tslint/usage/rule-flags) for reference.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/ban-tslint-comment": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/ban-tslint-comment": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6AIwEMnb9lGWtMgHsAtqMQt0URNGjDokcGAC%2BIFUA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
/* tslint:disable */
/* tslint:enable */
/* tslint:disable:rule1 rule2 rule3... */
/* tslint:enable:rule1 rule2 rule3... */
// tslint:disable-next-line
someCode(); // tslint:disable-line
// tslint:disable-next-line:rule1 rule2 rule3...
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6AIwEMnb9lGWtMgHsAtqMQt0URNGjDokcGAC%2BIFUA&code=PQKgBALgzgNglgOwgLgCZygQwEYwKZgjABQoksiKeCO%2BhJZ08SaGteyATgK74CMYHvgBMg3ngDMAOhn1S4JpWTV2XcQKF5Rm6bKKlg5ZinRZceALQI8ADwgXmeYlAD2AWzwBhF6jwAKAEoAbjBgQ0UWU3YHRCcwoyUo8ytbe0c1fjERLMkZKSA&fileType=.ts)```
// This is a comment that just happens to mention tslint
/* This is a multiline comment that just happens to mention tslint */
someCode(); // This is a comment that just happens to mention tslint
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6AIwEMnb9lGWtMgHsAtqMQt0URNGjDokcGAC%2BIFUA&code=PTAEBUAsEsGdTqAhqAxgewLaYKYDsAXUAyJIgKwFdYjSAHO-eA9UXQ6dPY2AG2kIAoYACoIMeIhSZKvAtH54caLOyIkyoKjVD1GeZqzWduBPgKIjgg2FhwBhdABMcACgCUAblAhxiKSrY%2BOqkFNS0SAxMxEbBJjyKBEA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you are still using TSLint alongside ESLint.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/ban-tslint-comment.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/ban-tslint-comment.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/ban-tslint-comment.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)