# Source: https://docs.knock.app/api-reference/objects/set_channel_data.md

# Source: https://docs.knock.app/api-reference/users/set_channel_data.md

### Set channel data

Updates or creates channel data for a specific user and channel ID. If no user exists in the current environment for the given `user_id`, Knock will create the user entry as part of this request.

#### Endpoint

`PUT /v1/users/{user_id}/channel_data/{channel_id}`

**Rate limit tier:** 3

#### Path parameters

- **user_id** (string) *required* - The unique identifier of the user.
- **channel_id** (string) *required* - The unique identifier for the channel.

#### Request body

A request to set channel data for a type of channel.

##### Example

```json
{
  "data": {
    "tokens": [
      "push_token_1"
    ]
  }
}
```

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

