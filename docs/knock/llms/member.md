# Source: https://docs.knock.app/mapi-reference/members/schemas/member.md

### Member

A member of the account.

#### Attributes

- **created_at** (string) *required* - The timestamp of when the member joined the account.
- **id** (string) *required* - The unique identifier of the member.
- **role** (string) *required* - The member's role in the account.
- **updated_at** (string) *required* - The timestamp of when the member was last updated.
- **user** (object) *required* - Information about a user within the Knock dashboard. Not to be confused with an external user (recipient) of a workflow.

#### Example

```json
{
  "created_at": "2024-01-15T10:30:00Z",
  "id": "d4b8e8e0-1234-5678-9abc-def012345678",
  "role": "admin",
  "updated_at": "2024-06-20T14:45:00Z",
  "user": {
    "avatar_url": "https://www.gravatar.com/avatar/abc123",
    "created_at": "2024-01-10T08:00:00Z",
    "email": "jane@example.com",
    "id": "a1b2c3d4-5678-9abc-def0-123456789abc",
    "name": "Jane Doe",
    "updated_at": "2024-06-18T12:00:00Z"
  }
}
```

