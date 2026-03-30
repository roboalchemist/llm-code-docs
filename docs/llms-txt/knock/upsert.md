# Source: https://docs.knock.app/mapi-reference/translations/upsert.md

# Source: https://docs.knock.app/mapi-reference/message_types/upsert.md

# Source: https://docs.knock.app/mapi-reference/guides/upsert.md

# Source: https://docs.knock.app/mapi-reference/partials/upsert.md

# Source: https://docs.knock.app/mapi-reference/email_layouts/upsert.md

# Source: https://docs.knock.app/mapi-reference/broadcasts/upsert.md

# Source: https://docs.knock.app/mapi-reference/workflows/upsert.md

# Source: https://docs.knock.app/mapi-reference/channel_groups/upsert.md

### Upsert a channel group

Creates or updates a channel group by key.

#### Endpoint

`PUT /v1/channel_groups/{channel_group_key}`

#### Path parameters

- **channel_group_key** (string) *required* - The key of the channel group to upsert.

#### Request body

Wraps the ChannelGroupRequest request under the channel_group key.

##### Example

```json
{
  "channel_group": {
    "channel_rules": [
      {
        "channel_key": "push-fcm",
        "index": 0,
        "rule_type": "always"
      }
    ],
    "channel_type": "push",
    "name": "Push Notification Group",
    "operator": "any"
  }
}
```

#### Responses

##### 200

OK

###### Example

```json
{
  "channel_group": {
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
}
```

