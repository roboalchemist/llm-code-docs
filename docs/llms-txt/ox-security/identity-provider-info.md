# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/identity-provider-info.md

# identityProviderInfo

Configuration for identity provider integration.

### Examples

```graphql
type IdentityProviderInfo {
  baseURL: String
  urlParams: String
  scope: String
  configText: String
  user_scope: String
}
```

### Fields

| Field                | Description                                         | Supported fields |
| -------------------- | --------------------------------------------------- | ---------------- |
| baseURL `String`     | Base URL of the identity provider                   |                  |
| urlParams `String`   | URL parameters for identity provider authentication |                  |
| scope `String`       | Required permission scopes                          |                  |
| configText `String`  | Instructions for configuring the identity provider  |                  |
| user\_scope `String` | Optional user-specific permission scopes            |                  |

### References

#### Fields with this object

* [{} Connector.identityProviderInfo](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
