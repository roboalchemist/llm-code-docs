# Source: https://typescript-eslint.io/rules/no-unsafe-type-assertion

On this page# no-unsafe-type-assertion
Disallow type assertions that narrow a type.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
Type assertions are a way to tell TypeScript what the type of a value is. This can be useful but also unsafe if you use type assertions to narrow down a type.
This rule forbids using type assertions to narrow a type, as this bypasses TypeScript&#x27;s type-checking. Type assertions that broaden a type are safe because TypeScript essentially knows *less* about a type.
Instead of using type assertions to narrow a type, it&#x27;s better to rely on type guards, which help avoid potential runtime errors caused by unsafe type assertions.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unsafe-type-assertion": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unsafe-type-assertion": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZolpFStPsmSJo%2BShyboo06B2iRwYAL4hNQA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
function f() {
return Math.random() < 0.5 ? 42 : &#x27;oops&#x27;;
}
const z = f() as number;
const items = [1, &#x27;2&#x27;, 3, &#x27;4&#x27;];
const number = items[0] as number;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZolpFStPsmSJo%2BShyboo06B2iRwYAL4hNQA&code=GYVwdgxgLglg9mABMAFASkQbwFCMQJwFMoR8kBZAQygAsA6fSsAEzgFt1EAeRABjoCsiAPyIALACZEALkQByOHAAOAZzkBubAF9s2CAhVREAL0QBeZJ0orEYEGwBGhfJr0GjMKITY2LAbQBGABp5CTkQgGYQuTE5AF1XfTBDW3snfHNET28VP144xGtUx2d1IA&fileType=.ts)```
function f() {
return Math.random() < 0.5 ? 42 : &#x27;oops&#x27;;
}
const z = f() as number | string | boolean;
const items = [1, &#x27;2&#x27;, 3, &#x27;4&#x27;];
const number = items[0] as number | string | undefined;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZolpFStPsmSJo%2BShyboo06B2iRwYAL4hNQA&code=GYVwdgxgLglg9mABMAFASkQbwFCMQJwFMoR8kBZAQygAsA6fSsAEzgFt1EAeRABjoCsiAPyIALACZEALkQByOHAAOAZzkBubAF9s2CAhVREAL0QBeZJ0orEYEGwBGhfIgA%2BiQ-hhgA5m8QOigA2hEyaegZGMFCEbDYWANoAjAA08hJyaQDMaXJicgC64fpghrb2Ti4W0bEqCbwFiNbljs7%2Bnt5%2B7uDMhMDehMzqQA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your codebase has many unsafe type assertions, then it may be difficult to enable this rule.
It may be easier to skip the `no-unsafe-*` rules pending increasing type safety in unsafe areas of your project.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
If your project frequently stubs objects in test files, the rule may trigger a lot of reports. Consider disabling the rule for such files to reduce frequent warnings.
## Further Reading[​](#further-reading)
- More on TypeScript&#x27;s [type assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unsafe-type-assertion.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unsafe-type-assertion.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unsafe-type-assertion.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Further Reading](#further-reading)- [Resources](#resources)