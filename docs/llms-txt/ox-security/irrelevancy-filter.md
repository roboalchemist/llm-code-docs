# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/irrelevancy-filter.md

# irrelevancyFilter

Reasons for marking applications as irrelevant for security scanning.

### Examples

```graphql
enum IrrelevancyFilter {
  Archived
  FailedClone
  NoFiles
  LastCodeChange
  NoCodeChanges
  SetByClient
}
```

### Enum values

| Enum value     | Description                          |
| -------------- | ------------------------------------ |
| Archived       | Repository has been archived         |
| FailedClone    | Failed to clone the repository       |
| NoFiles        | Repository contains no files         |
| LastCodeChange | No recent code changes detected      |
| NoCodeChanges  | No code changes recorded             |
| SetByClient    | Manually set as irrelevant by client |

### References

#### Fields with this object

* [{} GetApplicationsInput.irrelevancyFilters](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
