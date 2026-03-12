# Source: https://docs.port.io/api-reference/update-an-integrations-config.md

# Update an integration's config

```
PATCH 
/v1/integration/:identifier/config
```

This route allows you to modify an integration's configuration in your Port organization.<br /><br />To learn more about integrations, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404
* 413
* 422

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
