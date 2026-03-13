# Source: https://developers-classic.mailerlite.com/docs/request.md

# Request

[block:api-header]
{
  "type": "basic",
  "title": "Base URL"
}
[/block]

```
https://api.mailerlite.com/api/v2/
```

[block:callout]
{
  "type": "info",
  "body": "It's important to use HTTPS in your requests, otherwise, you might experience unexpected results.",
  "title": "Important!"
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Acceptable content types"
}
[/block]

We accept the following `Content-Type` header values when using `POST` or `PUT` methods:

* `application/json` (this is the default and is recommended)
* `multipart/form-data`
* `application/x-www-form-urlencoded`

[block:api-header]
{
  "type": "basic",
  "title": "HTTP methods"
}
[/block]

[block:parameters]
{
  "data": {
    "0-0": "GET",
    "1-0": "POST",
    "2-0": "PUT",
    "3-0": "DELETE",
    "h-0": "Verb",
    "h-1": "Description",
    "0-1": "Obtain information. Query path parameters are allowed.",
    "1-1": "Add new information. Body is allowed.",
    "2-1": "Modify existing information. Body is allowed.",
    "3-1": "Remove information."
  },
  "cols": 2,
  "rows": 4
}
[/block]