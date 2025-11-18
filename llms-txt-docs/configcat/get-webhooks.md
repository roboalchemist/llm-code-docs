# Source: https://configcat.com/docs/api/reference/get-webhooks.md

# List Webhooks

```
GET 
/v1/products/:productId/webhooks
```

This endpoint returns the list of the Webhooks that belongs to the given Product identified by the `productId` parameter, which can be obtained from the [List Products](https://configcat.com/docs/docs/api/reference/get-products/.md) endpoint.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 429

Too many requests. In case of the request rate exceeds the rate limits.
