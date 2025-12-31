# Source: https://configcat.com/docs/api/reference/create-permission-group.md

# Create Permission Group

```
POST 
/v1/products/:productId/permissions
```

This endpoint creates a new Permission Group in a specified Product identified by the `productId` parameter, which can be obtained from the [List Products](https://configcat.com/docs/docs/api/reference/get-products/.md) endpoint.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 201
* 400
* 404
* 429

When the creation was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
