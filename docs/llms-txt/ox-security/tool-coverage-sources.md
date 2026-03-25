# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/tool-coverage-sources.md

# toolCoverageSources

Represents a source contributing to tool coverage for an application.

### Examples

```graphql
type ToolCoverageSources {
  match: String
  type: String
}
```

### Fields

| Field          | Description                                                     | Supported fields |
| -------------- | --------------------------------------------------------------- | ---------------- |
| match `String` | The specific match or identifier related to the coverage source |                  |
| type `String`  | The type of source                                              |                  |

### References

#### Fields with this object

* [{} AppToolCoverage.sources](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-tool-coverage)
