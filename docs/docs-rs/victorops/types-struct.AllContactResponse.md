victorops::types
# Struct AllContactResponse 
Source 

```
pub struct AllContactResponse {
    pub phones: Option<ContactGroup>,
    pub emails: Option<ContactGroup>,
    pub devices: Option<ContactGroup>,
}
```

## Fields§
§`phones: Option<ContactGroup>`

The phone contact methods for the user.
§`emails: Option<ContactGroup>`

The email contact methods for the user.
§`devices: Option<ContactGroup>`

The device contact methods for the user.

## Trait Implementations§