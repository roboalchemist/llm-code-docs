# Source: https://docs.port.io/api-reference/update-an-actions-permissions.md

# Update an action's permissions

```
PATCH 
/v1/actions/:action_identifier/permissions
```

This route allows you to update the permissions of a self-service action.<br /><br />To learn more about action RBAC, check out the [documentation](https://docs.port.io/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/).

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
