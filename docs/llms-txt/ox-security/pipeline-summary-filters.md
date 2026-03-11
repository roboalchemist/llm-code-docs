# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/pipeline-summary-filters.md

# pipelineSummaryFilters

Filter criteria for searching and filtering pipeline summary data.

### Examples

```graphql
input PipelineSummaryFilters {
  apps: [String]
  result: [String]
  jobTriggeredBy: [String]
  sourceBranches: [String]
  targetBranches: [String]
  severities: [String]
  eventTypes: [String]
  cicdTypes: [String]
  tags: [String]
  jobId: [String]
  scanCompletionStatus: [String]
  pipelineScanType: [String]
  pipelineArtifactName: [String]
  pipelineArtifactTag: [String]
  workflows: [String]
}
```

### Fields

| Field                           | Description                                                                       | Supported fields |
| ------------------------------- | --------------------------------------------------------------------------------- | ---------------- |
| apps `[String]`                 | Filter by specific application names                                              |                  |
| result `[String]`               | Filter by pipeline execution results (passed, failed, etc.)                       |                  |
| jobTriggeredBy `[String]`       | Filter by users or systems that triggered the pipeline jobs                       |                  |
| sourceBranches `[String]`       | Filter by source branch names                                                     |                  |
| targetBranches `[String]`       | Filter by target branch names (usually main, master, develop)                     |                  |
| severities `[String]`           | Filter by security issue severity levels                                          |                  |
| eventTypes `[String]`           | Filter by pipeline event types (push, pull request, manual, etc.)                 |                  |
| cicdTypes `[String]`            | Filter by CI/CD platform types (GitHub Actions, Jenkins, GitLab CI, etc.)         |                  |
| tags `[String]`                 | Filter by tag names associated with the pipeline                                  |                  |
| jobId `[String]`                | Filter by specific job identifiers                                                |                  |
| scanCompletionStatus `[String]` | Filter by scan completion status (success, timeout, failure)                      |                  |
| pipelineScanType `[String]`     | Filter by pipeline scan type (Source Code, Source Code (IDE), Pipeline Container) |                  |
| pipelineArtifactName `[String]` | Filter by pipeline artifact name                                                  |                  |
| pipelineArtifactTag `[String]`  | Filter by pipeline artifact tag                                                   |                  |
| workflows `[String]`            | Filter by workflow                                                                |                  |

### References

#### Fields with this object

* [{} GetPipelineSummaryInput.filters](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/get-pipeline-summary-input)
