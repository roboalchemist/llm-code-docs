asyncapi::channel_binding
# Struct AMQPChannelBinding 
Source 

```
pub struct AMQPChannelBinding {
    pub is: Option<String>,
    pub exchange: Option<AMQPChannelBindingExchange>,
    pub queue: Option<AMQPChannelBindingQueue>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`is: Option<String>`

Defines what type of channel is it. Can be either `queue` or `routingKey` (default).
§`exchange: Option<AMQPChannelBindingExchange>`

When `is`=`routingKey`, this object defines the exchange properties.
§`queue: Option<AMQPChannelBindingQueue>`

When `is`=`queue`, this object defines the queue properties.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§