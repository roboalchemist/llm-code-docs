# Source: https://configcat.com/docs/api/reference/delete-permission-group.md

# Delete Permission Group

```
DELETE 
/v1/permissions/:permissionGroupId
```

This endpoint removes a Permission Group identified by the `permissionGroupId` parameter.

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
