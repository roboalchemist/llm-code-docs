dune
# Enum Diagnostic 
Source 

```
pub enum Diagnostic {
    Valid,
    InvalidStringEscapes(Box<[StrSlice]>),
    InvalidNumber(StrSlice),
    IllegalChar(StrSlice),
    NotTokenized(StrSlice),
}
```

## Variants§
§
### Valid