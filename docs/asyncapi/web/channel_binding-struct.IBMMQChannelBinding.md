asyncapi::channel_binding
# Struct IBMMQChannelBinding 
Source 

```
pub struct IBMMQChannelBinding {
    pub destination_type: Option<String>,
    pub queue: Option<IBMMQChannelBindingQueue>,
    pub topic: Option<IBMMQChannelBindingTopic>,
    pub max_msg_length: Option<i32>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`destination_type: Option<String>`

Defines the type of AsyncAPI channel.

MUST be either `topic` or `queue`. For type `topic`,
the AsyncAPI channel name MUST be assumed for the
IBM MQ topic string unless overridden.
§`queue: Option<IBMMQChannelBindingQueue>`

Defines the properties of a queue.

`queue` and `topic` fields MUST NOT coexist within a channel binding
§`topic: Option<IBMMQChannelBindingTopic>`

Defines the properties of a topic.

`queue` and `topic` fields MUST NOT coexist within a channel binding.
§`max_msg_length: Option<i32>`

The maximum length of the physical message (in bytes) accepted
by the Topic or Queue. Messages produced that are greater in size
than this value may fail to be delivered. More information on the
maximum message length can be found on this
page
in the IBM MQ Knowledge Center.

MUST be `0-104,857,600` bytes (100 MB).
§`binding_version: Option<String>`

The version of this binding.

## Trait Implementations§