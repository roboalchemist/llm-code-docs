# Source: https://docs.port.io/api-reference/cancel-a-migration.md

# Cancel a migration

```
POST 
/v1/migrations/:migration_id/cancel
```

This route allows you to cancel a running migration in your Port organization.

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
