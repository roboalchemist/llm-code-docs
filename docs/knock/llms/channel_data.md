# Source: https://docs.knock.app/api-reference/recipients/channel_data/schemas/channel_data.md

### ChannelData

Channel data for a given channel type.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **channel_id** (string) *required* - The unique identifier for the channel.
- **data** (object) *required* - Channel data for a given channel type.
- **provider** (string) - The type of provider.

#### Example

```json
{
  "__typename": "ChannelData",
  "channel_id": "123e4567-e89b-12d3-a456-426614174000",
  "data": {
    "devices": [
      {
        "locale": null,
        "timezone": null,
        "token": "device_1"
      }
    ],
    "tokens": [
      "push_token_1"
    ]
  }
}
```

