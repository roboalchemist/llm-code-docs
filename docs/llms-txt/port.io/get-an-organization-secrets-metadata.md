# Source: https://docs.port.io/api-reference/get-an-organization-secrets-metadata.md

# Get an organization secret's metadata

```
GET 
/v1/organization/secrets/:secret_name
```

This route allows you to retrieve metadata about a specific secret in your organization. Note that this endpoint returns only the metadata of the secret, not the secret content itself.<br /><br />To learn more about secrets management in Port, check out the [documentation](https://docs.port.io/sso-rbac/port-secrets).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404

Default Response

Default Response

A resource with the provided identifier was not found
