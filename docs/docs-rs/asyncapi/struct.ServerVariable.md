asyncapi
# Struct ServerVariable 
Source 

```
pub struct ServerVariable {
    pub en: Option<Vec<String>>,
    pub default: Option<String>,
    pub description: Option<String>,
    pub examples: Option<Vec<String>>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`en: Option<Vec<String>>`

An enumeration of string values to be used if the substitution options are from a limited set.
§`default: Option<String>`

The default value to use for substitution, and to send,
if an alternate value is not supplied.
§`description: Option<String>`

An optional description for the server variable.
CommonMark syntax
MAY be used for rich text representation.
§`examples: Option<Vec<String>>`

An array of examples of the server variable.
§`extensions: IndexMap<String, Value>`

This object MAY be extended with
Specification Extensions.

## Trait Implementations§