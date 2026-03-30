# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/ox-workflow.md

# oxWorkflow

Fields related to OX Workflow.

### Examples

```graphql
type OxWorkflow {
  id: String
  name: String
}
```

### Fields

| Field         | Description                       | Supported fields |
| ------------- | --------------------------------- | ---------------- |
| id `String`   | Unique identifier of the workflow |                  |
| name `String` | Name of the workflow              |                  |

### References

#### Fields with this object

* [{} CICDFields.workflows](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/cicd-fields)
* [{} PipelineSummary.workflows](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary)
