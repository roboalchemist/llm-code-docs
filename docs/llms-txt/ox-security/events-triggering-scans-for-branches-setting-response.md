# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/events-triggering-scans-for-branches-setting-response.md

# eventsTriggeringScansForBranchesSettingResponse

### Examples

```graphql
type EventsTriggeringScansForBranchesSettingResponse {
  branchNamePatternBranchSelection: String
  genericOptionBranchSelection: GenericOptionBranchSelectionType
  events: [TriggeringEventResponse!]!
}
```

### Fields

| Field                                                                                                                                                                                      | Description                                                                                    | Supported fields                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| branchNamePatternBranchSelection `String`                                                                                                                                                  | Either this or `genericOptionBranchSelection` is guaranteed to be provided by the resolver     |                                                                                                                                                                                                               |
| genericOptionBranchSelection [`GenericOptionBranchSelectionType`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/enums/generic-option-branch-selection-type) | Either this or `branchNamePatternBranchSelection` is guaranteed to be provided by the resolver |                                                                                                                                                                                                               |
| events [`[TriggeringEventResponse!]!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/triggering-event-response)                                     |                                                                                                | <p>type <a href="../enums/triggering-event-type"><code>TriggeringEventType!</code></a><br>value <a href="boolean-setting-response"><code>BooleanSettingResponse!</code></a><br>label <code>String!</code></p> |

### References

#### Fields with this object

* [{} GetPipelineScanSettingsResponse.eventsTriggeringScansForBranches](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
* [{} GetPipelineScanSettingsResponse.eventsTriggeringScansForBranchesForBitbucketApp](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
* [{} GetPipelineScanSettingsResponse.eventsTriggeringScansForBranchesForGitLabWebhooks](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
