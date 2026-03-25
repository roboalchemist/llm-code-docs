# Source: https://redocly.com/docs/cli/rules/oas/path-parameters-defined.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/path-parameters-defined.md

# path-parameters-defined

Requires all path template variables are defined as path parameters.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

You declared them?
Now define them.
This rule verifies the path parameters are defined.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `error` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  path-parameters-defined: error
```

## Examples

Given this configuration:


```yaml
rules:
  path-parameters-defined: error
```

Example of an **incorrect** path:


```yaml
paths:
  /customers/{id}:
    post:
      parameters:
        - name: filter
          in: query
```

Example of a **correct** path:


```yaml
paths:
  /customers/{id}:
    post:
      parameters:
        - name: id
          in: path
          required: true
          description: The customer's ID.
```

## Related rules

- [path-declaration-must-exist](/docs/cli/v1/rules/oas/path-declaration-must-exist)
- [path-excludes-patterns](/docs/cli/v1/rules/oas/path-excludes-patterns)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/path-params-defined.ts)
- [Paths docs](https://redocly.com/docs/openapi-visual-reference/paths/)