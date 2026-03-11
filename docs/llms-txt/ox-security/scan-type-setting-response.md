# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/scan-type-setting-response.md

# scanTypeSettingResponse

### Examples

```graphql
type ScanTypeSettingResponse {
  type: String!
  count: Float!
  tooltip: String!
}
```

### Fields

| Field             | Description                                            | Supported fields |
| ----------------- | ------------------------------------------------------ | ---------------- |
| type `String!`    | Scan speed                                             |                  |
| count `Float!`    | Count of applications with this specific option chosen |                  |
| tooltip `String!` | Tooltip for scan speed                                 |                  |

### References

#### Fields with this object

* [{} GetPipelineScanSettingsResponse.performance](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
