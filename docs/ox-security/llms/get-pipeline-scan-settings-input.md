# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/get-pipeline-scan-settings-input.md

# getPipelineScanSettingsInput

Input payload for fetching pipeline scan settings for applications.

### Examples

```graphql
input GetPipelineScanSettingsInput {
  appIds: [String!]!
}
```

### Fields

| Field               | Description                            | Supported fields |
| ------------------- | -------------------------------------- | ---------------- |
| appIds `[String!]!` | Application IDs to fetch settings for. |                  |

### References

#### Queries using this object

* [\<?> getPipelineScanSettings.input](https://docs.ox.security/api-documentation/api-reference/api--pipeline/queries/get-pipeline-scan-settings)
