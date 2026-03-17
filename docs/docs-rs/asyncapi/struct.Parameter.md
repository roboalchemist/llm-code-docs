asyncapi
# Struct Parameter 
Source 

```
pub struct Parameter {
    pub description: Option<String>,
    pub schema: Option<ReferenceOr<Schema>>,
    pub location: Option<String>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`description: Option<String>`

A verbose explanation of the parameter.
CommonMark syntax
can be used for rich text representation.
§`schema: Option<ReferenceOr<Schema>>`

Definition of the parameter.
§`location: Option<String>`

A runtime expression
that specifies the location of the parameter value.
Even when a definition for the target field exists,
it MUST NOT be used to validate this parameter but,
instead, the `schema` property MUST be used.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§