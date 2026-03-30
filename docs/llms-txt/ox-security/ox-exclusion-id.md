# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/ox-exclusion-id.md

# oxExclusionId

Unique identifier types for exclusions.

### Examples

```graphql
enum OxExclusionId {
  issue
  issueCve
  repoCve
  allReposCve
  cveAndLibrary
  repo
  allRepos
  secret
  url
  repoSecret
  repoImage
}
```

### Enum values

| Enum value    | Description                            |
| ------------- | -------------------------------------- |
| issue         | Issue-based exclusion identifier       |
| issueCve      |                                        |
| repoCve       |                                        |
| allReposCve   |                                        |
| cveAndLibrary |                                        |
| repo          | Repository-based exclusion identifier  |
| allRepos      | All repositories exclusion identifier  |
| secret        | Secret-based exclusion identifier      |
| url           |                                        |
| repoSecret    | Repository secret exclusion identifier |
| repoImage     | Repository image exclusion identifier  |

### References

#### Fields with this object

* [{} ExclusionRuleInput.oxRuleId](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclusion-rule-input)
