taos
# Enum JsonMeta 
Source 

```
pub enum JsonMeta {
    Plural {
        tmq_meta_version: FastStr,
        metas: Vec<MetaUnit>,
    },
    Single(MetaUnit),
}
```

## Variants§
§
### Plural