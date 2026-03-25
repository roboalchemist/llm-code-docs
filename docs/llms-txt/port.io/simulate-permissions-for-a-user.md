# Source: https://docs.port.io/api-reference/simulate-permissions-for-a-user.md

# Simulate permissions for a user

```
POST 
/v1/blueprints/:blueprint_identifier/permissions/simulate
```

This route allows you to simulate what permissions a specific user would have for entities in a blueprint. Provide a userIdentifier and operation to see which entities are accessible, or additionally provide an entityIdentifier to see detailed permission checks for that specific entity. To learn more, see the [permission simulator documentation](https://docs.port.io/build-your-software-catalog/set-catalog-rbac/set-catalog-rbac#permission-simulator).

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
