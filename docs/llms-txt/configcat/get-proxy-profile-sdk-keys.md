# Source: https://configcat.com/docs/api/reference/get-proxy-profile-sdk-keys.md

# Get selected SDK keys

```
GET 
/v1/proxy-profiles/:proxyProfileId/sdk-keys
```

This endpoint returns the list of SDK keys selected for a Proxy Profile identified by the `proxyProfileId`.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the SDK keys selected for the Proxy Profile are returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
