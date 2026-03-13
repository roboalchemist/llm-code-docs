taos
# Enum MetaCreate 
Source 

```
pub enum MetaCreate {
    Super {
        table_name: String,
        columns: Vec<FieldMore>,
        tags: Vec<Field>,
    },
    Child {
        table_name: String,
        using: String,
        tags: Vec<TagWithValue>,
        tag_num: Option<usize>,
    },
    Normal {
        table_name: String,
        columns: Vec<FieldMore>,
    },
}
```

## Variants§
§
### Super