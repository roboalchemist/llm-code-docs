# Source: https://developers-classic.mailerlite.com/reference/subscribers-in-a-group-by-type.md

# /groups/:id/subscribers/:type

Get all subscribers in a specified group [Rate limited]

The same endpoint as `/groups/:id/subscribers` but it has `type` parameter defined so results are filtered by its value.

Possible values of `:type`:

* `active`
* `unsubscribed`
* `bounced`
* `junk`
* `unconfirmed`

Response is the array of [Single Subscriber](https://developers-classic.mailerlite.com/docs/single-subscriber) objects.

[block:api-header]
{
  "type": "basic",
  "title": "Getting a count of subscibers by type in a group"
}
[/block]

\##Endpoint

```
GET /groups/:group_id/subscribers/:type/count
```

\##Response Example

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"count\": 5\n}",
      "language": "json",
      "name": "200 OK"
    }
  ]
}
[/block]