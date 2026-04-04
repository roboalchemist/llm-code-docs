# Source: https://typescript-eslint.io/rules/no-array-delete

On this page# no-array-delete
Disallow using the `delete` operator on array values.
✅Extending [`"plugin:@typescript-eslint/recommended-type-checked"`](/users/configs#recommended-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
When using the `delete` operator with an array value, the array&#x27;s `length` property is not affected,
but the element at the specified index is removed and leaves an empty slot in the array.
This is likely to lead to unexpected behavior. As mentioned in the
[MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete#deleting_array_elements),
the recommended way to remove an element from an array is by using the
[`Array#splice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice) method.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-array-delete": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-array-delete": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oENppvCtACaIk%2BROiiI%2BHaJHBgAviEVA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
declare const arr: number[];
delete arr[0];
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oENppvCtACaIk%2BROiiI%2BHaJHBgAviEVA&code=CYUwxgNghgTiAEYD2A7AzgF3rGAueKArgLYBGIMA2gLoDcAUPaBCBgjpQAx1A&fileType=.ts)```
declare const arr: number[];
arr.splice(0, 1);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oENppvCtACaIk%2BROiiI%2BHaJHBgAviEVA&code=CYUwxgNghgTiAEYD2A7AzgF3rGAueKArgLYBGIMA2gLoDcAUPTgHRoAOEAlmCABQAMAGngBGAJS0gA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
When you want to allow the delete operator with array expressions.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-array-delete.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-array-delete.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-array-delete.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)