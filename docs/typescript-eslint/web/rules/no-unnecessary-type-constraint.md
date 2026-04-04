# Source: https://typescript-eslint.io/rules/no-unnecessary-type-constraint

On this page# no-unnecessary-type-constraint
Disallow unnecessary constraints on generic types.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
Generic type parameters (`<T>`) in TypeScript may be "constrained" with an [`extends` keyword](https://www.typescriptlang.org/docs/handbook/generics.html#generic-constraints).
When no `extends` is provided, type parameters default a constraint to `unknown`.
It is therefore redundant to `extend` from `any` or `unknown`.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unnecessary-type-constraint": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unnecessary-type-constraint": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK0ipWmQ5Nk%2BaEOb50URNGgdokcGAC%2BIXUA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
interface FooAny<T extends any> {}
interface FooUnknown<T extends unknown> {}
type BarAny<T extends any> = {};
type BarUnknown<T extends unknown> = {};
class BazAny<T extends any> {
quxAny<U extends any>() {}
}
const QuuxAny = <T extends any>() => {};
function QuuzAny<T extends any>() {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK0ipWmQ5Nk%2BaEOb50URNGgdokcGAC%2BIXUA&code=JYOwLgpgTgZghgYwgAgGIHt0EEQE8A8AKshAB6QgAmAzsnHgHzIDeAvgFDuiSyIoboAqiADWIdAHcQREuQhVaAV1HipTNpzC4ADigBCcKDgLEyFGnUbIAvC1YBuTTv2HhYydNNyFyZe7U2do7sCAA2cNS0BgBexjJm8hb0uOrsyMgAjoqkcYKy5rTJDAAUAJR27Bwh6CDUYMgAiorZxoHx3kmMZTbqDpwwyghgwDWNzbF47QWWKd1sQA&fileType=.ts)```
interface Foo<T> {}
type Bar<T> = {};
class Baz<T> {
qux<U>() {}
}
const Quux = <T>() => {};
function Quuz<T>() {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tiacTJTIAhtEK0ipWmQ5Nk%2BaEOb50URNGgdokcGAC%2BIXUA&code=JYOwLgpgTgZghgYwgAgGIHt0B4AqA%2BZAbwF8AoUsATwAcUAhOKXAgXiOIG5yEAbOAZ37IGAL2ZFSyZAEcArgA8sAVTwAKAJTtSZUgnQh%2BYZAEVZC5G2YaLBEl1IxZIBGGD6TZsfmskgA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t care about the specific styles of your type constraints, or never use them in the first place, then you will not need this rule.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unnecessary-type-constraint.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unnecessary-type-constraint.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unnecessary-type-constraint.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)