# Source: https://docs.knock.app/mapi-reference/channels/schemas/email_channel_settings.md

### EmailChannelSettings

Email channel settings. Only used as configuration as part of a workflow channel step.

#### Attributes

- **bcc_address** (string) - The BCC address on email notifications. Supports liquid.
- **cc_address** (string) - The CC address on email notifications. Supports liquid.
- **from_address** (string) - The email address from which this channel will send. Supports liquid.
- **from_name** (string) - The name from which this channel will send. Supports liquid.
- **json_overrides** (string) - A JSON template for any custom overrides to merge into the API payload that is sent to the email provider. Supports liquid.
- **link_tracking** (boolean) - Whether to track link clicks on email notifications.
- **open_tracking** (boolean) - Whether to track opens on email notifications.
- **reply_to_address** (string) - The Reply-to address on email notifications. Supports liquid.
- **to_address** (string) - The email address to which this channel will send. Defaults to `recipient.email`. Supports liquid.

#### Example

```json
{
  "bcc_address": null,
  "cc_address": null,
  "from_address": "hello@example.com",
  "from_name": "John Doe",
  "json_overrides": "{\"some_override\": true}",
  "link_tracking": true,
  "open_tracking": true,
  "reply_to_address": null,
  "to_address": "hello@example.com"
}
```

