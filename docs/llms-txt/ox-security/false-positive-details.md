# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/false-positive-details.md

# falsePositiveDetails

Additional details for false positives on issue level.

### Examples

```graphql
type FalsePositiveDetails {
  canceledBy: String
  reportedBy: String
  commentWhenCanceled: String
  aggregationsStatus: String
}
```

### Fields

| Field                        | Description                                                                                                                      | Supported fields |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| canceledBy `String`          | User email who canceled the false positive                                                                                       |                  |
| reportedBy `String`          | User email who reported the false positive                                                                                       |                  |
| commentWhenCanceled `String` | Comment at the time when the false positive was canceled                                                                         |                  |
| aggregationsStatus `String`  | The enum of values to describe different scenarios like full or part of aggregations listed as false positive, for display in UI |                  |

### References

#### Fields with this object

* [{} Issue.falsePositiveDetails](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
