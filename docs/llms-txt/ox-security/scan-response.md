# Source: https://docs.ox.security/api-documentation/api-reference/api--scan/types/objects/scan-response.md

# scanResponse

Response containing information about a triggered scan.

### Examples

```graphql
type ScanResponse {
  scanID: String
  isFullScan: Boolean
  isContainerFullScan: Boolean
  isSingleRepoScan: Boolean
  isDastFullScan: Boolean
  isDastSingleTarget: Boolean
  scannerTag: String
}
```

### Fields

| Field                         | Description                                                                | Supported fields |
| ----------------------------- | -------------------------------------------------------------------------- | ---------------- |
| scanID `String`               | Unique identifier for tracking the scan progress                           |                  |
| isFullScan `Boolean`          | Indicates if this is a full code scan rather than an incremental scan      |                  |
| isContainerFullScan `Boolean` | Indicates if this is a full container scan rather than an incremental scan |                  |
| isSingleRepoScan `Boolean`    | Indicates if this is a scan of a single repository                         |                  |
| isDastFullScan `Boolean`      | Indicates if this is a full DAST scan rather than an incremental scan      |                  |
| isDastSingleTarget `Boolean`  | Indicates if this is a single DAST target scan                             |                  |
| scannerTag `String`           | Scanner image tag                                                          |                  |

### References

#### Mutations using this object

* [<\~> scanAll](https://docs.ox.security/api-documentation/api-reference/api--scan/mutations/scan-all)
* [<\~> singleRepoScan](https://docs.ox.security/api-documentation/api-reference/api--scan/mutations/single-repo-scan)
* [<\~> triggerSingleTargetScan](https://docs.ox.security/api-documentation/api-reference/api--scan/mutations/trigger-single-target-scan)
