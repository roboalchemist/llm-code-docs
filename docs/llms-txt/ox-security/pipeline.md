# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/pipeline.md

# pipeline

Source type for application tool coverage information, indicating how security tools are integrated.

### Examples

```graphql
type Pipeline {
  jobId: String
  jobTriggeredAt: Float
  scanResult: PipelineScanResult
  issuesCount: Int
  jobTriggeredBy: String
  jobUrl: String
}
```

### Fields

| Field                                                                                                                                         | Description                                                        | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------- |
| jobId `String`                                                                                                                                | The unique identifier of the job associated with the pipeline scan |                  |
| jobTriggeredAt `Float`                                                                                                                        | The timestamp when the pipeline job was triggered                  |                  |
| scanResult [`PipelineScanResult`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/pipeline-scan-result) | The result of the pipeline scan                                    |                  |
| issuesCount `Int`                                                                                                                             | The number of issues detected during the scan                      |                  |
| jobTriggeredBy `String`                                                                                                                       | The user or system that triggered the pipeline job                 |                  |
| jobUrl `String`                                                                                                                               | The URL link to the pipeline job details                           |                  |

### References

#### Fields with this object

* [{} Application.pipeline](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
