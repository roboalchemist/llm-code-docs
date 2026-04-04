# Source: https://configcat.com/docs/api/reference/create-setting.md

# Create Flag

Copy page

This endpoint creates a new Feature Flag or Setting in a specified Config identified by the `configId` parameter.

**Important:** The `key` attribute must be unique within the given Config.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 201
* 400
* 404
* 429

When the creation was successful.

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
