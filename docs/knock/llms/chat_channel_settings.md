# Source: https://docs.knock.app/mapi-reference/channels/schemas/chat_channel_settings.md

### ChatChannelSettings

Chat channel settings. Only used as configuration as part of a workflow channel step.

#### Attributes

- **email_based_user_id_resolution** (boolean) - Whether to resolve chat provider user IDs using a Knock user's email address. Only relevant for Slack channels for the time being.
- **link_tracking** (boolean) - Whether to track link clicks on chat notifications.

#### Example

```json
{
  "email_based_user_id_resolution": true,
  "link_tracking": true
}
```

