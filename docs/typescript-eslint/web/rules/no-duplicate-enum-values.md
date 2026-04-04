# Source: https://typescript-eslint.io/rules/no-duplicate-enum-values

On this page# no-duplicate-enum-values
Disallow duplicate enum member values.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
Although TypeScript supports duplicate enum member values, people usually expect members to have unique values within the same enum. Duplicate values can lead to bugs that are hard to track down.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-duplicate-enum-values": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-duplicate-enum-values": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNZjGyAQ3yJ6TWAFtaAN0HxYKdFETRoHaJHBgAviG1A)
## Examples[​](#examples)
This rule disallows defining an enum with multiple members initialized to the same value.
This rule only enforces on enum members initialized with string or number literals.
Members without an initializer or initialized with an expression are not checked by this rule.
- ❌ Incorrect- ✅ Correct```
enum E {
A = 0,
B = 0,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNZjGyAQ3yJ6TWAFtaAN0HxYKdFETRoHaJHBgAviG1A&code=KYOwrgtgBAolDeAoKUCCUC8UAMAaZUAQpjvgL5A&fileType=.ts)```
enum E {
A = &#x27;A&#x27;,
B = &#x27;A&#x27;,
C = `A`,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNZjGyAQ3yJ6TWAFtaAN0HxYKdFETRoHaJHBgAviG1A&code=KYOwrgtgBAolDeAoKUCCUC8UDkrsBpkoAhTHPQlAYTIANVbCBfIA&fileType=.ts)```
enum E {
A = 0,
B = 1,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNZjGyAQ3yJ6TWAFtaAN0HxYKdFETRoHaJHBgAviG1A&code=KYOwrgtgBAolDeAoKUCCUC8UAMAaZUAQplAIz4C%2BQA&fileType=.ts)```
enum E {
A = &#x27;A&#x27;,
B = &#x27;B&#x27;,
C = `C`,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNZjGyAQ3yJ6TWAFtaAN0HxYKdFETRoHaJHBgAviG1A&code=KYOwrgtgBAolDeAoKUCCUC8UDkrsBpkoAhTHYgogYTIAMrbCBfIA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
It can sometimes be useful to include duplicate enum members for very specific use cases.
For example, when renaming an enum member, it can sometimes be useful to keep the old name until a scheduled major breaking change.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
In general, if your project intentionally duplicates enum member values, you can avoid this rule.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-duplicate-enum-values.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-duplicate-enum-values.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-duplicate-enum-values.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)