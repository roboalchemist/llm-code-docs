# Source: https://docs.ox.security/api-documentation/api-reference/api--scan/types/inputs/single-repo-scan-input.md

# singleRepoScanInput

Input for specifying repositories to scan.

### Examples

```graphql
input SingleRepoScanInput {
  applications: [ApplicationToScanInput]!
}
```

### Fields

| Field                                                                                                                                                 | Description                        | Supported fields                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| applications [`[ApplicationToScanInput]!`](https://docs.ox.security/api-documentation/api-reference/api--scan/types/inputs/application-to-scan-input) | List of applications to be scanned | <p>appId <code>String!</code><br>appName <code>String!</code><br>connectorId <code>String!</code><br>credentialsId <code>String!</code></p> |

### References

#### Mutations using this object

* [<\~> singleRepoScan.singleRepoScanInput](https://docs.ox.security/api-documentation/api-reference/api--scan/mutations/single-repo-scan)
