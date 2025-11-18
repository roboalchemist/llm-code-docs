# Source: https://configcat.com/docs/api/reference/update-product-preferences.md

# Update Product Preferences

```
POST 
/v1/products/:productId/preferences
```

This endpoint updates the preferences of a Product identified by the `productId` parameter.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When the update was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
