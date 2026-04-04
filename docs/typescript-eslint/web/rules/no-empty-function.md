# Source: https://typescript-eslint.io/rules/no-empty-function

On this page# no-empty-function
Disallow empty functions.
🎨Extending [`"plugin:@typescript-eslint/stylistic"`](/users/configs#stylistic) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
This rule extends the base [`no-empty-function`](https://eslint.org/docs/latest/rules/no-empty-function) rule from ESLint core. It adds support for handling TypeScript specific code that would otherwise trigger the rule.
One example of valid TypeScript specific code that would otherwise trigger the `no-empty-function` rule is the use of [parameter properties](https://www.typescriptlang.org/docs/handbook/classes.html#parameter-properties) in constructor functions.
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"no-empty-function": "off",
"@typescript-eslint/no-empty-function": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"no-empty-function": "off",
"@typescript-eslint/no-empty-function": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaRAWwAcAXAT0IDNZcBjCgS313Sn1tsgBpw2SAAFqZFI2gtKxZPBa4KAegLFy1Og2ZsOGSImjR80SIIC%2BIM0A)
## Options[​](#options)
See [`eslint/no-empty-function`&#x27;s options](https://eslint.org/docs/rules/no-empty-function#options).
This rule adds the following options:
```
type AdditionalAllowOptionEntries =
| &#x27;private-constructors&#x27;
| &#x27;protected-constructors&#x27;
| &#x27;decoratedFunctions&#x27;
| &#x27;overrideMethods&#x27;;
type AllowOptionEntries =
| BaseNoEmptyFunctionAllowOptionEntries
| AdditionalAllowOptionEntries;
interface Options extends BaseNoEmptyFunctionOptions {
allow?: Array<AllowOptionEntries>;
}
const defaultOptions: Options = {
...baseNoEmptyFunctionDefaultOptions,
allow: [],
};
```
### allow: `private-constructors`[​](#allow-private-constructors)
Examples of correct code for the `{ "allow": ["private-constructors"] }` option:
```
class Foo {
private constructor() {}
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaRAWwAcAXAT0IDNZcBjCgS313Sn1tsgBpw2SAAFqZFI2gtKxZPBa4KAegLFy1Og2ZsOGANqDsURNGj5o-Q9ixGhAQ3jx8Ad04HbtyGSkA3OxURCRnZkCjhmc1QrIwBdaLAAXys4iCSEoA&code=MYGwhgzhAEBiD29oG8BQ1oAcBOBLAbmAC4Cm0w8AdhEdgK7BHzYAUAlCgL6qdA&fileType=.ts)
### allow: `protected-constructors`[​](#allow-protected-constructors)
Examples of correct code for the `{ "allow": ["protected-constructors"] }` option:
```
class Foo {
protected constructor() {}
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaRAWwAcAXAT0IDNZcBjCgS313Sn1tsgBpw2SAAFqZFI2gtKxZPBa4KAegLFy1Og2ZsOGANqDsURNGj5o-Q9ixGhAQ3jx8Ad04HbtyGTMVEzRAAmhIzsyBRwzOaoVkYAujFgAL5W8RDJiUA&code=MYGwhgzhAEBiD29oG8BQ1oAcBO8AuApsIQCbTDwB2Ee2ArsfNgBQCUKAvqh0A&fileType=.ts)
### allow: `decoratedFunctions`[​](#allow-decoratedfunctions)
Examples of correct code for the `{ "allow": ["decoratedFunctions"] }` option:
```
class Foo {
@decorator()
foo() {}
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaRAWwAcAXAT0IDNZcBjCgS313Sn1tsgBpw2SAAFqZFI2gtKxZPBa4KAegLFy1Og2ZsOGANqDsURNGj5o-Q9ixGhAQ3jx8Ad04HbtyABNEjc3YpELwAxLVZ2VCsjAF0osABfK1iIRPigA&code=MYGwhgzhAEBiD29oG8BQ1oAEAmBTY8ATmAC5EAUAlOtAGaJUoC%2BqTQA&fileType=.ts)
### allow: `overrideMethods`[​](#allow-overridemethods)
Examples of correct code for the `{ "allow": ["overrideMethods"] }` option:
```
abstract class Base {
protected greet(): void {
console.log(&#x27;Hello!&#x27;);
}
}
class Foo extends Base {
protected override greet(): void {}
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaRAWwAcAXAT0IDNZcBjCgS313Sn1tsgBpw2SAAFqZFI2gtKxZPBa4KAegLFy1Og2ZsOGANqDsURNGj5o-Q9ixGhAQ3jx8Ad04HbtyPgBuJqQBNEAFlECgALfH9UKyMAXRiwAF8reIhkxKA&code=IYIwzgLgTsDGEAJYBthjAgQmgpgg3gFAIIAOUA9hDvDgCYIDmUOOEAFAJQBcCAbhQCWDIiRKwKAOzAVkOAHTIKjdgHIAEjmRKAhKs4BuYggC%2BhM4RRoMAMQoUEOAB7VJdDNjB5RZStVoMFHw4UFDCeMysHDz8QiJmJkA&fileType=.ts)
## When Not To Use It[​](#when-not-to-use-it)
If you are working with external APIs that require functions even if they do nothing, then you may want to avoid this rule.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
Test code often violates this rule as well.
If your testing setup doesn&#x27;t support "mock" or "spy" functions such as [`jest.fn()`](https://jestjs.io/docs/mock-functions), [`sinon.spy()`](https://sinonjs.org/releases/latest/spies), or [`vi.fn()`](https://vitest.dev/guide/mocking.html), you may wish to disable this rule in test files.
Again, if those cases aren&#x27;t extremely common, you might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule in test files.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-empty-function.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-empty-function.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/no-empty-function.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-empty-function.mdx)- [How to Use](#how-to-use)- [Options](#options)[allow: `private-constructors`](#allow-private-constructors)- [allow: `protected-constructors`](#allow-protected-constructors)- [allow: `decoratedFunctions`](#allow-decoratedfunctions)- [allow: `overrideMethods`](#allow-overridemethods)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)