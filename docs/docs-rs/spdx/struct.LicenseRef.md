spdx
# Struct LicenseRef 
Source 

```
pub struct LicenseRef {
    pub doc_ref: Option<String>,
    pub lic_ref: String,
}
```

## Fields§
§`doc_ref: Option<String>`

Identify any external SPDX documents referenced within this SPDX document.

See the spec for
more details.
§`lic_ref: String`

Provide a locally unique identifier to refer to licenses that are not found on the SPDX License List.

See the spec for
more details.

## Trait Implementations§