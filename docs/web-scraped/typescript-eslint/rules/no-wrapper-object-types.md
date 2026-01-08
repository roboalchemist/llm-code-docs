# Source: https://typescript-eslint.io/rules/no-wrapper-object-types

On this page# no-wrapper-object-types
Disallow using confusing built-in primitive class wrappers.
✅Extending [`"plugin:@typescript-eslint/recommended"`](/users/configs#recommended) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
TypeScript defines several confusing pairs of types that look very similar to each other, but actually mean different things: `boolean`/`Boolean`, `number`/`Number`, `string`/`String`, `bigint`/`BigInt`, `symbol`/`Symbol`, `object`/`Object`.
In general, only the lowercase variant is appropriate to use.
Therefore, this rule enforces that you only use the lowercase variant.
JavaScript has [8 data types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures) at runtime, and these are described in TypeScript by the lowercase types `undefined`, `null`, `boolean`, `number`, `string`, `bigint`, `symbol`, and `object`.
As for the uppercase types, these are *structural types* which describe JavaScript "wrapper" objects for each of the data types, such as [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) and [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number).
Additionally, due to the quirks of structural typing, the corresponding primitives are *also* assignable to these uppercase types, since they have the same "shape".
It is a universal best practice to work directly with the built-in primitives, like `0`, rather than objects that "look like" the corresponding primitive, like `new Number(0)`.
- Primitives have the expected value semantics with `==` and `===` equality checks, whereas their object counterparts are compared by reference.
That is to say, `"str" === "str"` but `new String("str") !== new String("str")`.
- Primitives have well-known behavior around truthiness/falsiness which is common to rely on, whereas all objects are truthy, regardless of the wrapped value (e.g. `new Boolean(false)` is truthy).
- TypeScript only allows arithmetic operations (e.g. `x - y`) to be performed on numeric primitives, not objects.
As a result, using the lowercase type names like `number` in TypeScript types instead of the uppercase names like `Number` is a better practice that describes code more accurately.
Examples of code for this rule:
- ❌ Incorrect- ✅ Correct```
let myBigInt: BigInt;
let myBoolean: Boolean;
let myNumber: Number;
let myString: String;
let mySymbol: Symbol;
let myObject: Object = &#x27;allowed by TypeScript&#x27;;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oHdoBDYqWi0OAIwBWiMnSKlUGSImjQO0SODABfEJqA&code=DYUwLgBAtgngQgSwOYEkB2YBcFGowbgChRJY4B7c0AQzWwqpFqJOhgDkBXKAIxACdsXXgJbg2AZTD8EaJNiky5Y0jAkxeVBRp5UixcbADyPAFYgAxlggnzViAF4IAcmrBg5AO4gAJhB4wEAAqMAAOIBIWMqFgzvhAA&fileType=.ts)```
let myBigint: bigint;
let myBoolean: boolean;
let myNumber: number;
let myString: string;
let mySymbol: symbol;
let myObject: object = "Type &#x27;string&#x27; is not assignable to type &#x27;object&#x27;.";
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oHdoBDYqWi0OAIwBWiMnSKlUGSImjQO0SODABfEJqA&code=DYUwLgBAtgngQgSwOYIHZgFwQEbLWAbgChRJY4B7C0AQ1S2yttWNOhgDkBXKbEAJyyoeffq3DsAymH5okWAM4y54sjEkxe1RZsbBiJCbADy2AFYgAxpggVzVyAF4IAIgAqMAA4gIAciWyqEi%2BEAgKEKgUkDQKCsioNNigEGAUKV4%2BvnYW1r4AdC4EQA&fileType=.ts)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-wrapper-object-types": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-wrapper-object-types": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oHdoBDYqWi0OAIwBWiMnSKlUGSImjQO0SODABfEJqA)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
If your project is a rare one that intentionally deals with the class equivalents of primitives, it might not be worthwhile to use this rule.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) for those specific situations instead of completely disabling this rule.
## Further Reading[​](#further-reading)
- [MDN documentation on primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
- [MDN documentation on `string` primitives and `String` objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_primitives_and_string_objects)
## Related To[​](#related-to)
- [Revamping the `ban-types` rule](/blog/revamping-the-ban-types-rule)
- [`no-empty-object-type`](/rules/no-empty-object-type)
- [`no-restricted-types`](/rules/no-restricted-types)
- [`no-unsafe-function-type`](/rules/no-unsafe-function-type)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-wrapper-object-types.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-wrapper-object-types.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-wrapper-object-types.mdx)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Further Reading](#further-reading)- [Related To](#related-to)- [Resources](#resources)