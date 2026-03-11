# Source: https://redocly.com/docs/cli/rules/oas/no-unresolved-refs.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/no-unresolved-refs.md

# no-unresolved-refs

Ensures that all `$ref` instances in your API descriptions are resolved.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

The `$ref` (reference object) is useful for keeping your OpenAPI descriptions DRY (don't repeat yourself).
But if you make a typo, your `$ref` might not be resolvable.
This rule prevents that from happening.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `error` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  no-unresolved-refs: error
```

## Examples

Given this configuration:


```yaml
rules:
  no-unresolved-refs: error
```

Example of an **incorrect** `$ref`:


```yaml
components:
  schemas:
    Car:
      type: object
      properties:
        color:
          type: string
        tires:
          $ref: '#/components/schemas/Tires'
    Tire:
      type: object
      properties:
        name:
          type: string
        size:
          type: string
```

Example of a **correct** `$ref`:


```yaml
components:
  schemas:
    Car:
      type: object
      properties:
        color:
          type: string
        tires:
          $ref: '#/components/schemas/Tire'
    Tire:
      type: object
      properties:
        name:
          type: string
        size:
          type: string
```

## Related rules

- [spec](/docs/cli/v1/rules/oas/struct)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)
- [no-unused-components](/docs/cli/v1/rules/oas/no-unused-components)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/no-unresolved-refs.ts)
- Read our guide on [how to use JSON references ($refs)](https://redocly.com/docs/resources/ref-guide)