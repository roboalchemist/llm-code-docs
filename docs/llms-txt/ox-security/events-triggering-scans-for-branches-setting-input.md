# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/events-triggering-scans-for-branches-setting-input.md

# eventsTriggeringScansForBranchesSettingInput

Branch selection and events that trigger scans.

### Examples

```graphql
input EventsTriggeringScansForBranchesSettingInput {
  branchNamePatternBranchSelection: String
  genericOptionBranchSelection: GenericOptionBranchSelectionType
  events: [TriggeringEventInput!]!
}
```

### Fields

| Field                                                                                                                                                                                      | Description                                  | Supported fields                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| branchNamePatternBranchSelection `String`                                                                                                                                                  | Branch name pattern to match.                |                                                                                                                           |
| genericOptionBranchSelection [`GenericOptionBranchSelectionType`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/enums/generic-option-branch-selection-type) | Predefined branch selection option.          |                                                                                                                           |
| events [`[TriggeringEventInput!]!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/triggering-event-input)                                            | Events that trigger scans for the selection. | <p>type <a href="../enums/triggering-event-type"><code>TriggeringEventType!</code></a><br>value <code>Boolean!</code></p> |

### References

#### Fields with this object

* [{} SetPipelineScanSettingsInput.eventsTriggeringScansForBranches](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/set-pipeline-scan-settings-input)
* [{} SetPipelineScanSettingsInput.eventsTriggeringScansForBranchesForBitbucketApp](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/set-pipeline-scan-settings-input)
* [{} SetPipelineScanSettingsInput.eventsTriggeringScansForBranchesForGitLabWebhooks](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/set-pipeline-scan-settings-input)
