spdx
# Struct Exception 
Source 

```
pub struct Exception {
    pub name: &'static str,
    pub index: usize,
    pub flags: Type,
}
```

## Fields§
§`name: &'static str`

The name of the exception
§`index: usize`

The index in the full exception list where this exception is positioned
§`flags: Type`

The flags for the exception

## Auto Trait Implementations§
§
### impl Freeze for Exception