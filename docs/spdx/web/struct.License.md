spdx
# Struct License 
Source 

```
pub struct License {
    pub name: &'static str,
    pub full_name: &'static str,
    pub index: usize,
    pub flags: Type,
}
```

## Fields§
§`name: &'static str`

The short identifier for the license
§`full_name: &'static str`

The full name of the license
§`index: usize`

The index in the full license list where this license is positioned
§`flags: Type`

The flags for this license

## Auto Trait Implementations§
§
### impl Freeze for License