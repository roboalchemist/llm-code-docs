# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/fix-issue.md

# fixIssue

Details about a fix available for an issue, including status and metadata.

### Examples

```graphql
type FixIssue {
  fixType: String
  fixTitle: String
  fixDescription: String
  isFixApplied: Boolean
  fixAppliedBy: String
  sourceControlType: String
  fixDate: Date
}
```

### Fields

| Field                      | Description                                         | Supported fields |
| -------------------------- | --------------------------------------------------- | ---------------- |
| fixType `String`           | Type of fix available for the issue                 |                  |
| fixTitle `String`          | Title of the fix, shown in the user interface       |                  |
| fixDescription `String`    | Description of the fix, shown in the user interface |                  |
| isFixApplied `Boolean`     | Indicates whether the fix has been applied          |                  |
| fixAppliedBy `String`      | User or system who applied the fix                  |                  |
| sourceControlType `String` | Source control type used for the fix                |                  |
| fixDate `Date`             | Date when the fix was applied                       |                  |

### References

#### Fields with this object

* [{} Issue.fixIssue](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
* [{} Issue.autoFix](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
