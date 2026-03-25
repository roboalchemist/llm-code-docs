asyncapi
# Struct OperationTrait 
Source 

```
pub struct OperationTrait {
    pub operation_id: Option<String>,
    pub summary: Option<String>,
    pub description: Option<String>,
    pub tags: Vec<Tag>,
    pub external_docs: Option<ExternalDocumentation>,
    pub bindings: Option<ReferenceOr<OperationBinding>>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`operation_id: Option<String>`

Unique string used to identify the operation. The id MUST be unique among all
operations described in the API. The operationId value is **case-sensitive**.
Tools and libraries MAY use the operationId to uniquely identify an operation,
therefore, it is RECOMMENDED to follow common programming naming conventions.
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

A map where the keys describe the name of the protocol and the values describe
protocol-specific definitions for the operation.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§