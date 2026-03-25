faktory::error
# Enum Connect 
Source 

```
#[non_exhaustive]pub enum Connect {
    BadScheme {
        scheme: String,
    },
    MissingHostname,
    AuthenticationNeeded,
    VersionMismatch {
        ours: usize,
        theirs: usize,
    },
    ParseUrl(ParseError),
}
```

## Variants (Non-exhaustive)§
§
### BadScheme