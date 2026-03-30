lopdf::xref
# Enum XrefEntry 
Source 

```
pub enum XrefEntry {
    Free,
    UnusableFree,
    Normal {
        offset: u32,
        generation: u16,
    },
    Compressed {
        container: u32,
        index: u16,
    },
}
```

## Variants§
§
### Free