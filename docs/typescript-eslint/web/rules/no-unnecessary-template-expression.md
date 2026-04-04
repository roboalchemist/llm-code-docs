# Source: https://typescript-eslint.io/rules/no-unnecessary-template-expression

On this page# no-unnecessary-template-expression
Disallow unnecessary template expressions.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
This rule reports template literals that contain substitution expressions (also variously referred to as embedded expressions or string interpolations) that are unnecessary and can be simplified.
Migration from `no-useless-template-literals`This rule was formerly known as [`no-useless-template-literals`](/rules/no-useless-template-literals).
The new name is a drop-in replacement with identical functionality.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unnecessary-template-expression": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unnecessary-template-expression": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK18iALbF4QifQAexaIMocm6KImjQO0SODABfEEaA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
// Static values can be incorporated into the surrounding template.
const ab1 = `${&#x27;a&#x27;}${&#x27;b&#x27;}`;
const ab2 = `a${&#x27;b&#x27;}`;
type AB1 = `${&#x27;A&#x27;}${&#x27;B&#x27;}`;
type AB2 = `A${&#x27;B&#x27;}`;
const stringWithNumber = `${&#x27;1 + 1 = &#x27;}${2}`;
const stringWithBoolean = `${&#x27;true is &#x27;}${true}`;
// Some simple expressions that are already strings
// can be rewritten without a template at all.
const text = &#x27;a&#x27;;
const wrappedText = `${text}`;
type Text = &#x27;A&#x27;;
type WrappedText = `${Text}`;
declare const intersectionWithString: string & { _brand: &#x27;test-brand&#x27; };
const wrappedIntersection = `${intersectionWithString}`;
type IntersectionWithString = string & { _brand: &#x27;test-brand&#x27; };
type WrappedIntersection = `${IntersectionWithString}`;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK18iALbF4QifQAexaIMocm6KImjQO0SODABfEEaA&code=PTAEGUBcENISwMagG7QDYFcCmBnUDoA7UAIy1DkIQHsAnABztiwBMLDJrRIALcnDLVrUMhFpQDm3LAFt6aZgDoAUMpqEckUNBIBGUAF5QAAwAkAbwDk0SwF8LlkneMBuNdQ1adAJkMnoDk62rsqQAJ705ACCAEL6RmZWUXYOMc5u4ZGgsb4JUanpquqaoJq0kgDqcLwAchgyZLR%2BiZb6ANSg8aAp5t7Bbu6epZDlhBJVvDHU1GhYRM0OI9gUeD1LWP2qIBDUMvxwcrOgWAAe9LS4OHAeeLyw2hfaaBfQLGHDoxI4ytsExGSgC4Ad3KkEgWGIQOqPBEXmkh2Y2i8aDQKkGJXBJy0RmsljcxS0IOg9EiLAAKqdsSYLJjIJtMuQKVi-JZkhkIuQKrRiaSmVTEnzNsoWFgEApHgT2ODaDhRfAPBMeFBPgAuD6SUAAMlA5lAAH0SNyxGrLODNABaQ1EFiWUC2fE3QnckmsACSHCwMrl12ICQslGlsoQ8sIiuVknpHNA7sD3oV0PDYz8ZQ12t1BqNLBNZsglsztvtoSjXJ5bo9XuDPoW5hjnqDIbDIwjriAA&fileType=.ts)```
// Static values can be incorporated into the surrounding template.
const ab1 = `ab`;
const ab2 = `ab`;
type AB = `AB`;
// Transforming enum members into string unions using template literals is allowed.
enum ABC {
A = &#x27;A&#x27;,
B = &#x27;B&#x27;,
C = &#x27;C&#x27;,
}
type ABCUnion = `${ABC}`;
type A = `${ABC.A}`;
// Interpolating type parameters is allowed.
type TextUtil<T extends string> = `${T}`;
const stringWithNumber = `1 + 1 = 2`;
const stringWithBoolean = `true is true`;
// Some simple expressions that are already strings
// can be rewritten without a template at all.
const text = &#x27;a&#x27;;
const wrappedText = text;
type Text = &#x27;A&#x27;;
type WrappedText = Text;
declare const intersectionWithString: string & { _brand: &#x27;test-brand&#x27; };
const wrappedIntersection = intersectionWithString;
type IntersectionWithString = string & { _brand: &#x27;test-brand&#x27; };
type WrappedIntersection = IntersectionWithString;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK18iALbF4QifQAexaIMocm6KImjQO0SODABfEEaA&code=PTAEGUBcENISwMagG7QDYFcCmBnUDoA7UAIy1DkIQHsAnABztiwBMLDJrRIALcnDLVrUMhFpQDm3LAFt6aZgDoAUMpqEckUNBIBGUAF5QAAx3GA3GuoatOgEyGTZy5ACe9cgEEAQo%2BM%2BLVRBQABVaIhwAMzoZSVAsQgwZUBlZMlo8Sk5QTVo40ThrPAwcOMhZeWZQNDhy8LRMvHQ0agB3VhUEpNAfAGFQAG9lUB7HAHJPMYAaYdBfIzHvadn%2Bhd7lgF9lNw8e716AVUJC4iNjABIBvo3Ana8-S77FTxvLZWCASQ4sBmoFeEIUjuoHo0HCqTqjW0aBa7RYKmBISwAA9IAd4GgADwheKohIsPC5SQAPgeAxCr1U6k0OUgeUBAHVajwAHJJdJ%2BfQAalA%2BiMdkCVhstPpEiZvG81D%2BWCIfjp2AoeHlWEFwXA1FSOTgcjQ5BR9FouFKRW4PFg2kN0MN0BYrhFkhw7zABGIZFAhtaeUg5WIrWZIls0h1VXNzRUQpp5VR42gY0s1K0nug9A8LCR0aMUcgLnc5HTWgWkxzuwZ4RTrHzjnzbxYWAQCktCfYkLr8Gs4p4UFFAC57YDQAAyQagAD6JHCYl7Y3KmgAtOOiCwxqANvGiomy6mvi2EG3Ts2fjhWycO13JMXyNvD8f28yz-2jET%2B0OBqOF5PQNPcJB5xOlyuL1AUtky3b4Mhvfcr3A3cTzvOlzyAA&fileType=.ts)
infoThis rule does not aim to flag template literals without substitution expressions that could have been written as an ordinary string.
That is to say, this rule will not help you turn ``this`` into `"this"`.
If you are looking for such a rule, you can configure the [`@stylistic/ts/quotes`](https://eslint.style/rules/ts/quotes) rule to do this.
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
When you want to allow string expressions inside template literals.
## Related To[​](#related-to)
- [`restrict-template-expressions`](/rules/restrict-template-expressions)
- [`@stylistic/ts/quotes`](https://eslint.style/rules/ts/quotes)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unnecessary-template-expression.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unnecessary-template-expression.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unnecessary-template-expression.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)