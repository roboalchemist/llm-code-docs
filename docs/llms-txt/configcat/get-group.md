# Source: https://configcat.com/docs/api/scim/get-group.md

# Get Group

```
GET 
/v2/:organizationId/Groups/:groupId
```

This endpoint returns a group.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 401
* 404
* 429

Unauthorized. In case of the SCIM token is invalid.

Too many requests. In case of the request rate exceeds the rate limits.
