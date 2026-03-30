# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/types/inputs/invitation-input.md

# invitationInput

Input parameters required to create a new organization invitation.

### Examples

```graphql
input InvitationInput {
  inviteeEmail: String!
  inviteeRoles: [String]!
  scopes: String
  invitationTTLSec: Int
}
```

### Fields

| Field                    | Description                                                                                                          | Supported fields |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------- |
| inviteeEmail `String!`   | Email address of the person to invite                                                                                |                  |
| inviteeRoles `[String]!` | List of role identifiers to be assigned to the invitee upon acceptance                                               |                  |
| scopes `String`          | Permission scopes to be granted to the invitee upon acceptance                                                       |                  |
| invitationTTLSec `Int`   | Time-to-live for the invitation in seconds. Default is 7 days (604800 seconds), maximum is 30 days (2592000 seconds) |                  |

### References

#### Mutations using this object

* [<\~> createInvitation.invitationInfo](https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/create-invitation)
* [<\~> createMultipleInvitations.invitationsInfo](https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/create-multiple-invitations)
