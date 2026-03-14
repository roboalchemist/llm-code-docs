# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/triggering-event-input.md

# triggeringEventInput

Triggering event configuration for branch scan settings.

### Examples

```graphql
input TriggeringEventInput {
  type: TriggeringEventType!
  value: Boolean!
}
```

### Fields

| Field                                                                                                                                   | Description                                         | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------- |
| type [`TriggeringEventType!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/enums/triggering-event-type) | Event type that can trigger a scan.                 |                  |
| value `Boolean!`                                                                                                                        | Whether the event triggers scans for the selection. |                  |

### References

#### Fields with this object

* [{} EventsTriggeringScansForBranchesSettingInput.events](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/inputs/events-triggering-scans-for-branches-setting-input)
