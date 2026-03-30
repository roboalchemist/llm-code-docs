# Source: https://developers-classic.mailerlite.com/reference/subscribers-in-a-group.md

# /groups/:id/subscribers

Get all subscribers in a specified group [Rate limited]

Response is the array of [Single Subscriber](https://developers-classic.mailerlite.com/docs/single-subscriber) objects.

[block:api-header]
{
  "type": "basic",
  "title": "Additional endpoints"
}
[/block]

Also there is some additional endpoints associated with subscribers in group:

[block:api-header]
{
  "type": "basic",
  "title": "Getting a count of subscibers in a group"
}
[/block]

\##Endpoint

```
GET /groups/:group_id/subscribers/count
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

[block:api-header]
{
  "type": "basic",
  "title": "Getting subscribers in a group by type"
}
[/block]

\##Endpoint

```
GET /groups/:group_id/subscribers/:type
```

Possible values of `:type`:

* `active`
* `unsubscribed`
* `bounced`
* `junk`
* `unconfirmed`

\##Response Example
The same structure as it is described above so response is the array of [Single Subscriber](https://developers-classic.mailerlite.com/docs/single-subscriber) objects.

[block:api-header]
{
  "title": "Using filters"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# get all subscribers who were created in a provided period\n\ncurl -v http://api.mailerlite.com/api/v2/groups/3640549/subscribers?filters[date_created][$gte]=2017-03-01&filters[date_created][$lt]=2017-04-01 \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\"\n\n# get all subscribers who were after the selected day\n\ncurl -v http://api.mailerlite.com/api/v2/groups/3640549/subscribers?filters[date_created][$gte]=2017-03-01 \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\"",
      "language": "curl"
    }
  ]
}
[/block]

Available keys:

`date_subscribe`
`date_unsubscribe`
`date_created`
`date_updated`

Available operators:

`$gt` - greater than
`$gte` - greater than or equal
`$lt` - less than
`$lte` - less than or equal