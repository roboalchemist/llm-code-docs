# Source: https://typescript-eslint.io/rules/no-non-null-asserted-optional-chain

On this page# no-non-null-asserted-optional-chain
Disallow non-null assertions after an optional chain expression.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
`?.` optional chain expressions provide `undefined` if an object is `null` or `undefined`.
Using a `!` non-null assertion to assert the result of an `?.` optional chain expression is non-nullable is likely wrong.
Most of the time, either the object was not nullable and did not need the `?.` for its property lookup, or the `!` is incorrect and introducing a type safety hole.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-non-null-asserted-optional-chain": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-non-null-asserted-optional-chain": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8iACa0ONShyaCBZABaDm6KGOgdokcGAC%2BIQ0A)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
foo?.bar!;
foo?.bar()!;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8iACa0ONShyaCBZABaDm6KGOgdokcGAC%2BIQ0A&code=GYexH4DoCMEMCcCEBuAUKCMEAoCUKg&fileType=.ts)```
foo?.bar;
foo?.bar();
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8iACa0ONShyaCBZABaDm6KGOgdokcGAC%2BIQ0A&code=GYexH4DoCMEMCcDcAoUEYIBQEpFA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your project&#x27;s types don&#x27;t yet fully describe whether certain values may be nullable, such as if you&#x27;re transitioning to `strictNullChecks`, this rule might create many false reports.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Further Reading[​](#further-reading)
- [TypeScript 3.7 Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html)
- [Optional Chaining Proposal](https://github.com/tc39/proposal-optional-chaining/)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-non-null-asserted-optional-chain.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-non-null-asserted-optional-chain.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-non-null-asserted-optional-chain.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Further Reading](#further-reading)- [Resources](#resources)