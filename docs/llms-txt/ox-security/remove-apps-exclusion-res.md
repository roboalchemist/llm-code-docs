# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/remove-apps-exclusion-res.md

# removeAppsExclusionRes

### Examples

```graphql
type RemoveAppsExclusionRes {
  removeAppsExclusion: [RemoveAppSingleExclusionRes]
}
```

### Fields

| Field                                                                                                                                                                         | Description | Supported fields                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------- |
| removeAppsExclusion [`[RemoveAppSingleExclusionRes]`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/remove-app-single-exclusion-res) |             | <p>isSucceeded <code>Boolean!</code><br>exclusionId <code>String</code></p> |

### References

#### Mutations using this object

* [<\~> removeAppsExclusion](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/remove-apps-exclusion)
