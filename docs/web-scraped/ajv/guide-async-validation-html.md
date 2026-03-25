# Source: https://ajv.js.org/guide/async-validation.html

Title: Ajv JSON schema validator

URL Source: https://ajv.js.org/guide/async-validation.html

Published Time: Sat, 14 Feb 2026 15:27:26 GMT

Markdown Content:
Asynchronous validation | Ajv JSON schema validator
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

    *   [Why use AJV](https://ajv.js.org/guide/why-ajv.html)
    *   [Getting started](https://ajv.js.org/guide/getting-started.html)
    *   [Using with TypeScript](https://ajv.js.org/guide/typescript.html)
    *   [Choosing schema language](https://ajv.js.org/guide/schema-language.html)
    *   [Managing schemas](https://ajv.js.org/guide/managing-schemas.html)
    *   [Combining schemas](https://ajv.js.org/guide/combining-schemas.html)
    *   [Format validation](https://ajv.js.org/guide/formats.html)
    *   [Modifying data during validation](https://ajv.js.org/guide/modifying-data.html)
    *   [User-defined keywords](https://ajv.js.org/guide/user-keywords.html)
    *   [Asynchronous validation](https://ajv.js.org/guide/async-validation.html)

    *   [Execution environments](https://ajv.js.org/guide/environments.html)

*   Reference

*   Extending Ajv

*   Contributors

*   Information

[#](https://ajv.js.org/guide/async-validation.html#asynchronous-validation) Asynchronous validation
===================================================================================================

You can define formats and keywords that perform validation asynchronously by accessing database or some other service. You should add `async: true` in the keyword or format definition (see [addFormat](https://ajv.js.org/guide/api.html#api-addformat), [addKeyword](https://ajv.js.org/guide/api.html#api-addkeyword) and [User-defined keywords](https://ajv.js.org/guide/keywords.html)).

If your schema uses asynchronous formats/keywords or refers to some schema that contains them it should have `"$async": true` keyword so that Ajv can compile it correctly. If asynchronous format/keyword or reference to asynchronous schema is used in the schema without `$async` keyword Ajv will throw an exception during schema compilation.

Use $async: true in referenced schemas

All asynchronous subschemas that are referenced from the current or other schemas should have `"$async": true` keyword as well, otherwise the schema compilation will fail.

Validation function for an asynchronous format/keyword should return a promise that resolves with `true` or `false` (or rejects with `new Ajv.ValidationError(errors)` if you want to return errors from the keyword function).

Ajv compiles asynchronous schemas to [async functions(opens new window)](http://tc39.github.io/ecmascript-asyncawait/). Async functions are supported in Node.js 7+ and all modern browsers. You can supply a transpiler as a function via `processCode` option. See [Options](https://ajv.js.org/guide/api.html#options).

The compiled validation function has `$async: true` property (if the schema is asynchronous), so you can differentiate these functions if you are using both synchronous and asynchronous schemas.

Validation result will be a promise that resolves with validated data or rejects with an exception `Ajv.ValidationError` that contains the array of validation errors in `errors` property.

Example:

```
const ajv = new Ajv()

ajv.addKeyword({
  keyword: "idExists",
  async: true,
  type: "number",
  validate: checkIdExists,
})

async function checkIdExists(schema, data) {
  // this is just an example, you would want to avoid SQL injection in your code
  const rows = await sql(`SELECT id FROM ${schema.table} WHERE id = ${data}`)
  return !!rows.length // true if record is found
}

const schema = {
  $async: true,
  properties: {
    userId: {
      type: "integer",
      idExists: {table: "users"},
    },
    postId: {
      type: "integer",
      idExists: {table: "posts"},
    },
  },
}

const validate = ajv.compile(schema)

validate({userId: 1, postId: 19})
  .then(function (data) {
    console.log("Data is valid", data) // { userId: 1, postId: 19 }
  })
  .catch(function (err) {
    if (!(err instanceof Ajv.ValidationError)) throw err
    // data is invalid
    console.log("Validation errors:", err.errors)
  })
```

### [#](https://ajv.js.org/guide/async-validation.html#using-transpilers) Using transpilers

```
const ajv = new Ajv({processCode: transpileFunc})
const validate = ajv.compile(schema) // transpiled es7 async function
validate(data).then(successFunc).catch(errorFunc)
```

See [Options](https://ajv.js.org/options).

[Edit this page](https://github.com/ajv-validator/ajv/edit/master/docs/guide/async-validation.md)(opens new window)

← [User-defined keywords](https://ajv.js.org/guide/user-keywords.html)[Execution environments](https://ajv.js.org/guide/environments.html) →
