# Source: https://docs.knock.app/mapi-reference/broadcasts/schemas/broadcast.md

### Broadcast

A broadcast object.

#### Attributes

- **archived_at** (string) - The timestamp of when the broadcast was archived.
- **categories** (array) - A list of categories that the broadcast belongs to.
- **created_at** (string) *required* - The timestamp of when the broadcast was created. (read-only).
- **description** (string) - An arbitrary string attached to a broadcast object. Useful for adding notes about the broadcast for internal purposes. Maximum of 280 characters allowed.
- **environment** (string) *required* - The slug of the environment in which the broadcast exists. (read-only).
- **key** (string) *required* - The unique key string for the broadcast object. Must be at minimum 3 characters and at maximum 255 characters in length. Must be in the format of ^[a-z0-9_-]+$.
- **name** (string) *required* - A name for the broadcast. Must be at maximum 255 characters in length.
- **scheduled_at** (string) - The timestamp of when the broadcast is scheduled to be sent.
- **sent_at** (string) - The timestamp of when the broadcast was sent. (read-only).
- **settings** (object) - A map of broadcast settings.
- **sha** (string) *required* - The SHA hash of the workflow data. (read-only).
- **status** (string) *required* - The current status of the broadcast. One of: `draft`, `scheduled`, `sent`.
- **steps** (array) *required* - A list of broadcast step objects in the broadcast. Broadcasts only support channel, branch, and delay steps.
- **target_audience_key** (string) - The key of the audience to target for this broadcast.
- **updated_at** (string) *required* - The timestamp of when the broadcast was last updated. (read-only).
- **valid** (boolean) *required* - Whether the broadcast and its steps are in a valid state. (read-only).

#### Example

```json
{
  "categories": [
    "marketing",
    "promotions"
  ],
  "created_at": "2022-12-16T19:07:50.027113Z",
  "description": "Holiday promotion broadcast for December",
  "environment": "development",
  "key": "december-promotion",
  "name": "December Promotion",
  "scheduled_at": null,
  "sent_at": null,
  "settings": {
    "is_commercial": true,
    "override_preferences": false
  },
  "sha": "f7e9d3b2a1c8e6m4k5j7h9g0i2l3n4p6q8r0t1u3v5w7x9y",
  "status": "draft",
  "steps": [
    {
      "channel_key": "in-app-feed",
      "description": "Main in-app feed",
      "name": "In-app step",
      "ref": "in_app_feed_1",
      "template": {
        "action_url": "{{ vars.app_url }}",
        "markdown_body": "Hello **{{ recipient.name }}**"
      },
      "type": "channel"
    }
  ],
  "target_audience_key": "premium-users",
  "updated_at": "2023-02-08T22:15:19.846681Z",
  "valid": true
}
```

