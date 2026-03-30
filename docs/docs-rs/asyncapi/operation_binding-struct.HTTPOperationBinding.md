asyncapi::operation_binding
# Struct HTTPOperationBinding 
Source 

```
pub struct HTTPOperationBinding {
    pub typ: String,
    pub method: Option<String>,
    pub query: Option<Schema>,
    pub binding_version: Option<String>,
}
```

## Fields§
§`typ: String`

Required. Type of operation. Its value MUST be either `request` or `response`.
§`method: Option<String>`

When `type` is `request`, this is the HTTP method, otherwise it MUST be ignored.
Its value MUST be one of `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`,
`OPTIONS`, `CONNECT`, and `TRACE`.
§`query: Option<Schema>`

A Schema object containing the definitions for each query parameter.
This schema MUST be of type `object` and have a `properties` key.
§`binding_version: Option<String>`

The version of this binding. If omitted, “latest” MUST be assumed.

## Trait Implementations§