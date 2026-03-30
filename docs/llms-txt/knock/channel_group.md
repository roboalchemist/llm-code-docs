# Source: https://docs.knock.app/mapi-reference/channel_groups/schemas/channel_group.md

### ChannelGroup

A group of channels with rules for when they are applicable.

#### Attributes

- **archived_at** (string) - The timestamp of when the channel group was archived (soft deleted).
- **channel_rules** (array) *required* - Rules for determining which channels should be used.
- **channel_type** (string) *required* - The type of channels contained in this group.
- **created_at** (string) *required* - The timestamp of when the channel group was created.
- **key** (string) *required* - Unique identifier for the channel group within a project.
- **name** (string) *required* - The human-readable name of the channel group.
- **operator** (string) *required* - Determines how the channel rules are applied ('any' means any rule can match, 'all' means all rules must match).
- **source** (string) *required* - Whether this channel group was created by the system or a user. Only user created channel groups can be modified.
- **updated_at** (string) *required* - The timestamp of when the channel group was last updated.

#### Example

```json
{
  "channel_rules": [
    {
      "channel": {
        "archived_at": null,
        "created_at": "2021-01-01T00:00:00Z",
        "custom_icon_url": null,
        "id": "01234567-89ab-cdef-0123-456789abcdef",
        "key": "my-sendgrid-channel",
        "name": "My Sendgrid Channel",
        "provider": "sendgrid",
        "type": "email",
        "updated_at": "2021-01-01T00:00:00Z"
      },
      "created_at": "2021-01-01T00:00:00Z",
      "index": 0,
      "rule_type": "always",
      "updated_at": "2021-01-01T00:00:00Z"
    }
  ],
  "channel_type": "push",
  "created_at": "2021-01-01T00:00:00Z",
  "key": "push-group",
  "name": "Push Notification Group",
  "operator": "any",
  "source": "user",
  "updated_at": "2021-01-01T00:00:00Z"
}
```

