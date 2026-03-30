# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/applications-filter.md

# applicationsFilter

Filters for classifying applications based on their deployment and development status.

### Examples

```graphql
enum ApplicationsFilter {
  New
  InDevelopment
  DeployedProd
  ExternallyFacing
  Relevant
  Irrelevant
}
```

### Enum values

| Enum value       | Description                                             |
| ---------------- | ------------------------------------------------------- |
| New              | Recently added applications                             |
| InDevelopment    | Applications currently under development                |
| DeployedProd     | Applications deployed to production environments        |
| ExternallyFacing | Applications exposed to external networks or users      |
| Relevant         | Applications marked as relevant for security scanning   |
| Irrelevant       | Applications marked as irrelevant for security scanning |

### References

#### Fields with this object

* [{} GetApplicationsInput.applicationFilters](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
