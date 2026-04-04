# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/remove-apps-exclusion-input.md

# removeAppsExclusionInput

Input for removing multiple application exclusions.

### Examples

```graphql
input RemoveAppsExclusionInput {
  relevance: ExclusionRelevance!
  exclusionIds: [String!]!
}
```

### Fields

| Field                                                                                                                                       | Description                                  | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ---------------- |
| relevance [`ExclusionRelevance!`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-relevance) | Relevance status of the exclusions to remove |                  |
| exclusionIds `[String!]!`                                                                                                                   | List of exclusion IDs to remove              |                  |

### References

#### Mutations using this object

* [<\~> removeAppsExclusion.input](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/remove-apps-exclusion)
