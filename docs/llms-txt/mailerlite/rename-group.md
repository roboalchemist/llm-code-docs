# Source: https://developers-classic.mailerlite.com/reference/rename-group.md

# /groups/:id

Update existing group. [Rate limited]

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
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "1-0": "`name`",
    "0-1": "*integer*",
    "1-1": "*string*",
    "2-0": "`total`",
    "2-1": "*integer*",
    "3-0": "`active`",
    "3-1": "*integer*",
    "4-0": "`unsubscribed`",
    "4-1": "*integer*",
    "5-0": "`bounced`",
    "5-1": "*integer*",
    "6-0": "`unconfirmed`",
    "6-1": "*integer*",
    "7-0": "`junk`",
    "7-1": "*integer*",
    "8-0": "`sent`",
    "8-1": "*integer*",
    "9-0": "`opened`",
    "10-0": "`clicked`",
    "9-1": "*integer*",
    "10-1": "*integer*",
    "0-2": "ID of group",
    "1-2": "Title of group",
    "2-2": "Total count of people in group",
    "3-2": "Total count of active people in group",
    "4-2": "Total count of unsubscribed people in group",
    "5-2": "Total count of bounced people in group",
    "6-2": "Total count of unconfirmed people in group",
    "7-2": "Total count of junk people in group",
    "8-2": "Total count of sent emails in a group",
    "9-2": "Total count of opens in a group",
    "10-2": "Total count of clicks in a group",
    "12-0": "`date_updated`",
    "11-0": "`date_created`",
    "12-1": "*string*",
    "11-1": "*string*",
    "12-2": "Date & time when group is updated",
    "11-2": "Date & time when group is created"
  },
  "cols": 3,
  "rows": 13
}
[/block]