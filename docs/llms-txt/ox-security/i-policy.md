# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/i-policy.md

# iPolicy

Represents a policy associated with an issue or system.

### Examples

```graphql
type IPolicy {
  id: String
  name: String
  detailedDescription: String
}
```

### Fields

| Field                        | Description                                                | Supported fields |
| ---------------------------- | ---------------------------------------------------------- | ---------------- |
| id `String`                  | Unique identifier of the policy                            |                  |
| name `String`                | Name of the policy                                         |                  |
| detailedDescription `String` | Detailed description of what the policy enforces or covers |                  |

### References

#### Fields with this object

* [{} Issue.policy](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
