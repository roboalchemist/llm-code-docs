# Source: https://redocly.com/docs/cli/rules/oas/operation-parameters-unique.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/operation-parameters-unique.md

# operation-parameters-unique

Verifies parameters are unique for any given operation.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

Identical twins are the topic of social research.
And some interesting studies have been published over the years that used identical twins in their studies.
Identical parameters, on the other hand, are a design mistake.
Solve it before you ship it.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `error` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  operation-parameters-unique: error
```

## Examples

Given this configuration:


```yaml
rules:
  operation-parameters-unique: error
```

Example of an **incorrect** operation:


```yaml
paths:
  /cars:
    get:
      parameters:
        - name: filter
          in: query
        - name: filter
          in: query
```

Example of a **correct** operation:


```yaml
paths:
  /cars:
    get:
      parameters:
        - name: filter
          in: query
        - name: another-filter
          in: query
```

## Related rules

- [path-parameters-defined](/docs/cli/v1/rules/oas/path-parameters-defined)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/operation-parameters-unique.ts)
- [Operation object docs](https://redocly.com/docs/openapi-visual-reference/operation/)
- [Parameter object docs](https://redocly.com/docs/openapi-visual-reference/parameter/)