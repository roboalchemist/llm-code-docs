# Source: https://configcat.com/docs/api/reference/get-product-members.md

# List Product Members

```
GET 
/v1/products/:productId/members
```

This endpoint returns the list of Members that belongs to the given Product, identified by the `productId` parameter.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
