# Source: https://docs.port.io/api-reference/get-all-organization-secrets-metadata.md

# Get all organization secrets' metadata

```
GET 
/v1/organization/secrets
```

This route allows you to retrieve metadata about all secrets in your organization. Note that this endpoint returns only the metadata of the secrets, not the secret content itself.<br /><br />To learn more about secrets management in Port, check out the [documentation](https://docs.port.io/sso-rbac/port-secrets).

## Responses[â](#responses "Direct link to Responses")

* 401
* 404

Default Response

A resource with the provided identifier was not found
