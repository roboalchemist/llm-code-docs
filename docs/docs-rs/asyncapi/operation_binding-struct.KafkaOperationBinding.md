asyncapi::operation_binding
# Struct KafkaOperationBinding 
Source 

```
pub struct KafkaOperationBinding {
    pub group_id: Option<Schema>,
    pub client_id: Option<Schema>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`group_id: Option<Schema>`

Id of the consumer group.
§`client_id: Option<Schema>`

Id of the consumer inside a consumer group.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§