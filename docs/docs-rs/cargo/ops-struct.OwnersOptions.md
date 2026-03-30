cargo::ops

# Struct OwnersOptions

Source

```
pub struct OwnersOptions {
    pub krate: Option<String>,
    pub token: Option<Secret<String>>,
    pub reg_or_index: Option<RegistryOrIndex>,
    pub to_add: Option<Vec<String>>,
    pub to_remove: Option<Vec<String>>,
    pub list: bool,
}
```

## Fields§

§`krate: Option<String>`§`token: Option<Secret<String>>`§`reg_or_index: Option<RegistryOrIndex>`§`to_add: Option<Vec<String>>`§`to_remove: Option<Vec<String>>`§`list: bool`

## Auto Trait Implementations§

§

### impl Freeze for OwnersOptions
