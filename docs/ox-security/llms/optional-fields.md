# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/optional-fields.md

# optionalFields

Optional configuration fields for connectors.

### Examples

```graphql
type OptionalFields {
  SSHKey: String
  RepoSearchQuery: String
  Config: String
  buildIssueToCloud: Boolean
}
```

### Fields

| Field                       | Description                               | Supported fields |
| --------------------------- | ----------------------------------------- | ---------------- |
| SSHKey `String`             | SSH key for repository access             |                  |
| RepoSearchQuery `String`    | Custom query for repository search        |                  |
| Config `String`             | Additional configuration in string format |                  |
| buildIssueToCloud `Boolean` | Flag to enable building issues to cloud   |                  |

### References

#### Fields with this object

* [{} TokenCredentials.optionalFields](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-credentials)
* [{} ClientIdSecretApiUrlCredentials.optionalFields](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/client-id-secret-api-url-credentials)
* [{} OrganizationIdAndClientIdSecretApiUrlCredentials.optionalFields](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/organization-id-and-client-id-secret-api-url-credentials)
* [{} TokenOnlyCredentials.optionalFields](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/token-only-credentials)
