# Source: https://configcat.com/docs/api/reference/update-webhook.md

# Update Webhook

Copy page

This endpoint updates a Webhook identified by the `webhookId` parameter with a collection of [JSON Patch](https://jsonpatch.com) operations.

The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don't want to change.

For example: We have the following resource.

```json
{
  "webhookId": 6,
  "url": "https://example.com/hook",
  "httpMethod": "post",
  "content": "null",
  "webHookHeaders": []
}

```

If we send an update request body as below (it changes the `content` field and adds a new HTTP header):

```json
[
  {
    "op": "replace", 
    "path": "/content", 
    "value": "Some webhook content."
  }, 
  {
    "op": "add", 
    "path": "/webHookHeaders/-", 
    "value": {
      "key": "X-Custom-Header", 
      "value": "Custom header value"
    }
  }
]

```

Only the `content` and `webHookHeaders` are updated and all the other attributes remain unchanged. So we get a response like this:

```json
{
  "webhookId": 6,
  "url": "https://example.com/hook",
  "httpMethod": "post", 
  "content": "Some webhook content.", 
  "webHookHeaders": [
    {
      "key": "X-Custom-Header", 
      "value": "Custom header value", 
      "isSecure": false
    }
  ]
}

```

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When the update was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
