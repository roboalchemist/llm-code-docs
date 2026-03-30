asyncapi
# Struct Info 
Source 

```
pub struct Info {
    pub title: String,
    pub version: String,
    pub description: Option<String>,
    pub terms_of_service: Option<String>,
    pub contact: Option<Contact>,
    pub license: Option<License>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`title: String`

**Required.** The title of the application.
§`version: String`

**Required** Provides the version of the application API
(not to be confused with the specification version).
§`description: Option<String>`

A short description of the application.
CommonMark syntax can be used for rich text representation.
§`terms_of_service: Option<String>`

A URL to the Terms of Service for the API.
MUST be in the format of a URL.
§`contact: Option<Contact>`

The contact information for the exposed API.
§`license: Option<License>`

The license information for the exposed API.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§