# Source: https://typescript-eslint.io/rules/prefer-for-of

On this page# prefer-for-of
Enforce the use of `for-of` loop over the standard `for` loop where possible.
🎨Extending [`"plugin:@typescript-eslint/stylistic"`](/users/configs#stylistic) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
Many developers default to writing `for (let i = 0; i < ...` loops to iterate over arrays.
However, in many of those arrays, the loop iterator variable (e.g. `i`) is only used to access the respective element of the array.
In those cases, a `for-of` loop is easier to read and write.
This rule recommends a for-of loop when the loop index is only used to read from an array that is being iterated.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-for-of": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-for-of": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wlq4D2fAV3RRe0IZHBgAviFlA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
declare const array: string[];
for (let i = 0; i < array.length; i++) {
console.log(array[i]);
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wlq4D2fAV3RRe0IZHBgAviFlA&code=CYUwxgNghgTiAEYD2A7AzgF3rGUCeAXPJjAJYoDmA2gLoDcAUAwGZIzwAUEIWp8AvPAAMdeHwA82GLjwA6bpQwALUaQDUagJTwA3g3iJUaJN3lIKHHPiqkamxgF8gA&fileType=.ts)```
declare const array: string[];
for (const x of array) {
console.log(x);
}
for (let i = 0; i < array.length; i++) {
// i is used, so for-of could not be used.
console.log(i, array[i]);
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wlq4D2fAV3RRe0IZHBgAviFlA&code=CYUwxgNghgTiAEYD2A7AzgF3rGUCeAXPJjAJYoDmA2gLoDcAUAwGZIzwAUy6WAHvEmbYYuPAEp4AbwbxEqNEgggAdBCQUOvMYwC%2BTVuw5KspeAF54ABjrxTAHmGjVIShgAWN0gGovE6bIB6ANtbNHgAVzQQYAAaYiR4AwBaQTlwiGB4FCQsACMESOjlGTl0RRU1DVI4nHwqUhptBh0gA&fileType=.ts)
## DOM Elements[​](#dom-elements)
By default, TypeScript&#x27;s type checking only allows `for-of` loops over DOM iterables such as `HTMLCollectionOf` when the `dom.iterable` `lib` option is enabled.
If you are using this rule in a project that works with DOM elements, be sure to enable `dom.iterable` in your TSConfig `lib`.
See [aka.ms/tsconfig#lib](http://aka.ms/tsconfig#lib) for more information.
```
{
"compilerOptions": {
"strict": true,
"lib": ["esnext", "dom", "dom.iterable"]
}
}
```
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
Note that this rule does not use type information to determine whether iterated elements are arrays.
It only checks if a `.length` property is used in a loop.
If your project loops over objects that happen to have `.length`, this rule may report false positives.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-for-of.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-for-of.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-for-of.mdx)- [Examples](#examples)- [DOM Elements](#dom-elements)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)