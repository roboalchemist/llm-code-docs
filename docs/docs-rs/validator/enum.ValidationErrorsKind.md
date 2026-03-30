validator
# Enum ValidationErrorsKind 
Source 

```
pub enum ValidationErrorsKind {
    Struct(Box<ValidationErrors>),
    List(BTreeMap<usize, Box<ValidationErrors>>),
    Field(Vec<ValidationError>),
}
```

## Variants§
§
### Struct(Box<ValidationErrors>)