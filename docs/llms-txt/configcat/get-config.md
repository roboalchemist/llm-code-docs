# Source: https://configcat.com/docs/api/reference/get-config.md

# Get Config

```
GET 
/v1/configs/:configId
```

This endpoint returns the metadata of a Config identified by the `configId`.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

When everything is ok, the config data returned.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
