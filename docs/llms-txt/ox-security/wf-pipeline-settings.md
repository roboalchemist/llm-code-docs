# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-pipeline-settings.md

# wfPipelineSettings

### Examples

```graphql
type WfPipelineSettings {
  apps: [WfApp!]
}
```

### Fields

| Field                                                                                                                 | Description | Supported fields                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| apps [`[WfApp!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-app) |             | <p>appName <code>String</code><br>appType <code>String</code><br>appId <code>String</code><br>selected <code>Boolean</code><br>disabled <code>Boolean</code></p> |

### References

#### Fields with this object

* [{} WorkflowPolicy.wfPipelineSettings](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/workflow-policy)
