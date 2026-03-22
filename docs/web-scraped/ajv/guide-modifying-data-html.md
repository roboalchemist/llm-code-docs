# Source: https://ajv.js.org/guide/modifying-data.html

Title: Ajv JSON schema validator

URL Source: https://ajv.js.org/guide/modifying-data.html

Published Time: Sat, 14 Feb 2026 15:27:26 GMT

Markdown Content:
Modifying data during validation | Ajv JSON schema validator
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
        *   [General considerations](https://ajv.js.org/guide/modifying-data.html#general-considerations)
        *   [Removing additional properties](https://ajv.js.org/guide/modifying-data.html#removing-additional-properties)
        *   [Assigning defaults](https://ajv.js.org/guide/modifying-data.html#assigning-defaults)
        *   [Coercing data types](https://ajv.js.org/guide/modifying-data.html#coercing-data-types)

    *   [User-defined keywords](https://ajv.js.org/guide/user-keywords.html)
    *   [Asynchronous validation](https://ajv.js.org/guide/async-validation.html)
    *   [Execution environments](https://ajv.js.org/guide/environments.html)

*   Reference

*   Extending Ajv

*   Contributors

*   Information

[#](https://ajv.js.org/guide/modifying-data.html#modifying-data-during-validation) Modifying data during validation
===================================================================================================================

*   [General considerations](https://ajv.js.org/guide/modifying-data.html#general-considerations)
*   [Removing additional properties](https://ajv.js.org/guide/modifying-data.html#removing-additional-properties)
*   [Assigning defaults](https://ajv.js.org/guide/modifying-data.html#assigning-defaults)
*   [Coercing data types](https://ajv.js.org/guide/modifying-data.html#coercing-data-types)

[#](https://ajv.js.org/guide/modifying-data.html#general-considerations) General considerations
-----------------------------------------------------------------------------------------------

Ajv has several options that allow to modify data during validation:

*   removeAdditional - to remove properties not defined in the schema object.
*   useDefaults - to assign defaults from the schema to the validated data properties.
*   coerceTypes - to change data type, when possible, to match the type(s) in the schema.

You can also define keywords that modify data.

NOT possible to modify root data

It is not possible to modify the root data instance passed to the validation function, only data properties can be modified. This is related to how JavaScript passes parameters, and not a limitation of Ajv.

Non-portable functionality

This functionality is non-standard - this is likely to be unsupported in other JSON Schema validator implementations.

Unexpected results when modifying data

While pure schema validation produces the results independent of the keywords and subschema order, enabling any feature that may modify the data makes validation impure and its results are likely to depend on the order of evaluation of keywords and subschemas.

The order of evaluation of subschemas in keywords like `allOf` is always the same as the order of subschemas in the array.

On another hand, the order of evaluation of keywords, while consistent between validations and not dependent on how schema object is created, is neither documented nor guaranteed, so it can change in the future major versions (and, in rare cases, it can change in minor version - e.g. when there is bug that needs to be fixed).

It is strongly recommended to always put user-defined keywords that can mutate data in separate subschemas inside `allOf` keyword to make the order of evaluation unambiguous. The exceptions to this recommendation are pre-defined `default` and `type` keywords - they must remain in the same schema as other keywords.

[#](https://ajv.js.org/guide/modifying-data.html#removing-additional-properties) Removing additional properties
---------------------------------------------------------------------------------------------------------------

With [option `removeAdditional`](https://ajv.js.org/guide/api.html#options) (added by [andyscott(opens new window)](https://github.com/andyscott)) you can filter data during the validation.

This option modifies original data.

Example:

```
const ajv = new Ajv({removeAdditional: true})
const schema = {
  additionalProperties: false,
  properties: {
    foo: {type: "number"},
    bar: {
      additionalProperties: {type: "number"},
      properties: {
        baz: {type: "string"},
      },
    },
  },
}

const data = {
  foo: 0,
  additional1: 1, // will be removed; `additionalProperties` == false
  bar: {
    baz: "abc",
    additional2: 2, // will NOT be removed; `additionalProperties` != false
  },
}

const validate = ajv.compile(schema)

console.log(validate(data)) // true
console.log(data) // { "foo": 0, "bar": { "baz": "abc", "additional2": 2 }
```

If `removeAdditional` option in the example above were `"all"` then both `additional1` and `additional2` properties would have been removed.

If the option were `"failing"` then property `additional1` would have been removed regardless of its value and property `additional2` would have been removed only if its value were failing the schema in the inner `additionalProperties` (so in the example above it would have stayed because it passes the schema, but any non-number would have been removed).

Unexpected results when using removeAdditional with anyOf/oneOf

If you use `removeAdditional` option with `additionalProperties` keyword inside `anyOf`/`oneOf` keywords your validation can fail with this schema. To make it work as you expect, you have to use discriminated union with [discriminator](https://ajv.js.org/json-schema.html#discriminator) keyword (requires `discriminator` option).

For example, with this non-discriminated union you will have unexpected results:

```
{
  type: "object",
  oneOf: [
    {
      properties: {
        foo: {type: "string"}
      },
      required: ["foo"],
      additionalProperties: false
    },
    {
      properties: {
        bar: {type: "integer"}
      },
      required: ["bar"],
      additionalProperties: false
    }
  ]
}
```

The intention of the schema above is to allow objects with either the string property "foo" or the integer property "bar", but not with both and not with any other properties.

With the option `removeAdditional: true` the validation will pass for the object `{ "foo": "abc"}` but will fail for the object `{"bar": 1}`. It happens because while the first subschema in `oneOf` is validated, the property `bar` is removed because it is an additional property according to the standard (because it is not included in `properties` keyword in the same schema).

While this behaviour is unexpected (issues [#129(opens new window)](https://github.com/ajv-validator/ajv/issues/129), [#134(opens new window)](https://github.com/ajv-validator/ajv/issues/134)), it is correct. To have the expected behaviour (both objects are allowed and additional properties are removed) the schema has to be refactored in this way:

```
{
  type: "object",
  properties: {
    foo: {type: "string"},
    bar: {type: "integer"}
  },
  additionalProperties: false,
  oneOf: [{required: ["foo"]}, {required: ["bar"]}]
}
```

The schema above is also more efficient - it will compile into a faster function.

For discriminated unions you could schemas with [discriminator](https://ajv.js.org/json-schema.html#discriminator) keyword (it requires `discriminator: true` option):

```
{
  type: "object",
  discriminator: {propertyName: "tag"},
  required: ["tag"],
  oneOf: [
    {
      properties: {
        tag: {const: "foo"},
        foo: {type: "string"}
      },
      required: ["foo"],
      additionalProperties: false
    },
    {
      properties: {
        tag: {const: "bar"},
        bar: {type: "integer"}
      },
      required: ["bar"],
      additionalProperties: false
    }
  ]
}
```

With this schema, only one subschema in `oneOf` will be evaluated, so `removeAdditional` option will work as expected.

See [discriminator](https://ajv.js.org/json-schema.html#discriminator) keyword.

[#](https://ajv.js.org/guide/modifying-data.html#assigning-defaults) Assigning defaults
---------------------------------------------------------------------------------------

With [option `useDefaults`](https://ajv.js.org/guide/options.html#options) Ajv will assign values from `default` keyword in the schemas of `properties` and `items` (when it is the array of schemas) to the missing properties and items.

With the option value `"empty"` properties and items equal to `null` or `""` (empty string) will be considered missing and assigned defaults.

This option modifies original data.

Defaults are deep-cloned

The default value is inserted in the generated validation code as a literal, so the value inserted in the data will be the deep clone of the default in the schema.

Example 1 (`default` in `properties`):

```
const ajv = new Ajv({useDefaults: true})
const schema = {
  type: "object",
  properties: {
    foo: {type: "number"},
    bar: {type: "string", default: "baz"},
  },
  required: ["foo", "bar"],
}

const data = {foo: 1}

const validate = ajv.compile(schema)

console.log(validate(data)) // true
console.log(data) // { "foo": 1, "bar": "baz" }
```

Example 2 (`default` in `items`):

```
const schema = {
  type: "array",
  items: [{type: "number"}, {type: "string", default: "foo"}],
}

const data = [1]

const validate = ajv.compile(schema)

console.log(validate(data)) // true
console.log(data) // [ 1, "foo" ]
```

With `useDefaults` option `default` keywords throws exception during schema compilation when used in:

*   not in `properties` or `items` subschemas
*   in schemas inside `anyOf`, `oneOf` and `not` (see [#42(opens new window)](https://github.com/ajv-validator/ajv/issues/42))
*   in `if` schema
*   in schemas generated by user-defined _macro_ keywords

The strict mode option can change the behaviour for these unsupported defaults (`strict: false` to ignore them, `"log"` to log a warning).

See [Strict mode](https://ajv.js.org/strict-mode.html).

Default with discriminator keyword

Defaults will be assigned in schemas inside `oneOf` in case [discriminator](https://ajv.js.org/json-schema.html#discriminator) keyword is used.

[#](https://ajv.js.org/guide/modifying-data.html#coercing-data-types) Coercing data types
-----------------------------------------------------------------------------------------

When you are validating user inputs all your data properties are usually strings. The option `coerceTypes` allows you to have your data types coerced to the types specified in your schema `type` keywords, both to pass the validation and to use the correctly typed data afterwards.

This option modifies original data.

Type coercion with scalar values

If you pass a scalar value to the validating function its type will be coerced and it will pass the validation, but the value of the variable you pass won't be updated because scalars are passed by value.

Example 1:

```
const ajv = new Ajv({coerceTypes: true})
const schema = {
  type: "object",
  properties: {
    foo: {type: "number"},
    bar: {type: "boolean"},
  },
  required: ["foo", "bar"],
}

const data = {foo: "1", bar: "false"}

const validate = ajv.compile(schema)

console.log(validate(data)) // true
console.log(data) // { "foo": 1, "bar": false }
```

Example 2 (array coercions):

```
const ajv = new Ajv({coerceTypes: "array"})
const schema = {
  properties: {
    foo: {type: "array", items: {type: "number"}},
    bar: {type: "boolean"},
  },
}

const data = {foo: "1", bar: ["false"]}

const validate = ajv.compile(schema)

console.log(validate(data)) // true
console.log(data) // { "foo": [1], "bar": false }
```

The coercion rules, as you can see from the example, are different from JavaScript both to validate user input as expected and to have the coercion reversible (to correctly validate cases where different types are defined in subschemas of "anyOf" and other compound keywords).

See [Type coercion rules](https://ajv.js.org/coercion.html) for details.

[Edit this page](https://github.com/ajv-validator/ajv/edit/master/docs/guide/modifying-data.md)(opens new window)

← [Format validation](https://ajv.js.org/guide/formats.html)[User-defined keywords](https://ajv.js.org/guide/user-keywords.html) →
