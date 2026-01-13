# Source: https://typescript-eslint.io/rules/no-useless-default-assignment

On this page# no-useless-default-assignment
Disallow default values that will never be used.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
[Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters) and [default values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#default_value) are only used if the parameter or property is `undefined`.
That can happen when a value is missing, or when one is provided and set to `undefined`.
If a non-`undefined` value is guaranteed to be provided, then there is no need to define a default.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-useless-default-assignment": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-useless-default-assignment": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tmUSWWS0AJogBmAQwR1xAygHMmAW0Qt0URNGgdokcGAC%2BIfUA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
function Bar({ foo = &#x27;&#x27; }: { foo: string }) {
return foo;
}
const { foo = &#x27;&#x27; } = { foo: &#x27;bar&#x27; };
const [foo = &#x27;&#x27;] = [&#x27;bar&#x27;];
[1, 2, 3].map((a = 42) => a + 1);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tmUSWWS0AJogBmAQwR1xAygHMmAW0Qt0URNGgdokcGAC%2BIfUA&code=GYVwdgxgLglg9mABAIQIYCcAUBvRw5yIC8iA5KYgL4Bciu%2BctAzlOjGAOZUCUdAUIkToAplBDokDANx9KfPhAQs6eAsTIVK6%2BgVqkARhk0yFSqIgDaDdeQC66iwaO2TFgIwAaRACYvAZlsAOgBbVAAHTExUdQAWb14iAD5EaIBqRDduKSA&fileType=.ts)```
function Bar({ foo = &#x27;&#x27; }: { foo?: string }) {
return foo;
}
const { foo = &#x27;&#x27; } = { foo: undefined };
const [foo = &#x27;&#x27;] = [undefined];
[1, 2, 3, undefined].map((a = 42) => a + 1);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tmUSWWS0AJogBmAQwR1xAygHMmAW0Qt0URNGgdokcGAC%2BIfUA&code=GYVwdgxgLglg9mABAIQIYCcAUBvRw5yIC8iA5KYgL4Bciu%2BcA-LQM5ToxgDmVAlHQChEidAFMoIdEgYBuAZQECICNnTwFiZCpU30CtcABNRwTqMNU5SlVEQBtBpvIBdTXaMmzh51bsBGABpEACYggGYgj1Mwc2cAOgBbVAAHTExUTQAWYP4iAD5EDIBqRD9eGSA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you use default values defensively against runtime values that bypass type checking, or for documentation purposes, you may want to disable this rule.
In a few niche situations (e.g. [express.js error handler functions](https://expressjs.com/en/guide/error-handling.html)), the runtime [`.length`]([https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length) of a function) may be important to you.
In these rare cases, you may need to disable the fixes produced by this rule, which can affect function&#x27;s `.length` value.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-useless-default-assignment.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-useless-default-assignment.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-useless-default-assignment.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)