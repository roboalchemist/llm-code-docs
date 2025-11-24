# Source: https://configcat.com/docs/api/reference/delete-webhook.md

# Delete Webhook

```
DELETE 
/v1/webhooks/:webhookId
```

This endpoint removes a Webhook identified by the `webhookId` parameter.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 204
* 400
* 404
* 429

When the delete was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
