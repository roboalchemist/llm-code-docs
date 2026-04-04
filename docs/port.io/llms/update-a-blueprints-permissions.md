# Source: https://docs.port.io/api-reference/update-a-blueprints-permissions.md

# Update a blueprint's permissions

```
PATCH 
/v1/blueprints/:blueprint_identifier/permissions
```

This route allows you to update the permissions of a blueprint.<br /><br />To learn more about permissions, check out the [documentation](https://docs.port.io/build-your-software-catalog/set-catalog-rbac/examples).

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
