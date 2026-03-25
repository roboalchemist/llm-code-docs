# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/aggregation-column.md

# aggregationColumn

Represents a single column in an aggregation table or report.

### Examples

```graphql
type AggregationColumn {
  header: String
  key: String
  tooltip: String
  href: String
  type: String
}
```

### Fields

| Field            | Description                                        | Supported fields |
| ---------------- | -------------------------------------------------- | ---------------- |
| header `String`  | Header text displayed for the column               |                  |
| key `String`     | Key used to identify the column data               |                  |
| tooltip `String` | Tooltip text shown on hover over the column header |                  |
| href `String`    | Optional hyperlink associated with the column      |                  |
| type `String`    | Data type of the column                            |                  |

### References

#### Fields with this object

* [{} IAggColumns.columns](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/i-agg-columns)
