spdx
# Struct AdditionRef 
Source 

```
pub struct AdditionRef {
    pub doc_ref: Option<String>,
    pub add_ref: String,
}
```

## Fields§
§`doc_ref: Option<String>`

Purpose: Identify any external SPDX documents referenced within this SPDX document.
See the spec for
more details.
§`add_ref: String`

Purpose: Provide a locally unique identifier to refer to additional text that are not found on the SPDX License List.
See the spec for
more details.

## Trait Implementations§