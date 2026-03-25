statiq::sproc
# Struct SprocPagedResult 
Source 

```
pub struct SprocPagedResult<T> {
    pub items: Vec<T>,
    pub total_count: i64,
    pub page_number: i32,
    pub page_size: i32,
}
```

## Fields§
§`items: Vec<T>`§`total_count: i64`§`page_number: i32`§`page_size: i32`
## Trait Implementations§