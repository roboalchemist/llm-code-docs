asyncapi::message_binding
# Struct AMQPMessageBinding 
Source 

```
pub struct AMQPMessageBinding {
    pub content_encoding: Option<String>,
    pub message_type: Option<String>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`content_encoding: Option<String>`

A MIME encoding for the message content.
§`message_type: Option<String>`

Application-specific message type.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§