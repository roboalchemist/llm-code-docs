spdx::error
# Enum Reason 
Source 

```
pub enum Reason {
    UnknownLicense,
    UnknownException,
    InvalidCharacters,
    UnclosedParens,
    UnopenedParens,
    Empty,
    Unexpected(&'static [&'static str]),
    SeparatedPlus,
    UnknownTerm,
    GnuNoPlus,
    GnuPlusWithSuffix,
    DeprecatedLicenseId,
}
```

## Variants§
§
### UnknownLicense