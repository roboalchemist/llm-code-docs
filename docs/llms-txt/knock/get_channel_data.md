# Source: https://docs.knock.app/api-reference/objects/get_channel_data.md

# Source: https://docs.knock.app/api-reference/users/get_channel_data.md

### Get channel data

Retrieves the channel data for a specific user and channel ID.

#### Endpoint

`GET /v1/users/{user_id}/channel_data/{channel_id}`

**Rate limit tier:** 4

#### Path parameters

- **user_id** (string) *required* - The unique identifier of the user.
- **channel_id** (string) *required* - The unique identifier for the channel.

#### Responses

##### 200

OK

###### Example

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

