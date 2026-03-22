asyncapi
# Struct License 
Source 

```
pub struct License {
    pub name: String,
    pub url: Option<String>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`name: String`

**Required.** The license name used for the API.
§`url: Option<String>`

A URL to the license used for the API.
MUST be in the format of a URL.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§