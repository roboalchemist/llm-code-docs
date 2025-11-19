# Source: https://docs.apify.com/api/v2/webhooks-get.md

# Get list of webhooks


```
GET 
https://api.apify.com/v2/webhooks
```


Clientshttps://docs.apify.com/api/client/python/reference/class/WebhookCollectionClientAsync#listhttps://docs.apify.com/api/client/js/reference/class/WebhookCollectionClient#listGets the list of webhooks that the user created.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records. By default, the records are sorted by the `createdAt` field in ascending order. To sort the records in descending order, use the `desc=1` parameter.

## Request

## Responses

* 200

**Response Headers**

