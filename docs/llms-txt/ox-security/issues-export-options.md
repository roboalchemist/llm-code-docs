# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-export-options.md

# issuesExportOptions

Input for the options in the issues export.

### Examples

```graphql
input IssuesExportOptions {
  flattenAgg: Boolean
  isDemoEnabled: Boolean
  name: String
  columns: [IssuesExportColumn]
  rowsLimit: Int
}
```

### Fields

| Field                                                                                                                                   | Description                                                                   | Supported fields                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| flattenAgg `Boolean`                                                                                                                    | If true, aggregate data will be flattened in the export for simpler structure |                                                                                                                             |
| isDemoEnabled `Boolean`                                                                                                                 | Enables demo mode features or data if set to true                             |                                                                                                                             |
| name `String`                                                                                                                           | Name of the export                                                            |                                                                                                                             |
| columns [`[IssuesExportColumn]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-export-column) | Columns to export in the issues export                                        | <p>key <a href="../enums/issues-export-column-keys"><code>IssuesExportColumnKeys</code></a><br>name <code>String</code></p> |
| rowsLimit `Int`                                                                                                                         | Maximum number of rows to export                                              |                                                                                                                             |

### References

#### Fields with this object

* [{} IssuesInput.exportsOptions](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)
* [{} DisappearedIssuesInput.exportsOptions](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/disappeared-issues-input)
