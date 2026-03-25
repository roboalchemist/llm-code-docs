asyncapi
# Struct Components 
Source 

```
pub struct Components {}
```

## Fields§
§`schemas: IndexMap<String, ReferenceOr<Schema>>`

An object to hold reusable
Schema Objects.
§`messages: IndexMap<String, ReferenceOr<Message>>`

An object to hold reusable
Message Objects.
§`security_schemes: IndexMap<String, ReferenceOr<SecurityScheme>>`

An object to hold reusable
Security Scheme Objects.
§`parameters: IndexMap<String, ReferenceOr<Parameter>>`

An object to hold reusable
Parameter Objects.
§`correlation_ids: IndexMap<String, ReferenceOr<CorrelationId>>`

An object to hold reusable
Correlation ID Objects.
§`operation_traits: IndexMap<String, ReferenceOr<OperationTrait>>`

An object to hold reusable
Operation Trait Objects.
§`message_traits: IndexMap<String, ReferenceOr<MessageTrait>>`

An object to hold reusable
Message Trait Objects.
§`servers: IndexMap<String, ReferenceOr<Server>>`

An object to hold reusable Server Objects.
§`server_bindings: IndexMap<String, ReferenceOr<ServerBinding>>`

An object to hold reusable
Server Bindings Objects.
§`channels: IndexMap<String, Channel>`

An object to hold reusable Channel Item Objects.
§`channel_bindings: IndexMap<String, ReferenceOr<ChannelBinding>>`

An object to hold reusable
Channel Bindings Objects.
§`operation_bindings: IndexMap<String, ReferenceOr<OperationBinding>>`

An object to hold reusable
Operation Bindings Objects.
§`message_bindings: IndexMap<String, ReferenceOr<MessageBinding>>`

An object to hold reusable
Message Bindings Objects.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§