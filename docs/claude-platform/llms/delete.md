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

## Delete

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Path Parameters

- `message_batch_id: string`

  ID of the Message Batch.

### Returns

- `DeletedMessageBatch = object { id, type }`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    - `"message_batch_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
