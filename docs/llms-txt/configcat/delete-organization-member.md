# Source: https://configcat.com/docs/api/reference/delete-organization-member.md

# Delete Member from Organization

```
DELETE 
/v1/organizations/:organizationId/members/:userId
```

This endpoint removes a Member identified by the `userId` from the given Organization identified by the `organizationId` parameter.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 204
* 400
* 404
* 429

When the delete was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
