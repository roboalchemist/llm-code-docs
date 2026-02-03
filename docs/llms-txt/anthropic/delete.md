# Source: https://platform.claude.com/docs/en/api/admin/users/delete.md

# Source: https://platform.claude.com/docs/en/api/admin/workspaces/members/delete.md

# Source: https://platform.claude.com/docs/en/api/typescript/beta/skills/versions/delete.md

# Source: https://platform.claude.com/docs/en/api/ruby/beta/skills/versions/delete.md

# Source: https://platform.claude.com/docs/en/api/python/beta/skills/versions/delete.md

# Source: https://platform.claude.com/docs/en/api/kotlin/beta/skills/versions/delete.md

# Source: https://platform.claude.com/docs/en/api/java/beta/skills/versions/delete.md

# Source: https://platform.claude.com/docs/en/api/go/beta/skills/versions/delete.md

# Source: https://platform.claude.com/docs/en/api/beta/skills/versions/delete.md

# Source: https://platform.claude.com/docs/en/api/typescript/beta/skills/delete.md

# Source: https://platform.claude.com/docs/en/api/ruby/beta/skills/delete.md

# Source: https://platform.claude.com/docs/en/api/python/beta/skills/delete.md

# Source: https://platform.claude.com/docs/en/api/kotlin/beta/skills/delete.md

# Source: https://platform.claude.com/docs/en/api/java/beta/skills/delete.md

# Source: https://platform.claude.com/docs/en/api/go/beta/skills/delete.md

# Source: https://platform.claude.com/docs/en/api/beta/skills/delete.md

# Source: https://platform.claude.com/docs/en/api/admin/invites/delete.md

# Source: https://platform.claude.com/docs/en/api/typescript/beta/files/delete.md

# Source: https://platform.claude.com/docs/en/api/ruby/beta/files/delete.md

# Source: https://platform.claude.com/docs/en/api/python/beta/files/delete.md

# Source: https://platform.claude.com/docs/en/api/kotlin/beta/files/delete.md

# Source: https://platform.claude.com/docs/en/api/java/beta/files/delete.md

# Source: https://platform.claude.com/docs/en/api/go/beta/files/delete.md

# Source: https://platform.claude.com/docs/en/api/beta/files/delete.md

# Source: https://platform.claude.com/docs/en/api/typescript/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/ruby/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/python/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/kotlin/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/java/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/go/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/typescript/beta/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/ruby/beta/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/python/beta/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/kotlin/beta/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/java/beta/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/go/beta/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/beta/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/messages/batches/delete.md

# Source: https://platform.claude.com/docs/en/api/admin/workspaces/members/delete.md

## Delete

**delete** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

### Returns

- `type: "workspace_member_deleted"`

  Deleted object type.

  For Workspace Members, this is always `"workspace_member_deleted"`.

  - `"workspace_member_deleted"`

- `user_id: string`

  ID of the User.

- `workspace_id: string`

  ID of the Workspace.

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```
