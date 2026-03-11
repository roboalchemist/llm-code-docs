# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/fix-applied-deatils.md

# fixAppliedDeatils

Details about who applied a fix and when.

### Examples

```graphql
type FixAppliedDeatils {
  appliedBy: String
  appliedDate: Date
}
```

### Fields

| Field              | Description                          | Supported fields |
| ------------------ | ------------------------------------ | ---------------- |
| appliedBy `String` | Name of the user who applied the fix |                  |
| appliedDate `Date` | Date when the fix was applied        |                  |

### References

#### Fields with this object

* [{} Issue.fixAppliedDeatils](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
