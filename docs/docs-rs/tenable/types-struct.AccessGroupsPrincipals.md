tenable::types
# Struct AccessGroupsPrincipals 
Source 

```
pub struct AccessGroupsPrincipals {
    pub _type: Option<String>,
    pub principal_id: Option<String>,
    pub principal_name: Option<String>,
}
```

## Fields§
§`_type: Option<String>`

(Required) The type of principal. Valid values include:  - user—Grants access to the user you specify.  - group—Grants access to all users assigned to the user group you specify.
§`principal_id: Option<String>`

The UUID of a user or user group. This parameter is required if the request omits the `principal_name` parameter.
§`principal_name: Option<String>`

The name of the user or user group. This parameter is required if the request omits the `principal_id` parameter. If a request includes both `principal_id` and `principal_name`, Tenable.io assigns the user or user group to the access group based on the `principal_id` parameter, and ignores the `principal_name` parameter in the request.

## Trait Implementations§