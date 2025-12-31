# Source: https://configcat.com/docs/api/reference/delete-proxy-profile.md

# Delete Proxy Profile

```
DELETE 
/v1/proxy-profiles/:proxyProfileId
```

This endpoint removes a Proxy Profile identified by the `proxyProfileId` parameter.

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
