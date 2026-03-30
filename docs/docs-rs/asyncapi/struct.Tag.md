asyncapi
# Struct Tag 
Source 

```
pub struct Tag {
    pub name: String,
    pub description: Option<String>,
    pub external_docs: Option<ExternalDocumentation>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`name: String`

**Required**. The name of the tag.
§`description: Option<String>`

A short description of the target documentation.
CommonMark syntax can be used for rich text representation.
§`external_docs: Option<ExternalDocumentation>`

Additional external documentation for this tag.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§