# Source: https://docs.knock.app/api-reference/objects/unset_channel_data.md

# Source: https://docs.knock.app/api-reference/users/unset_channel_data.md

### Unset channel data

Deletes channel data for a specific user and channel ID.

#### Endpoint

`DELETE /v1/users/{user_id}/channel_data/{channel_id}`

**Rate limit tier:** 3

#### Path parameters

- **user_id** (string) *required* - The unique identifier of the user.
- **channel_id** (string) *required* - The unique identifier for the channel.

#### Responses

##### 204

No Content

