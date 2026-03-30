asyncapi
# Struct ExternalDocumentation 
Source 

```
pub struct ExternalDocumentation {
    pub description: Option<String>,
    pub url: String,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`description: Option<String>`

A short description of the target documentation.
CommonMark syntax can be used for rich text representation.
§`url: String`

**Required**. The URL for the target documentation.
Value MUST be in the format of a URL.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§