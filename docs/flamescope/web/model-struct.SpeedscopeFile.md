flamescope::model
# Struct SpeedscopeFile 
Source 

```
pub struct SpeedscopeFile {
    pub schema: &'static str,
    pub profiles: Vec<Profile>,
    pub shared: Shared,
    pub active_profile_index: Option<u64>,
    pub exporter: Option<String>,
    pub name: Option<String>,
}
```

## Fields§
§`schema: &'static str`§`profiles: Vec<Profile>`§`shared: Shared`§`active_profile_index: Option<u64>`§`exporter: Option<String>`§`name: Option<String>`
## Trait Implementations§