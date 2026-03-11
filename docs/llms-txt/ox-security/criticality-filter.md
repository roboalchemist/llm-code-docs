# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/criticality-filter.md

# criticalityFilter

### Examples

```graphql
enum CriticalityFilter {
  Info
  Low
  Medium
  High
  Critical
  Appoxalypse
}
```

### Enum values

| Enum value  | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| Info        | Informational issues with minimal security impact            |
| Low         | Low-risk issues requiring attention but not immediate action |
| Medium      | Moderate-risk issues that should be addressed                |
| High        | High-risk issues requiring prompt attention                  |
| Critical    | Critical issues demanding immediate attention                |
| Appoxalypse | Highest severity issues with potential catastrophic impact   |

### References

#### Fields with this object

* [{} IssueFilters.criticality](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issue-filters)
* [{} CICDIssueFilters.criticality](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issue-filters)
