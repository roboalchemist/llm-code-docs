# Source: https://docs.knock.app/mapi-reference/members/schemas/member_user.md

### MemberUser

Information about a user within the Knock dashboard. Not to be confused with an external user (recipient) of a workflow.

#### Attributes

- **avatar_url** (string) - The URL of the user's avatar image.
- **created_at** (string) *required* - The timestamp of when the user was created.
- **email** (string) *required* - The user's email address.
- **id** (string) *required* - The user's unique identifier.
- **name** (string) - The user's display name.
- **updated_at** (string) *required* - The timestamp of when the user was last updated.

#### Example

```json
{
  "avatar_url": "https://www.gravatar.com/avatar/abc123",
  "created_at": "2024-01-10T08:00:00Z",
  "email": "jane@example.com",
  "id": "a1b2c3d4-5678-9abc-def0-123456789abc",
  "name": "Jane Doe",
  "updated_at": "2024-06-18T12:00:00Z"
}
```

