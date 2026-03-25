taos
# Trait Helpers 
Source 

```
pub trait Helpers {
    // Provided methods
    fn table_vgroup_id(&self, _db: &str, _table: &str) -> Option<i32> { ... }
    fn tables_vgroup_ids<T>(&self, _db: &str, _tables: &[T]) -> Option<Vec<i32>>
       where T: AsRef<str> { ... }
}
```

## Provided Methods§
Source
#### fn table_vgroup_id(&self, _db: &str, _table: &str) -> Option<i32>