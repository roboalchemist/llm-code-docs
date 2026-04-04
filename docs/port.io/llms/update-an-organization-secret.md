# Source: https://docs.port.io/api-reference/update-an-organization-secret.md

# Update an organization secret

```
PATCH 
/v1/organization/secrets/:secret_name
```

This route allows you to update an organization secret.<br /><br />To learn more about secrets management, check out the [documentation](https://docs.port.io/sso-rbac/port-secrets).

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
