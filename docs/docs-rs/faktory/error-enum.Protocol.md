faktory::error
# Enum Protocol 
Source 

```
#[non_exhaustive]pub enum Protocol {
    Malformed {
        desc: String,
    },
    UniqueConstraintViolation {
        msg: String,
    },
    Internal {
        msg: String,
    },
    BadType {
        expected: &'static str,
        received: String,
    },
    BadResponse {
        typed_as: &'static str,
        error: &'static str,
        bytes: Vec<u8>,
    },
}
```

## Variants (Non-exhaustive)§
§
### Malformed