# Source: https://typescript-eslint.io/rules/no-dupe-class-members

On this page# no-dupe-class-members
Disallow duplicate class members.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
dangerThe code problem checked by this ESLint rule is automatically checked by the TypeScript compiler. Thus, it is not recommended to turn on this rule in new TypeScript projects. You only need to enable this rule if you prefer the ESLint error messages over the TypeScript compiler error messages.
This rule extends the base [`no-dupe-class-members`](https://eslint.org/docs/latest/rules/no-dupe-class-members) rule from ESLint core. It adds support for TypeScript&#x27;s method overload definitions.
## Options[​](#options)
See [`eslint/no-dupe-class-members`&#x27;s options](https://eslint.org/docs/rules/no-dupe-class-members#options).
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"no-dupe-class-members": "off",
"@typescript-eslint/no-dupe-class-members": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"no-dupe-class-members": "off",
"@typescript-eslint/no-dupe-class-members": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAE1gAdFCBjeAQ2WUIFtEmAjRaVDSfAMz6QANOGyQAAgBcAnhWRVoASzKTCKeItySA9ARLlKNeoxbtO3KJ2j5okUQF8Q9oA)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-dupe-class-members.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-dupe-class-members.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/no-dupe-class-members.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-dupe-class-members.mdx)- [Options](#options)- [How to Use](#how-to-use)- [Resources](#resources)