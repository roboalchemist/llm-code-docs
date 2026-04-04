# Source: https://typescript-eslint.io/rules/no-non-null-asserted-nullish-coalescing

On this page# no-non-null-asserted-nullish-coalescing
Disallow non-null assertions in the left operand of a nullish coalescing operator.
🔒Extending [`"plugin:@typescript-eslint/strict"`](/users/configs#strict) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
The `??` nullish coalescing runtime operator allows providing a default value when dealing with `null` or `undefined`.
Using a `!` non-null assertion type operator in the left operand of a nullish coalescing operator is redundant, and likely a sign of programmer error or confusion over the two operators.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-non-null-asserted-nullish-coalescing": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-non-null-asserted-nullish-coalescing": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8iACZ94jZAAtaZDoKTIyzAObooY6B2iRwYAL4gTQA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
foo! ?? bar;
foo.bazz! ?? bar;
foo!.bazz! ?? bar;
foo()! ?? bar;
let x!: string;
x! ?? &#x27;&#x27;;
let x: string;
x = foo();
x! ?? &#x27;&#x27;;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8iACZ94jZAAtaZDoKTIyzAObooY6B2iRwYAL4gTQA&code=GYexEIAIH5sgjAhgJwNwChQgHRIF55SwIoZbi6IFFxJqZgAUAlDSfegDYCmALpAA9wALkgBnXsgCWAOwDmGITDgByFRi59BoidPmLIAXkhYWitmtRA&fileType=.ts)```
foo ?? bar;
foo ?? bar!;
foo!.bazz ?? bar;
foo!.bazz ?? bar!;
foo() ?? bar;
// This is considered correct code because there&#x27;s no way for the user to satisfy it.
let x: string;
x! ?? &#x27;&#x27;;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1s6e4XloBDZMkTR8iACZ94jZAAtaZDoKTIyzAObooY6B2iRwYAL4gTQA&code=GYexAIH5PAjBDATgbgFCgtOSCEaM4B0CAXiVDAiumEaeVlXjSABQCUF21qA9L%2BAAqACwCWAZ3ATwAYxAA7caIAmAU0SrlskIg0yALtrVxVM%2BAFdxq8PuHrVAcknyIAd3gBPcKEQ274S3UbCHF4fQlgL1F9QlQAG1VDAA8ALnBxfURReQBzNCScLgcHZCA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your project&#x27;s types don&#x27;t yet fully describe whether certain values may be nullable, such as if you&#x27;re transitioning to `strictNullChecks`, this rule might create many false reports.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Further Reading[​](#further-reading)
- [TypeScript 3.7 Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html)
- [Nullish Coalescing Proposal](https://github.com/tc39/proposal-nullish-coalescing)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-non-null-asserted-nullish-coalescing.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-non-null-asserted-nullish-coalescing.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-non-null-asserted-nullish-coalescing.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Further Reading](#further-reading)- [Resources](#resources)