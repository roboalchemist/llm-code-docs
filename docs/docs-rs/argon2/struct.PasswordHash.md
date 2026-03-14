argon2
# Struct PasswordHash 
Source 

```
pub struct PasswordHash<'a> {
    pub algorithm: Ident<'a>,
    pub version: Option<u32>,
    pub params: ParamsString,
    pub salt: Option<Salt<'a>>,
    pub hash: Option<Output>,
}
```
Available on **crate feature `password-hash`** only.
## Fields§
§`algorithm: Ident<'a>`

Password hashing algorithm identifier.

This corresponds to the `<id>` field in a PHC string, a.k.a. the
symbolic name for the function.
§`version: Option<u32>`

Optional version field.

This corresponds to the `<version>` field in a PHC string.
§`params: ParamsString`

Algorithm-specific parameters.

This corresponds to the set of `$<param>=<value>(,<param>=<value>)*`
name/value pairs in a PHC string.
§`salt: Option<Salt<'a>>`

`Salt` string for personalizing a password hash output.

This corresponds to the `<salt>` value in a PHC string.
§`hash: Option<Output>`

Password hashing function `Output`, a.k.a. hash/digest.

This corresponds to the `<hash>` output in a PHC string.

## Implementations§