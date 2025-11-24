# Source: https://configcat.com/docs/api/reference/create-product.md

# Create Product

```
POST 
/v1/organizations/:organizationId/products
```

This endpoint creates a new Product in a specified Organization identified by the `organizationId` parameter, which can be obtained from the [List Organizations](https://configcat.com/docs/docs/api/reference/get-organizations/.md) endpoint.

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
