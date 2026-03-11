# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-artifact-info.md

# pipelineArtifactInfo

Minimal info about pipeline artifact.

### Examples

```graphql
type PipelineArtifactInfo {
  name: String!
  tag: String!
  digest: String!
}
```

### Fields

| Field            | Description            | Supported fields |
| ---------------- | ---------------------- | ---------------- |
| name `String!`   | Artifact name          |                  |
| tag `String!`    | Artifact tag           |                  |
| digest `String!` | Artifact digest (hash) |                  |

### References

#### Fields with this object

* [{} PipelineSummary.artifactInfo](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary)
