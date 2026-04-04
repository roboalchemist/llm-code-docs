# Source: https://docs.port.io/api-reference/update-an-integration.md

# Update an integration

```
PATCH 
/v1/integration/:identifier
```

This route allows you to modify an integration in your Port organization.<br /><br />To learn more about integrations, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/).<br /><br />**Note:** To trigger a resync of an integration without changing its mapping, simply provide its identifier and leave the body empty.

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404
* 413
* 422

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
