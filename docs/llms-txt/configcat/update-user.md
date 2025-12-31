# Source: https://configcat.com/docs/api/scim/update-user.md

# Update User

```
PATCH 
/v2/:organizationId/Users/:userId
```

This endpoint updates an existing user by applying JSON Patch operations.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 204
* 400
* 401
* 404
* 429

No content.

Unauthorized. In case of the SCIM token is invalid.

Too many requests. In case of the request rate exceeds the rate limits.
