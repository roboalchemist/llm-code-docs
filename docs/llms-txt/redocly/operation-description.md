# Source: https://redocly.com/docs/cli/rules/oas/operation-description.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/operation-description.md

# operation-description

Requires the `description` field for every operation in your API.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

Every operation should have a description to help your API consumers understand what it does and how to use it.
Without a description, people who want to use your API have to guess what an operation does, or try to decipher it from other parts of your API description, or from other documentation and external resources that may not be accurate. Your API description should be the single source of truth about your API.
Add the description field and delight both your (future) teammates and your API consumers.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  operation-description: error
```

## Examples

Given this configuration:


```yaml
rules:
  operation-description: error
```

Example of an **incorrect** operation:


```yaml
get:
  responses:
    '200':
      $ref: ../components/responses/Success.yaml
```

Example of a **correct** operation:


```yaml
get:
  description: Returns the latest updated user profile.
  responses:
    '200':
      $ref: ../components/responses/Success.yaml
```

## Related rules

- [tag-description](/docs/cli/v1/rules/oas/tag-description)
- [parameter-description](/docs/cli/v1/rules/oas/parameter-description)
- [operation-summary](/docs/cli/v1/rules/oas/operation-summary)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)
- [operation-operationId](/docs/cli/v1/rules/oas/operation-operationId)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/operation-description.ts)
- Consider using [configurable rules](/docs/cli/v1/rules/configurable-rules) for more specific rules for operation descriptions such as minimum length and pattern enforcement.
- [Operation object docs](https://redocly.com/docs/openapi-visual-reference/operation/)