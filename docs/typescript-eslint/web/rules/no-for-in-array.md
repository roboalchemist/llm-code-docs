# Source: https://typescript-eslint.io/rules/no-for-in-array

On this page# no-for-in-array
Disallow iterating over an array with a for-in loop.
✅Extending [`"plugin:@typescript-eslint/recommended-type-checked"`](/users/configs#recommended-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
A for-in loop (`for (const i in o)`) iterates over the properties of an Object.
While it is legal to use for-in loops with array values, it is not common. There are several potential bugs with this:
- It iterates over all enumerable properties, including non-index ones and the entire prototype chain. For example, [`RegExp.prototype.exec`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec) returns an array with additional properties, and `for-in` will iterate over them. Some libraries or even your own code may add additional methods to `Array.prototype` (either as polyfill or as custom methods), and if not done properly, they may be iterated over as well.
- It skips holes in the array. While sparse arrays are rare and advised against, they are still possible and your code should be able to handle them.
- The "index" is returned as a string, not a number. This can be caught by TypeScript, but can still lead to subtle bugs.
You may have confused for-in with for-of, which iterates over the elements of the array. If you actually need the index, use a regular `for` loop or the `forEach` method.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-for-in-array": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-for-in-array": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oDMPpbmtAIbRoQwuiiJRfSODABfEAqA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
declare const array: string[];
for (const i in array) {
console.log(array[i]);
}
for (const i in array) {
console.log(i, array[i]);
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oDMPpbmtAIbRoQwuiiJRfSODABfEAqA&code=CYUwxgNghgTiAEYD2A7AzgF3rGUCeAXPJjAJYoDmA2gLoDcAUAwGZIzwAUy6Wp852GLjwBKeAG8G8RKjRIIIAHQQkFDjnxVSNEYwC%2BTVuy6ze-FIOFjJ07nIXLVHUgBpLm7boZ6gA&fileType=.ts)```
declare const array: string[];
for (const value of array) {
console.log(value);
}
for (let i = 0; i < array.length; i += 1) {
console.log(i, array[i]);
}
array.forEach((value, i) => {
console.log(i, value);
});
for (const [i, value] of array.entries()) {
console.log(i, value);
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oDMPpbmtAIbRoQwuiiJRfSODABfEAqA&code=CYUwxgNghgTiAEYD2A7AzgF3rGUCeAXPJjAJYoDmA2gLoDcAUAwGZIzwAUy6WAblBACuCJM2wxceAJTwA3g3iJUaJBBAA6CEgod%2BQkFMYBfJq3Yc1WUvAC88AAx141gDzjJmkJQwALJ9YBqOwBGGXlFbhU1TW0OUgAad3wqUhpDBhMGHHx1MwBRKDAfDl0BYUTSGRsAPjkFJXRVDS0dBPg9YXSjdJY2TkisFMSOkBp4USS8dS8MMhA0Dikw%2BsimmNbhsoNjIA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your project is a rare one that intentionally loops over string indices of arrays, you can turn off this rule.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-for-in-array.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-for-in-array.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-for-in-array.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)