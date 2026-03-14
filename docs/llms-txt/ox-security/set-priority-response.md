# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/set-priority-response.md

# setPriorityResponse

Response indicates the result of priority setting operation.

### Examples

```graphql
type SetPriorityResponse {
  hasModifiedPriority: Boolean
}
```

### Fields

| Field                         | Description                                  | Supported fields |
| ----------------------------- | -------------------------------------------- | ---------------- |
| hasModifiedPriority `Boolean` | Whether any priority modifications were made |                  |

### References

#### Mutations using this object

* [<\~> setPriority](https://docs.ox.security/api-documentation/api-reference/api--application/mutations/set-priority)
