# Source: https://configcat.com/docs/api/reference/delete-product.md

# Delete Product

```
DELETE 
/v1/products/:productId
```

This endpoint removes a Product identified by the `productId` parameter.

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
