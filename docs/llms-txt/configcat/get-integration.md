# Source: https://configcat.com/docs/api/reference/get-integration.md

# Get Integration

```
GET 
/v1/integrations/:integrationId
```

This endpoint returns the metadata of an Integration identified by the `integrationId`.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the integration data returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
