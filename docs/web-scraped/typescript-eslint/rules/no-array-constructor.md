# Source: https://typescript-eslint.io/rules/no-array-constructor

On this page# no-array-constructor
Disallow generic `Array` constructors.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
This rule extends the base [`no-array-constructor`](https://eslint.org/docs/latest/rules/no-array-constructor) rule from ESLint core. It adds support for the generically typed `Array` constructor (`new Array<Foo>()`).
- ❌ Incorrect- ✅ Correct```
Array(0, 1, 2);
new Array(0, 1, 2);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAQ2mmIE9CBjfXZAFzmof2nSnwDMvIAacNkgABBhQAOKatACW4hoRTwZuBgHoCJMpRp1GzVuwyREZNpEEBfEJaA&code=IIJxEME8AoAYBoAEBGJAmAlAbgFADsBTAd0VAhgRXWyA&fileType=.ts)```
Array<number>(0, 1, 2);
new Array<Foo>(x, y, z);
Array(500);
new Array(someOtherArray.length);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAQ2mmIE9CBjfXZAFzmof2nSnwDMvIAacNkgABBhQAOKatACW4hoRTwZuBgHoCJMpRp1GzVuwyREZNpEEBfEJaA&code=IIJxEME8B4DsFcC2AjApiAfACgAwBoACARkICYBKAbgChZUB3A0CGAMQHt3sAPQyQgF5Vq1ZlCwBWHDmF1GYyFgDO7RKgDyAFwAW6BQDoANqlgBzHVSA&fileType=.ts)
## Options[​](#options)
See [`eslint/no-array-constructor`&#x27;s options](https://eslint.org/docs/rules/no-array-constructor#options).
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"no-array-constructor": "off",
"@typescript-eslint/no-array-constructor": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"no-array-constructor": "off",
"@typescript-eslint/no-array-constructor": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAQ2mmIE9CBjfXZAFzmof2nSnwDMvIAacNkgABBhQAOKatACW4hoRTwZuBgHoCJMpRp1GzVuwyREZNpEEBfEJaA)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-array-constructor.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-array-constructor.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/no-array-constructor.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-array-constructor.mdx)- [Options](#options)- [How to Use](#how-to-use)- [Resources](#resources)