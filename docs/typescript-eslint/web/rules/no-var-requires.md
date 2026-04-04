# Source: https://typescript-eslint.io/rules/no-var-requires

On this page# no-var-requires
Disallow `require` statements except in import statements.
DeprecatedThis rule has been deprecated in favour of the [`@typescript-eslint/no-require-imports`](/rules/no-require-imports) rule.
In other words, the use of forms such as `var foo = require("foo")` are banned. Instead use ES6 style imports or `import foo = require("foo")` imports.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-var-requires": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-var-requires": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oDcBDaWtEQBHWJSGoMkRNGgdokcGAC%2BIZUA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
var foo = require(&#x27;foo&#x27;);
const foo = require(&#x27;foo&#x27;);
let foo = require(&#x27;foo&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oDcBDaWtEQBHWJSGoMkRNGgdokcGAC%2BIZUA&code=G4QwTgBAZg9jEF4JgKYEcCuBLVAKA5LDPgJQDcAUAMYwB2AzgC7RyLLrZ6FymUA2KZkTapMOFASK8gA&fileType=.ts)```
import foo = require(&#x27;foo&#x27;);
require(&#x27;foo&#x27;);
import foo from &#x27;foo&#x27;;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oDcBDaWtEQBHWJSGoMkRNGgdokcGAC%2BIZUA&code=JYWwDg9gTgLgBAMwhOBeOUCmBHArsLACgHIkJiBKAbgCgs8DMSzLbRJZFlEoIQ5SyYlSA&fileType=.ts)
## Options[​](#options)
This rule accepts the following options:
```
type Options = [
{
/** Patterns of import paths to allow requiring from. */
allow?: string[];
},
];
const defaultOptions: Options = [{ allow: [] }];
```
### `allow`[​](#allow)
Patterns of import paths to allow requiring from. Default: `[]`.
A array of strings. These strings will be compiled into regular expressions with the `u` flag and be used to test against the imported path. A common use case is to allow importing `package.json`. This is because `package.json` commonly lives outside of the TS root directory, so statically importing it would lead to root directory conflicts, especially with `resolveJsonModule` enabled. You can also use it to allow importing any JSON if your environment doesn&#x27;t support JSON modules, or use it for other cases where `import` statements cannot work.
With `{allow: [&#x27;/package\\.json$&#x27;]}`:
- ❌ Incorrect- ✅ Correct```
const foo = require(&#x27;../data.json&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oDcBDaWtEQBHWJSGoMAbXDYciaNA7RIAGllysc7JF7x4HAO7owM7dsitivMgGteAc0QA6AFbIOTACSQN2gLp%2BEAC%2BfoEhIMFAA&code=MYewdgzgLgBAZiEMC8MBOBTAjgVwJaYAUA5AHSkD0AJgIZQ2kBWE4xAlANxA&fileType=.ts)```
const foo = require(&#x27;../package.json&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oDcBDaWtEQBHWJSGoMAbXDYciaNA7RIAGllysc7JF7x4HAO7owM7dsitivMgGteAc0QA6AFbIOTACSQN2gLp%2BEAC%2BfoEhIMFAA&code=MYewdgzgLgBAZiEMC8MBOBTAjgVwJaYAUA5AHSkD0ADgIbADWNA5hqQFYTjECUA3EA&fileType=.ts)
## When Not To Use It[​](#when-not-to-use-it)
If your project frequently uses older CommonJS `require`s, then this rule might not be applicable to you.
If only a subset of your project uses `require`s then you might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Related To[​](#related-to)
- [`no-require-imports`](/rules/no-require-imports)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-var-requires.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-var-requires.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-var-requires.mdx)- [Examples](#examples)- [Options](#options)[`allow`](#allow)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)