asyncapi
# Struct Message 
Source 

```
pub struct Message {}
```

## Fields§
§`headers: Option<ReferenceOr<Schema>>`

Schema definition of the application headers.
Schema MUST be of type “object”. It **MUST NOT** define the protocol headers.
§`payload: Option<Payload>`

Definition of the message payload. It can be of any type
but defaults to Schema object. It must match the schema format,
including encoding type - e.g Avro should be inlined as either
a YAML or JSON object NOT a string to be parsed as YAML or JSON.
§`correlation_id: Option<ReferenceOr<CorrelationId>>`

Definition of the correlation ID used for message tracing or matching.
§`schema_format: Option<String>`

A string containing the name of the schema
format/language used to define the message payload.
If omitted, implementations should parse the payload as a
Schema object.
§`content_type: Option<String>`

The content type to use when encoding/decoding a message’s payload.
The value MUST be a specific media type (e.g. application/json).
When omitted, the value MUST be the one specified on the defaultContentType field.
§`name: Option<String>`

A machine-friendly name for the message.
§`title: Option<String>`

A human-friendly title for the message.
§`summary: Option<String>`

A short summary of what the message is about.
§`description: Option<String>`

A verbose explanation of the message.
CommonMark syntax
can be used for rich text representation.
§`tags: Vec<Tag>`

A list of tags for API documentation control.
Tags can be used for logical grouping of messages.
§`external_docs: Option<ExternalDocumentation>`

Additional external documentation for this message.
§`bindings: Option<ReferenceOr<MessageBinding>>`

A map where the keys describe the name of
the protocol and the values describe protocol-specific definitions for the message.
§`examples: Vec<Example>`

An array with examples of valid message objects.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§