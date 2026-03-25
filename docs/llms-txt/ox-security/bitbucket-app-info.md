# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/bitbucket-app-info.md

# bitbucketAppInfo

Configuration for Bitbucket App integration.

### Examples

```graphql
type BitbucketAppInfo {
  baseURL: String
  queryParameters: [String]
  configText: String
}
```

### Fields

| Field                      | Description                                                       | Supported fields |
| -------------------------- | ----------------------------------------------------------------- | ---------------- |
| baseURL `String`           | Bitbucket App base URL                                            |                  |
| queryParameters `[String]` | '=' delimited query parameter key/value pairs appended to baseURL |                  |
| configText `String`        | Configuration Text to be displayed on Bitbucket App modal         |                  |

### References

#### Fields with this object

* [{} Connector.bitbucketAppInfo](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector)
