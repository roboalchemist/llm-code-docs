typebox::error
# Enum ParseError 
Source 

```
pub enum ParseError {
    TypeMismatch {
        expected: String,
        got: String,
    },
    MissingField {
        field: String,
    },
    InvalidLength {
        expected: usize,
        got: usize,
    },
    NoMatchingVariant,
    LiteralMismatch,
    EnumMismatch {
        allowed: Vec<String>,
        got: String,
    },
    InvalidPattern(String),
}
```

## Variants§
§
### TypeMismatch