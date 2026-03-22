asyncapi::message_binding
# Struct KafkaMessageBinding 
Source 

```
pub struct KafkaMessageBinding {
    pub key: Option<Schema>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`key: Option<Schema>`

The message key.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§