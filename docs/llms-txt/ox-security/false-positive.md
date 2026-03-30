# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/false-positive.md

# falsePositive

Object containing false positive information at the aggregation level. This allows marking individual aggregations. as false positives separately from the issue-level false positive status. Each aggregation can have its own false positive status, comment, and tracking of who reported/canceled it.

### Examples

```graphql
type FalsePositive {
  isFalsePositive: Boolean
  comment: String
  reportedBy: String
  reportedAt: Date
  isCanceled: Boolean
  cancelComment: String
  canceledBy: String
  canceledAt: Date
  commentWhenCanceled: String
}
```

### Fields

| Field                        | Description                                                              | Supported fields |
| ---------------------------- | ------------------------------------------------------------------------ | ---------------- |
| isFalsePositive `Boolean`    | Whether the issue is marked as a false positive                          |                  |
| comment `String`             | Comment explaining why the issue was marked as a false positive          |                  |
| reportedBy `String`          | User who reported the issue as a false positive                          |                  |
| reportedAt `Date`            | Date when the issue was reported as a false positive                     |                  |
| isCanceled `Boolean`         | Whether the false positive report has been canceled                      |                  |
| cancelComment `String`       | Comment explaining why the false positive report was canceled            |                  |
| canceledBy `String`          | User who canceled the false positive report                              |                  |
| canceledAt `Date`            | Date when the false positive report was canceled                         |                  |
| commentWhenCanceled `String` | Previous comment at the time when the false positive report was canceled |                  |

### References

#### Fields with this object

* [{} AggItem.falsePositive](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/agg-item)
