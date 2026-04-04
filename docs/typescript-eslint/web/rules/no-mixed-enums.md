# Source: https://typescript-eslint.io/rules/no-mixed-enums

On this page# no-mixed-enums
Disallow enums from having both number and string members.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
TypeScript enums are allowed to assign numeric or string values to their members.
Most enums contain either all numbers or all strings, but in theory you can mix-and-match within the same enum.
Mixing enum member types is generally considered confusing and a bad practice.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-mixed-enums": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-mixed-enums": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtKAPRABN6TWN1QZIiaNA7RI4MAF8QSoA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct (Explicit Numbers)- ✅ Correct (Implicit Numbers)- ✅ Correct (Strings)```
enum Status {
Unknown,
Closed = 1,
Open = &#x27;open&#x27;,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtKAPRABN6TWN1QZIiaNA7RI4MAF8QSoA&code=KYOwrgtgBAygLgQzmAzlA3gKClAqiAaxAHsB3EAGmygGEAbYlYAEygF4oBGKnAeQAdQ7KAHJigkCKoBfIA&fileType=.ts)```
enum Status {
Unknown = 0,
Closed = 1,
Open = 2,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtKAPRABN6TWN1QZIiaNA7RI4MAF8QSoA&code=KYOwrgtgBAygLgQzmAzlA3gKClAqiAaxAHsB3EKAXigAYAabKAYQBtiVgATKqARgZwB5AA6geAJgYBfIA&fileType=.ts)```
enum Status {
Unknown,
Closed,
Open,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtKAPRABN6TWN1QZIiaNA7RI4MAF8QSoA&code=KYOwrgtgBAygLgQzmAzlA3gKClAqiAaxAHsB3EAGmygGEAbYlYAEypwHkAHUKgXyA&fileType=.ts)```
enum Status {
Unknown = &#x27;unknown&#x27;,
Closed = &#x27;closed&#x27;,
Open = &#x27;open&#x27;,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oFtKAPRABN6TWN1QZIiaNA7RI4MAF8QSoA&code=KYOwrgtgBAygLgQzmAzlA3gKClAqiAaxAHsB3EKAXigHIxCTyaAabKAYQBtiVgATKrQDG3XnxZsA8gAdQgmsVkgJAXyA&fileType=.ts)
## Iteration Pitfalls of Mixed Enum Member Values[​](#iteration-pitfalls-of-mixed-enum-member-values)
Enum values may be iterated over using `Object.entries`/`Object.keys`/`Object.values`.
If all enum members are strings, the number of items will match the number of enum members:
```
enum Status {
Closed = &#x27;closed&#x27;,
Open = &#x27;open&#x27;,
}
// [&#x27;closed&#x27;, &#x27;open&#x27;]
Object.values(Status);
```
But if the enum contains members that are initialized with numbers -including implicitly initialized numbers— then iteration over that enum will include those numbers as well:
```
enum Status {
Unknown,
Closed = 1,
Open = &#x27;open&#x27;,
}
// ["Unknown", "Closed", 0, 1, "open"]
Object.values(Status);
```
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t mind the confusion of mixed enum member values and don&#x27;t iterate over enums, you can safely disable this rule.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-mixed-enums.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-mixed-enums.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-mixed-enums.mdx)- [Examples](#examples)- [Iteration Pitfalls of Mixed Enum Member Values](#iteration-pitfalls-of-mixed-enum-member-values)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)