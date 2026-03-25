# Source: https://developers-classic.mailerlite.com/reference/subscriber-custom-field.md

# Subscriber's Field Value

This object is used in [Single Subscriber](https://developers-classic.mailerlite.com/docs/single-subscriber) object. Subscriber has `fields` parameter and it is array of that kind of objects described below.

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
    "0-0": "`key`",
    "1-0": "`value`",
    "2-0": "`type`",
    "2-1": "*string*",
    "0-1": "*string*",
    "1-1": "*string*",
    "2-2": "Allowed type for field value.\n\nAvailable values:\n\n- `TEXT`\n- `NUMBER`\n- `DATE`",
    "0-2": "URL friendly field name",
    "1-2": "Value of field"
  },
  "cols": 3,
  "rows": 3
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Examples"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"key\": \"first_name\",\n  \"value\": \"Justinas\",\n  \"type\": \"TEXT\"\n}",
      "language": "json",
      "name": "Default field"
    },
    {
      "code": "{\n  \"key\": \"favourite_color\",\n  \"value\": \"MailerLite Green\",\n  \"field_type\": \"TEXT\"\n}",
      "language": "json",
      "name": "Custom field"
    }
  ]
}
[/block]