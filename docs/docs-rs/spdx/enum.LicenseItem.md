spdx
# Enum LicenseItem 
Source 

```
pub enum LicenseItem {
    Spdx {
        id: LicenseId,
        or_later: bool,
    },
    Other(Box<LicenseRef>),
}
```

## Variants§
§
### Spdx