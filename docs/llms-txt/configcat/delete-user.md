# Source: https://configcat.com/docs/api/scim/delete-user.md

# Delete User

```
DELETE 
/v2/:organizationId/Users/:userId
```

This endpoint deletes an existing user.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 204
* 401
* 404
* 429

No content.

Unauthorized. In case of the SCIM token is invalid.

Too many requests. In case of the request rate exceeds the rate limits.
