# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-relevance.md

# exclusionRelevance

Relevance status of an exclusion.

### Examples

```graphql
enum ExclusionRelevance {
  Irrelevant
  Relevant
  Default
}
```

### Enum values

| Enum value | Description                     |
| ---------- | ------------------------------- |
| Irrelevant | Exclusion is no longer relevant |
| Relevant   | Exclusion is currently relevant |
| Default    | Default relevance status        |

### References

#### Fields with this object

* [{} RemoveAppsExclusionInput.relevance](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/remove-apps-exclusion-input)
