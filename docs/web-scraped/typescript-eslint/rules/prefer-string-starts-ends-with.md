# Source: https://typescript-eslint.io/rules/prefer-string-starts-ends-with

On this page# prefer-string-starts-ends-with
Enforce using `String#startsWith` and `String#endsWith` over other equivalent methods of checking substrings.
🎨Extending [`"plugin:@typescript-eslint/stylistic-type-checked"`](/users/configs#stylistic-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
There are multiple ways to verify if a string starts or ends with a specific string, such as `foo.indexOf(&#x27;bar&#x27;) === 0`.
As of ES2015, the most common way in JavaScript is to use `String#startsWith` and `String#endsWith`.
Keeping to those methods consistently helps with code readability.
This rule reports when a string method can be replaced safely with `String#startsWith` or `String#endsWith`.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-string-starts-ends-with": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-string-starts-ends-with": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WluXxUmAc374AhtHzJ6TACYyA7pXwALdFF7QA9tEjgwAXxCGgA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
declare const foo: string;
// starts with
foo[0] === &#x27;b&#x27;;
foo.charAt(0) === &#x27;b&#x27;;
foo.indexOf(&#x27;bar&#x27;) === 0;
foo.slice(0, 3) === &#x27;bar&#x27;;
foo.substring(0, 3) === &#x27;bar&#x27;;
foo.match(/^bar/) != null;
/^bar/.test(foo);
// ends with
foo[foo.length - 1] === &#x27;b&#x27;;
foo.charAt(foo.length - 1) === &#x27;b&#x27;;
foo.lastIndexOf(&#x27;bar&#x27;) === foo.length - 3;
foo.slice(-3) === &#x27;bar&#x27;;
foo.substring(foo.length - 3) === &#x27;bar&#x27;;
foo.match(/bar$/) != null;
/bar$/.test(foo);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WluXxUmAc374AhtHzJ6TACYyA7pXwALdFF7QA9tEjgwAXxCGgA&code=CYUwxgNghgTiAEYD2A7AzgF3gMyUgXPJjAJYoDmA3AFDUD0dRGsGa8A7iRgBbW5IBtAAwBdeAF5J8AOQAjaTX4A6MN1gBBDAAohASglS5CvniVlQADwDy2LXNjT9k8fCGLTaCCTAgdAGngAZidDWQd3JCU0AFdZYjJyfyCQl3sYY2UAWygMVS06AD0wmDp9AEIXFGiICBpC4rolDBBMLX5dGnpGEBRgNk4eE0FlCB7yHngAWngARjFnGXkIlTUYTTbTUYoJ6ZmUxYzNqEwASV6Qa1s0xwMXEbGdoOXPb19J4NvF8KGo2PiKDaRLbjbhTZKfa7LbK5bj5YoAElK8Aq8CqNTqCMazVa7UoQA&fileType=.ts)```
declare const foo: string;
// starts with
foo.startsWith(&#x27;bar&#x27;);
// ends with
foo.endsWith(&#x27;bar&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WluXxUmAc374AhtHzJ6TACYyA7pXwALdFF7QA9tEjgwAXxCGgA&code=CYUwxgNghgTiAEYD2A7AzgF3gMyUgXPJjAJYoDmA3AFDUD0dRGsGa8A7iRgBbW5IA6TCzQB1LtwAUAcgBGsaQEoa9RiBTA2nHnzwD1m8TxnyYSykA&fileType=.ts)
## Options[​](#options)
This rule accepts the following options:
```
type Options = [
{
/** Whether to allow equality checks against the first or last element of a string. */
allowSingleElementEquality?:
| &#x27;never&#x27;
/** Whether to allow equality checks against the first or last element of a string. */
| &#x27;always&#x27;;
},
];
const defaultOptions: Options = [{ allowSingleElementEquality: &#x27;never&#x27; }];
```
### `allowSingleElementEquality`[​](#allowsingleelementequality)
Whether to allow equality checks against the first or last element of a string. Default: `"never"`.
If switched to `&#x27;always&#x27;`, the rule will allow equality checks against the first or last character in a string.
This can be preferable in projects that don&#x27;t deal with special character encodings and prefer a more succinct style.
The following code is considered incorrect by default, but is allowed with `allowSingleElementEquality: &#x27;always&#x27;`:
```
declare const text: string;
text[0] === &#x27;a&#x27;;
text[0] === text[0].toUpperCase();
text[0] === text[1];
text[text.length - 1] === &#x27;b&#x27;;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WluXxUmAc374AhtHzJ6TACYyA7pXwALdGADa4bDl7QA9tEgAaHbqy7skcfHgHFAZWbCkAUSQBbRCzcBHWFsVQg0beEVxQlRzbABfGIBdHXjYoA&code=CYUwxgNghgTiAEYD2A7AzgF3hkAPDAXPJjAJYoDmA3AFA074DaADALrwC8X8A5FD7QYYW7Lh2x5hbAHQYkAVQAOikDADCUNCAAUASkGSRnbkMYBGVgaZDpEEJQwALeAFp4F4%2BJ4AjAUA&fileType=.ts)
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t mind which style of string checking is used, you can turn this rule off safely.
However, keep in mind that inconsistent style can harm readability in a project.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-string-starts-ends-with.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-string-starts-ends-with.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-string-starts-ends-with.mdx)- [Examples](#examples)- [Options](#options)[`allowSingleElementEquality`](#allowsingleelementequality)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)