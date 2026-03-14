# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/enums/pipeline-scan-completion-status.md

# pipelineScanCompletionStatus

Status of pipeline scan completion indicating the outcome of the security analysis.

### Examples

```graphql
enum PipelineScanCompletionStatus {
  Success
  Timeout
  Failure
}
```

### Enum values

| Enum value | Description                                               |
| ---------- | --------------------------------------------------------- |
| Success    | Scan completed successfully with all checks passing       |
| Timeout    | Scan exceeded the maximum allowed time and was terminated |
| Failure    | Scan failed to complete due to errors                     |

### References

#### Fields with this object

* [{} PipelineSummary.scanCompletionStatus](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary)
