# Source: https://typescript-eslint.io/rules/no-magic-numbers

On this page# no-magic-numbers
Disallow magic numbers.
🧱 This is an "extension" rule that replaces a core ESLint rule to work with TypeScript. See [Rules > Extension Rules](/rules#extension-rules).
❄️This rule is currently [frozen](/rules#frozen-rules) and is not accepting feature requests.
This rule extends the base [`no-magic-numbers`](https://eslint.org/docs/latest/rules/no-magic-numbers) rule from ESLint core. It adds support for:
- numeric literal types (`type T = 1`),
- `enum` members (`enum Foo { bar = 1 }`),
- `readonly` class properties (`class Foo { readonly bar = 1 }`).
## How to Use[​](#how-to-use)
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
// Note: you must disable the base rule as it can report incorrect errors
"no-magic-numbers": "off",
"@typescript-eslint/no-magic-numbers": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
// Note: you must disable the base rule as it can report incorrect errors
"no-magic-numbers": "off",
"@typescript-eslint/no-magic-numbers": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6KC2j5okAQF8QFoA)
## Options[​](#options)
See [`eslint/no-magic-numbers`&#x27;s options](https://eslint.org/docs/rules/no-magic-numbers#options).
This rule adds the following options:
```
interface Options extends BaseNoMagicNumbersOptions {
ignoreEnums?: boolean;
ignoreNumericLiteralTypes?: boolean;
ignoreReadonlyClassProperties?: boolean;
ignoreTypeIndexes?: boolean;
}
const defaultOptions: Options = {
...baseNoMagicNumbersDefaultOptions,
ignoreEnums: false,
ignoreNumericLiteralTypes: false,
ignoreReadonlyClassProperties: false,
ignoreTypeIndexes: false,
};
```
### `ignoreEnums`[​](#ignoreenums)
Whether enums used in TypeScript are considered okay. `false` by default.
Examples of **incorrect** code for the `{ "ignoreEnums": false }` option:
```
enum foo {
SECOND = 1000,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6MAG0B2KC2j5ofU9ixnBlcgWiIAovWJswnUvGSIthAAvrYAugKhwUA&code=KYOwrgtgBAZg9nKBvAUFKBlAogYQPIByAIlALxQCMADDQDQoC%2BQA&fileType=.ts)
Examples of **correct** code for the `{ "ignoreEnums": true }` option:
```
enum foo {
SECOND = 1000,
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6MAG0B2KC2j5ofU9ixnBlcgWiIAovWJswIuIlsQAL62ALoCwYFAA&code=KYOwrgtgBAZg9nKBvAUFKBlAogYQPIByAIlALxQCMADDQDQoC%2BQA&fileType=.ts)
### `ignoreNumericLiteralTypes`[​](#ignorenumericliteraltypes)
Whether numbers used in TypeScript numeric literal types are considered okay. `false` by default.
Examples of **incorrect** code for the `{ "ignoreNumericLiteralTypes": false }` option:
```
type SmallPrimes = 2 | 3 | 5 | 7 | 11;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6MAG0B2KC2j5ofU9ixnBlcgWiIAcgxY0AMpREtSeAAVSRRDTkDkRFsIAF9bAF0BeNigA&code=C4TwDgpgBAygtgQwDZIAoCcCWcIGcoC8UATFAD5QDM5UArDQOw0CMzA3EA&fileType=.ts)
Examples of **correct** code for the `{ "ignoreNumericLiteralTypes": true }` option:
```
type SmallPrimes = 2 | 3 | 5 | 7 | 11;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6MAG0B2KC2j5ofU9ixnBlcgWiIAcgxY0AMpREtSeAAVSRRDEThEWwgAX1sAXQE4mKA&code=C4TwDgpgBAygtgQwDZIAoCcCWcIGcoC8UATFAD5QDM5UArDQOw0CMzA3EA&fileType=.ts)
### `ignoreReadonlyClassProperties`[​](#ignorereadonlyclassproperties)
Whether `readonly` class properties are considered okay.
Examples of **incorrect** code for the `{ "ignoreReadonlyClassProperties": false }` option:
```
class Foo {
readonly A = 1;
readonly B = 2;
public static readonly C = 1;
static readonly D = 1;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6MAG0B2KC2j5ofU9ixnBlcgWiIASolIATfLnhiAYXhSZGQABUspaBFKFENOUnhkRFsIAF9bAF0BDLSgA&code=MYGwhgzhAEBiD29oG8BQ1oCcCmYAm8AdiAJ7QCC0AvNAIwDc6WuBxZAQtdAEyMYAOAVwBGIAJbBoEAC5hpE5viKloAYS4MmMuQpxK20ACIbGAXyA&fileType=.ts)
Examples of **correct** code for the `{ "ignoreReadonlyClassProperties": true }` option:
```
class Foo {
readonly A = 1;
readonly B = 2;
public static readonly C = 1;
static readonly D = 1;
}
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6MAG0B2KC2j5ofU9ixnBlcgWiIASolIATfLnhiAYXhSZGQABUspaBFKFEMROERbCABfWwBdATSUoA&code=MYGwhgzhAEBiD29oG8BQ1oCcCmYAm8AdiAJ7QCC0AvNAIwDc6WuBxZAQtdAEyMYAOAVwBGIAJbBoEAC5hpE5viKloAYS4MmMuQpxK20ACIbGAXyA&fileType=.ts)
### `ignoreTypeIndexes`[​](#ignoretypeindexes)
Whether numbers used to index types are okay. `false` by default.
Examples of **incorrect** code for the `{ "ignoreTypeIndexes": false }` option:
```
type Foo = Bar[0];
type Baz = Parameters<Foo>[2];
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6MAG0B2KC2j5ofU9ixnBlcgWiIAKpMQBJXABNEAB4ohpyk8MiIthAAvrYAugKx0UA&code=C4TwDgpgBAYg9nKBeKAhAhgJwNoAYC6A3AFCiRroBeyUAClugLYTASYDOAPPHAHzYAmIkA&fileType=.ts)
Examples of **correct** code for the `{ "ignoreTypeIndexes": true }` option:
```
type Foo = Bar[0];
type Baz = Parameters<Foo>[2];
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQHYHsBaAWwEMBzASwGNDdZiAjRaVDSfAM08gBpxskAAIAXAJ4AHFNWiUJIwiniVcIgPQESFGnQbNW6MAG0B2KC2j5ofU9ixnBlcgWiIAKpMQBJXABNEAB4ohiJwiLYQAL62ALoC0ZFAA&code=C4TwDgpgBAYg9nKBeKAhAhgJwNoAYC6A3AFCiRroBeyUAClugLYTASYDOAPPHAHzYAmIkA&fileType=.ts)
## When Not To Use It[​](#when-not-to-use-it)
If your project frequently deals with constant numbers and you don&#x27;t wish to take up extra space to declare them, this rule might not be for you.
We recommend at least using descriptive comments and/or names to describe constants.
You might consider using [ESLint disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) instead of completely disabling this rule.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-magic-numbers.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-magic-numbers.test.ts)
Taken with ❤️ from [ESLint core](https://github.com/eslint/eslint/blob/main/docs/src/rules/no-magic-numbers.md).[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-magic-numbers.mdx)- [How to Use](#how-to-use)- [Options](#options)[`ignoreEnums`](#ignoreenums)- [`ignoreNumericLiteralTypes`](#ignorenumericliteraltypes)- [`ignoreReadonlyClassProperties`](#ignorereadonlyclassproperties)- [`ignoreTypeIndexes`](#ignoretypeindexes)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)