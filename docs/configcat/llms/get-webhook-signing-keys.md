# Source: https://configcat.com/docs/api/reference/get-webhook-signing-keys.md

# Get Webhook Signing Keys

Copy page

This endpoint returns the signing keys of a Webhook identified by the `webhookId`.

Signing keys are used for ensuring the Webhook requests you receive are actually sent by ConfigCat.

[Here](https://configcat.com/docs/advanced/notifications-webhooks.md#verifying-webhook-requests) you can read more about Webhook request verification.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the webhook signing keys are returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
