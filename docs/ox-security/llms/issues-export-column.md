# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-export-column.md

# issuesExportColumn

Input for the columns in the issues export.

### Examples

```graphql
input IssuesExportColumn {
  key: IssuesExportColumnKeys
  name: String
}
```

### Fields

| Field                                                                                                                                     | Description                          | Supported fields |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------- |
| key [`IssuesExportColumnKeys`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issues-export-column-keys) | Key of the column for issues export  |                  |
| name `String`                                                                                                                             | Name of the column for issues export |                  |

### References

#### Fields with this object

* [{} IssuesExportOptions.columns](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-export-options)
