# Source: https://configcat.com/docs/api/reference/create-config.md

# Create Config

Copy page

This endpoint creates a new Config in a specified Product identified by the `productId` parameter, which can be obtained from the [List Products](https://configcat.com/docs/api/reference/get-products.md) endpoint.

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
