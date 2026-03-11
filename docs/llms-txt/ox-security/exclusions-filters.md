# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclusions-filters.md

# exclusionsFilters

Filters for querying exclusions.

### Examples

```graphql
input ExclusionsFilters {
  appName: [String!]
  exclusionId: [String!]
  exclusionType: [ExclusionType!]
  exclusionMode: [ExclusionMode!]
  policyName: [String!]
  modifiedBy: [String!]
  issueName: [String!]
  status: [String!]
  expiredAt: ExpiredAtFilter
}
```

### Fields

| Field                                                                                                                                   | Description                                 | Supported fields                                              |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------- |
| appName `[String!]`                                                                                                                     | Filter by application names                 |                                                               |
| exclusionId `[String!]`                                                                                                                 | Filter by exclusion IDs                     |                                                               |
| exclusionType [`[ExclusionType!]`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-type) | Filter by exclusion types                   |                                                               |
| exclusionMode [`[ExclusionMode!]`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-mode) | Filter by exclusion modes                   |                                                               |
| policyName `[String!]`                                                                                                                  | Filter by policy names                      |                                                               |
| modifiedBy `[String!]`                                                                                                                  | Filter by users who modified the exclusions |                                                               |
| issueName `[String!]`                                                                                                                   | Filter by issue names                       |                                                               |
| status `[String!]`                                                                                                                      | Filter by exclusion status                  |                                                               |
| expiredAt [`ExpiredAtFilter`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/expired-at-filter)  | Filter by expiration date range             | <p>gte <code>DateTime</code><br>lte <code>DateTime</code></p> |

### References

#### Fields with this object

* [{} GetExclusionsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/get-exclusions-input)
