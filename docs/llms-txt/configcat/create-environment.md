# Source: https://configcat.com/docs/api/reference/create-environment.md

# Create Environment

```
POST 
/v1/products/:productId/environments
```

This endpoint creates a new Environment in a specified Product identified by the `productId` parameter, which can be obtained from the [List Products](https://configcat.com/docs/docs/api/reference/get-products/.md) endpoint.

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
