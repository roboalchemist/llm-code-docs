# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/git-hub-app-info.md

# gitHubAppInfo

Configuration for GitHub App integration.

### Examples

```graphql
type GitHubAppInfo {
  baseURL: String
  urlPath: String
  configText: String
}
```

### Fields

| Field               | Description                                            | Supported fields |
| ------------------- | ------------------------------------------------------ | ---------------- |
| baseURL `String`    | GitHub App base URL                                    |                  |
| urlPath `String`    | URL path leading to the GitHub App installation page   |                  |
| configText `String` | Configuration Text to be displayed on GitHub App modal |                  |

### References

#### Fields with this object

* [{} Connector.gitHubAppInfo](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
