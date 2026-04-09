pgp::composed
# Struct ArmorOptions 
Source 

```
pub struct ArmorOptions<'a> {
    pub headers: Option<&'a Headers>,
    pub include_checksum: bool,
}
```

## Fields§
§`headers: Option<&'a Headers>`

Armor headers
§`include_checksum: bool`

Should a checksum be included? Default to `true`.

## Trait Implementations§