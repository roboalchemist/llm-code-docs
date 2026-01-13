# Source: https://typescript-eslint.io/rules/prefer-find

On this page# prefer-find
Enforce the use of Array.prototype.find() over Array.prototype.filter() followed by [0] when looking for a single result.
🎨Extending [`"plugin:@typescript-eslint/stylistic-type-checked"`](/users/configs#stylistic-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
When searching for the first item in an array matching a condition, it may be tempting to use code like `arr.filter(x => x > 0)[0]`.
However, it is simpler to use [Array.prototype.find()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find) instead, `arr.find(x => x > 0)`, which also returns the first entry matching a condition.
Because the `.find()` only needs to execute the callback until it finds a match, it&#x27;s also more efficient.
infoBeware the difference in short-circuiting behavior between the approaches.
`.find()` will only execute the callback on array elements until it finds a match, whereas `.filter()` executes the callback for all array elements.
Therefore, when fixing errors from this rule, be sure that your `.filter()` callbacks do not have side effects.
- ❌ Incorrect- ✅ Correct```
[1, 2, 3].filter(x => x > 1)[0];
[1, 2, 3].filter(x => x > 1).at(0);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wlq%2BYATdFF7QA9tEjgwAXxCygA&code=NoRgNABATJDMC6A6AZgSwDYBcCmAnAFAB4QC8AfBMRSAJTAAM8A3AFAuiQwQIoY4HFylCNRqIAhpnz0aTIA&fileType=.ts)```
[1, 2, 3].find(x => x > 1);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wlq%2BYATdFF7QA9tEjgwAXxCygA&code=NoRgNABATJDMC6A6AZgSwHYBMAUAPCAvAHwT4kgCUA3EA&fileType=.ts)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-find": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-find": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wlq%2BYATdFF7QA9tEjgwAXxCygA)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you intentionally use patterns like `.filter(callback)[0]` to execute side effects in `callback` on all array elements, you will want to avoid this rule.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-find.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-find.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-find.mdx)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)