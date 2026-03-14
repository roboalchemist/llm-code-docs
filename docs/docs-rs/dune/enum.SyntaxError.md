dune
# Enum SyntaxError 
Source 

```
pub enum SyntaxError {
    TokenizationErrors(Box<[Diagnostic]>),
    Expected {
        input: StrSlice,
        expected: &'static str,
        found: Option<String>,
        hint: Option<&'static str>,
    },
    ExpectedChar {
        expected: char,
        at: Option<StrSlice>,
    },
    NomError {
        kind: ErrorKind,
        at: Option<StrSlice>,
        cause: Option<Box<SyntaxError>>,
    },
    InternalError,
}
```

## Variants§
§
### TokenizationErrors(Box<[Diagnostic]>)