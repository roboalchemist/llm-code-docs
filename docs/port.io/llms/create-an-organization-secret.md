# Source: https://docs.port.io/api-reference/create-an-organization-secret.md

# Create an organization secret

```
POST 
/v1/organization/secrets
```

This route allows you to create an organization secret.<br /><br />To learn more about secrets management in Port, check out the [documentation](https://docs.port.io/sso-rbac/port-secrets).

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
