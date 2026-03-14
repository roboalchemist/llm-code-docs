rpm
# Trait Tag 
Source 

```
pub trait Tag:
    FromPrimitive
    + PartialEq
    + Display
    + Debug
    + Copy {
    // Required methods
    fn tag_type_name() -> &'static str;
    fn to_u32(&self) -> u32;
}
```

## Required Methods§
Source
#### fn tag_type_name() -> &'static str