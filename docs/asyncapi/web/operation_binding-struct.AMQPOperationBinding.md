asyncapi::operation_binding
# Struct AMQPOperationBinding 
Source 

```
pub struct AMQPOperationBinding {
    pub expiration: Option<i32>,
    pub user_id: Option<String>,
    pub cc: Vec<String>,
    pub priority: Option<i32>,
    pub delivery_mode: Option<i32>,
    pub mandatory: Option<bool>,
    pub bcc: Vec<String>,
    pub reply_to: Option<String>,
    pub timestamp: Option<bool>,
    pub ack: Option<bool>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`expiration: Option<i32>`

TTL (Time-To-Live) for the message. It MUST be greater than or equal to zero.
§`user_id: Option<String>`

Identifies the user who has sent the message.
§`cc: Vec<String>`

The routing keys the message should be routed to at the time of publishing.
§`priority: Option<i32>`

A priority for the message.
§`delivery_mode: Option<i32>`

Delivery mode of the message. Its value MUST be either 1 (transient) or 2 (persistent).
§`mandatory: Option<bool>`

Whether the message is mandatory or not.
§`bcc: Vec<String>`

Like cc but consumers will not receive this information.
§`reply_to: Option<String>`

Name of the queue where the consumer should send the response.
§`timestamp: Option<bool>`

Whether the message should include a timestamp or not.
§`ack: Option<bool>`

Whether the consumer should ack the message or not.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§