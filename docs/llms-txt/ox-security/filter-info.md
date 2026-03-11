# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-info.md

# filterInfo

Filter information with counts, percentages, and additional metadata.

### Examples

```graphql
type FilterInfo {
  id: String
  filterId: String
  label: String
  count: Int
  percent: Int
  changeNumber: Float
  policyId: String
  extraInfo: [FilterExtraInfo]
}
```

### Fields

| Field                                                                                                                                      | Description                                           | Supported fields                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------- |
| id `String`                                                                                                                                | Filter identifier                                     |                                                             |
| filterId `String`                                                                                                                          | Internal filter identifier                            |                                                             |
| label `String`                                                                                                                             | Human-readable filter label                           |                                                             |
| count `Int`                                                                                                                                | Number of items matching this filter                  |                                                             |
| percent `Int`                                                                                                                              | Percentage of total items matching this filter        |                                                             |
| changeNumber `Float`                                                                                                                       | Change in count compared to previous period           |                                                             |
| policyId `String`                                                                                                                          | Policy identifier associated with this filter         |                                                             |
| extraInfo [`[FilterExtraInfo]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-extra-info) | Additional information array for extended filter data | <p>key <code>String</code><br>value <code>String</code></p> |

### References

#### Fields with this object

* [{} FilterLazy.items](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy)
