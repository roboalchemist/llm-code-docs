# Source: https://configcat.com/docs/api/scim/replace-user.md

# Replace User

```
PUT 
/v2/:organizationId/Users/:userId
```

This endpoint updates an existing user by replacing all attributes present in the request.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 401
* 404
* 429

Unauthorized. In case of the SCIM token is invalid.

Too many requests. In case of the request rate exceeds the rate limits.
