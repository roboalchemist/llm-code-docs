# Source: https://typescript-eslint.io/rules/no-invalid-this

On this page# no-invalid-this
Disallow `this` keywords outside of classes or class-like objects.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
dangerThe code problem checked by this ESLint rule is automatically checked by the TypeScript compiler. Thus, it is not recommended to turn on this rule in new TypeScript projects. You only need to enable this rule if you prefer the ESLint error messages over the TypeScript compiler error messages.
(Note that technically, TypeScript will only catch this if you have the `strict` or `noImplicitThis` flags enabled. These are enabled in most TypeScript projects, since they are considered to be best practice.)
This rule extends the base [`no-invalid-this`](https://eslint.org/docs/latest/rules/no-invalid-this) rule from ESLint core. It adds support for TypeScript&#x27;s `this` parameters.
## Options[​](#options)
See [`eslint/no-invalid-this`&#x27;s options](https://eslint.org/docs/rules/no-invalid-this#options).
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"no-invalid-this": "off",
"@typescript-eslint/no-invalid-this": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"no-invalid-this": "off",
"@typescript-eslint/no-invalid-this": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAS1wDcBDeYgE0IBcALY1DSfAMw8gBpxtIAAXoBPAA4oAxtGJj6hFNVz0A9ARLkqtBs1ZRE0aPmiR%2BAXxBmgA)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-invalid-this.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-invalid-this.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/no-invalid-this.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-invalid-this.mdx)- [Options](#options)- [How to Use](#how-to-use)- [Resources](#resources)