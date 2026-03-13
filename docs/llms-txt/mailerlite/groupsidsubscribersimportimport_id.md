# Source: https://developers-classic.mailerlite.com/reference/groupsidsubscribersimportimport_id.md

# /groups/:id/subscribers/import/:import_id

Add many new subscribers to specified group at once [Rate limited]

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
    "0-1": "*id*",
    "0-2": "ID of an import",
    "1-0": "`type`",
    "1-1": "*string*",
    "1-2": "Action type",
    "2-0": "`stats`",
    "2-1": "*object*",
    "3-0": "`stats.imported`",
    "4-0": "`stats.duplicates`",
    "5-0": "`stats.invalid`",
    "6-0": "`stats.unchanged`",
    "7-0": "`stats.total`",
    "3-1": "*integer*",
    "4-1": "*integer*",
    "5-1": "*integer*",
    "6-1": "*integer*",
    "7-1": "*integer*",
    "8-0": "`options`",
    "8-1": "*object*",
    "9-0": "`options.resubscribe`",
    "10-0": "`options.autoresponders`",
    "9-1": "*boolean*",
    "10-1": "*boolean*",
    "11-0": "`is_finished`",
    "12-0": "`is_importing`",
    "13-0": "`is_killed`",
    "14-0": "`created_at`",
    "11-1": "*boolean*",
    "12-1": "*boolean*",
    "13-1": "*boolean*",
    "14-1": "*string*",
    "14-2": "Datetime, UTC.\n\nFormat: `Y-m-d H:i:s`",
    "11-2": "Determines if an import is finished",
    "12-2": "Determines if an import is in progress",
    "13-2": "Determines if an import is stopped",
    "10-2": "Determines if it is needed to trigger automations",
    "9-2": "Determines if it needed to activate unsubscribed/bounced/unconfirmed subscribers",
    "7-2": "Total emails in the import",
    "6-2": "Total unchanged subscribers",
    "5-2": "Total invalid email adresses",
    "4-2": "Total duplicated items in a single import",
    "3-2": "Total created subscribers"
  },
  "cols": 3,
  "rows": 15
}
[/block]