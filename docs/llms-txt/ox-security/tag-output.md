# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/tag-output.md

# tagOutput

Tag information associated with pipeline executions.

### Examples

```graphql
type TagOutput {
  tagId: String
  tagType: String
  name: String
  displayName: String
  createdBy: String
  appliedBy: String
  tagCategory: String
}
```

### Fields

| Field                | Description                                    | Supported fields |
| -------------------- | ---------------------------------------------- | ---------------- |
| tagId `String`       | Unique identifier for the tag                  |                  |
| tagType `String`     | Type of tag (environment, team, project, etc.) |                  |
| name `String`        | Tag name                                       |                  |
| displayName `String` | Human-readable display name for the tag        |                  |
| createdBy `String`   | User who created the tag                       |                  |
| appliedBy `String`   | User who applied the tag to the pipeline       |                  |
| tagCategory `String` | Category or classification of the tag          |                  |

### References

#### Fields with this object

* [{} PipelineSummary.tags](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary)
