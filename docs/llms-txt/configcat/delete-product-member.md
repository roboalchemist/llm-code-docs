# Source: https://configcat.com/docs/api/reference/delete-product-member.md

# Delete Member from Product

```
DELETE 
/v1/products/:productId/members/:userId
```

This endpoint removes a Member identified by the `userId` from the given Product identified by the `productId` parameter.

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
