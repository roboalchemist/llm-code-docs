# Source: https://configcat.com/docs/api/reference/get-settings-by-tag.md

# List Settings by Tag

```
GET 
/v1/tags/:tagId/settings
```

This endpoint returns the list of the Settings that has the specified Tag, identified by the `tagId` parameter.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the settings data returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
