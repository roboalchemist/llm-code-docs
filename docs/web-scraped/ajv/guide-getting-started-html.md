# Source: https://ajv.js.org/guide/getting-started.html

Title: Ajv JSON schema validator

URL Source: https://ajv.js.org/guide/getting-started.html

Markdown Content:
[#](https://ajv.js.org/guide/getting-started.html#getting-started) Getting started
----------------------------------------------------------------------------------

*   [Install](https://ajv.js.org/guide/getting-started.html#install)
*   [Basic data validation](https://ajv.js.org/guide/getting-started.html#basic-data-validation)
*   [Parsing and serializing JSON New](https://ajv.js.org/guide/getting-started.html#parsing-and-serializing-json)

[#](https://ajv.js.org/guide/getting-started.html#install) Install
------------------------------------------------------------------

To install Ajv version 8:

If you need to use Ajv with [JSON Schema draft-04](https://ajv.js.org/guide/schema-language#draft-04), you need to install Ajv version 6:

See [Contributing](https://ajv.js.org/CONTRIBUTING.html) on how to run the tests locally

[#](https://ajv.js.org/guide/getting-started.html#basic-data-validation) Basic data validation
----------------------------------------------------------------------------------------------

Ajv takes a schema for your JSON data and converts it into a very efficient JavaScript code that validates your data according to the schema. To create a schema you can use either [JSON Schema](https://ajv.js.org/json-schema) or [JSON Type Definition](https://ajv.js.org/json-type-definition) - check out [Choosing schema language](https://ajv.js.org/guide/schema-language), they have different advantages and disadvantages.

For example, to validate an object that has a required property "foo" (an integer number), an optional property "bar" (a string) and no other properties:

Ajv compiles schemas to functions and caches them in all cases (using the schema itself as a key in a Map), so that the next time the same schema object is used it won't be compiled again.

Best performance: compile and getSchema methods

The best performance is achieved when using compiled functions returned by `compile` or `getSchema` methods.

While execution of the compiled validation function is very fast, its compilation is relatively slow, so you need to make sure that you compile schemas only once and re-use compiled validation functions. See [Managing multiple schemas](https://ajv.js.org/guide/managing-schemas).

Save errors property

Every time a validation function (or `ajv.validate`) is called the `errors` property is overwritten. You need to copy the `errors` array reference to another variable if you want to use it later (e.g. in the callback). See [Validation errors](https://ajv.js.org/api.html#validation-errors).

[#](https://ajv.js.org/guide/getting-started.html#parsing-and-serializing-json) Parsing and serializing JSON New
----------------------------------------------------------------------------------------------------------------

Ajv can compile efficient parsers and serializers from [JSON Type Definition](https://ajv.js.org/json-type-definition) schemas.

Serializing the data with a function specialized to your data shape can be more than 10x compared with `JSON.stringify`.

Parsing the data replaces the need for separate validation after generic parsing with `JSON.parse` (although validation itself is usually much faster than parsing). In case your JSON string is valid, the specialized parsing is approximately as fast as JSON.parse, but in case your JSON is invalid, the specialized parsing would fail much faster - so it can be very efficient in some scenarios.

For the same data structure, you can compile parser and serializer in this way:

Lower parsing performance of empty schemas

You would have smaller performance benefits in case your schema contains some properties or other parts that are empty schemas (`{}`) - parser would call `JSON.parse` in this case.

JTD discriminator schema

The performance of parsing discriminator schemas depends on the position of discriminator tag in the schema - the best parsing performance will be achieved if the tag is the first property - this is how compiled JTD serializers generate JSON in case of discriminator schemas.

Also, if discriminator tag were to be repeated in JSON, the second value would be ignored and the object still validated according to the first tag.

Compiled parsers do NOT throw exceptions

Compiled parsers, unlike JSON.parse, do not throw the exception in case JSON string is not a valid JSON or in case data is invalid according to the schema. As soon as the parser determines that either JSON or data is invalid, it returns `undefined` and reports error and position via parsers properties `message` and `position`.
