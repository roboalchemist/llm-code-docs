# Source: https://typescript-eslint.io/rules/no-deprecated

On this page# no-deprecated
Disallow using code marked as `@deprecated`.
🔒Extending [`"plugin:@typescript-eslint/strict-type-checked"`](/users/configs#strict-type-checked) in an [ESLint configuration](https://eslint.org/docs/latest/user-guide/configuring/configuration-files#extending-configuration-files) enables this rule.
💭This rule requires [type information](/getting-started/typed-linting) to run, which comes with performance tradeoffs.
The [JSDoc `@deprecated` tag](https://jsdoc.app/tags-deprecated) can be used to document some piece of code being deprecated.
It&#x27;s best to avoid using code marked as deprecated.
This rule reports on any references to code marked as `@deprecated`.
note[TypeScript recognizes the `@deprecated` tag](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html#deprecated), allowing editors to visually indicate deprecated code — usually with a strikethrough.
However, TypeScript doesn&#x27;t report type errors for deprecated code on its own.
- Flat Config- Legacy Configeslint.config.mjs```
export default tseslint.config({
rules: {
"@typescript-eslint/no-deprecated": "error"
}
});
```.eslintrc.cjs```
module.exports = {
"rules": {
"@typescript-eslint/no-deprecated": "error"
}
};
```
[Try this rule in the playground ↗
](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNFjpEZAIb5E3dFETRoHaJHBgAviEVA)
## Examples[​](#examples)
- ❌ Incorrect- ✅ Correct```
/** @deprecated Use apiV2 instead. */
declare function apiV1(): Promise<string>;
declare function apiV2(): Promise<string>;
await apiV1();
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNFjpEZAIb5E3dFETRoHaJHBgAviEVA&code=PQKhAIAEBMFMAcBOsDGBDALra4CqBnWcNeASwDUAmcUgO3yzWgDpwRgAoOFAGzWXAAzAK60UGUgHtaxMuQCMACgCUALnAAFRJIC2pQgB4GiOgHMAfAG4OXVHwEixE6bIqUV6rbv2wjGE7QW1hxoAO5opBiuCiqWQA&fileType=.ts)```
import { parse } from &#x27;node:url&#x27;;
// &#x27;parse&#x27; is deprecated. Use the WHATWG URL API instead.
const url = parse(&#x27;/foo&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNFjpEZAIb5E3dFETRoHaJHBgAviEVA&code=JYWwDg9gTgLgBAbzmAhlAzgUzgXzgMyghDgHIA7CAE0wC4BXKAG1IG4Aodgei7NQ0yk4wdHBpgomAMYoYmKgDo4AVSxwYAC2wB1ABIBBACraA4ioBKAGTj6ACgElh5dHJSL2UiM-iMmcALzIaFgAFKRc%2BBAQpACUrEA&fileType=.ts)```
/** @deprecated Use apiV2 instead. */
declare function apiV1(): Promise<string>;
declare function apiV2(): Promise<string>;
await apiV2();
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNFjpEZAIb5E3dFETRoHaJHBgAviEVA&code=PQKhAIAEBMFMAcBOsDGBDALra4CqBnWcNeASwDUAmcUgO3yzWgDpwRgAoOFAGzWXAAzAK60UGUgHtaxMuQCMACgCUALnAAFRJIC2pQgB4GiOgHMAfAG4OXVHwEixE6bIqUV6rbv2wjGE7QW1hxoAO5opBiuVCqWQA&fileType=.ts)```
// Modern Node.js API, uses `new URL()`
const url2 = new URL(&#x27;/foo&#x27;, &#x27;http://www.example.com&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNFjpEZAIb5E3dFETRoHaJHBgAviEVA&code=PTAEFkHsBMFMCcB2oByNYDoBWBnUBBABQEkAaUAVx1jwANFYB3UAVQCUAZACgEpaAoAMaREOAC6V4AGwBMoALygGzdtwDkwAGaRIa8moAWYsQAcAXCEZWMsAB4BDALYmpmYY7U8A3EA&fileType=.ts)
## Options[​](#options)
This rule accepts the following options:
```
type Options = [
{
/** Type specifiers that can be allowed. */
allow?: (
| {
from: &#x27;file&#x27;;
name: string | string[];
path?: string;
}
| {
from: &#x27;lib&#x27;;
name: string | string[];
}
| {
from: &#x27;package&#x27;;
name: string | string[];
package: string;
}
| string
)[];
},
];
const defaultOptions: Options = [{ allow: [] }];
```
### `allow`[​](#allow)
Type specifiers that can be allowed. Default: `[]`.
This option takes the shared [`TypeOrValueSpecifier` format](/packages/type-utils/type-or-value-specifier).
Examples of code for this rule with:
```
{
"allow": [
{ "from": "file", "name": "apiV1" },
{ "from": "lib", "name": "escape" }
]
}
```
- ❌ Incorrect- ✅ Correct```
/** @deprecated */
declare function apiV2(): Promise<string>;
await apiV2();
// `unescape` has been deprecated since ES5.
unescape(&#x27;...&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNFjpEZAIb5E3dGADa4bDkTRoHaJAA0M2VlnZIQ%2BPA4B3CdK1bNp2ZABmigLYTrlJKvUWcTIbcQOhxSgDUARkhXUwBfNTcIcyjrOwdGACMXKO0PLwdyX29QrTDciABdXPzZYoh8sKA&code=PQKhAIAEBMFMAcBOsDGBDALra4TAFBwoA2ay4AZgK4B2KGAlgPY3hrwMBqATABQCUALnAAFREwC2DAM6wAPNIyIGNAOYA%2BANz58aAO5oGGNhx4Dt%2BYMHAADWrGnp4sG%2BAAWaaeABGsWKzgkVExscGkVFFhwAFEAZQBWADp8e0d2WF4AckSczP5NIA&fileType=.ts)```
import { Bar } from &#x27;bar-lib&#x27;;
/** @deprecated */
declare function apiV1(): Promise<string>;
await apiV1();
// `escape` has been deprecated since ES5.
escape(&#x27;...&#x27;);
```[Open in Playground](/play#eslintrc=N4KABGBEBOCuA2BTAzpAXGUEKQAIBcBPABxQGNoBLY-AWhXkoDt8B6Jge1oBNFjpEZAIb5E3dGADa4bDkTRoHaJAA0M2VlnZIQ%2BPA4B3CdK1bNp2ZABmigLYTrlJKvUWcTIbcQOhxSgDUARkhXUwBfNTcIcyjrOwdGACMXKO0PLwdyX29QrTDciABdXPzZYoh8sKA&code=JYWwDg9gTgLgBAbzgIQIZTgXzgMyhEOAcgCN0BaAG2BKIG4AoAegCoW4ABAEwFMwoeAY1QweXOCyYNegyuh64ArgDtBMYBGVxUYYADUAjAAoAlAC44ABXwhgAZx4AeOzCjBlAcwB8jBqgDuqMDwOvrGJr5MTHAABjx2wmA8MXAAFqh2cCQ8PFq8-EIiYnB27oIKAKIAygCsAHQM8Yk8RkR17UQRQA&fileType=.ts)
## When Not To Use It[​](#when-not-to-use-it)
If portions of your project heavily use deprecated APIs and have no plan for moving to non-deprecated ones, you might want to disable this rule in those portions.
## Related To[​](#related-to)
- [`import/no-deprecated`](https://github.com/import-js/eslint-plugin-import/blob/main/docs/rules/no-deprecated.md) and [`import-x/no-deprecated`](https://github.com/un-ts/eslint-plugin-import-x/blob/master/docs/rules/no-deprecated.md): Does not use type information, but does also support [TomDoc](http://tomdoc.org)
- [`eslint-plugin-deprecation`](https://github.com/gund/eslint-plugin-deprecation) ([`deprecation/deprecation`](https://github.com/gund/eslint-plugin-deprecation?tab=readme-ov-file#rules)): Predecessor to this rule in a separate plugin
Type checked lint rules are more powerful than traditional lint rules, but also require configuring [type checked linting](/getting-started/typed-linting).
See [Troubleshooting > Linting with Type Information > Performance](/troubleshooting/typed-linting/performance) if you experience performance degradations after enabling type checked rules.
## Resources[​](#resources)
- [Rule source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/src/rules/no-deprecated.ts)
- [Test source](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/tests/rules/no-deprecated.test.ts)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/no-deprecated.mdx)- [Examples](#examples)- [Options](#options)[`allow`](#allow)- [When Not To Use It](#when-not-to-use-it)- [Related To](#related-to)- [Resources](#resources)