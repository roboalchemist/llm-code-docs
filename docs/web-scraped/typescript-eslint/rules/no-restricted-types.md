# Source: https://typescript-eslint.io/rules/no-restricted-types

On this page# no-restricted-types
Disallow certain types.
🔧Some problems reported by this rule are automatically fixable by the [`--fix` ESLint command line option](https://eslint.org/docs/latest/user-guide/command-line-interface#--fix).
💡Some problems reported by this rule are manually fixable by editor [suggestions](https://eslint.org/docs/latest/developer-guide/working-with-rules#providing-suggestions).
It can sometimes be useful to ban specific types from being used in type annotations.
For example, a project might be migrating from using one type to another, and want to ban references to the old type.
This rule can be configured to ban a list of specific types and can suggest alternatives.
Note that it does not ban the corresponding runtime objects from being used.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-restricted-types": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-restricted-types": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1uhXyrPyIAJrSKlUGSImjQO0SODABfEEqA)
## Options[​](#options)
This rule accepts the following options:
```
type BanConfig =
/** Bans a type. */
| {
/** Type to autofix replace with. Note that autofixers can be applied automatically - so you need to be careful with this option. */
fixWith?: string;
/** Custom error message. */
message?: string;
/** Types to suggest replacing with. */
suggest?: string[];
}
/** Bans the type with a custom message. */
| string
/** Bans the type with the default message. */
| true;
type Options = [
{
/** An object whose keys are the types you want to ban, and the values are error messages. */
types?: {
[k: string]: BanConfig;
};
},
];
const defaultOptions: Options = [{}];
```
### `types`[​](#types)
An object whose keys are the types you want to ban, and the values are error messages.
The type can either be a type name literal (`OldType`) or a a type name with generic parameter instantiation(s) (`OldType<MyArgument>`).
The values can be:
- A string, which is the error message to be reported; or
- An object with the following properties:
`message: string`: the message to display when the type is matched.
- `fixWith?: string`: a string to replace the banned type with when the fixer is run. If this is omitted, no fix will be done.
- `suggest?: string[]`: a list of suggested replacements for the banned type.
Example configuration:
```
{
"@typescript-eslint/no-restricted-types": [
"error",
{
"types": {
// add a custom message to help explain why not to use it
"OldType": "Don&#x27;t use OldType because it is unsafe",
// add a custom message, and tell the plugin how to fix it
"OldAPI": {
"message": "Use NewAPI instead",
"fixWith": "NewAPI",
},
// add a custom message, and tell the plugin how to suggest a fix
"SoonToBeOldAPI": {
"message": "Use NewAPI instead",
"suggest": ["NewAPIOne", "NewAPITwo"],
},
},
},
],
}
```
## When Not To Use It[​](#when-not-to-use-it)
If you have no need to ban specific types from being used in type annotations, you don&#x27;t need this rule.
## Related To[​](#related-to)
- [Revamping the `ban-types` rule](/blog/revamping-the-ban-types-rule)
- [`no-empty-object-type`](/rules/no-empty-object-type)
- [`no-unsafe-function-type`](/rules/no-unsafe-function-type)
- [`no-wrapper-object-types`](/rules/no-wrapper-object-types)
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-restricted-types.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-restricted-types.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-restricted-types.mdx)- [Options](#options)[`types`](#types)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)