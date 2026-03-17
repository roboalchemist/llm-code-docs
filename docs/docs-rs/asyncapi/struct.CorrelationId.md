asyncapi
# Struct CorrelationId 
Source 

```
pub struct CorrelationId {
    pub description: Option<String>,
    pub location: String,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`description: Option<String>`

An optional description of the identifier.
CommonMark syntax
can be used for rich text representation.
§`location: String`

**REQUIRED**.
A runtime expression
that specifies the location of the correlation ID.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§