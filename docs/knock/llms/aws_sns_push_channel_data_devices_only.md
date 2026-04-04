# Source: https://docs.knock.app/api-reference/recipients/channel_data/schemas/aws_sns_push_channel_data_devices_only.md

### AWSSNSPushChannelDataDevicesOnly

AWS SNS push channel data.

#### Attributes

- **devices** (array) *required* - A list of devices. Each device contains a target_arn, and optionally a locale and timezone.

#### Example

```json
{
  "devices": [
    {
      "locale": "en-US",
      "target_arn": "arn:aws:sns:us-west-2:123456789012:endpoint/GCM/gcmpushapp/5e3e9847-3183-3f18-a7e8-671c3a57d4b3",
      "timezone": "America/Los_Angeles"
    }
  ]
}
```

