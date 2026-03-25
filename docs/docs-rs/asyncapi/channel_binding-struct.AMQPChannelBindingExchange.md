asyncapi::channel_binding
# Struct AMQPChannelBindingExchange 
Source 

```
pub struct AMQPChannelBindingExchange {
    pub name: Option<String>,
    pub typ: Option<String>,
    pub durable: Option<bool>,
    pub auto_delete: Option<bool>,
    pub vhost: Option<String>,
}
```

## Fields§
§`name: Option<String>`

The name of the exchange. It MUST NOT exceed 255 characters long.
§`typ: Option<String>`

The type of the exchange. Can be either
`topic`, `direct`, `fanout`, `default` or `headers`.
§`durable: Option<bool>`

Whether the exchange should survive broker restarts or not.
§`auto_delete: Option<bool>`

Whether the exchange should be deleted when the last queue is unbound from it.
§`vhost: Option<String>`

The virtual host of the exchange. Defaults to `/`.

## Trait Implementations§