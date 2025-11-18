# Source: https://configcat.com/docs/api/reference/delete-integration.md

# Delete Integration

```
DELETE 
/v1/integrations/:integrationId
```

This endpoint removes a Integration identified by the `integrationId` parameter.

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
