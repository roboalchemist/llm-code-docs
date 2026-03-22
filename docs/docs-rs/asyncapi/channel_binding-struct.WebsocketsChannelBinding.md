asyncapi::channel_binding
# Struct WebsocketsChannelBinding 
Source 

```
pub struct WebsocketsChannelBinding {
    pub method: Option<String>,
    pub query: Option<Schema>,
    pub headers: Option<Schema>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`method: Option<String>`

The HTTP method to use when establishing the connection.
Its value MUST be either `GET` or `POST`.
§`query: Option<Schema>`

A Schema object containing the definitions for each query parameter.
This schema MUST be of type `object` and have a `properties` key.
§`headers: Option<Schema>`

A Schema object containing the definitions of the HTTP headers to use when
establishing the connection. This schema MUST be of type `object` and have
a `properties` key.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§