# Source: https://configcat.com/docs/api/reference/get-permission-groups.md

# List Permission Groups

```
GET 
/v1/products/:productId/permissions
```

This endpoint returns the list of the Permission Groups that belongs to the given Product identified by the `productId` parameter, which can be obtained from the [List Products](https://configcat.com/docs/docs/api/reference/get-products/.md) endpoint.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
