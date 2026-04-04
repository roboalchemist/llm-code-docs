# Source: https://typescript-eslint.io/rules/no-unsafe-declaration-merging

On this page# no-unsafe-declaration-merging
Disallow unsafe declaration merging.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
TypeScript&#x27;s "declaration merging" supports merging separate declarations with the same name.
Declaration merging between classes and interfaces is unsafe.
The TypeScript compiler doesn&#x27;t check whether properties are initialized, which can lead to TypeScript not detecting code that will cause runtime errors.
```
interface Foo {
nums: number[];
}
class Foo {}
const foo = new Foo();
foo.nums.push(1); // Runtime Error: Cannot read properties of undefined.
```
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unsafe-declaration-merging": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unsafe-declaration-merging": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZoloATRGXh9offJQ5NaAW0TQA5s1XooK6B2iRwYAL4gjQA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
interface Foo {}
class Foo {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZoloATRGXh9offJQ5NaAW0TQA5s1XooK6B2iRwYAL4gjQA&code=JYOwLgpgTgZghgYwgAgGIHt3IN4F8BQ%2BCANnAM5lqY65A&fileType=.ts)```
interface Foo {}
class Bar implements Foo {}
namespace Baz {}
namespace Baz {}
enum Baz {}
namespace Qux {}
function Qux() {}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZoloATRGXh9offJQ5NaAW0TQA5s1XooK6B2iRwYAL4gjQA&code=JYOwLgpgTgZghgYwgAgGIHt3IN4F8BQCANnAM6nIBCcUywAtgA5ET0TgUZZ774hxtSjRCmoAvHAX6DhSKnAk92AV3rzFBPgIhCRyAIrKAHpPwxlIBGGDoQB4wAoAlJKA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your project intentionally defines classes and interfaces with unsafe declaration merging patterns, this rule might not be for you.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Further Reading[​](#further-reading)
- [Declaration Merging](https://www.typescriptlang.org/docs/handbook/declaration-merging.html)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unsafe-declaration-merging.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unsafe-declaration-merging.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unsafe-declaration-merging.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Further Reading](#further-reading)- [Resources](#resources)