asyncapi::channel_binding
# Struct AMQPChannelBindingQueue 
Source 

```
pub struct AMQPChannelBindingQueue {
    pub name: Option<String>,
    pub durable: Option<bool>,
    pub exclusive: Option<bool>,
    pub auto_delete: Option<bool>,
    pub vhost: Option<String>,
}
```

## Fields§
§`name: Option<String>`

The name of the queue. It MUST NOT exceed 255 characters long.
§`durable: Option<bool>`

Whether the queue should survive broker restarts or not.
§`exclusive: Option<bool>`

Whether the queue should be used only by one connection or not.
§`auto_delete: Option<bool>`

Whether the queue should be deleted when the last consumer unsubscribes.
§`vhost: Option<String>`

The virtual host of the queue. Defaults to `/`.

## Trait Implementations§