# Source: https://typescript-eslint.io/rules/no-unnecessary-type-conversion

On this page# no-unnecessary-type-conversion
Disallow conversion idioms when they do not change the type or value of the expression.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
JavaScript provides several commonly used idioms to convert values to a specific type:
- Primitive coercion (e.g. `Boolean(value)`, `String(value)`): using a built-in primitive function
- String concatenation (e.g. `value + &#x27;&#x27;`): turning a value into a string
- Unary coercion (e.g. `+value`, `!!value`): using a built-in operator
- The `.toString()` method defined on many types
These conversions are unnecessary if the value is already of that type.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unnecessary-type-conversion": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unnecessary-type-conversion": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK0ipWmQ5MAbomjJKM9FAXQO0SODABfELqA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
String(&#x27;123&#x27;);
&#x27;123&#x27;.toString();
&#x27;&#x27; + &#x27;123&#x27;;
&#x27;123&#x27; + &#x27;&#x27;;
Number(123);
+123;
~~123;
Boolean(true);
!!true;
BigInt(BigInt(1));
let str = &#x27;123&#x27;;
str += &#x27;&#x27;;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK0ipWmQ5MAbomjJKM9FAXQO0SODABfELqA&code=MoFwTglgdg5gFAcgIwCYDMCCUBuAUM9BAOhAHtRJY4d8EACAajoIzxfqYQT1wDkBXALYAjAKZg4qNDQZS8AP3lzcuAEKlSAG1EBDKHHD9RNAIQnDonqogwAklBBxrdh5Mw1c2kHQDO4OgC8zFLcuH5gjEFc2EA&fileType=.ts)```
function foo(bar: string | number) {
String(bar);
bar.toString();
&#x27;&#x27; + bar;
bar + &#x27;&#x27;;
Number(bar);
+bar;
~~bar;
Boolean(bar);
!!bar;
BigInt(1);
bar += &#x27;&#x27;;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK0ipWmQ5MAbomjJKM9FAXQO0SODABfELqA&code=GYVwdgxgLglg9mABMOcAUAjAhgJwFyIDOUOMYA5ogD6JggC2GApjgJSIDeAUIogMoky5TLlYBuHomw4AdFDgDSFNOMkByNYgDUU3BN7TtiDRMkA5Bsxwi2%2B7dLsA-Rw66SAQqgA2TLGBuqvACEQa4eMOQAkmBQaACMqpKGWgC8xmoSAL5AA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t care about having no-op type conversions in your code, then you can turn off this rule.
If you have types which are not accurate, then this rule might cause you to remove conversions that you actually do need.
## Related To[​](#related-to)
- [no-unnecessary-type-assertion](/rules/no-unnecessary-type-assertion)
- [no-useless-template-literals](/rules/no-useless-template-literals)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unnecessary-type-conversion.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unnecessary-type-conversion.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unnecessary-type-conversion.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)