rpm
# Enum FileMode 
Source 

```
#[non_exhaustive]pub enum FileMode {
    Dir {
        permissions: u16,
    },
    Regular {
        permissions: u16,
    },
    SymbolicLink {
        permissions: u16,
    },
    Invalid {
        raw_mode: i32,
        reason: &'static str,
    },
}
```

## Variants (Non-exhaustive)§
§
### Dir