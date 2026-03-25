# Source: https://docs.knock.app/mapi-reference/broadcasts/send.md

### Send a broadcast

Sends a broadcast immediately or schedules it to send at a future time.


#### Endpoint

`PUT /v1/broadcasts/{broadcast_key}/send`

#### Path parameters

- **broadcast_key** (string) *required* - The key of the broadcast.

#### Query parameters

- **environment** (string) *required* - The environment slug.
- **branch** (string) - The slug of a branch to use. This option can only be used when `environment` is `"development"`.

#### Request body

A request to send or schedule a broadcast.

##### Example

```json
{
  "send_at": "2024-03-20T10:00:00Z"
}
```

#### Responses

##### 200

OK

###### Example

```json
{
  "broadcast": {
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
}
```

