# Source: https://docs.knock.app/api-reference/recipients/channel_data/schemas/aws_sns_push_channel_data_target_arns_only.md

### AWSSNSPushChannelDataTargetARNsOnly

AWS SNS push channel data.

#### Attributes

- **target_arns** (array) *required* - A list of platform endpoint ARNs. See [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).

#### Example

```json
{
  "target_arns": [
    "arn:aws:sns:us-west-2:123456789012:endpoint/GCM/gcmpushapp/5e3e9847-3183-3f18-a7e8-671c3a57d4b3"
  ]
}
```

