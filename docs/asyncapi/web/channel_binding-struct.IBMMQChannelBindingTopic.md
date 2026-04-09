asyncapi::channel_binding
# Struct IBMMQChannelBindingTopic 
Source 

```
pub struct IBMMQChannelBindingTopic {
    pub string: Option<String>,
    pub object_name: Option<String>,
    pub durable_permitted: Option<bool>,
    pub last_msg_retained: Option<bool>,
}
```

## Fields§
§`string: Option<String>`

The value of the IBM MQ topic string to be used.

Note: if specified, SHALL override AsyncAPI channel name.

MUST NOT exceed 10240 characters in length.
MAY coexist with `topic.objectName`
§`object_name: Option<String>`

The name of the IBM MQ topic object.

Note: if specified, SHALL override AsyncAPI channel name.

MUST NOT exceed 48 characters in length.
MAY coexist with `topic.string`
§`durable_permitted: Option<bool>`

Defines if the subscription may be durable.
§`last_msg_retained: Option<bool>`

Defines if the last message published will be made
available to new subscriptions.

## Trait Implementations§