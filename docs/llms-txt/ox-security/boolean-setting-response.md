# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/boolean-setting-response.md

# booleanSettingResponse

### Examples

```graphql
type BooleanSettingResponse {
  true: Float!
  false: Float!
}
```

### Fields

| Field          | Description                                      | Supported fields |
| -------------- | ------------------------------------------------ | ---------------- |
| true `Float!`  | Count of applications with `true` option chosen  |                  |
| false `Float!` | Count of applications with `false` option chosen |                  |

### References

#### Fields with this object

* [{} GetPipelineScanSettingsResponse.failOnTimeout](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
* [{} GetPipelineScanSettingsResponse.failOnError](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
* [{} GetPipelineScanSettingsResponse.scansEnabled](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
* [{} GetPipelineScanSettingsResponse.scanSummaryAsCommentEnabled](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
* [{} TriggeringEventResponse.value](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/triggering-event-response)
* [{} GetPipelineScanSettingsResponse.scansEnabledForBitbucketApp](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
* [{} GetPipelineScanSettingsResponse.scansEnabledForGitLabWebhooks](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
