victorops::types
# Struct User 
Source 

```
pub struct User {
    pub first_name: Option<String>,
    pub last_name: Option<String>,
    pub username: Option<String>,
    pub email: Option<String>,
    pub admin: Option<bool>,
    pub expiration_hours: Option<i32>,
    pub created_at: Option<String>,
    pub password_last_updated: Option<String>,
    pub verified: Option<bool>,
}
```

## Fields§
§`first_name: Option<String>`

The first name of the user.
§`last_name: Option<String>`

The last name of the user.
§`username: Option<String>`

The username of the user.
§`email: Option<String>`

The email address of the user.
§`admin: Option<bool>`

Whether the user has admin privileges.
§`expiration_hours: Option<i32>`

The number of hours until the user’s session expires.
§`created_at: Option<String>`

The timestamp when the user was created.
§`password_last_updated: Option<String>`

The timestamp when the user’s password was last updated.
§`verified: Option<bool>`

Whether the user’s account has been verified.

## Trait Implementations§