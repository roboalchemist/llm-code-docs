# Source: https://redocly.com/docs/cli/rules/oas/scalar-property-missing-example.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/scalar-property-missing-example.md

# scalar-property-missing-example

Requires that every scalar property in the API description has either `example` or `examples`Ë defined.
Scalar properties are any of the following types: `string`, `number`, `null`, `boolean`, `integer`.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

One of the main goals of your API description (and your API documentation) is to help consumers understand how your API behaves and what to expect when working with it.

Providing examples for properties in your API description not only improves the developer and user experience of working with your APIs, but also makes the documentation more complete. Many API documentation tools are able to automatically extract such example values from the API description, and let consumers use those values to test the APIs or send (mock) requests to the API directly from the documentation.

## Configuration

To configure the rule, add it to the `rules` object in your configuration file.
Set the desired [severity](/docs/cli/v1/rules#severity-settings) for the rule.


```yaml
rules:
  scalar-property-missing-example:
    severity: error
```

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  scalar-property-missing-example: error
```

## Examples

Given this configuration:


```yaml
rules:
  scalar-property-missing-example: error
```

Example of an **incorrect** schema:


```yaml
schemas:
  User:
    type: object
    properties:
      email:
        description: User email address
        type: string
        format: email
```

Example of a **correct** schema:


```yaml
schemas:
  User:
    type: object
    properties:
      email:
        description: User email address
        type: string
        format: email
        example: john.smith@example.com
```

## Related rules

- [no-invalid-media-type-examples](/docs/cli/v1/rules/oas/no-invalid-media-type-examples)
- [no-invalid-parameter-examples](/docs/cli/v1/rules/oas/no-invalid-parameter-examples)
- [no-invalid-schema-examples](/docs/cli/v1/rules/oas/no-invalid-schema-examples)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/scalar-property-missing-example.ts)
- [Schema docs](https://redocly.com/docs/openapi-visual-reference/schemas/)