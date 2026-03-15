botan
# Struct Version 
Source 

```
pub struct Version {
    pub major: u32,
    pub minor: u32,
    pub patch: u32,
    pub release_date: u32,
    pub ffi_api: u32,
    pub string: String,
}
```

## Fields§
§`major: u32`

The major version of the library
§`minor: u32`

The minor version of the library
§`patch: u32`

The patch version of the library
§`release_date: u32`

The release date of the library, as YYYYMMDD, for example
2.7.0 has value 20180702. Will be 0 for unreleased versions.
§`ffi_api: u32`

The version of the FFI API, as a YYYYMMDD field.
§`string: String`

A free-form string describing the library version

## Implementations§