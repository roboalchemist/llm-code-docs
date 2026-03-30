# Source: https://developers-classic.mailerlite.com/reference/campaign-actions-and-triggers.md

# /campaigns/:id/actions/:action

Send, schedule or cancel campaign [Rate limited]

Every action is active due to some conditions (campaign type) described in table below.

[block:parameters]
{
  "data": {
    "h-0": "Action",
    "h-1": "Campaign type",
    "h-2": "Campaign Status",
    "h-3": "Description",
    "0-0": "`send`",
    "0-3": "You can send every campaign in `draft` which has `step` value equal to `3`",
    "0-2": "`draft`",
    "0-1": "`regular`\n`ab`\n`followup`",
    "1-0": "`cancel`",
    "1-1": "`regular`\n`ab`\n`followup`\n`rss`",
    "1-3": "You can cancel every campaign in `outbox`.",
    "1-2": "`outbox`"
  },
  "cols": 4,
  "rows": 2
}
[/block]

Please take attention that every action is available only for specific type campaigns:

* `send`: you can send or schedule those campaigns which are in `draft` and has `step` value equal to `3`
* `cancel`: you can cancel only those campaigns which are in `outbox`

[block:api-header]
{
  "type": "basic",
  "title": "Send or schedule campaign"
}
[/block]

Send or schedule endpoint has additional body parameters associated with Google analytics, schedule and followup campaigns.

[block:api-header]
{
  "type": "basic",
  "title": "Campaign sending time"
}
[/block]

We provide two options how campaign can be sent regarding to sending time.

\##Send now
There is no need to use request parameters for all types of campaigns.

\##Send later (schedule)
For all types of campaigns:

* `type = 2`
* `date` is required
* `timezone_id` is optional. Default value is ID of timezone which is associated with [Account](https://developers-classic.mailerlite.com/docs/retrieving-user-accounts)

[block:callout]
{
  "type": "info",
  "body": "If campaign type is `followup`, its followup mail will be sent 24 hours from campaign sending time by default. If you want to set custom time for followup campaign, then use these additional request parameters:\n- `followup_schedule = specific`\n- `followup_date` is required\n- `followup_timezone_id` is optional. Default value is ID of timezone which is associated with [Account](https://developers-classic.mailerlite.com/docs/retrieving-user-accounts)",
  "title": "Followup campaign schedule"
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Request Body Parameters"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "**type**",
    "0-1": "`Integer`",
    "0-2": "Possible values:\n\n- `1` - send instantly (default value)\n- `2` - schedule send",
    "1-0": "**followup_schedule**",
    "1-1": "`String`",
    "1-2": "Possible values:\n\n- `24h` - followup mail is sent in 24 hours (default value)\n- `specific` - must provide custom time described below\n\n**Only for `followup` campaigns**",
    "3-0": "**date**",
    "4-0": "**timezone_id**",
    "3-1": "`String`",
    "3-2": "Format:\n\n`yyyy-mm-dd H:i`\n\n**Available when `type` is `2`**",
    "4-1": "`Integer`",
    "4-2": "ID of [Timezone](https://developers-classic.mailerlite.com/reference/timezone) \n\n**Available when `type` is `2`**",
    "5-0": "**followup_date**",
    "5-1": "`String`",
    "5-2": "Format:\n\n`yyyy-mm-dd H:i`\n\n**Available only for `followup` campaigns when `followup_schedule` is `specific`**",
    "6-0": "**followup_timezone_id**",
    "6-1": "`Integer`",
    "6-2": "ID of [Timezone](https://developers-classic.mailerlite.com/reference/timezone)\n\n**Available only for `followup` campaigns when `followup_schedule` is `specific`**",
    "2-0": "**analytics**",
    "2-2": "Possible values:\n\n- `0` - false\n- `1` - true",
    "2-1": "`Integer`"
  },
  "cols": 3,
  "rows": 7
}
[/block]