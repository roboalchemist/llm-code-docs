# Source: https://ajv.js.org/codegen.html

Title: Ajv JSON schema validator

URL Source: https://ajv.js.org/codegen.html

Published Time: Sat, 14 Feb 2026 15:27:26 GMT

Markdown Content:
Code generation design | Ajv JSON schema validator
===============

[![Image 1: Ajv JSON schema validator](https://ajv.js.org/img/ajv.svg)Ajv JSON schema validator](https://ajv.js.org/)

[Home](https://ajv.js.org/)

Guide Guide
*   [Why use Ajv](https://ajv.js.org/guide/why-ajv.html)
*   [Getting started](https://ajv.js.org/guide/getting-started.html)
*   [Using with TypeScript](https://ajv.js.org/guide/typescript.html)
*   [Choosing schema language](https://ajv.js.org/guide/schema-language.html)
*   [Managing schemas](https://ajv.js.org/guide/managing-schemas.html)
*   [Combining schemas](https://ajv.js.org/guide/combining-schemas.html)
*   [Format validation](https://ajv.js.org/guide/formats.html)
*   [Modifying data](https://ajv.js.org/guide/modifying-data.html)
*   [User-defined keywords](https://ajv.js.org/guide/user-keywords.html)
*   [Asynchronous validation](https://ajv.js.org/guide/async-validation.html)
*   [Execution environments](https://ajv.js.org/guide/environments.html)

Reference Reference
*   [API Reference](https://ajv.js.org/api.html)
*   [Ajv options](https://ajv.js.org/options.html)
*   [JSON Schema](https://ajv.js.org/json-schema.html)
*   [JSON Type Definition](https://ajv.js.org/json-type-definition.html)
*   [Strict mode](https://ajv.js.org/strict-mode.html)
*   [Standalone validation code](https://ajv.js.org/standalone.html)
*   [User defined keywords](https://ajv.js.org/keywords.html)
*   [Type coercion rules](https://ajv.js.org/coercion.html)

Learn more Learn more
*   #### Extending Ajv

    *   [Extending Ajv](https://ajv.js.org/packages/)
    *   [ajv-cli](https://ajv.js.org/packages/ajv-cli.html)
    *   [ajv-errors](https://ajv.js.org/packages/ajv-errors.html)
    *   [ajv-formats](https://ajv.js.org/packages/ajv-formats.html)
    *   [ajv-i18n](https://ajv.js.org/packages/ajv-i18n.html)
    *   [ajv-keywords](https://ajv.js.org/packages/ajv-keywords.html)

*   #### Contributors

    *   [Contributing guide](https://ajv.js.org/contributing.html)
    *   [Code generation design](https://ajv.js.org/codegen.html)
    *   [Code components](https://ajv.js.org/components.html)
    *   [Code of Conduct](https://ajv.js.org/code_of_conduct.html)

*   #### Information

    *   [News](https://ajv.js.org/news/)
    *   [FAQ](https://ajv.js.org/faq.html)
    *   [Security](https://ajv.js.org/security.html)
    *   [Migrate from v6](https://ajv.js.org/v6-to-v8-migration.html)
    *   [What users say](https://ajv.js.org/testimonials.html)
    *   [License](https://ajv.js.org/license.html)

[Home](https://ajv.js.org/)

Guide Guide
*   [Why use Ajv](https://ajv.js.org/guide/why-ajv.html)
*   [Getting started](https://ajv.js.org/guide/getting-started.html)
*   [Using with TypeScript](https://ajv.js.org/guide/typescript.html)
*   [Choosing schema language](https://ajv.js.org/guide/schema-language.html)
*   [Managing schemas](https://ajv.js.org/guide/managing-schemas.html)
*   [Combining schemas](https://ajv.js.org/guide/combining-schemas.html)
*   [Format validation](https://ajv.js.org/guide/formats.html)
*   [Modifying data](https://ajv.js.org/guide/modifying-data.html)
*   [User-defined keywords](https://ajv.js.org/guide/user-keywords.html)
*   [Asynchronous validation](https://ajv.js.org/guide/async-validation.html)
*   [Execution environments](https://ajv.js.org/guide/environments.html)

Reference Reference
*   [API Reference](https://ajv.js.org/api.html)
*   [Ajv options](https://ajv.js.org/options.html)
*   [JSON Schema](https://ajv.js.org/json-schema.html)
*   [JSON Type Definition](https://ajv.js.org/json-type-definition.html)
*   [Strict mode](https://ajv.js.org/strict-mode.html)
*   [Standalone validation code](https://ajv.js.org/standalone.html)
*   [User defined keywords](https://ajv.js.org/keywords.html)
*   [Type coercion rules](https://ajv.js.org/coercion.html)

Learn more Learn more
*   #### Extending Ajv

    *   [Extending Ajv](https://ajv.js.org/packages/)
    *   [ajv-cli](https://ajv.js.org/packages/ajv-cli.html)
    *   [ajv-errors](https://ajv.js.org/packages/ajv-errors.html)
    *   [ajv-formats](https://ajv.js.org/packages/ajv-formats.html)
    *   [ajv-i18n](https://ajv.js.org/packages/ajv-i18n.html)
    *   [ajv-keywords](https://ajv.js.org/packages/ajv-keywords.html)

*   #### Contributors

    *   [Contributing guide](https://ajv.js.org/contributing.html)
    *   [Code generation design](https://ajv.js.org/codegen.html)
    *   [Code components](https://ajv.js.org/components.html)
    *   [Code of Conduct](https://ajv.js.org/code_of_conduct.html)

*   #### Information

    *   [News](https://ajv.js.org/news/)
    *   [FAQ](https://ajv.js.org/faq.html)
    *   [Security](https://ajv.js.org/security.html)
    *   [Migrate from v6](https://ajv.js.org/v6-to-v8-migration.html)
    *   [What users say](https://ajv.js.org/testimonials.html)
    *   [License](https://ajv.js.org/license.html)

*   Guide

*   Reference

*   Extending Ajv

*   Contributors

    *   [Contributing guide](https://ajv.js.org/contributing/)
    *   [Code generation design](https://ajv.js.org/codegen.html)
        *   [Safe code generation](https://ajv.js.org/codegen.html#safe-code-generation)
        *   [Code optimization](https://ajv.js.org/codegen.html#code-optimization)
        *   [User-defined keywords](https://ajv.js.org/codegen.html#user-defined-keywords)

    *   [Code components](https://ajv.js.org/components.html)
    *   [Code of conduct](https://ajv.js.org/code_of_conduct/)

*   Information

[#](https://ajv.js.org/codegen.html#code-generation-design) Code generation design
==================================================================================

*   [Safe code generation](https://ajv.js.org/codegen.html#safe-code-generation)
*   [Code optimization](https://ajv.js.org/codegen.html#code-optimization)
*   [User-defined keywords](https://ajv.js.org/codegen.html#user-defined-keywords)

Starting from v7 Ajv uses [CodeGen module(opens new window)](https://github.com/ajv-validator/ajv/blob/master/lib/compile/codegen/index.ts) that replaced [doT(opens new window)](https://github.com/olado/dot) templates used earlier.

The motivations for this change:

*   doT templates were difficult to maintain and to change, particularly for the occasional contributors.
*   they discouraged modularity within validation keywords code and also led to implicit dependencies between different parts of code.
*   they had risks of remote code execution in case untrusted schemas were used, even though all identified issues were patched.
*   ES6 template literals that are now widely supported offer a great alternative to both ASTs and to plain string concatenation - this option was not available when Ajv started.

[#](https://ajv.js.org/codegen.html#safe-code-generation) Safe code generation
------------------------------------------------------------------------------

CodeGen module defines two tagged templates that should be passed to all code generation methods and used in other tagged templates:

*   `_` - to create instances of private _Code class that will not be escaped when used in code or other tagged templates.
*   `str` - to create code for string expressions.

For example, this code:

```
const x = 0
// Name is a subclass of _Code that can be safely used in code - it only allows valid identifiers
// gen.const creates a unique variable name with the prefix "num".
const num: Name = gen.const("num", 5)
gen.if(
  // _`...` returns the instance of _Code with safe interpolation of `num` and `x`.
  // if `x` was a string, it would be inserted into code as a quoted string value rather than as a code fragment,
  // so if `x` contained some code, it would not be executed.
  _`${num} > ${x}`,
  () => log("greater"),
  () => log("smaller or equal")
)

function log(comparison: string): void {
  // msg creates a string expression with concatenation - see generated code below
  // type Code = _Code | Name, _Code can only be constructed with template literals
  const msg: Code = str`${num} is ${comparison} than ${x}`
  // msg is _Code instance, so it will be inserted via another template without quotes
  gen.code(_`console.log(${msg})`)
}
```

generates this javascript code:

```
const num0 = 5
if (num0 > 0) {
  console.log(num0 + " is greater than 0")
} else {
  console.log(num0 + " is smaller or equal than 0")
}
```

`.const`, `.if` and `.code` above are methods of CodeGen class that generate code inside class instance `gen` - see [source code(opens new window)](https://github.com/ajv-validator/ajv/blob/master/lib/compile/codegen/index.ts) for all available methods and [tests(opens new window)](https://github.com/ajv-validator/ajv/blob/master/spec/codegen.spec.ts) for other code generation examples.

These methods only accept instances of private class `_Code`, other values will be rejected by Typescript compiler - the risk to pass unsafe string is mitigated on type level.

If a string variable were used in `_` template literal, its value would be safely wrapped in quotes - in many cases it is quite useful, as it allows to inject values that can be either string or number via the same template. In the worst case, the generated code could be invalid, but it will prevent the risk of code execution that attacker could pass via untrusted schema as a string value that should be inserted in code (e.g., instead of a number). Also see the comment in the example.

[#](https://ajv.js.org/codegen.html#code-optimization) Code optimization
------------------------------------------------------------------------

CodeGen class generates code trees and performs several optimizations before the code is rendered:

1.   removes empty and unreachable branches (e.g. `else` branch after `if(true)`, etc.).
2.   removes unused variable declarations.
3.   replaces variables that are used only once and assigned expressions that are explicitly marked as "constant" (i.e. having referential transparency) with the expressions themselves.

Optimizations assume no side effects

These optimizations assume that the expressions in `if` conditions, `for` statement headers and assigned expressions are free of any side effects - this is the case for all pre-defined validation keywords.

See [these tests(opens new window)](https://github.com/ajv-validator/ajv/blob/master/spec/codegen.spec.ts) for examples.

By default Ajv does 1-pass optimization - based on the test suite it reduces the code size by 10.5% and the number of tree nodes by 16.7% (TODO benchmark the validation time). The second optimization pass changes it by less than 0.1%, so you won't need it unless you have really complex schemas or if you generate standalone code and want it to pass relevant eslint rules.

Optimization mode can be changed with [options](https://ajv.js.org/api.html#options):

*   `{code: {optimize: false}}` - to disable (e.g., when schema compilation time is more important),
*   `{code: {optimize: 2}}` - 2-pass optimization.

[#](https://ajv.js.org/codegen.html#user-defined-keywords) User-defined keywords
--------------------------------------------------------------------------------

While tagged template literals wrap passed strings based on their run-time values, CodeGen class methods rely on types to ensure safety of passed parameters - there is no run-time checks that the passed value is an instance of _Code class.

It is strongly recommended to define additional keywords only with Typescript - using plain JavaScript would still allow passing unsafe strings to code generation methods.

Optimization and side-effects

If your user-defined keywords need to have side-effects that are removed by optimization (see above), you may need to disable it.

[Edit this page](https://github.com/ajv-validator/ajv/edit/master/docs/codegen.md)(opens new window)

← [Contributing guide](https://ajv.js.org/contributing/)[Code components](https://ajv.js.org/components.html) →
