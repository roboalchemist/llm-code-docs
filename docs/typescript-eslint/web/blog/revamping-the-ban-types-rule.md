# Source: https://typescript-eslint.io/blog/revamping-the-ban-types-rule

# Revamping the `ban-types` rule
January 5, 2026 · 6 min read[](https://github.com/JoshuaKGoldberg)[Josh Goldberg](https://github.com/JoshuaKGoldberg)typescript-eslint MaintainerFor many years, `@typescript-eslint/ban-types` was one of the more prominent rules in typescript-eslint.
It served three purposes:
- It banned usage of the unsafe "empty object" `{}` type
- It banned uses of dangerous or misleading built-in types: `Function`, `Number`, and so on
- It also allowed users to provide additional types to ban
Those are all great areas for linting!
However, `@typescript-eslint/ban-types` suffered from several key design issues:
- By targeting all three areas of banning, it was hard to configure to only what a project needs
- It was overly strict on banning `{}`, to the point of confusing and inconveniencing users
- It was limited in what auto-fixes and edge cases it could handle for its default banned types
This post will explain how `@typescript-eslint/ban-types` came to be, its benefits and drawbacks, and the new rules that better handle its targeted functionality.
## A Brief History of `ban-types`[​](#a-brief-history-of-ban-types)
The first version of a *"ban types"* lint rule came from [TSLint](https://palantir.github.io/tslint), a now-deprecated TypeScript-only linter predating typescript-eslint.
[TSLint&#x27;s `ban-type` rule](http://palantir.github.io/tslint/rules/ban-types) didn&#x27;t ban any types by default.
It would only ban types explicitly declared in a project&#x27;s linting config.
When the rule was ported to `@typescript-eslint/ban-types`, it was changed to additionally lint against known dangerous built-in types by default.
Doing so meant that the `plugin:typescript-eslint/recommended` preset config would lint against them by default.
The drawback of linting against those types by default was that nuanced types such as `object` and `{}` went through the same limited configuration channels as more straightforward types like `Function`.
`{}` in particular has nuance of when it should be used -- which is not describable in a rule configuration format.
As of typescript-eslint v8, the old `@typescript-eslint/ban-types` rule has now been split into several more targeted rules.
Those rules each capture one of the targeted areas of the now-deprecated `@ytpescript-eslint/ban-types` rule.
By splitting into several rules, each has more specific, user-friendly configuration options and documentation pages.
## Empty Object Types[​](#empty-object-types)
[`@typescript-eslint/no-empty-object-type`](/rules/no-empty-object-type) is the new rule for banning the built-in `{}` type in confusing locations.
The `{}`, or "empty object" type in TypeScript is a common source of confusion for developers unfamiliar with TypeScript&#x27;s structural typing.
These developers think `{}` represents "an object with no properties", however `{}` represents any *non-nullish value*. This means that it can represent any object with 0 or more properties or even primitives like strings, numbers, and booleans:
```
let anyNonNullishValue: {} = &#x27;Intentionally allowed by TypeScript.&#x27;;**
```
Often, developers writing `{}` actually mean either:
- `object`: representing any *object* value
- `unknown`: representing any value at all, including `null` and `undefined`
In other words, the "empty object" type `{}` really means *"any value that is defined"*.
That includes arrays, class instances, functions, and primitives such as `string` and `symbol`.
The word "object" in its name is a bit of a misnomer.
`{}` empty objects are permissible in a few edge cases, most commonly:
- Intersection constituents (e.g. types like TypeScript&#x27;s `type NonNullable<T> = T & {}`)
- Interfaces that extend from multiple other interfaces and add no fields of their own
Those cases could not be described with the old `@typescript-eslint/ban-types` format.
Now, they are encoded as exemptions in the new [`@typescript-eslint/no-empty-object-type`](/rules/no-empty-object-type) rule.
## `Function` Types[​](#function-types)
[`@typescript-eslint/no-unsafe-function-type`](/rules/no-unsafe-function-type) is the new rule for banning the built-in `Function` type.
The built-in `Function` type is an overly permissive way to describe a function.
It allows being called with any number of arguments and returns type `any`.
```
const anyFunction: Function = (arg: boolean) => {};
anyFunction(); // Ok
anyFunction(123); // Ok
anyFunction(&#x27;abc&#x27;); // Ok
const numberValue: number = anyFunction(); // Ok
const stringValue: string = anyFunction(); // Ok
```
Instead of using `Function`, code should generally specify function parameters and return types in types.
Common cases and more examples are noted in the new [`@typescript-eslint/no-unsafe-function-type`](/rules/no-unsafe-function-type) rule&#x27;s documentation.
## Primitive Wrapper Types[​](#primitive-wrapper-types)
[`@typescript-eslint/no-wrapper-object-types`](/rules/no-wrapper-object-types) is the new rule for banning `Object` and built-in class wrappers such as `Boolean` and `Number`.
TypeScript defines uppercase "wrapper" object types corresponding to each of JavaScript&#x27;s primitive data types and equivalent wrapper classes: `boolean`/`Boolean`, `number`/`Number`, and so on.
```
let myNumber: Number;
myNumber = 0; // Ok
myNumber = Number(0); // Ok
let myObject: Object = &#x27;allowed by TypeScript&#x27;; // Ok
```
Due to the quirks of TypeScript&#x27;s structural typing, the corresponding primitives are also assignable to these uppercase types, since they have the same "shape".
Instances of the uppercase class types also have surprisingly different behaviors at runtime, including always being truthy (even for values like `new Boolean(false)`) and being compared by reference (`new String("a") !== new String("a")`).
Instead of using uppercase wrapper object types, code should generally stick with lower-case primitive types.
Common cases and more examples are noted in the new [`@typescript-eslint/no-wrapper-object-types`](/rules/no-wrapper-object-types) rule&#x27;s documentation.
## User-Defined Type Bans[​](#user-defined-type-bans)
[`@typescript-eslint/no-restricted-types`](/rules/no-restricted-types) is the new rule for banning a configurable list of type names.
It acts similarly to the old `ban-types` rule:
- It defines no types by default: i.e. it must be configured to be useful
- It allows specifying types to ban, along with optional messages to display
As with `@typescript-eslint/ban-types`, `@typescript-eslint/no-restricted-types` additionally allows specifying auto-fixes to replace types with.
The new rule also allows specifying suggestions to surface in editors, for cases when the fix isn&#x27;t known to be reliable.
Here&#x27;s an example of configuring the new rule to ban a deprecated API, with a custom message and two suggestions:
```
{
"@typescript-eslint/no-restricted-types": [
"error",
{
"types": {
"DeprecatedOldAPI": {
"message": "Use either NewAPIOne or NewAPITwo instead",
"suggest": ["NewAPIOne", "NewAPITwo"],
},
},
},
],
}
```
By acting as a purely user-configured rule, `@typescript-eslint/no-restricted-types`&#x27;s behavior falls in line with core ESLint rules like [`no-restricted-imports`](https://eslint.org/docs/latest/no-restricted-imports) and [`no-restricted-syntax`](https://eslint.org/docs/latest/no-restricted-syntax).
See the new [`@typescript-eslint/no-restricted-types`](/rules/no-restricted-types) rule&#x27;s documentation for more information on how to configure it.
## Closing Thoughts[​](#closing-thoughts)
We&#x27;d like to give a big thanks to all the users who gave feedback on the old `@typescript-eslint/ban-types` rule.
In particular, we&#x27;d like to thank [Ryan Cavanaugh](https://github.com/RyanCavanaugh) from the TypeScript team for advising on the rule&#x27;s design (and for dealing with users frequently sending issues to TypeScript itself on what was actually an overly aggressive lint rule).
## Supporting typescript-eslint[​](#supporting-typescript-eslint)
If you enjoyed this blog post and/or use typescript-eslint, please consider [supporting us on Open Collective](https://opencollective.com/typescript-eslint). We&#x27;re a small volunteer team and could use your support to make the ESLint experience on TypeScript great. Thanks! 💖
Tags:**- [ban-types](/blog/tags/ban-types)- [interfaces](/blog/tags/interfaces)- [no-empty-object-type](/blog/tags/no-empty-object-type)- [no-restricted-types](/blog/tags/no-restricted-types)- [no-unsafe-function-type](/blog/tags/no-unsafe-function-type)- [no-wrapper-object-types](/blog/tags/no-wrapper-object-types)- [objects](/blog/tags/objects)