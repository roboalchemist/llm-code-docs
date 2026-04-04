# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-details-tabs.md

# issueDetailsTabs

Tabs available in the issue details view.

### Examples

```graphql
type IssueDetailsTabs {
  id: String
  label: String
  featureFlag: String
}
```

### Fields

| Field                | Description                                        | Supported fields |
| -------------------- | -------------------------------------------------- | ---------------- |
| id `String`          | Unique identifier for the tab                      |                  |
| label `String`       | Label to be displayed for the tab                  |                  |
| featureFlag `String` | Feature flag controlling the visibility of the tab |                  |

### References

#### Fields with this object

* [{} Issue.issueDetailsHeaders](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
