spdx::lexer
# Enum Token 
Source 

```
pub enum Token<'a> {
    Spdx(LicenseId),
    LicenseRef {
        doc_ref: Option<&'a str>,
        lic_ref: &'a str,
    },
    Exception(ExceptionId),
    AdditionRef {
        doc_ref: Option<&'a str>,
        add_ref: &'a str,
    },
    Unknown(&'a str),
    Plus,
    OpenParen,
    CloseParen,
    With,
    And,
    Or,
}
```

## Variants§
§
### Spdx(LicenseId)