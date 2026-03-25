# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/pipeline-settings-input.md

# pipelineSettingsInput

Pipeline scan settings for a workflow.

### Examples

```graphql
input PipelineSettingsInput {
  apps: [AppInput!]
}
```

### Fields

| Field                                                                                                                      | Description                                     | Supported fields                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| apps [`[AppInput!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/app-input) | List of applications for this pipeline workflow | <p>appId <code>String!</code><br>appName <code>String!</code><br>appType <code>String!</code><br>selected <code>Boolean!</code><br>disabled <code>Boolean!</code></p> |

### References

#### Fields with this object

* [{} UpdateWorkflowPolicyInput.pipelineSettings](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/update-workflow-policy-input)
