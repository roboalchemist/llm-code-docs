# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-tool-coverage.md

# appToolCoverage

Represents coverage information for a security tool in an application.

### Examples

```graphql
type AppToolCoverage {
  toolName: String
  oxDelivered: Boolean
  coverage: Boolean
  type: String
  sources: [ToolCoverageSources]
}
```

### Fields

| Field                                                                                                                                            | Description                                                 | Supported fields                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------ |
| toolName `String`                                                                                                                                | The name of the security tool                               |                                                              |
| oxDelivered `Boolean`                                                                                                                            | Indicates whether the tool is delivered by Ox               |                                                              |
| coverage `Boolean`                                                                                                                               | Indicates whether the tool has coverage for the application |                                                              |
| type `String`                                                                                                                                    | The type of tool coverage                                   |                                                              |
| sources [`[ToolCoverageSources]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/tool-coverage-sources) | The sources that contributed to the tool's coverage         | <p>match <code>String</code><br>type <code>String</code></p> |

### References

#### Fields with this object

* [{} Application.toolsCoverage](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
