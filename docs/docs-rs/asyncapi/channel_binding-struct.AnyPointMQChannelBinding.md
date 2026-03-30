asyncapi::channel_binding
# Struct AnyPointMQChannelBinding 
Source 

```
pub struct AnyPointMQChannelBinding {
    pub destination: Option<String>,
    pub destination_type: Option<String>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`destination: Option<String>`

**Optional**, defaults to the channel name. The destination (queue or exchange)
name for this channel. SHOULD only be specified if the channel name differs
from the actual destination name, such as when the channel name is not a valid
destination name in Anypoint MQ.
§`destination_type: Option<String>`

**Optional**, defaults to `queue`. The type of destination, which MUST be
either `exchange` or `queue` or `fifo-queue`. SHOULD be specified to document
the messaging model (publish/subscribe, point-to-point, strict message
ordering) supported by this channel.
§`binding_version: Option<String>`

**Optional**, defaults to `latest`. The version of this binding.

## Trait Implementations§