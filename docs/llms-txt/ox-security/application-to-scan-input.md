# Source: https://docs.ox.security/api-documentation/api-reference/api--scan/types/inputs/application-to-scan-input.md

# applicationToScanInput

Configuration for an individual application to be scanned.

### Examples

```graphql
input ApplicationToScanInput {
  appId: String!
  appName: String!
  connectorId: String!
  credentialsId: String!
}
```

### Fields

| Field                   | Description                                             | Supported fields |
| ----------------------- | ------------------------------------------------------- | ---------------- |
| appId `String!`         | Unique identifier of the application                    |                  |
| appName `String!`       | Name of the application                                 |                  |
| connectorId `String!`   | Identifier of the connector to use for scanning         |                  |
| credentialsId `String!` | Identifier of the credentials to use for authentication |                  |

### References

#### Fields with this object

* [{} SingleRepoScanInput.applications](https://docs.ox.security/api-documentation/api-reference/api--scan/types/inputs/single-repo-scan-input)
