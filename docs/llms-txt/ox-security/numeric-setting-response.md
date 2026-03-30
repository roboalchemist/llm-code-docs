# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/numeric-setting-response.md

# numericSettingResponse

### Examples

```graphql
type NumericSettingResponse {
  option: Float!
  count: Float!
}
```

### Fields

| Field           | Description                                                    | Supported fields |
| --------------- | -------------------------------------------------------------- | ---------------- |
| option `Float!` | Numeric option, i.e. 5, 10, 15...                              |                  |
| count `Float!`  | Count of applications with this specific numeric option chosen |                  |

### References

#### Fields with this object

* [{} GetPipelineScanSettingsResponse.timeout](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/get-pipeline-scan-settings-response)
