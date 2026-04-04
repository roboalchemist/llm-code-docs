# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/i-agg-columns.md

# iAggColumns

Columns configuration used in aggregation displays.

### Examples

```graphql
type IAggColumns {
  columns: [AggregationColumn]
  comment: String
}
```

### Fields

| Field                                                                                                                                 | Description                                 | Supported fields                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| columns [`[AggregationColumn]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/aggregation-column) | List of columns included in the aggregation | <p>header <code>String</code><br>key <code>String</code><br>tooltip <code>String</code><br>href <code>String</code><br>type <code>String</code></p> |
| comment `String`                                                                                                                      | Optional comment describing the columns     |                                                                                                                                                     |

### References

#### Fields with this object

* [{} IAggregations.columns](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/i-aggregations)
