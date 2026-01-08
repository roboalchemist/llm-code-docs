# Source: https://typescript-eslint.io/packages/type-utils/type-or-value-specifier

On this page# TypeOrValueSpecifierSome lint rules include options to describe specific *types* and/or *values*.
These options use a standardized format exported from the `type-utils` package, **`TypeOrValueSpecifier`**.
`TypeOrValueSpecifier` allows three object forms of specifiers:
- [`FileSpecifier`](#filespecifier): for types or values declared in local files
- [`LibSpecifier`](#libspecifier): for types or values declared in TypeScript&#x27;s built-in lib definitions
- [`PackageSpecifier`](#packagespecifier): for types or values imported from packages
For example, the following configuration of [`@typescript-eslint/no-floating-promises` > `allowForKnownSafeCalls`](/rules/no-floating-promises#allowforknownsafecalls) marks `node:test`&#x27;s `it` as safe using a package specifier:
```
{
"@typescript-eslint/no-floating-promises": [
"error",
{
"allowForKnownSafeCalls": [
{ "from": "package", "name": "it", "package": "node:test" }
]
}
]
}
```
Each object format requires at least:
- `from`: which specifier to use, as `&#x27;file&#x27; | &#x27;lib&#x27; | &#x27;package&#x27;`
- `name`: a `string` or `string[]` for type or value name(s) to match on
## FileSpecifier[​](#filespecifier)
```
interface FileSpecifier {
from: &#x27;file&#x27;;
name: string[] | string;
path?: string;
}
```
Describes specific types or values declared in local files.
`path` may be used to specify a file the types or values must be declared in.
If omitted, all files will be matched.
### FileSpecifier Examples[​](#filespecifier-examples)
Matching all types and values named `Props`:
```
{ "from": "file", "name": "Props" }
```
Matching all types and values named `Props` in `file.tsx`:
```
{ "from": "file", "name": "Props", "path": "file.tsx" }
```
## LibSpecifier[​](#libspecifier)
```
interface LibSpecifier {
from: &#x27;lib&#x27;;
name: string[] | string;
}
```
Describes specific types or values declared in TypeScript&#x27;s built-in `lib.*.d.ts` ("lib") types.
Lib types include `lib.dom.d.ts` globals such as `Window` and `lib.es*.ts` globals such as `Array`.
### LibSpecifier Examples[​](#libspecifier-examples)
Matching all strings:
```
{ "from": "lib", "name": "string" }
```
Matching all array-typed values:
```
{ "from": "lib", "name": "Array" }
```
Matching all `Promise` and `PromiseLike`-typed values:
```
{ "from": "lib", "name": ["Promise", "PromiseLike"] }
```
## PackageSpecifier[​](#packagespecifier)
```
interface PackageSpecifier {
from: &#x27;package&#x27;;
name: string[] | string;
package: string;
}
```
Describes specific types or values imported from packages.
`package` must be used to specify the package name.
### PackageSpecifier Examples[​](#packagespecifier-examples)
Matching the `SafePromise` type from `@reduxjs/toolkit`:
```
{ "from": "package", "name": "SafePromise", "package": "@reduxjs/toolkit" }
```
Matching the `describe`, `it`, and `test` values from `vitest`:
```
{ "from": "package", "name": ["describe", "it", "test"], "package": "vitest" }
```
## Universal String Specifiers[​](#universal-string-specifiers)
`TypeOrValueSpecifier` also allows providing a plain string specifier to match all names regardless of declaration source.
For example, providing `"RegExp"` matches *all* types and values named `RegExp`.
dangerWe strongly recommend not using universal string specifiers.
Matching *all* names without specifying a source file, library, or package can accidentally match other types or values with a coincidentally similar name.
Universal string specifiers will be removed in a future major version of typescript-eslint.
## Rule Options Using This Format[​](#rule-options-using-this-format)
- [`@typescript-eslint/no-floating-promises` > `allowForKnownSafeCalls`](/rules/no-floating-promises#allowforknownsafecalls)
- [`@typescript-eslint/no-floating-promises` > `allowForKnownSafePromises`](/rules/no-floating-promises#allowforknownsafepromises)
- [`@typescript-eslint/only-throw-error` > `allow`](/rules/only-throw-error/#allow)
- [`@typescript-eslint/prefer-readonly-parameter-types` > `allow`](/rules/prefer-readonly-parameter-types/#allow)
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../../docs/packages/type-utils/TypeOrValueSpecifier.mdx)- [FileSpecifier](#filespecifier)[FileSpecifier Examples](#filespecifier-examples)- [LibSpecifier](#libspecifier)[LibSpecifier Examples](#libspecifier-examples)- [PackageSpecifier](#packagespecifier)[PackageSpecifier Examples](#packagespecifier-examples)- [Universal String Specifiers](#universal-string-specifiers)- [Rule Options Using This Format](#rule-options-using-this-format)