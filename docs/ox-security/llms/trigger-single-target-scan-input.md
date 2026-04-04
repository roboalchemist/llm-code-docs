# Source: https://docs.ox.security/api-documentation/api-reference/api--scan/types/inputs/trigger-single-target-scan-input.md

# triggerSingleTargetScanInput

Input for triggering a single DAST target scan.

### Examples

```graphql
input TriggerSingleTargetScanInput {
  targetId: String!
}
```

### Fields

| Field              | Description            | Supported fields |
| ------------------ | ---------------------- | ---------------- |
| targetId `String!` | DAST target ID to scan |                  |

### References

#### Mutations using this object

* [<\~> triggerSingleTargetScan.triggerSingleTargetScanInput](https://docs.ox.security/api-documentation/api-reference/api--scan/mutations/trigger-single-target-scan)
