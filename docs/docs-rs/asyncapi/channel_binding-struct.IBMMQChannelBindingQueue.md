asyncapi::channel_binding
# Struct IBMMQChannelBindingQueue 
Source 

```
pub struct IBMMQChannelBindingQueue {
    pub object_name: String,
    pub is_partitioned: Option<bool>,
    pub exclusive: Option<bool>,
}
```

## Fields§
§`object_name: String`

Defines the name of the IBM MQ queue associated with the channel.

A value MUST be specified. MUST NOT exceed 48 characters in length.
MUST be a valid IBM MQ queue name
§`is_partitioned: Option<bool>`

Defines if the queue is a cluster queue and therefore partitioned.
If true, a binding option MAY be specified when accessing the queue.
More information on binding options can be found on this
page
in the IBM MQ Knowledge Center.

If `false`, binding options SHOULD NOT be specified when accessing the queue.
§`exclusive: Option<bool>`

Specifies if it is recommended to open the queue exclusively.

## Trait Implementations§