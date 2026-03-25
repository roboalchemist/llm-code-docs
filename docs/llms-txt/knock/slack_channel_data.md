# Source: https://docs.knock.app/api-reference/recipients/channel_data/schemas/slack_channel_data.md

### SlackChannelData

Slack channel data.

#### Attributes

- **connections** (array) *required* - List of Slack channel connections.
- **token** (object) - A Slack connection token.

#### Example

```json
{
  "connections": [
    {
      "access_token": "xoxb-1234567890",
      "channel_id": "C01234567890",
      "user_id": "U01234567890"
    }
  ],
  "token": {
    "access_token": "xoxb-1234567890"
  }
}
```

