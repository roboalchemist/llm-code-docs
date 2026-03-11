# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/extra-optional-creds.md

# extraOptionalCreds

Extra optional credentials for specific services.

### Examples

```graphql
type ExtraOptionalCreds {
  atlassian: AtlassianCredsOutput
}
```

### Fields

| Field                                                                                                                                             | Description                    | Supported fields                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------- |
| atlassian [`AtlassianCredsOutput`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/atlassian-creds-output) | Atlassian-specific credentials | <p>organizationId <code>String</code><br>apiKey <code>String</code></p> |

### References

#### Fields with this object

* [{} TokenCredentials.extraOptionalCreds](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-credentials)
* [{} UserPasswordCredentials.extraOptionalCreds](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/user-password-credentials)
