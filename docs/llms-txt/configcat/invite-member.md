# Source: https://configcat.com/docs/api/reference/invite-member.md

# Invite Member

```
POST 
/v1/products/:productId/members/invite
```

This endpoint invites a Member into the given Product identified by the `productId` parameter.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When the invite was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
