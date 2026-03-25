# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/user-input-dto.md

# userInputDto

Input type for user information and their associated applications.

### Examples

```graphql
input UserInputDTO {
  name: String
  email: String
  appIds: [String!]!
}
```

### Fields

| Field               | Description                                      | Supported fields |
| ------------------- | ------------------------------------------------ | ---------------- |
| name `String`       | Name of the user                                 |                  |
| email `String`      | Email address of the user                        |                  |
| appIds `[String!]!` | List of application IDs associated with the user |                  |

### References

#### Fields with this object

* [{} OwnersByRoleInput.owners](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/owners-by-role-input)
