# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclude-issues-input.md

# excludeIssuesInput

Input for excluding multiple alerts.

### Examples

```graphql
input ExcludeIssuesInput {
  issueIds: [String!]!
  comment: String
  expiredAt: DateTime
}
```

### Fields

| Field                 | Description                                                            | Supported fields |
| --------------------- | ---------------------------------------------------------------------- | ---------------- |
| issueIds `[String!]!` | List of issue IDs to exclude                                           |                  |
| comment `String`      | Comment explaining the exclusion                                       |                  |
| expiredAt `DateTime`  | Date when the exclusion expires in the format YYYY-MM-DDTHH:mm:ss.SSSZ |                  |

### References

#### Mutations using this object

* [<\~> excludeIssues.input](https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/exclude-issues)
