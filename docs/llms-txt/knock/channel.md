# Source: https://docs.knock.app/mapi-reference/channels/schemas/channel.md

### Channel

A configured channel, which is a way to route messages to a provider.

#### Attributes

- **archived_at** (string) - The timestamp of when the channel was deleted.
- **created_at** (string) *required* - The timestamp of when the channel was created.
- **custom_icon_url** (string) - Optional URL to a custom icon for the channel. Only used for display purposes in the dashboard.
- **description** (string) - Optional description of the channel's purpose or usage.
- **id** (string) *required* - The unique identifier for the channel.
- **key** (string) *required* - Unique identifier for the channel within a project (immutable once created).
- **name** (string) *required* - The human-readable name of the channel.
- **provider** (string) *required* - The ID of the provider that this channel uses to deliver messages. Learn more about the providers available [in our documentation](https://docs.knock.app/integrations/overview).
- **type** (string) *required* - The type of channel, determining what kind of messages it can send.
- **updated_at** (string) *required* - The timestamp of when the channel was last updated.

#### Example

```json
{
  "archived_at": null,
  "created_at": "2021-01-01T00:00:00Z",
  "custom_icon_url": null,
  "id": "01234567-89ab-cdef-0123-456789abcdef",
  "key": "my-sendgrid-channel",
  "name": "My Sendgrid Channel",
  "provider": "sendgrid",
  "type": "email",
  "updated_at": "2021-01-01T00:00:00Z"
}
```

