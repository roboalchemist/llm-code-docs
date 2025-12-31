# Source: https://configcat.com/docs/api/reference/get-permission-group.md

# Get Permission Group

```
GET 
/v1/permissions/:permissionGroupId
```

This endpoint returns the metadata of a Permission Group identified by the `permissionGroupId`.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the permission group data returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
