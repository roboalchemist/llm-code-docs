# Source: https://redocly.com/docs/cli/rules/oas/operation-tag-defined.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/operation-tag-defined.md

# operation-tag-defined

Disallows use of tags in operations that aren't globally defined.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |


## API design principles

OpenAPI tags can be used for different purposes.
Tags are declared in the root of the OpenAPI description.
Then, they are used in operations. They are recommmended for grouping common operations within your api description.

This rule first checks if a tag exists on the operation. Subsequently, if an operation uses a tag, it must be defined in the root `tags` declaration.
This rule helps prevent typos and tag explosion.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `off` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  operation-tag-defined: error
```

## Examples

Given this configuration:


```yaml
rules:
  operation-tag-defined: error
```

Example of **incorrect** operation:


```yaml
tags:
  - name: Anchovy
paths:
  /customers:
    post:
      tags:
        - Customers
      operationId: # ...
```

Example of **correct** operation:


```yaml
tags:
  - name: Anchovy
  - name: Customers
paths:
  /customers:
    post:
      tags:
        - Customers
      operationId: # ...
```

## Related rules

- [operation-singular-tag](/docs/cli/v1/rules/oas/operation-singular-tag)
- [tags-alphabetical](/docs/cli/v1/rules/oas/tags-alphabetical)
- [tag-description](/docs/cli/v1/rules/oas/tag-description)
- [configurable rules](/docs/cli/v1/rules/configurable-rules)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/operation-tag-defined.ts)
- [Operation object docs](https://redocly.com/docs/openapi-visual-reference/operation/)
- [Tags docs](https://redocly.com/docs/openapi-visual-reference/tags/)