asyncapi
# Struct Contact 
Source 

```
pub struct Contact {
    pub name: Option<String>,
    pub url: Option<String>,
    pub email: Option<String>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`name: Option<String>`

The identifying name of the contact person/organization.
§`url: Option<String>`

The URL pointing to the contact information.
MUST be in the format of a URL.
§`email: Option<String>`

The email address of the contact person/organization.
MUST be in the format of an email address.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§