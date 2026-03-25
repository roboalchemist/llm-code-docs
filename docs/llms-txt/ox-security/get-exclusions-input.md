# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/get-exclusions-input.md

# getExclusionsInput

Input for getting exclusions with pagination and filters.

### Examples

```graphql
input GetExclusionsInput {
  filters: ExclusionsFilters
  limit: Float
  offset: Float
  search: String
}
```

### Fields

| Field                                                                                                                                   | Description                                                                  | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filters [`ExclusionsFilters`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclusions-filters) | Filters to apply to the query                                                | <p>appName <code>\[String!]</code><br>exclusionId <code>\[String!]</code><br>exclusionType <a href="../enums/exclusion-type"><code>\[ExclusionType!]</code></a><br>exclusionMode <a href="../enums/exclusion-mode"><code>\[ExclusionMode!]</code></a><br>policyName <code>\[String!]</code><br>modifiedBy <code>\[String!]</code><br>issueName <code>\[String!]</code><br>status <code>\[String!]</code><br>expiredAt <a href="expired-at-filter"><code>ExpiredAtFilter</code></a></p> |
| limit `Float`                                                                                                                           | Maximum number of results to return, must be between 1 and 500, default: 100 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| offset `Float`                                                                                                                          | Number of results to skip, must be greater than or equal to 0, default: 0    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| search `String`                                                                                                                         | Search by issue name or application name                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### References

#### Queries using this object

* [\<?> getExclusions.getExclusionsInput](https://docs.ox.security/api-documentation/api-reference/api--exclusions/queries/get-exclusions)
