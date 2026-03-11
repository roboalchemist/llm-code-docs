# Source: https://redocly.com/docs/cli/rules/oas/operation-operationId.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/operation-operationId.md

# operation-operationId

Requires each operation to have an `operationId` defined.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

The `operationId` is used by tooling to identify operations (which are otherwise done through scary looking JSON pointers).
OpenAPI does not consider `operationId` a required field, but we'd describe it as a strongly recommended field.

This rule is unopinionated.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `warn` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  operation-operationId: error
```

## Examples

Given this configuration:


```yaml
rules:
  operation-operationId: error
```

Example of an **incorrect** operation:


```yaml
paths:
  /cars:
    get:
      responses:
        '200':
          $ref: ./Success.yaml
```

Example of a **correct** operation:


```yaml
paths:
  /cars:
    get:
      operationId: GetCar
      responses:
        '200':
          $ref: ./Success.yaml
```

## Related rules

- [operation-operationId-unique](/docs/cli/v1/rules/oas/operation-operationId-unique)
- [operation-operationId-url-safe](/docs/cli/v1/rules/oas/operation-operationId-url-safe)


## Resources

- [OperationIds make good API design - Redocly Blog](https://redocly.com/blog/operationid-is-api-design/)
- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/operation-operationId.ts)
- [Operation object docs](https://redocly.com/docs/openapi-visual-reference/operation/)
- Consider using [configurable rules](/docs/cli/v1/rules/configurable-rules) for more specific rules for `operationId`s such as length, casing, and pattern enforcement.