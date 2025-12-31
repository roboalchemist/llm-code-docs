# Source: https://configcat.com/docs/api/reference/get-proxy-profile.md

# Get Proxy Profile

```
GET 
/v1/proxy-profiles/:proxyProfileId
```

This endpoint returns a Proxy Profile identified by the `proxyProfileId`.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the Proxy Profile is returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
