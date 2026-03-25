# Source: https://docs.knock.app/api-reference/recipients/channel_data/schemas/push_channel_data_devices_only.md

### PushChannelDataDevicesOnly

Push channel data.

#### Attributes

- **devices** (array) *required* - A list of devices. Each device contains a token, and optionally a locale and timezone.

#### Example

```json
{
  "devices": [
    {
      "locale": "en-US",
      "timezone": "America/Los_Angeles",
      "token": "push_token_1"
    }
  ]
}
```

