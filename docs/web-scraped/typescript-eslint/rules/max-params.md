# Source: https://typescript-eslint.io/rules/max-params

On this page# max-params
Enforce a maximum number of parameters in function definitions.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
This rule extends the base [`max-params`](https://eslint.org/docs/latest/rules/max-params) rule from ESLint core. It adds support for TypeScript `this` parameters so they won&#x27;t be counted as a parameter.
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"max-params": "off",
"@typescript-eslint/max-params": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"max-params": "off",
"@typescript-eslint/max-params": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQLYEMAPAWgAd9p9dUNIB7AMwcgBpxtIABAFwE9SUAY2gBLUt2Ip4IgHbcA9ARLlK1dFETRodaJHYBfEPqA)
## Options[​](#options)
See [`eslint/max-params`&#x27;s options](https://eslint.org/docs/rules/max-params#options).
This rule adds the following options:
```
interface Options extends BaseMaxParamsOptions {
countVoidThis?: boolean;
}
const defaultOptions: Options = {
...baseMaxParamsOptions,
countVoidThis: false,
};
```
### `countVoidThis`[​](#countvoidthis)
Whether to count a `this` declaration when the type is `void`. Default: `false`.
Example of a code when `countVoidThis` is set to `false` and `max` is `1`:
- ❌ Incorrect- ✅ Correct```
function hasNoThis(this: void, first: string, second: string) {
// ...
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQLYEMAPAWgAd9p9dUNIB7AMwcgBpxtIABAFwE9SUAY2gBLUt2Ip4IgHbcA9ARLlK1dGADa7bFETRodaK23YsOjoLqw5ANToiAJgBUAFiJpgG%2BeMkRtzHErqAIwmEAC%2BJgC67JHhQA&code=GYVwdgxgLglg9mABACwIYGcBycAqyboAUU%2B6AXIgG5wwAmANIsDAE7pQXssxgDmj6AKYQEtTlG58AlIgDeAKESIA9MsQA6TfIC%2BQA&fileType=.ts)```
function hasNoThis(this: void, first: string) {
// ...
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQLYEMAPAWgAd9p9dUNIB7AMwcgBpxtIABAFwE9SUAY2gBLUt2Ip4IgHbcA9ARLlK1dGADa7bFETRodaK23YsOjoLqw5ANToiAJgBUAFiJpgG%2BeMkRtzHErqAIwmEAC%2BJgC67JHhQA&code=GYVwdgxgLglg9mABACwIYGcBycAqyboAUU%2B6AXIgG5wwAmANIsDAE7pQXssxgDmAlIgDeAKESIA9BMQA6OSIC%2BQA&fileType=.ts)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/max-params.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/max-params.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/max-params.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/max-params.mdx)- [How to Use](#how-to-use)- [Options](#options)[`countVoidThis`](#countvoidthis)- [Resources](#resources)