# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/cicd-issue-status.md

# cicdIssueStatus

Status of an issue in the CI/CD pipeline.

### Examples

```graphql
enum CICDIssueStatus {
  New
  Old
}
```

### Enum values

| Enum value | Description                                            |
| ---------- | ------------------------------------------------------ |
| New        | Issue was first discovered in the current pipeline run |
| Old        | Issue existed in previous pipeline runs                |

### References

#### Fields with this object

* [{} CICDFields.issueStatus](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/cicd-fields)
