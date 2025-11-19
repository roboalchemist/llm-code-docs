# Source: https://docs.apify.com/api/v2/webhook-put.md

# Update webhook


```
PUT 
https://api.apify.com/v2/webhooks/:webhookId
```


Clientshttps://docs.apify.com/api/client/python/reference/class/WebhookClientAsync#updatehttps://docs.apify.com/api/client/js/reference/class/WebhookClient#updateUpdates a webhook using values specified by a webhook object passed as JSON in the POST payload. If the object does not define a specific property, its value will not be updated.

The response is the full webhook object as returned by the  endpoint.

The request needs to specify the `Content-Type: application/json` HTTP header!

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

## Request

## Responses

* 200

**Response Headers**

