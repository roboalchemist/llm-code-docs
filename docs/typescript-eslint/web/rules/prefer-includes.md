# Source: https://typescript-eslint.io/rules/prefer-includes

On this page# prefer-includes
Enforce `includes` method over `indexOf` method.
🎨Extending [`"plugin:@typescript-eslint/stylistic-type-checked"`](/users/configs#stylistic-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
Prior to ES2015, `Array#indexOf` and `String#indexOf` comparisons against `-1` were the standard ways to check whether a value exists in an array or string, respectively.
Alternatives that are easier to read and write now exist: ES2015 added `String#includes` and ES2016 added `Array#includes`.
This rule reports when an `.indexOf` call can be replaced with an `.includes`.
Additionally, this rule reports the tests of simple regular expressions in favor of `String#includes`.
This rule will report on any receiver object of an `indexOf` method call that has an `includes` method where the two methods have the same parameters.
Matching types include: `String`, `Array`, `ReadonlyArray`, and typed arrays.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/prefer-includes": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/prefer-includes": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WlubLxYAExToovaAHtokcGAC%2BIBUA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
const str: string;
const array: any[];
const readonlyArray: ReadonlyArray<any>;
const typedArray: UInt8Array;
const maybe: string;
const userDefined: {
indexOf(x: any): number;
includes(x: any): boolean;
};
str.indexOf(value) !== -1;
array.indexOf(value) !== -1;
readonlyArray.indexOf(value) === -1;
typedArray.indexOf(value) > -1;
maybe?.indexOf(&#x27;&#x27;) !== -1;
userDefined.indexOf(value) >= 0;
/example/.test(str);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WlubLxYAExToovaAHtokcGAC%2BIBUA&code=MYewdgzgLgBNBOAuOV4EswHMDcAoUksAhvPEQJ7JFjkDaAungdDPAKZEAm4ANuQIKkKyAEoduYPoLLkAPNXIA%2BJuBZRyABzadpwmAFUAkmCgAOXeRWEYAWwoAjNsgQYc%2BVbACuENvAAibABmGNrIAN64MDAYnGwAHgDygQAUcVQ0AJTIYJ42jvB4URjAPJ6xEKnp5Fkw9iAgPBxgeAC%2BeLgIAHQx8UnJAG5EpWwZMACEALwTMAC0AIx4JDLdYLGJKYPDo5PT83jsXLwCQuQra32bniMwU7sLuOpaOidnvRtDV6OKs-d25I4Afle62SAHJQdspj88N5fAFgmBtMCLh9roppgAGdoAeniRBsGka2M6UDY0GSCAy2CAA&fileType=.ts)```
const str: string;
const array: any[];
const readonlyArray: ReadonlyArray<any>;
const typedArray: UInt8Array;
const maybe: string;
const userDefined: {
indexOf(x: any): number;
includes(x: any): boolean;
};
str.includes(value);
array.includes(value);
!readonlyArray.includes(value);
typedArray.includes(value);
maybe?.includes(&#x27;&#x27;);
userDefined.includes(value);
str.includes(&#x27;example&#x27;);
// The two methods have different parameters.
declare const mismatchExample: {
indexOf(x: unknown, fromIndex?: number): number;
includes(x: unknown): boolean;
};
mismatchExample.indexOf(value) >= 0;
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Y6RAM0WlubLxYAExToovaAHtokcGAC%2BIBUA&code=MYewdgzgLgBNBOAuOV4EswHMDcAoUksAhvPEQJ7JFjkDaAungdDPAKZEAm4ANuQIKkKyAEoduYPoLLkAPNXIA%2BJuBZRyABzadpwmAFUAkmCgAOXeRWEYAWwoAjNsgQYc%2BVbACuENvAAibABmGNrIAN64MDAYnGwAHgDygQAUcVQ0AJTIYJ42jvB4URjAPJ6xEKnp5Fkw9iAgPBxgeAC%2BeLgIAHTFpeXJAG5EpWwZeCQy3WAlZWwVg8OjuACE7Fy8AkLkk9N9854jeOpaOpvbvbMDQ-uLduSOAPxnMxUA5C%2BL3r4BwWDaT7tXA64Dqof4XF7xIg2DSNd7tAD08JgABUABZsGBQADuIFsbCgqJAnAgMFRRH6GM4aECgV8bBMMA0JCh%2BN8EE6uFiJRIGOYsBsaAgdigwFRAFE4lCYU4YBEimBYokUmkYJ4wABrMAgLFgAA0MEC8BANmMivu2Vy%2BRqOTyvkK0Sm5wqKrVmu1YBqdQaTVaeAFQqIIvFkuhjUmiqSlwWMEUAF4YAAGbBAA&fileType=.ts)
## Options[​](#options)
This rule is not configurable.
## When Not To Use It[​](#when-not-to-use-it)
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/prefer-includes.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/prefer-includes.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/prefer-includes.mdx)- [Examples](#examples)- [Options](#options)- [When Not To Use It](#when-not-to-use-it)- [Resources](#resources)