# Source: https://developers-classic.mailerlite.com/reference/campaigns-by-type.md

# /campaigns/:status

Returns all campaigns you have in your account by `:status` which is required. Also basic summary for each campaign including the ID. [Rate limited]

[block:api-header]
{
  "type": "basic",
  "title": "Request"
}
[/block]

There are three possible values of `:status` parameter:

* `sent` - campaigns which are sent already
* `draft` - campaigns which aren't completed or sent to subscribers
* `outbox` - campaigns which are being sent right now or scheduled campaigns

If you do not specify `:status` parameter, it defaults to `sent`.

There are some optional parameters which are described above.

[block:api-header]
{
  "type": "basic",
  "title": "Response Body Parameters"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "0-0": "**id**",
    "1-0": "**total_recipients**",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "Description",
    "2-0": "**type**",
    "3-0": "**date_created**",
    "4-0": "**date_send**",
    "5-0": "**name**",
    "7-0": "**status**",
    "7-1": "`String`",
    "5-1": "`String`",
    "4-1": "`String`",
    "3-1": "`String`",
    "2-1": "`String`",
    "0-1": "`Integer`",
    "1-1": "`Integer`",
    "2-3": "",
    "2-2": "**Possible values:**\n  * `regular`\n  * `ab`\n  * `followup`\n  * `rss`",
    "1-2": "Total count of receivers in campaign",
    "3-2": "When the campaign was created",
    "5-2": "The internal campaign name.",
    "7-2": "**Possible values:**\n\n- `sent`\n- `draft`\n- `outbox`",
    "4-2": "When the email was sent. If campaign type is `outbox`, this parameter will show the scheduled date.",
    "0-2": "ID of a campaign",
    "8-0": "**opened**",
    "8-1": "`Object`",
    "8-2": "",
    "11-0": "**clicked**",
    "11-1": "`Object`",
    "11-2": "",
    "9-0": "**opened.count**",
    "9-1": "`Integer`",
    "9-2": "Total opens of campaign.\n\nAvailable only for `sent` campaigns.\n\nDefault value: `0`",
    "10-0": "**opened.rate**",
    "10-1": "`Float`",
    "10-2": "Open rate of campaign.\n\nAvailable only for `sent` campaigns.\n\nDefault value: `0`",
    "12-0": "**clicked.count**",
    "12-1": "`Integer`",
    "12-2": "Total clicks of campaign.\n\nAvailable only for `sent` campaigns.\n\nDefault value: `0`",
    "13-1": "`Float`",
    "13-0": "**clicked.rate**",
    "13-2": "Click rate of campaign.\n\nAvailable only for `sent` campaigns.\n\nDefault value: `0`",
    "6-0": "**subject**",
    "6-1": "`String`",
    "6-2": "The subject of the email."
  },
  "cols": 3,
  "rows": 14
}
[/block]

[block:api-header]
{
  "type": "get",
  "title": "/campaigns/:status/count"
}
[/block]

You can retrieve only the number of campaigns by type. If you do not specify `:status`, it defaults to `sent`.

[block:api-header]
{
  "type": "basic",
  "title": "Response example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"count\": 3\n}",
      "language": "json",
      "name": "200 OK"
    }
  ]
}
[/block]