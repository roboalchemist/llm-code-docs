# Source: https://redocly.com/docs/cli/rules/oas/spec-no-invalid-encoding-combinations.md

# spec-no-invalid-encoding-combinations

Ensures that MediaType objects have valid combinations of encoding fields according to the OpenAPI 3.2.0 specification.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |
| 3.2 | â |



```mermaid
flowchart TD

Root ==> Paths --> PathItem --> Operation --> Parameter --> MediaType
PathItem --> Parameter
Operation --> RequestBody --> MediaType
Operation --> Responses --> MediaType

style MediaType fill:#codaf9,stroke:#0044d4,stroke-width:5px
```

## API design principles

According to the [OpenAPI 3.2.0 specification](https://spec.openapis.org/oas/v3.2.0.html#fixed-fields-11), MediaType objects have strict rules about which encoding fields can be used together.
This rule ensures that only valid encoding field combinations are used in MediaType objects.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `error` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  spec-no-invalid-encoding-combinations: error
```

## Examples

Given this configuration:


```yaml
rules:
  spec-no-invalid-encoding-combinations: error
```

Example of **incorrect** MediaType objects:


```yaml
requestBody:
  content:
    'multipart/form-data':
      schema:
        type: object
        properties:
          id:
            type: integer
      encoding:
        id:
          style: form
      prefixEncoding:
        - style: form
    'application/x-www-form-urlencoded':
      schema:
        type: object
        properties:
          name:
            type: string
      encoding:
        name:
          style: form
      itemEncoding:
        style: form
```

Example of **correct** MediaType objects:


```yaml
requestBody:
  content:
    'multipart/form-data':
      schema:
        type: object
        properties:
          id:
            type: integer
      encoding:
        id:
          style: form
    'multipart/form-data-positional':
      schema:
        type: object
        properties:
          items:
            type: array
      prefixEncoding:
        - style: form
      itemEncoding:
        style: form
```

## Related rules

- [struct](/docs/cli/rules/common/struct)
- [spec-example-values](/docs/cli/rules/oas/spec-example-values)
- [spec-discriminator-defaultMapping](/docs/cli/rules/oas/spec-discriminator-defaultMapping)
- [spec-no-invalid-tag-parents](/docs/cli/rules/oas/spec-no-invalid-tag-parents)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/oas3/spec-no-invalid-encoding-combinations.ts)
- [MediaType object docs](https://redocly.com/docs/openapi-visual-reference/media-type/)