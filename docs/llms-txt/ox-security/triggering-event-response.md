# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/triggering-event-response.md

# triggeringEventResponse

### Examples

```graphql
type TriggeringEventResponse {
  type: TriggeringEventType!
  value: BooleanSettingResponse!
  label: String!
}
```

### Fields

| Field                                                                                                                                            | Description | Supported fields                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ------------------------------------------------------------ |
| type [`TriggeringEventType!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/enums/triggering-event-type)          |             |                                                              |
| value [`BooleanSettingResponse!`](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/boolean-setting-response) |             | <p>true <code>Float!</code><br>false <code>Float!</code></p> |
| label `String!`                                                                                                                                  |             |                                                              |

### References

#### Fields with this object

* [{} EventsTriggeringScansForBranchesSettingResponse.events](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/events-triggering-scans-for-branches-setting-response)
