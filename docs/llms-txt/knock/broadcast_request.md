# Source: https://docs.knock.app/mapi-reference/broadcasts/schemas/broadcast_request.md

### BroadcastRequest

A broadcast request for upserting a broadcast.

#### Attributes

- **categories** (array) - A list of categories that the broadcast belongs to.
- **description** (string) - An arbitrary string attached to a broadcast object. Useful for adding notes about the broadcast for internal purposes. Maximum of 280 characters allowed.
- **name** (string) *required* - A name for the broadcast. Must be at maximum 255 characters in length.
- **scheduled_at** (string) - The timestamp of when the broadcast is scheduled to be sent.
- **settings** (object) - A map of broadcast settings.
- **steps** (array) *required* - A list of broadcast step objects in the broadcast. Broadcasts only support channel, branch, and delay steps.
- **target_audience_key** (string) - The key of the audience to target for this broadcast.

#### Example

```json
{
  "categories": [
    "announcement"
  ],
  "description": "A broadcast to all users",
  "name": "My Broadcast",
  "settings": {
    "is_commercial": true,
    "override_preferences": false
  },
  "steps": [
    {
      "channel_key": "in-app-feed",
      "name": "Channel 1",
      "ref": "channel_1",
      "template": {
        "action_url": "{{ vars.app_url }}",
        "markdown_body": "Hello **{{ recipient.name }}**"
      },
      "type": "channel"
    }
  ],
  "target_audience_key": "all-users"
}
```

