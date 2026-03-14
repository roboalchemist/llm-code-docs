# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/types/inputs/update-member-input.md

# updateMemberInput

### Examples

```graphql
input UpdateMemberInput {
  userId: String!
  roleIDs: [String]
  scopes: String
}
```

### Fields

| Field              | Description                                                                                                                                                                                                                                                                                      | Supported fields |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| userId `String!`   | user ID                                                                                                                                                                                                                                                                                          |                  |
| roleIDs `[String]` | list of role id's assigned to the user                                                                                                                                                                                                                                                           |                  |
| scopes `String`    | list of scopes id's assigned to the user as string where the id's are comma separated and space separated between owners and tags owners starting with 'app-owner:' prefix and tags starting with 'tags:' prefix (eg. 'app-owner:<usermail@acme.com>,<usermail2@acme.com> tags:XXX-XXX-XXX-XXX') |                  |

### References

#### Mutations using this object

* [<\~> updateMember.updateMemberInput](https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/update-member)
