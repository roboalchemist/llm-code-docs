# Source: https://docs.knock.app/api-reference/audiences/schemas/audience_member.md

### AudienceMember

An audience member.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **added_at** (string) *required* - Timestamp when the resource was created.
- **tenant** (string) - The unique identifier for the tenant.
- **user** (object) *required* - A [User](/concepts/users) represents an individual in your system who can receive notifications through Knock. Users are the most common recipients of notifications and are always referenced by your internal identifier.
- **user_id** (string) *required* - The unique identifier of the user.

#### Example

```json
{
  "__typename": "AudienceMember",
  "added_at": "1993-06-10T14:30:00Z",
  "tenant": "ingen_isla_nublar",
  "user": {
    "__typename": "User",
    "created_at": null,
    "email": "alan.grant@dig.site.mt",
    "id": "dr_grant",
    "name": "Dr. Alan Grant",
    "updated_at": "1993-06-09T08:15:00Z"
  },
  "user_id": "dr_grant"
}
```

