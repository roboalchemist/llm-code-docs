bat
# Enum MappingTarget 
Source 

```
#[non_exhaustive]pub enum MappingTarget<'a> {
    MapTo(&'a str),
    MapToUnknown,
    MapExtensionToUnknown,
}
```

## Variants (Non-exhaustive)§
§
### MapTo(&'a str)