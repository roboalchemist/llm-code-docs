# Source: https://typescript-eslint.io/rules/related-getter-setter-pairs

On this page# related-getter-setter-pairs
Enforce that `get()` types should be assignable to their equivalent `set()` type.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
TypeScript allows defining different types for a `get` parameter and its corresponding `set` return.
Prior to TypeScript 4.3, the types had to be identical.
From TypeScript 4.3 to 5.0, the `get` type had to be a subtype of the `set` type.
As of TypeScript 5.1, the types may be completely unrelated as long as there is an explicit type annotation.
Defining drastically different types for a `get` and `set` pair can be confusing.
It means that assigning a property to itself would not work:
```
// Assumes box.value&#x27;s get() return is assignable to its set() parameter
box.value = box.value;
```
This rule reports cases where a `get()` and `set()` have the same name, but the `get()`&#x27;s type is not assignable to the `set()`&#x27;s.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/related-getter-setter-pairs": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/related-getter-setter-pairs": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6aReAQ30QBNaAc0T5e0WshFjaxLpWioMkRNGgB7aJHBgAviB1A)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
interface Box {
get value(): string;
set value(newValue: number);
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6aReAQ30QBNaAc0T5e0WshFjaxLpWioMkRNGgB7aJHBgAviB1A&code=JYOwLgpgTgZghgYwgAgEIHsAeyDeAoZZAcwjGQDc4AbAVwgAoBKALmQGcwpQiBuA90hWp16ICAHcAasIisQNALYAjaIz4BfIA&fileType=.ts)```
interface Box {
get value(): string;
set value(newValue: string);
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6aReAQ30QBNaAc0T5e0WshFjaxLpWioMkRNGgB7aJHBgAviB1A&code=JYOwLgpgTgZghgYwgAgEIHsAeyDeAoZZAcwjGQDc4AbAVwgAoBKALmQGcwpQiBuA90hWp16ICAHcAasIisOXEEUZ8AvkA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your project needs to model unusual relationships between data, such as older DOM types, this rule may not be useful for you.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Further Reading[​](#further-reading)
- [MDN documentation on `get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
- [MDN documentation on `set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
- [TypeScript 5.1 Release Notes > Unrelated Types for Getters and Setters](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-1.html#unrelated-types-for-getters-and-setters)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/related-getter-setter-pairs.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/related-getter-setter-pairs.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/related-getter-setter-pairs.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Further Reading](#further-reading)- [Resources](#resources)