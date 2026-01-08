# Source: https://typescript-eslint.io/rules/no-unsafe-function-type

On this page# no-unsafe-function-type
Disallow using the unsafe built-in Function type.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
TypeScript&#x27;s built-in `Function` type allows being called with any number of arguments and returns type `any`.
`Function` also allows classes or plain objects that happen to possess all properties of the `Function` class.
It&#x27;s generally better to specify function parameters and return types with the function type syntax.
"Catch-all" function types include:
- `() => void`: a function that has no parameters and whose return is ignored
- `(...args: never) => unknown`: a "top type" for functions that can be assigned any function type, but can&#x27;t be called
Examples of code for this rule:
- ❌ Incorrect- ✅ Correct```
let noParametersOrReturn: Function;
noParametersOrReturn = () => {};
let stringToNumber: Function;
stringToNumber = (text: string) => text.length;
let identity: Function;
identity = value => value;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZoloCeZfJQ5NaRUuiiJo0DtEjgwAXxAagA&code=DYUwLgBAdg9gCgQwE4ILbhEgzgeSQJXAFckoAuCAMSKgGMwBLGKAbgChZEV0xNcDipCAF4IACgCUIgHwQA3gF92bUJCxgkDKAHMAKjAByRVACNMFanUbN26zTv1HTmEeN4APMBTtbtU4bIeYAB0oDpgABbKqhAMACYgUIxgAJ4WNPRMrGzxickprgBuCMBEIDIQxaUgLEA&fileType=.ts)```
let noParametersOrReturn: () => void;
noParametersOrReturn = () => {};
let stringToNumber: (text: string) => number;
stringToNumber = text => text.length;
let identity: <T>(value: T) => T;
identity = value => value;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZoloCeZfJQ5NaRUuiiJo0DtEjgwAXxAagA&code=DYUwLgBAdg9gCgQwE4ILbhEgzgeSQJXAFckoAuCACgEoIBeAPggDcYBLAEwG4AoWRFOjCZcBYqXpVajCAG8Avrx6hIWMEjZQA5gBUYAOSKoARpgqVhADzAU1G7dKZQjppLzubdBl5klXIMv4AdKDaYAAWSioQnCBQYGxgAJ4UADw6DJTMCMBEIBQ6jhA6vLHxiUmS2bkg9EzVeVxAA&fileType=.ts)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unsafe-function-type": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unsafe-function-type": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZoloCeZfJQ5NaRUuiiJo0DtEjgwAXxAagA)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your project is still onboarding to TypeScript, it might be difficult to fully replace all unsafe `Function` types with more precise function types.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Related To[​](#related-to)
- [Avoiding `any`s with Linting and TypeScript](/blog/avoiding-anys)
- [Revamping the `ban-types` rule](/blog/revamping-the-ban-types-rule)
- [`no-empty-object-type`](/rules/no-empty-object-type)
- [`no-restricted-types`](/rules/no-restricted-types)
- [`no-unsafe-call`](/rules/no-unsafe-call)
- [`no-wrapper-object-types`](/rules/no-wrapper-object-types)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unsafe-function-type.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unsafe-function-type.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unsafe-function-type.mdx)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)