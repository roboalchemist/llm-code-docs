# Source: https://docs.ox.security/api-documentation/api-reference/api--scan/types/objects/scan-in-progress-response.md

# scanInProgressResponse

Status information about an ongoing scan.

### Examples

```graphql
type ScanInProgressResponse {
  scanID: String
  isInProgress: Boolean
  scanStage: ScanStage
  isFullScan: Boolean
  isContainerFullScan: Boolean
  isSingleRepoScan: Boolean
  isDastFullScan: Boolean
}
```

### Fields

| Field                                                                                                              | Description                                                                | Supported fields |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ---------------- |
| scanID `String`                                                                                                    | Unique identifier of the scan                                              |                  |
| isInProgress `Boolean`                                                                                             | Indicates if a scan is currently running                                   |                  |
| scanStage [`ScanStage`](https://docs.ox.security/api-documentation/api-reference/api--scan/types/enums/scan-stage) | Current stage of the scan process                                          |                  |
| isFullScan `Boolean`                                                                                               | Indicates if this is a full code scan rather than an incremental scan      |                  |
| isContainerFullScan `Boolean`                                                                                      | Indicates if this is a full container scan rather than an incremental scan |                  |
| isSingleRepoScan `Boolean`                                                                                         | Indicates if this is a scan of a single repository                         |                  |
| isDastFullScan `Boolean`                                                                                           | Indicates if this is a full DAST scan rather than an incremental scan      |                  |

### References

#### Queries using this object

* [\<?> checkScanInProgress](https://docs.ox.security/api-documentation/api-reference/api--scan/queries/check-scan-in-progress)
