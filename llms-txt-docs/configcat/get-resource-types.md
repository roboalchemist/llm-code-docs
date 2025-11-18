# Source: https://configcat.com/docs/api/scim/get-resource-types.md

# Get Resource Types

```
GET 
/v2/:organizationId/ResourceTypes
```

This endpoint returns the supported resource types.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 401
* 429

Unauthorized. In case of the SCIM token is invalid.

Too many requests. In case of the request rate exceeds the rate limits.
