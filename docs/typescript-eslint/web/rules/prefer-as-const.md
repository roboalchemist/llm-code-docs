# Source: https://typescript-eslint.io/rules/prefer-as-const

On this page# prefer-as-const
Enforce the use of `as const` over literal type.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
There are two common ways to tell TypeScript that a literal value should be interpreted as its literal type (e.g. `2`) rather than general primitive type (e.g. `number`);
- `as const`: telling TypeScript to infer the literal type automatically
- `as` with the literal type: explicitly telling the literal type to TypeScript
`as const` is generally preferred, as it doesn&#x27;t require re-typing the literal value.
This rule reports when an `as` with an explicit literal type can be replaced with an `as const`.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-as-const": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-as-const": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WloENktMgHsmyfOii9oI6JHBgAviCVA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
let bar: 2 = 2;
let foo = <&#x27;bar&#x27;>&#x27;bar&#x27;;
let foo = { bar: &#x27;baz&#x27; as &#x27;baz&#x27; };
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WloENktMgHsmyfOii9oI6JHBgAviCVA&code=DYUwLgBARghgTgLggJggXhQbgFCkgMwHtD0IAeAcljgoD4r4Kc8IiSMBvaeJBgLwoQYAZwj9BAX0xA&fileType=.ts)```
let foo = &#x27;bar&#x27;;
let foo = &#x27;bar&#x27; as const;
let foo: &#x27;bar&#x27; = &#x27;bar&#x27; as const;
let bar = &#x27;bar&#x27; as string;
let foo = <string>&#x27;bar&#x27;;
let foo = { bar: &#x27;baz&#x27; };
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WloENktMgHsmyfOii9oI6JHBgAviCVA&code=DYUwLgBAZg9jEF4IHIBGBDATsg3AKFElniTS2QnQGcIBjGAOyrH0OjgC4UNtFvzKNekxYFwEHnzK9qEZpgCWDAOatxxPgB55S5QD5puMUTh8A3hKxcyALwoBfHEA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t care about which style of literals assertions is used in your code, then you will not need this rule.
However, keep in mind that inconsistent style can harm readability in a project.
We recommend picking a single option for this rule that works best for your project.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-as-const.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-as-const.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-as-const.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)