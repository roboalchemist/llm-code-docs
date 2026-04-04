# Source: https://typescript-eslint.io/rules/no-non-null-assertion

On this page# no-non-null-assertion
Disallow non-null assertions using the `!` postfix operator.
🔒Extending [`"plugin:@typescript-eslint/strict"`](/users/configs#strict) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
TypeScript&#x27;s `!` non-null assertion operator asserts to the type system that an expression is non-nullable, as in not `null` or `undefined`.
Using assertions to tell the type system new information is often a sign that code is not fully type-safe.
It&#x27;s generally better to structure program logic so that TypeScript understands when values may be nullable.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-non-null-assertion": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-non-null-assertion": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8lDk3RQx0DtEjgwAXxAqgA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
interface Example {
property?: string;
}
declare const example: Example;
const includesBaz = example.property!.includes(&#x27;baz&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8lDk3RQx0DtEjgwAXxAqgA&code=JYOwLgpgTgZghgYwgAgKIA84FsAOAbFAbwChlkcoB7HaMATwH4AuZAZzClAHMBuYgX2LEAJhAR44UFAkoh2yCJlwEWGbPgh8ZcsMlDiArqNYAhOAC9kAXgVKNAOgrVadAIT39eIxFYAKAOQARhb%2BAJQ8QA&fileType=.ts)```
interface Example {
property?: string;
}
declare const example: Example;
const includesBaz = example.property?.includes(&#x27;baz&#x27;) ?? false;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8lDk3RQx0DtEjgwAXxAqgA&code=JYOwLgpgTgZghgYwgAgKIA84FsAOAbFAbwChlkcoB7HaMATwH4AuZAZzClAHMBuYgX2LEAJhAR44UFAkoh2yCJlwEWGbPgh8ZcsMlDiArqNYAhOAC9kAXgVKNAOgrVaje-rxGIrABQByAEYWvgCUyAwMyPB4rJpAA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your project&#x27;s types don&#x27;t yet fully describe whether certain values may be nullable, such as if you&#x27;re transitioning to `strictNullChecks`, this rule might create many false reports.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-non-null-assertion.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-non-null-assertion.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-non-null-assertion.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)