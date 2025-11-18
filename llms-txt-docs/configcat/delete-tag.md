# Source: https://configcat.com/docs/api/reference/delete-tag.md

# Delete Tag

```
DELETE 
/v1/tags/:tagId
```

This endpoint deletes a Tag identified by the `tagId` parameter. To remove a Tag from a Feature Flag or Setting use the [Update Flag](https://configcat.com/docs/docs/api/reference/update-setting/.md) endpoint.

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
