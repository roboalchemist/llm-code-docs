# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/set-pipeline-scan-settings-response.md

# setPipelineScanSettingsResponse

Result of updating pipeline scan settings.

### Examples

```graphql
type SetPipelineScanSettingsResponse {
  success: Boolean!
}
```

### Fields

| Field              | Description                                          | Supported fields |
| ------------------ | ---------------------------------------------------- | ---------------- |
| success `Boolean!` | Whether all settings updates completed successfully. |                  |

### References

#### Mutations using this object

* [<\~> setPipelineScanSettings](https://docs.ox.security/api-documentation/api-reference/api--pipeline/mutations/set-pipeline-scan-settings)
