asyncapi::operation_binding
# Struct MQTTOperationBinding 
Source 

```
pub struct MQTTOperationBinding {
    pub qos: Option<i32>,
    pub retain: Option<bool>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`qos: Option<i32>`

Defines the Quality of Service (QoS) levels for the message flow between client
and server. Its value MUST be either 0 (At most once delivery),
1 (At least once delivery), or 2 (Exactly once delivery).
§`retain: Option<bool>`

Whether the broker should retain the message or not.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§