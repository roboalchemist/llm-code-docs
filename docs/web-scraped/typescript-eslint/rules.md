# Source: https://typescript-eslint.io/rules/?=recommended-typeInformation

On this page# Overview`@typescript-eslint/eslint-plugin` includes over 100 rules that detect best practice violations, bugs, and/or stylistic issues specifically for TypeScript code. All of our rules are listed below.
tipInstead of enabling rules one by one, we recommend using one of [our pre-defined configs](/users/configs) to enable a large set of recommended rules.
## Rules[​](#rules)
The rules are listed in alphabetical order. You can optionally filter them based on these categories:
*Config Group (⚙️)*- ✅ recommended- 🔒 strict- 🎨 stylistic*Metadata*- 🔧 fixable- 💡 has suggestions- 💭 type checked- 🧱 extension- 💀 deprecated(These categories are explained in [more detail below](#filtering).)
Rule⚙️🔧💭🧱💀[`@typescript-eslint/adjacent-overload-signatures`](/rules/adjacent-overload-signatures)
Require that function overload signatures be consecutive🎨[`@typescript-eslint/array-type`](/rules/array-type)
Require consistently using either `T[]` or `Array<T>` for arrays🎨🔧[`@typescript-eslint/await-thenable`](/rules/await-thenable)
Disallow awaiting a value that is not a Thenable✅💡💭[`@typescript-eslint/ban-ts-comment`](/rules/ban-ts-comment)
Disallow `@ts-<directive>` comments or require descriptions after directives✅💡[`@typescript-eslint/ban-tslint-comment`](/rules/ban-tslint-comment)
Disallow `// tslint:<rule-flag>` comments🎨🔧[`@typescript-eslint/class-literal-property-style`](/rules/class-literal-property-style)
Enforce that literals on classes are exposed in a consistent style🎨💡[`@typescript-eslint/class-methods-use-this`](/rules/class-methods-use-this)
Enforce that class methods utilize `this`🧱[`@typescript-eslint/consistent-generic-constructors`](/rules/consistent-generic-constructors)
Enforce specifying generic type arguments on type annotation or constructor name of a constructor call🎨🔧[`@typescript-eslint/consistent-indexed-object-style`](/rules/consistent-indexed-object-style)
Require or disallow the `Record` type🎨🔧
💡[`@typescript-eslint/consistent-return`](/rules/consistent-return)
Require `return` statements to either always or never specify values💭🧱[`@typescript-eslint/consistent-type-assertions`](/rules/consistent-type-assertions)
Enforce consistent usage of type assertions🎨🔧
💡[`@typescript-eslint/consistent-type-definitions`](/rules/consistent-type-definitions)
Enforce type definitions to consistently use either `interface` or `type`🎨🔧[`@typescript-eslint/consistent-type-exports`](/rules/consistent-type-exports)
Enforce consistent usage of type exports🔧💭[`@typescript-eslint/consistent-type-imports`](/rules/consistent-type-imports)
Enforce consistent usage of type imports🔧[`@typescript-eslint/default-param-last`](/rules/default-param-last)❄️
Enforce default parameters to be last🧱[`@typescript-eslint/dot-notation`](/rules/dot-notation)❄️
Enforce dot notation whenever possible🎨🔧💭🧱[`@typescript-eslint/explicit-function-return-type`](/rules/explicit-function-return-type)
Require explicit return types on functions and class methods[`@typescript-eslint/explicit-member-accessibility`](/rules/explicit-member-accessibility)
Require explicit accessibility modifiers on class properties and methods🔧
💡[`@typescript-eslint/explicit-module-boundary-types`](/rules/explicit-module-boundary-types)
Require explicit return and argument types on exported functions&#x27; and classes&#x27; public class methods[`@typescript-eslint/init-declarations`](/rules/init-declarations)❄️
Require or disallow initialization in variable declarations🧱[`@typescript-eslint/max-params`](/rules/max-params)
Enforce a maximum number of parameters in function definitions🧱[`@typescript-eslint/member-ordering`](/rules/member-ordering)❄️
Require a consistent member declaration order[`@typescript-eslint/method-signature-style`](/rules/method-signature-style)
Enforce using a particular method signature syntax🔧[`@typescript-eslint/naming-convention`](/rules/naming-convention)❄️
Enforce naming conventions for everything across a codebase💭[`@typescript-eslint/no-array-constructor`](/rules/no-array-constructor)
Disallow generic `Array` constructors✅🔧🧱[`@typescript-eslint/no-array-delete`](/rules/no-array-delete)
Disallow using the `delete` operator on array values✅💡💭[`@typescript-eslint/no-base-to-string`](/rules/no-base-to-string)
Require `.toString()` and `.toLocaleString()` to only be called on objects which provide useful information when stringified✅💭[`@typescript-eslint/no-confusing-non-null-assertion`](/rules/no-confusing-non-null-assertion)
Disallow non-null assertion in locations that may be confusing🎨💡[`@typescript-eslint/no-confusing-void-expression`](/rules/no-confusing-void-expression)
Require expressions of type void to appear in statement position🔒🔧
💡💭[`@typescript-eslint/no-deprecated`](/rules/no-deprecated)
Disallow using code marked as `@deprecated`🔒💭[`@typescript-eslint/no-dupe-class-members`](/rules/no-dupe-class-members)
Disallow duplicate class members🧱[`@typescript-eslint/no-duplicate-enum-values`](/rules/no-duplicate-enum-values)
Disallow duplicate enum member values✅[`@typescript-eslint/no-duplicate-type-constituents`](/rules/no-duplicate-type-constituents)
Disallow duplicate constituents of union or intersection types✅🔧💭[`@typescript-eslint/no-dynamic-delete`](/rules/no-dynamic-delete)
Disallow using the `delete` operator on computed key expressions🔒[`@typescript-eslint/no-empty-function`](/rules/no-empty-function)
Disallow empty functions🎨💡🧱[`@typescript-eslint/no-empty-interface`](/rules/no-empty-interface)
Disallow the declaration of empty interfaces🔧
💡💀[`@typescript-eslint/no-empty-object-type`](/rules/no-empty-object-type)
Disallow accidentally using the "empty object" type✅💡[`@typescript-eslint/no-explicit-any`](/rules/no-explicit-any)
Disallow the `any` type✅🔧
💡[`@typescript-eslint/no-extra-non-null-assertion`](/rules/no-extra-non-null-assertion)
Disallow extra non-null assertions✅🔧[`@typescript-eslint/no-extraneous-class`](/rules/no-extraneous-class)
Disallow classes used as namespaces🔒[`@typescript-eslint/no-floating-promises`](/rules/no-floating-promises)
Require Promise-like statements to be handled appropriately✅💡💭[`@typescript-eslint/no-for-in-array`](/rules/no-for-in-array)
Disallow iterating over an array with a for-in loop✅💭[`@typescript-eslint/no-implied-eval`](/rules/no-implied-eval)
Disallow the use of `eval()`-like functions✅💭🧱[`@typescript-eslint/no-import-type-side-effects`](/rules/no-import-type-side-effects)
Enforce the use of top-level import type qualifier when an import only has specifiers with inline type qualifiers🔧[`@typescript-eslint/no-inferrable-types`](/rules/no-inferrable-types)
Disallow explicit type declarations for variables or parameters initialized to a number, string, or boolean🎨🔧[`@typescript-eslint/no-invalid-this`](/rules/no-invalid-this)
Disallow `this` keywords outside of classes or class-like objects🧱[`@typescript-eslint/no-invalid-void-type`](/rules/no-invalid-void-type)
Disallow `void` type outside of generic or return types🔒[`@typescript-eslint/no-loop-func`](/rules/no-loop-func)
Disallow function declarations that contain unsafe references inside loop statements🧱[`@typescript-eslint/no-loss-of-precision`](/rules/no-loss-of-precision)
Disallow literal numbers that lose precision🧱💀[`@typescript-eslint/no-magic-numbers`](/rules/no-magic-numbers)❄️
Disallow magic numbers🧱[`@typescript-eslint/no-meaningless-void-operator`](/rules/no-meaningless-void-operator)
Disallow the `void` operator except when used to discard a value🔒🔧
💡💭[`@typescript-eslint/no-misused-new`](/rules/no-misused-new)
Enforce valid definition of `new` and `constructor`✅[`@typescript-eslint/no-misused-promises`](/rules/no-misused-promises)
Disallow Promises in places not designed to handle them✅💭[`@typescript-eslint/no-misused-spread`](/rules/no-misused-spread)
Disallow using the spread operator when it might cause unexpected behavior🔒💡💭[`@typescript-eslint/no-mixed-enums`](/rules/no-mixed-enums)
Disallow enums from having both number and string members🔒💭[`@typescript-eslint/no-namespace`](/rules/no-namespace)
Disallow TypeScript namespaces✅[`@typescript-eslint/no-non-null-asserted-nullish-coalescing`](/rules/no-non-null-asserted-nullish-coalescing)
Disallow non-null assertions in the left operand of a nullish coalescing operator🔒💡[`@typescript-eslint/no-non-null-asserted-optional-chain`](/rules/no-non-null-asserted-optional-chain)
Disallow non-null assertions after an optional chain expression✅💡[`@typescript-eslint/no-non-null-assertion`](/rules/no-non-null-assertion)
Disallow non-null assertions using the `!` postfix operator🔒💡[`@typescript-eslint/no-redeclare`](/rules/no-redeclare)
Disallow variable redeclaration🧱[`@typescript-eslint/no-redundant-type-constituents`](/rules/no-redundant-type-constituents)
Disallow members of unions and intersections that do nothing or override type information✅💭[`@typescript-eslint/no-require-imports`](/rules/no-require-imports)
Disallow invocation of `require()`✅[`@typescript-eslint/no-restricted-imports`](/rules/no-restricted-imports)
Disallow specified modules when loaded by `import`🧱[`@typescript-eslint/no-restricted-types`](/rules/no-restricted-types)
Disallow certain types🔧
💡[`@typescript-eslint/no-shadow`](/rules/no-shadow)
Disallow variable declarations from shadowing variables declared in the outer scope🧱[`@typescript-eslint/no-this-alias`](/rules/no-this-alias)
Disallow aliasing `this`✅[`@typescript-eslint/no-type-alias`](/rules/no-type-alias)
Disallow type aliases💀[`@typescript-eslint/no-unnecessary-boolean-literal-compare`](/rules/no-unnecessary-boolean-literal-compare)
Disallow unnecessary equality comparisons against boolean literals🔒🔧💭[`@typescript-eslint/no-unnecessary-condition`](/rules/no-unnecessary-condition)
Disallow conditionals where the type is always truthy or always falsy🔒💡💭[`@typescript-eslint/no-unnecessary-parameter-property-assignment`](/rules/no-unnecessary-parameter-property-assignment)
Disallow unnecessary assignment of constructor property parameter[`@typescript-eslint/no-unnecessary-qualifier`](/rules/no-unnecessary-qualifier)
Disallow unnecessary namespace qualifiers🔧💭[`@typescript-eslint/no-unnecessary-template-expression`](/rules/no-unnecessary-template-expression)
Disallow unnecessary template expressions🔒🔧💭[`@typescript-eslint/no-unnecessary-type-arguments`](/rules/no-unnecessary-type-arguments)
Disallow type arguments that are equal to the default🔒🔧💭[`@typescript-eslint/no-unnecessary-type-assertion`](/rules/no-unnecessary-type-assertion)
Disallow type assertions that do not change the type of an expression✅🔧💭[`@typescript-eslint/no-unnecessary-type-constraint`](/rules/no-unnecessary-type-constraint)
Disallow unnecessary constraints on generic types✅💡[`@typescript-eslint/no-unnecessary-type-conversion`](/rules/no-unnecessary-type-conversion)
Disallow conversion idioms when they do not change the type or value of the expression🔒💡💭[`@typescript-eslint/no-unnecessary-type-parameters`](/rules/no-unnecessary-type-parameters)
Disallow type parameters that aren&#x27;t used multiple times🔒💡💭[`@typescript-eslint/no-unsafe-argument`](/rules/no-unsafe-argument)
Disallow calling a function with a value with type `any`✅💭[`@typescript-eslint/no-unsafe-assignment`](/rules/no-unsafe-assignment)
Disallow assigning a value with type `any` to variables and properties✅💭[`@typescript-eslint/no-unsafe-call`](/rules/no-unsafe-call)
Disallow calling a value with type `any`✅💭[`@typescript-eslint/no-unsafe-declaration-merging`](/rules/no-unsafe-declaration-merging)
Disallow unsafe declaration merging✅[`@typescript-eslint/no-unsafe-enum-comparison`](/rules/no-unsafe-enum-comparison)
Disallow comparing an enum value with a non-enum value✅💡💭[`@typescript-eslint/no-unsafe-function-type`](/rules/no-unsafe-function-type)
Disallow using the unsafe built-in Function type✅[`@typescript-eslint/no-unsafe-member-access`](/rules/no-unsafe-member-access)
Disallow member access on a value with type `any`✅💭[`@typescript-eslint/no-unsafe-return`](/rules/no-unsafe-return)
Disallow returning a value with type `any` from a function✅💭[`@typescript-eslint/no-unsafe-type-assertion`](/rules/no-unsafe-type-assertion)
Disallow type assertions that narrow a type💭[`@typescript-eslint/no-unsafe-unary-minus`](/rules/no-unsafe-unary-minus)
Require unary negation to take a number✅💭[`@typescript-eslint/no-unused-expressions`](/rules/no-unused-expressions)
Disallow unused expressions✅🧱[`@typescript-eslint/no-unused-private-class-members`](/rules/no-unused-private-class-members)
Disallow unused private class members🧱[`@typescript-eslint/no-unused-vars`](/rules/no-unused-vars)
Disallow unused variables✅🧱[`@typescript-eslint/no-use-before-define`](/rules/no-use-before-define)
Disallow the use of variables before they are defined🧱[`@typescript-eslint/no-useless-constructor`](/rules/no-useless-constructor)
Disallow unnecessary constructors🔒💡🧱[`@typescript-eslint/no-useless-default-assignment`](/rules/no-useless-default-assignment)
Disallow default values that will never be used🔒🔧💭[`@typescript-eslint/no-useless-empty-export`](/rules/no-useless-empty-export)
Disallow empty exports that don&#x27;t change anything in a module file🔧[`@typescript-eslint/no-var-requires`](/rules/no-var-requires)
Disallow `require` statements except in import statements💀[`@typescript-eslint/no-wrapper-object-types`](/rules/no-wrapper-object-types)
Disallow using confusing built-in primitive class wrappers✅🔧[`@typescript-eslint/non-nullable-type-assertion-style`](/rules/non-nullable-type-assertion-style)
Enforce non-null assertions over explicit type assertions🎨🔧💭[`@typescript-eslint/only-throw-error`](/rules/only-throw-error)
Disallow throwing non-`Error` values as exceptions✅💭🧱[`@typescript-eslint/parameter-properties`](/rules/parameter-properties)
Require or disallow parameter properties in class constructors[`@typescript-eslint/prefer-as-const`](/rules/prefer-as-const)
Enforce the use of `as const` over literal type✅   🔧
💡[`@typescript-eslint/prefer-destructuring`](/rules/prefer-destructuring)❄️
Require destructuring from arrays and/or objects🔧💭🧱[`@typescript-eslint/prefer-enum-initializers`](/rules/prefer-enum-initializers)
Require each enum member value to be explicitly initialized💡[`@typescript-eslint/prefer-find`](/rules/prefer-find)
Enforce the use of Array.prototype.find() over Array.prototype.filter() followed by [0] when looking for a single result🎨💡💭[`@typescript-eslint/prefer-for-of`](/rules/prefer-for-of)
Enforce the use of `for-of` loop over the standard `for` loop where possible🎨[`@typescript-eslint/prefer-function-type`](/rules/prefer-function-type)
Enforce using function types instead of interfaces with call signatures🎨🔧[`@typescript-eslint/prefer-includes`](/rules/prefer-includes)
Enforce `includes` method over `indexOf` method🎨🔧💭[`@typescript-eslint/prefer-literal-enum-member`](/rules/prefer-literal-enum-member)
Require all enum members to be literal values🔒[`@typescript-eslint/prefer-namespace-keyword`](/rules/prefer-namespace-keyword)
Require using `namespace` keyword over `module` keyword to declare custom TypeScript modules✅🔧[`@typescript-eslint/prefer-nullish-coalescing`](/rules/prefer-nullish-coalescing)
Enforce using the nullish coalescing operator instead of logical assignments or chaining🎨💡💭[`@typescript-eslint/prefer-optional-chain`](/rules/prefer-optional-chain)
Enforce using concise optional chain expressions instead of chained logical ands, negated logical ors, or empty objects🎨🔧
💡💭[`@typescript-eslint/prefer-promise-reject-errors`](/rules/prefer-promise-reject-errors)
Require using Error objects as Promise rejection reasons✅💭🧱[`@typescript-eslint/prefer-readonly`](/rules/prefer-readonly)
Require private members to be marked as `readonly` if they&#x27;re never modified outside of the constructor🔧💭[`@typescript-eslint/prefer-readonly-parameter-types`](/rules/prefer-readonly-parameter-types)
Require function parameters to be typed as `readonly` to prevent accidental mutation of inputs💭[`@typescript-eslint/prefer-reduce-type-parameter`](/rules/prefer-reduce-type-parameter)
Enforce using type parameter when calling `Array#reduce` instead of using a type assertion🔒🔧💭[`@typescript-eslint/prefer-regexp-exec`](/rules/prefer-regexp-exec)
Enforce `RegExp#exec` over `String#match` if no global flag is provided🎨🔧💭[`@typescript-eslint/prefer-return-this-type`](/rules/prefer-return-this-type)
Enforce that `this` is used when only `this` type is returned🔒🔧💭[`@typescript-eslint/prefer-string-starts-ends-with`](/rules/prefer-string-starts-ends-with)
Enforce using `String#startsWith` and `String#endsWith` over other equivalent methods of checking substrings🎨🔧💭[`@typescript-eslint/prefer-ts-expect-error`](/rules/prefer-ts-expect-error)
Enforce using `@ts-expect-error` over `@ts-ignore`🔧💀[`@typescript-eslint/promise-function-async`](/rules/promise-function-async)
Require any function or method that returns a Promise to be marked async🔧💭[`@typescript-eslint/related-getter-setter-pairs`](/rules/related-getter-setter-pairs)
Enforce that `get()` types should be assignable to their equivalent `set()` type🔒💭[`@typescript-eslint/require-array-sort-compare`](/rules/require-array-sort-compare)
Require `Array#sort` and `Array#toSorted` calls to always provide a `compareFunction`💭[`@typescript-eslint/require-await`](/rules/require-await)
Disallow async functions which do not return promises and have no `await` expression✅💡💭🧱[`@typescript-eslint/restrict-plus-operands`](/rules/restrict-plus-operands)
Require both operands of addition to be the same type and be `bigint`, `number`, or `string`✅💭[`@typescript-eslint/restrict-template-expressions`](/rules/restrict-template-expressions)
Enforce template literal expressions to be of `string` type✅💭[`@typescript-eslint/return-await`](/rules/return-await)
Enforce consistent awaiting of returned promises🔒🔧
💡💭[`@typescript-eslint/sort-type-constituents`](/rules/sort-type-constituents)
Enforce constituents of a type union/intersection to be sorted alphabetically🔧
💡💀[`@typescript-eslint/strict-boolean-expressions`](/rules/strict-boolean-expressions)
Disallow certain types in boolean expressions💡💭[`@typescript-eslint/switch-exhaustiveness-check`](/rules/switch-exhaustiveness-check)
Require switch-case statements to be exhaustive💡💭[`@typescript-eslint/triple-slash-reference`](/rules/triple-slash-reference)
Disallow certain triple slash directives in favor of ES6-style import declarations✅[`@typescript-eslint/typedef`](/rules/typedef)
Require type annotations in certain places💀[`@typescript-eslint/unbound-method`](/rules/unbound-method)
Enforce unbound methods are called with their expected scope✅💭[`@typescript-eslint/unified-signatures`](/rules/unified-signatures)
Disallow two overloads that could be unified into one with a union or an optional/rest parameter🔒[`@typescript-eslint/use-unknown-in-catch-callback-variable`](/rules/use-unknown-in-catch-callback-variable)
Enforce typing arguments in Promise rejection callbacks as `unknown`🔒💡💭
## Filtering[​](#filtering)
### Config Group (⚙️)[​](#config-group-️)
"Config Group" refers to the [pre-defined config](/users/configs) that includes the rule. Extending from a configuration preset allow for enabling a large set of recommended rules all at once.
### Metadata[​](#metadata)
- `🔧 fixable` refers to whether the rule contains an [ESLint `--fix` auto-fixer](https://eslint.org/docs/latest/use/command-line-interface#--fix).
- `💡 has suggestions` refers to whether the rule contains an ESLint suggestion fixer.
Sometimes, it is not safe to automatically fix the code with an auto-fixer. But in these cases, we often have a good guess of what the correct fix should be, and we can provide it as a suggestion to the developer.
- `💭 requires type information` refers to whether the rule requires [typed linting](/getting-started/typed-linting).
- `🧱 extension rule` means that the rule is an extension of an [core ESLint rule](https://eslint.org/docs/latest/rules) (see [Extension Rules](#extension-rules)).
- `💀 deprecated rule` means that the rule should no longer be used and will be removed from the plugin in a future version.
## Extension Rules[​](#extension-rules)
Some core ESLint rules do not support TypeScript syntax: either they crash, ignore the syntax, or falsely report against it.
In these cases, we create what we call an "extension rule": a rule within our plugin that has the same functionality, but also supports TypeScript.
Extension rules generally completely replace the base rule from ESLint core.
If the base rule is enabled in a config you extend from, you&#x27;ll need to disable the base rule:
```
module.exports = {
extends: [&#x27;eslint:recommended&#x27;],
rules: {
// Note: you must disable the base rule as it can report incorrect errors
&#x27;no-unused-vars&#x27;: &#x27;off&#x27;,
&#x27;@typescript-eslint/no-unused-vars&#x27;: &#x27;error&#x27;,
},
};
```
[Search for `🧱 extension rule`s](/rules/?=extension#rules) in this page to see all extension rules.
## Frozen Rules[​](#frozen-rules)
When rules are feature complete, they are marked as frozen (indicated with ❄️ in the documentation). This applies to standalone rules that are complete, as well as [extension rules](#extension-rules) whose underlying core ESLint rules are frozen. After that point, we expect users to use [disable comments](https://eslint.org/docs/latest/use/configure/rules#using-configuration-comments-1) when they find an edge case that isn’t covered.
When a rule is frozen, it means:
- **Bug fixes**: We will still fix confirmed bugs.
- **New ECMAScript features**: We will ensure compatibility with new ECMAScript features, meaning the rule will not break on new syntax.
- **TypeScript support**: We will ensure compatibility with TypeScript syntax, meaning the rule will not break on TypeScript syntax and violations are appropriate for TypeScript.
- **New options**: We will not add any new options unless an option is the only way to fix a bug or support a newly-added ECMAScript feature.
If you find that a frozen rule would work better for you with a change, we recommend copying the rule source code and modifying it to fit your needs.
[Edit this page](https://github.com/typescript-eslint/typescript-eslint/edit/main/packages/website/../eslint-plugin/docs/rules/README.md)- [Rules](#rules)- [Filtering](#filtering)[Config Group (⚙️)](#config-group-️)- [Metadata](#metadata)- [Extension Rules](#extension-rules)- [Frozen Rules](#frozen-rules)