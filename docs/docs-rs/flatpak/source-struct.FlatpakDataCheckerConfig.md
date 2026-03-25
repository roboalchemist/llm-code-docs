flatpak::source
# Struct FlatpakDataCheckerConfig 
Source 

```
pub struct FlatpakDataCheckerConfig {
    pub type: Option<String>,
    pub url: Option<String>,
    pub version_pattern: Option<String>,
    pub is_main_source: Option<bool>,
    pub versions: BTreeMap<String, String>,
}
```

## Fields§
§`type: Option<String>`§`url: Option<String>`§`version_pattern: Option<String>`§`is_main_source: Option<bool>`§`versions: BTreeMap<String, String>`

The constraints placed on version checking.
See https://github.com/flathub/flatpak-external-data-checker#version-constraining

## Trait Implementations§