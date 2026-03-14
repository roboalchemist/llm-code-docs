# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/invitation.md

# invitation

Represents an invitation sent to a user to join an organization. Contains all details about the invitation including who sent it, who will receive it, and its validity period.

### Examples

```graphql
type Invitation {
  id: String
  inviteeEmail: String
  invitation_url: String
  created_at: String
  expires_at: String
}
```

### Fields

| Field                    | Description                                                    | Supported fields |
| ------------------------ | -------------------------------------------------------------- | ---------------- |
| id `String`              | Unique identifier for the invitation                           |                  |
| inviteeEmail `String`    | Email address of the person receiving the invitation           |                  |
| invitation\_url `String` | Complete URL that the invitee can use to accept the invitation |                  |
| created\_at `String`     | Timestamp when this invitation was created, in ISO 8601 format |                  |
| expires\_at `String`     | Timestamp when this invitation will expire, in ISO 8601 format |                  |

### References

#### Queries using this object

* [\<?> getInvitations](https://docs.ox.security/api-documentation/api-reference/api--organization/queries/get-invitations)

#### Mutations using this object

* [<\~> createInvitation](https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/create-invitation)
* [<\~> createMultipleInvitations](https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/create-multiple-invitations)
* [<\~> resendInvitation](https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/resend-invitation)
