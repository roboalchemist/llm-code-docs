# Source: https://typescript-eslint.io/rules/no-unsafe-enum-comparison

On this page# no-unsafe-enum-comparison
Disallow comparing an enum value with a non-enum value.
✅Extending [`"plugin:@typescript-eslint/recommended-type-checked"`](/users/configs#recommended-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
The TypeScript compiler can be surprisingly lenient when working with enums.
While overt safety problems with enums were [resolved in TypeScript 5.0](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/#all-enums-are-union-enums), some logical pitfalls remain permitted.
For example, it is allowed to compare enum values against non-enum values:
```
enum Vegetable {
Asparagus = &#x27;asparagus&#x27;,
}
declare const vegetable: Vegetable;
vegetable === &#x27;asparagus&#x27;; // No error
```
The above code snippet should instead be written as `vegetable === Vegetable.Asparagus`.
Allowing non-enums in comparisons subverts the point of using enums in the first place.
By enforcing comparisons with properly typed enums:
- It makes a codebase more resilient to enum members changing values.
- It allows for code IDEs to use the "Rename Symbol" feature to quickly rename an enum.
- It aligns code to the proper enum semantics of referring to them by name and treating their values as implementation details.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-unsafe-enum-comparison": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-unsafe-enum-comparison": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZonpNYAW1pkOY4nyrIOTdFETRoHaJHBgAviB1A)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
enum Fruit {
Apple,
}
declare let fruit: Fruit;
// bad - comparison between enum and explicit value instead of named enum member
fruit === 0;
enum Vegetable {
Asparagus = &#x27;asparagus&#x27;,
}
declare let vegetable: Vegetable;
// bad - comparison between enum and explicit value instead of named enum member
vegetable === &#x27;asparagus&#x27;;
declare let anyString: string;
// bad - comparison between enum and non-enum value
anyString === Vegetable.Asparagus;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZonpNYAW1pkOY4nyrIOTdFETRoHaJHBgAviB1A&code=KYOwrgtgBAYgTmAlgFygbwFBSgQQA54A2wANBgL4YYAmwAxoQIZzBTGoBmCKAXLN8gDcVAPQioAI0bUoAWih0A9hDzNEAZ0UhJwZAHdgoKKEhRGIGcAAeRRHRRQAbo0JhWiEOuTBpURRygQRghgS3BoEIgJYDgMLiRUAF5kqAAGYQwTaAA1YABzXUYJYnQsXHVVOEY8sHUoRKgAckYK5mraxrJKGnomFjZdJ3zC4uA%2BXILkIuIMsUlfeSUVNU1taP1DbSyzC2MbQjsHZ1d3T29ff0Dg0ONwqEjo2MdhqdH6lObWqpr1RozaBjMVjsHYATwAysg4B48nwvNCQHlZuIpDJFspKhotDoNkZtuYZCAtLJtsc3BhzBCoTD3g0JiNiAA6HBfdrqQRAA&fileType=.ts)```
enum Fruit {
Apple,
}
declare let fruit: Fruit;
fruit === Fruit.Apple;
enum Vegetable {
Asparagus = &#x27;asparagus&#x27;,
}
declare let vegetable: Vegetable;
vegetable === Vegetable.Asparagus;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1tieQEMAZonpNYAW1pkOY4nyrIOTdFETRoHaJHBgAviB1A&code=KYOwrgtgBAYgTmAlgFygbwFBSgQQA54A2wANBgL4YYAmwAxoQIZzBTGoBmCKAXLN8gDcVLklQBeSfzEA6fEWDCMoSFABqwAObBkjAEbF0WXAGc8zRprAmo4qAHJGZi1ZP2ylGvSYs2OqABuWjr6xHwa2roGilRBkaGsknYRIdFyznCW1oJAA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If you don&#x27;t mind enums being treated as a namespaced bag of values, rather than opaque identifiers, you likely don&#x27;t need this rule.
Sometimes, you may want to ingest a value from an API or user input, then use it as an enum throughout your application.
While validating the input, it may be appropriate to disable the rule.
Alternately, you might consider making use of a validation library like [Zod](https://zod.dev/?id=native-enums).
See further discussion of this topic in [#8557](https://github.com/typescript-eslint/typescript-eslint/issues/8557).
Finally, in the rare case of relying on an third party enums that are only imported as `type`s, it may be difficult to adhere to this rule.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-unsafe-enum-comparison.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-unsafe-enum-comparison.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-unsafe-enum-comparison.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)