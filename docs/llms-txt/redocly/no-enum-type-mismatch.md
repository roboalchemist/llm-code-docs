# Source: https://redocly.com/docs/cli/rules/common/no-enum-type-mismatch.md

# Source: https://redocly.com/docs/cli/v1/rules/oas/no-enum-type-mismatch.md

# no-enum-type-mismatch

Requires that the contents of every `enum` value in your API description conform to the corresponding schema's specified `type`.

| OAS | Compatibility |
|  --- | --- |
| 2.0 | â |
| 3.0 | â |
| 3.1 | â |



```mermaid
flowchart TD

Root ==> Paths --> PathItem --> Operation --> Parameter --> Schema
PathItem --> Parameter
NamedParameters --> Parameter
Operation --> RequestBody --> MediaType --> Schema
Operation --> Responses --> MediaType
NamedSchemas --> Schema
Root ==> components

subgraph components
NamedParameters
NamedSchemas
end

style Schema fill:#codaf9,stroke:#0044d4,stroke-width:5px
```

## API design principles

If a property is defined for a certain type, then its corresponding `enum` values should comply with that type.
Lack of compliance is most likely the result of a typo.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| severity | string | Possible values: `off`, `warn`, `error`. Default `error` (in `recommended` configuration). |


An example configuration:


```yaml
rules:
  no-enum-type-mismatch: error
```

## Examples

Given this configuration:


```yaml
rules:
  no-enum-type-mismatch: error
```

Example of **incorrect** enum values given the enum type:


```yaml
properties:
  huntingSkill:
    type: string
    description: The measured skill for hunting
    enum:
      - adventurous
      - 12
      - 3.14
```

Example of **correct** enum values given the enum type:


```yaml
properties:
  huntingSkill:
    type: string
    description: The measured skill for hunting
    enum:
      - adventurous
      - aggressive
      - passive
```

## Related rules

- [configurable rules](/docs/cli/v1/rules/configurable-rules)
- [no-invalid-media-type-examples](/docs/cli/v1/rules/oas/no-invalid-media-type-examples)
- [no-invalid-parameter-examples](/docs/cli/v1/rules/oas/no-invalid-parameter-examples)
- [no-invalid-schema-examples](/docs/cli/v1/rules/oas/no-invalid-schema-examples)


## Resources

- [Rule source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/rules/common/no-enum-type-mismatch.ts)
- [Enum documentation](https://redocly.com/docs/openapi-visual-reference/schemas/#enum)