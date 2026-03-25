# Source: https://redocly.com/docs/cli/rules/oas/parameter-description.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/parameter-description.md

# parameter-description

Ensure that every parameter has a description.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

A parameter should have a description because documentation is important.
That parameter `filter` that is self-documenting and intuitive is the same filter that you need to look into the source code to determine what kind of values to provide to it 7 months from now.
Document it!

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  parameter-description: error
```

## Examples

Given this configuration:


```yaml
rules:
  parameter-description: error
```

Example of an **incorrect** parameter:


```yaml
paths:
  /customers/{id}:
    post:
      parameters:
        - name: id
          in: path
          required: true
```

Example of a **correct** parameter:


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

- [tag-description](/docs/cli/v1/rules/oas/tag-description)
- [operation-description](/docs/cli/v1/rules/oas/operation-description)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/parameter-description.ts)
- [Parameter docs](https://redocly.com/docs/openapi-visual-reference/parameter/)