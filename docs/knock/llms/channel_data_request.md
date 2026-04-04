# Source: https://docs.knock.app/api-reference/recipients/channel_data/schemas/channel_data_request.md

### ChannelDataRequest

A request to set channel data for a type of channel.

#### Attributes

- **data** (object) *required* - Channel data for a given channel type.

#### Example

```json
{
  "data": {
    "tokens": [
      "push_token_1"
    ]
  }
}
```

