asyncapi
# Struct Operation 
Source 

```
pub struct Operation {
    pub operation_id: Option<String>,
    pub summary: Option<String>,
    pub description: Option<String>,
    pub tags: Vec<Tag>,
    pub external_docs: Option<ExternalDocumentation>,
    pub bindings: Option<ReferenceOr<OperationBinding>>,
    pub traits: Vec<ReferenceOr<OperationTrait>>,
    pub message: Option<OperationMessageType>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`operation_id: Option<String>`

Unique string used to identify the operation.
The id MUST be unique among all operations described in the API.
The operationId value is **case-sensitive**.
Tools and libraries MAY use the operationId to uniquely identify an
operation, therefore, it is RECOMMENDED to follow common programming
naming conventions.
§`summary: Option<String>`

A short summary of what the operation is about.
§`description: Option<String>`

A verbose explanation of the operation.
CommonMark syntax
can be used for rich text representation.
§`tags: Vec<Tag>`

A list of tags for API documentation control.
Tags can be used for logical grouping of operations.
§`external_docs: Option<ExternalDocumentation>`

Additional external documentation for this operation.
§`bindings: Option<ReferenceOr<OperationBinding>>`

A map where the keys describe the name of the protocol and the
values describe protocol-specific definitions for the operation.
§`traits: Vec<ReferenceOr<OperationTrait>>`

A list of traits to apply to the operation object.
Traits MUST be merged into the operation object using the
JSON Merge Patch
algorithm in the same order they are defined here.
§`message: Option<OperationMessageType>`

A definition of the message that will be published or received on
this channel. `oneOf` is allowed here to specify multiple messages, however,
**a message MUST be valid only against one of the referenced message objects.**
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§