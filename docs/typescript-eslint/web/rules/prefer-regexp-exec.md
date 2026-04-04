# Source: https://typescript-eslint.io/rules/prefer-regexp-exec

On this page# prefer-regexp-exec
Enforce `RegExp#exec` over `String#match` if no global flag is provided.
🎨Extending [`"plugin:@typescript-eslint/stylistic-type-checked"`](/users/configs#stylistic-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
`String#match` is defined to work the same as `RegExp#exec` when the regular expression does not include the `g` flag.
Keeping to consistently using one of the two can help improve code readability.
This rule reports when a `String#match` call can be replaced with an equivalent `RegExp#exec`.
`RegExp#exec` may also be slightly faster than `String#match`; this is the reason to choose it as the preferred usage.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-regexp-exec": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-regexp-exec": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls4DmiAB7F6wxGXRRe0APbRI4MAF8QKoA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
&#x27;something&#x27;.match(/thing/);
&#x27;some things are just things&#x27;.match(/thing/);
const text = &#x27;something&#x27;;
const search = /thing/;
text.match(search);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls4DmiAB7F6wxGXRRe0APbRI4MAF8QKoA&code=OQZw9gtgpgLgFgSwHYHNgDoIEMYGM4AUA9PMikQJQDcAUDaJFAASmohNYBOzAVgK4gYLRGwzY8hEiPLU6uMEkEsoADyEBeJg2is0teYqEgoXfE01SyRWjFUxMOfAWOm41IA&fileType=.ts)```
/thing/.exec(&#x27;something&#x27;);
&#x27;some things are just things&#x27;.match(/thing/g);
const text = &#x27;something&#x27;;
const search = /thing/;
search.exec(text);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls4DmiAB7F6wxGXRRe0APbRI4MAF8QKoA&code=PQFwFglgdg5sB0BTAHogxgCgOQGcD2AtouNDFgJQDcAUNboYgAQmw6MCGATkwFYCuOEM0iss8AuxBowGUCLgwqtNHiiDmKIQF5G9IizI0VaoTkRdpjHXNLAaZi2CSpMITVSA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you prefer consistent use of `String#match` for both with `g` flag and without it, you can turn this rule off.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-regexp-exec.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-regexp-exec.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-regexp-exec.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)