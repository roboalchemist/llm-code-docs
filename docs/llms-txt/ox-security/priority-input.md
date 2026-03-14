# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/priority-input.md

# priorityInput

Input for setting application business priority.

### Examples

```graphql
input PriorityInput {
  priority: Int!
  appId: [String]!
}
```

### Fields

| Field             | Description                                        | Supported fields |
| ----------------- | -------------------------------------------------- | ---------------- |
| priority `Int!`   | Application business priority score from 0 to 100. |                  |
| appId `[String]!` | List of application identifiers to update          |                  |

### References

#### Mutations using this object

* [<\~> setPriority.priorityInput](https://docs.ox.security/api-documentation/api-reference/api--application/mutations/set-priority)
