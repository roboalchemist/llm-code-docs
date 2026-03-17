asyncapi::message_binding
# Struct HTTPMessageBinding 
Source 

```
pub struct HTTPMessageBinding {
    pub headers: Option<Schema>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`headers: Option<Schema>`

A Schema object containing the definitions for HTTP-specific headers.
This schema MUST be of type object and have a properties key.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§