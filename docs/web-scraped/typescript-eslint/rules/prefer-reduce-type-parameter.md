# Source: https://typescript-eslint.io/rules/prefer-reduce-type-parameter

On this page# prefer-reduce-type-parameter
Enforce using type parameter when calling `Array#reduce` instead of using a type assertion.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
It&#x27;s common to call `Array#reduce` with a generic type, such as an array or object, as the initial value.
Since these values are empty, their types are not usable:
- `[]` has type `never[]`, which can&#x27;t have items pushed into it as nothing is type `never`
- `{}` has type `{}`, which doesn&#x27;t have an index signature and so can&#x27;t have properties added to it
A common solution to this problem is to use an `as` assertion on the initial value.
While this will work, it&#x27;s not the most optimal solution as type assertions have subtle effects on the underlying types that can allow bugs to slip in.
A better solution is to pass the type in as a generic type argument to `Array#reduce` explicitly.
This means that TypeScript doesn&#x27;t have to try to infer the type, and avoids the common pitfalls that come with assertions.
This rule looks for calls to `Array#reduce`, and reports if an initial value is being passed & asserted.
It will suggest instead pass the asserted type to `Array#reduce` as a generic type argument.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-reduce-type-parameter": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-reduce-type-parameter": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls4AmsMolpFStYgENoUgLaJ8vdFF7QA9tEjgwAXxC6gA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
[1, 2, 3].reduce((arr, num) => arr.concat(num * 2), [] as number[]);
[&#x27;a&#x27;, &#x27;b&#x27;].reduce(
(accum, name) => ({
...accum,
[name]: true,
}),
{} as Record<string, boolean>,
);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls4AmsMolpFStYgENoUgLaJ8vdFF7QA9tEjgwAXxC6gA&code=NoRgNABATJDMC6A6ATgUwCYFcDGqAUeAhsspAHaYC2AlBALwB8Exyi2A9mdoQC54WUIAKmjVIweMwDOEAQCNUyCdQDcAKDXAA5IS2QtcrUjRZceNRAhFs2KuUKVUtRlYDeFyxETfCNux8tgMgdUeAAuCB5kTFQwDwBfMQ9XeOkIACVUDmR0AB4pKIBLMgBzSDl2dgAbVEIyBjjVIA&fileType=.ts)```
[1, 2, 3].reduce<number[]>((arr, num) => arr.concat(num * 2), []);
[&#x27;a&#x27;, &#x27;b&#x27;].reduce<Record<string, boolean>>(
(accum, name) => ({
...accum,
[name]: true,
}),
{},
);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0Wls4AmsMolpFStYgENoUgLaJ8vdFF7QA9tEjgwAXxC6gA&code=NoRgNABATJDMC6A6ATgUwCYFcDGqA8AdpgLYBGqyw8AfABS0CGyykRxAlBALzURPKJsAewLYGAF1psIAKmjtIVdgG4AUKuAByBpsibSmpGiy48AJVTDk6PAGdxyAJYEA5pFJChAG1QMC1OlUICEZsbBJWBmJUTh4QgG8g4IhEVIYwiKTg4AIo1HgALggHTFQwJIBfBST4ivKVIA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
This rule can sometimes be difficult to work around when creating objects using a `.reduce`.
See [[prefer-reduce-type-parameter] unfixable reporting #3440](https://github.com/typescript-eslint/typescript-eslint/issues/3440) for more details.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-reduce-type-parameter.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-reduce-type-parameter.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-reduce-type-parameter.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)