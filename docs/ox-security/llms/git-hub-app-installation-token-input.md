# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/git-hub-app-installation-token-input.md

# gitHubAppInstallationTokenInput

### Examples

```graphql
input GitHubAppInstallationTokenInput {
  token: String!
  createdAt: String
  expiresAt: String
}
```

### Fields

| Field              | Description                                       | Supported fields |
| ------------------ | ------------------------------------------------- | ---------------- |
| token `String!`    | access token issued for a GitHub App installation |                  |
| createdAt `String` | UTC timestamp                                     |                  |
| expiresAt `String` | UTC timestamp                                     |                  |

### References

#### Fields with this object

* [{} CredentialsInput.installationToken](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/credentials-input)
