# Source: https://developers-classic.mailerlite.com/reference/activity-of-single-subscriber.md

# /subscribers/(:id or :email)/activity

Get activity (clicks, opens, etc) of selected subscriber [Rate limited]

[block:api-header]
{
  "type": "basic",
  "title": "Response Body Parameters"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Paramater",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`date`",
    "0-1": "*string*",
    "0-2": "Date & time when action is performed",
    "1-0": "`report_id`",
    "1-1": "*integer*",
    "2-0": "`subject`",
    "2-1": "*string*",
    "3-0": "`type`",
    "3-1": "*string*",
    "3-2": "Available values:\n\n- `open`\n- `click`\n- `junk`\n- `bounce`\n- `unsubscribe`\n- `forward`",
    "2-2": "Subject of received email",
    "1-2": "ID of report actions belongs to"
  },
  "cols": 3,
  "rows": 4
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Additional Response Body Parameters"
}
[/block]

These parameters are provided when the following condition is true:

```
type = click
```

[block:parameters]
{
  "data": {
    "0-0": "`link_id`",
    "1-0": "`link`",
    "0-1": "*integer*",
    "1-1": "*string*",
    "0-2": "ID of link object",
    "1-2": "URL value",
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description"
  },
  "cols": 3,
  "rows": 2
}
[/block]

These parameters are provided when the following condition is true:

```
type = forward
```

[block:parameters]
{
  "data": {
    "0-0": "`receiver`",
    "2-0": "`receiver.email`",
    "4-0": "`sender.name`",
    "5-0": "`sender.email`",
    "0-1": "*object*",
    "2-1": "*string*",
    "4-1": "*string*",
    "5-1": "*string*",
    "0-2": "",
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "2-2": "Email of forwarded email receiver",
    "4-2": "Name of forwarded mail sender",
    "5-2": "Email of forwarded mail sender",
    "1-0": "`receiver.name`",
    "3-0": "`sender`",
    "3-1": "*object*",
    "1-1": "*string*",
    "1-2": "Name of forwarded email receiver"
  },
  "cols": 3,
  "rows": 6
}
[/block]