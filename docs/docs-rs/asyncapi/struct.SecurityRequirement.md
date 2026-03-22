asyncapi
# Struct SecurityRequirement 
Source 

```
pub struct SecurityRequirement {
    pub values: IndexMap<String, Vec<String>>,
}
```

## Fields§
§`values: IndexMap<String, Vec<String>>`

Each name MUST correspond to a security scheme which is declared in the
Security Schemes
under the Components Object.
If the security scheme is of type `"oauth2"` or `"openIdConnect"`, then
the value is a list of scope names. Provide scopes that are required to
establish successful connection with the server. If scopes are not
needed, the list can be empty. For other security scheme types, the
array MUST be empty.

## Trait Implementations§