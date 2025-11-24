# Source: https://configcat.com/docs/api/reference/add-member-to-group.md

# Update Member Permissions

```
POST 
/v1/organizations/:organizationId/members/:userId
```

This endpoint updates the permissions of a Member identified by the `userId`. This endpoint can also be used to move a Member between Permission Groups within a Product. Only a single Permission Group can be set per Product.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When the update was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
