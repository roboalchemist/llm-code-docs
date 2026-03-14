victorops::types
# Struct Contact 
Source 

```
pub struct Contact {
    pub phone_number: Option<String>,
    pub email: Option<String>,
    pub label: Option<String>,
    pub rank: Option<i32>,
    pub ext_id: Option<String>,
    pub id: Option<i32>,
    pub value: Option<String>,
    pub verified: Option<String>,
}
```

## Fields§
§`phone_number: Option<String>`

The phone number for phone-based contact methods.
§`email: Option<String>`

The email address for email-based contact methods.
§`label: Option<String>`

The label or description of this contact method.
§`rank: Option<i32>`

The priority rank of this contact method.
§`ext_id: Option<String>`

The external ID of this contact method.
§`id: Option<i32>`

The unique identifier of this contact method.
§`value: Option<String>`

The value of this contact method.
§`verified: Option<String>`

The verification status of this contact method.

## Implementations§