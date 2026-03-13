wundergraph::diesel_ext
# Enum MaybeNull 
Source 

```
pub enum MaybeNull<T> {
    Expr(T),
    Null,
}
```

## Variants§
§
### Expr(T)