# Source: https://typescript-eslint.io/rules/prefer-enum-initializers

On this page# prefer-enum-initializers
Require each enum member value to be explicitly initialized.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
TypeScript `enum`s are a practical way to organize semantically related constant values.
Members of `enum`s that don&#x27;t have explicit values are by default given sequentially increasing numbers.
In projects where the value of `enum` members are important, allowing implicit values for enums can cause bugs if `enum`s are modified over time.
This rule recommends having each `enum` member value explicitly initialized.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-enum-initializers": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-enum-initializers": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WnqdgBbWs0r5KAQ0YAvXqgyRe0APbRI4MAF8QmoA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
enum Status {
Open = 1,
Close,
}
enum Direction {
Up,
Down,
}
enum Color {
Red,
Green = &#x27;Green&#x27;,
Blue = &#x27;Blue&#x27;,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WnqdgBbWs0r5KAQ0YAvXqgyRe0APbRI4MAF8QmoA&code=KYOwrgtgBAygLgQzmAzlA3gKClA8gB1CgF4oBGAGmygGEAbAexWCoF9NNRIoARASwBOwAMZw%2BDEBmoBVfFRw8GAdxBsOXaDQaMBUnACVgAE3lQA4kKKkA5BeChrpgEJ0wwElGsu3jzKyA&fileType=.ts)```
enum Status {
Open = &#x27;Open&#x27;,
Close = &#x27;Close&#x27;,
}
enum Direction {
Up = 1,
Down = 2,
}
enum Color {
Red = &#x27;Red&#x27;,
Green = &#x27;Green&#x27;,
Blue = &#x27;Blue&#x27;,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WnqdgBbWs0r5KAQ0YAvXqgyRe0APbRI4MAF8QmoA&code=KYOwrgtgBAygLgQzmAzlA3gKClA8gB1CgF4oByA0MgGmygGEAbAexWBPKdeBswF9MmUJCgARAJYAnYAGM445iAx0Aqvg4BGWjlHMA7ktIAmWgKHho9Zi0nKcAJWAATDmUdPeOAOLSipMj7AVNpQAEKMYOz%2B4ZG8fEA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t care about `enum`s having implicit values you can safely disable this rule.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-enum-initializers.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-enum-initializers.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-enum-initializers.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)