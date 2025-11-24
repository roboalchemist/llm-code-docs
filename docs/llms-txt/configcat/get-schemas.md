# Source: https://configcat.com/docs/api/scim/get-schemas.md

# Get Schemas

```
GET 
/v2/:organizationId/Schemas
```

This endpoint returns the supported schema list.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 401
* 429

Unauthorized. In case of the SCIM token is invalid.

Too many requests. In case of the request rate exceeds the rate limits.
