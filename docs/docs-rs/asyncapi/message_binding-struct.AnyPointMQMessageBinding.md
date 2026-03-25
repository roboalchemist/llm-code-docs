asyncapi::message_binding
# Struct AnyPointMQMessageBinding 
Source 

```
pub struct AnyPointMQMessageBinding {
    pub headers: Option<Schema>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`headers: Option<Schema>`

**Optional**. A Schema object containing the definitions for Anypoint MQ-specific headers
(so-called protocol headers). This schema MUST be of type object and have a properties key.
Examples of Anypoint MQ protocol headers are messageId and messageGroupId.
§`binding_version: Option<String>`

**Optional**, defaults to `latest`. The version of this binding.

## Trait Implementations§