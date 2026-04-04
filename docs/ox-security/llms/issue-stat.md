# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issue-stat.md

# issueStat

Describes statistical information about a specific category of issues.

### Examples

```graphql
type IssueStat {
  name: String
  total: Int
}
```

### Fields

| Field         | Description                            | Supported fields |
| ------------- | -------------------------------------- | ---------------- |
| name `String` | Name of the category or tool           |                  |
| total `Int`   | Total count of issues in this category |                  |

### References

#### Fields with this object

* [{} IssuesStats.sourceTools](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issues-stats)
* [{} IssuesStats.categories](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issues-stats)
* [{} IssuesStats.severities](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issues-stats)
