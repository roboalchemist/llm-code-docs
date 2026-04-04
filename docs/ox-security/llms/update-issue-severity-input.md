# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/update-issue-severity-input.md

# updateIssueSeverityInput

Input for updating the severity of a security issue.

### Examples

```graphql
input UpdateIssueSeverityInput {
  issueId: String!
  severity: Int!
}
```

### Fields

| Field             | Description                                                                                                                      | Supported fields |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| issueId `String!` | Unique identifier of the issue to update                                                                                         |                  |
| severity `Int!`   | New severity level to assign to the issue. Values: - 0: Info - 1: Low - 2: Medium - 3: High - 4: Critical - 5: Appoxalypse/Appox |                  |

### References

#### Mutations using this object

* [<\~> updateIssueSeverity.input](https://docs.ox.security/api-documentation/api-reference/api--issue/mutations/update-issue-severity)
