# Source: https://configcat.com/docs/api/reference/replace-proxy-profile.md

# Replace Proxy Profile

```
PUT 
/v1/proxy-profiles/:proxyProfileId
```

This endpoint replaces a Proxy Profile identified by the `proxyProfileId` parameter.

**Important:** As this endpoint is doing a complete replace, it's important to set every other attribute that you don't want to change in its original state. Not listing one means it will reset.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When the replace was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
