# Source: https://configcat.com/docs/api/reference/get-proxy-profiles.md

# List Proxy Profiles

```
GET 
/v1/organizations/:organizationId/proxy-profiles
```

This endpoint returns the list of Proxy profiles for the given Organization identified by the `organizationId` parameter.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
