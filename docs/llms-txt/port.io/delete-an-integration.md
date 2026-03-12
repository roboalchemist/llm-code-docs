# Source: https://docs.port.io/api-reference/delete-an-integration.md

# Delete an integration

```
DELETE 
/v1/integration/:identifier
```

This route allows you to delete an integration in your Port organization.<br /><br />To learn more about integrations, check out the [documentation](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/).

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
