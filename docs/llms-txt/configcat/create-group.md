# Source: https://configcat.com/docs/api/scim/create-group.md

# Create Group

```
POST 
/v2/:organizationId/Groups
```

This endpoint creates a new group with the given attributes.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 201
* 400
* 401
* 409
* 429

Unauthorized. In case of the SCIM token is invalid.

Too many requests. In case of the request rate exceeds the rate limits.
