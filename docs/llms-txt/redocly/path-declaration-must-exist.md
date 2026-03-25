# Source: https://redocly.com/docs/cli/rules/oas/path-declaration-must-exist.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/path-declaration-must-exist.md

# path-declaration-must-exist

Requires definition of all path template variables.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

The path template variables must have a string.
This rule is for spec correctness.
This rule is not opinionated.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `error` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  path-declaration-must-exist: error
```

## Examples

Given this configuration:


```yaml
rules:
  path-declaration-must-exist: error
```

Example of an **incorrect** path:


```yaml
paths:
  /customers/{}:
    post:
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

- [path-parameters-defined](/docs/cli/v1/rules/oas/path-parameters-defined)
- [path-excludes-patterns](/docs/cli/v1/rules/oas/path-excludes-patterns)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/path-declaration-must-exist.ts)
- [Parameter docs](https://redocly.com/docs/openapi-visual-reference/parameter/)
- [Paths docs](https://redocly.com/docs/openapi-visual-reference/paths/)