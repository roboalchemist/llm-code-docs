# Source: https://typescript-eslint.io/rules/no-unused-expressions

On this page# no-unused-expressions
Disallow unused expressions.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
This rule extends the base [`no-unused-expressions`](https://eslint.org/docs/latest/rules/no-unused-expressions) rule from ESLint core. It supports TypeScript-specific expressions:
- Marks directives in modules declarations (`"use strict"`, etc.) as not unused
- Marks the following expressions as unused if their wrapped value expressions are unused:
Assertion expressions: `x as number;`, `x!;`, `<number>x;`
- Instantiation expressions: `Set<number>;`
Although the type expressions never have runtime side effects (that is, `x!;` is the same as `x;`), they can be used to assert types for testing purposes.
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
Set<number>;
1 as number;
window!;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaWXWZRAE0MQA8AHaFZAS311Q0nwDNvIAacNkgABAC4BPOigDG0ZnTHVk8ZrjEB6AsVLkqtBk1bt0URNGj5okIQF8QtoA&code=MoUwLgPAdgrgtgIxAJwHwG4BQBGABAQwGddZEUsB3ASygBMB7CgQnSA&fileType=.ts)```
function getSet() {
return Set;
}
// Funtion calls are allowed, so type expressions that wrap function calls are allowed
getSet()<number>;
getSet() as Set<unknown>;
getSet()!;
// Namespaces can have directives
namespace A {
&#x27;use strict&#x27;;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaWXWZRAE0MQA8AHaFZAS311Q0nwDNvIAacNkgABAC4BPOigDG0ZnTHVk8ZrjEB6AsVLkqtBk1bt0URNGj5okIQF8QtoA&code=GYVwdgxgLglg9mABAcwKZQMroBQEpEDeAUIogE7ohlJZQDcRAvkUQPSuIBi4sCiEAQwA2QgM6IBFCSLgB3VABMANIlFxEUAJ4AHVIlQAPbRVGj4YcVAAWAqIllkB2xKEi8kgkeMl7hQuYpEaJg4uAA8YCAAtgBGqGQAfAzBtHgS4rRh4ADWYHJgSUHoqbgAhAxsHAByAlGootoCEPX8Akg2AG56CjAU0DBdokRgtfWNzYgAgoQkiADkIKJ6olBkMNBzDIxAA&fileType=.ts)
## Options[​](#options)
See [`eslint/no-unused-expressions`&#x27;s options](https://eslint.org/docs/rules/no-unused-expressions#options).
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"no-unused-expressions": "off",
"@typescript-eslint/no-unused-expressions": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"no-unused-expressions": "off",
"@typescript-eslint/no-unused-expressions": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaWXWZRAE0MQA8AHaFZAS311Q0nwDNvIAacNkgABAC4BPOigDG0ZnTHVk8ZrjEB6AsVLkqtBk1bt0URNGj5okIQF8QtoA)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unused-expressions.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unused-expressions.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/no-unused-expressions.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unused-expressions.mdx)- [Examples](#examples)- [Options](#options)- [How to Use](#how-to-use)- [Resources](#resources)