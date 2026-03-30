# Source: https://redocly.com/docs/cli/rules/oas/required-string-property-missing-min-length.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/required-string-property-missing-min-length.md

# required-string-property-missing-min-length

Requires that every required property in the API description with type `string` has a `minLength`.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

The `minLength` keyword constrains string values. When a property of type `string` is `required`, defining the `minLength` helps prevent common mistakes, such as empty strings. Use the `minLength` property as a best practice to ensure data integrity and enhances the overall quality of the API.

## Configuration

To configure the rule, add it to the `rules` object in your configuration file.
Set the desired [severity](/docs/cli/v1/rules#severity-settings) for the rule.


```yaml
rules:
  required-string-property-missing-min-length:
    severity: error
```

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  required-string-property-missing-min-length: error
```

## Examples

Given this configuration:


```yaml
rules:
  required-string-property-missing-min-length: error
```

Example of an **incorrect** schema:


```yaml
schemas:
  User:
    type: object
    required:
        - name
    properties:
      name:
        description: User name
        type: string
```

Example of a **correct** schema:


```yaml
schemas:
  User:
    type: object
    required:
        - name
    properties:
      name:
        description: User name
        type: string
        minLength: 2
```

## Related rules

- [no-invalid-schema-examples](/docs/cli/v1/rules/oas/no-invalid-schema-examples)
- [response-contains-property](/docs/cli/v1/rules/oas/response-contains-property)
- [Custom rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/required-string-property-missing-min-length.ts)
- [Schema docs](https://redocly.com/docs/openapi-visual-reference/schemas/)