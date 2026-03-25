asyncapi
# Enum ReferenceOr 
Source 

```
pub enum ReferenceOr<T> {
    Reference {
        reference: String,
    },
    Item(T),
}
```

## Variants§
§
### Reference