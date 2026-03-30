apk::res

# Struct ResTablePackageHeader

Source

```
pub struct ResTablePackageHeader {
    pub id: u32,
    pub name: String,
    pub type_strings: u32,
    pub last_public_type: u32,
    pub key_strings: u32,
    pub last_public_key: u32,
    pub type_id_offset: u32,
}
```

## Fields§

§`id: u32`

If this is a base package, its ID. Package IDs start
at 1 (corresponding to the value of the package bits in a
resource identifier). 0 means this is not a base package.
§`name: String`

Actual name of this package, \0-terminated.
§`type_strings: u32`

Offset to a ResStringPoolHeader defining the resource
type symbol table. If zero, this package is inheriting
from another base package (overriding specific values in it).
§`last_public_type: u32`

Last index into type_strings that is for public use by others.
§`key_strings: u32`

Offset to a ResStringPoolHeader defining the resource key
symbol table. If zero, this package is inheriting from another
base package (overriding specific values in it).
§`last_public_key: u32`

Last index into key_strings that is for public use by others.
§`type_id_offset: u32`

## Implementations§
