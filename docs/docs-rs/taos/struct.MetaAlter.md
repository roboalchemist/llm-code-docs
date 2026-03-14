taos
# Struct MetaAlter 
Source 

```
pub struct MetaAlter {
    pub table_name: String,
    pub alter_type: AlterType,
    pub field: Field,
    pub col_new_name: Option<String>,
    pub col_value: Option<String>,
    pub col_value_null: Option<bool>,
}
```

## Fields§
§`table_name: String`§`alter_type: AlterType`§`field: Field`§`col_new_name: Option<String>`§`col_value: Option<String>`§`col_value_null: Option<bool>`
## Trait Implementations§