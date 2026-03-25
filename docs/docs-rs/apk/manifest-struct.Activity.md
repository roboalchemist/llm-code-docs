apk::manifest

# Struct Activity

Source

```
pub struct Activity {
    pub config_changes: Option<String>,
    pub label: Option<String>,
    pub launch_mode: Option<String>,
    pub name: Option<String>,
    pub orientation: Option<String>,
    pub window_soft_input_mode: Option<String>,
    pub exported: Option<bool>,
    pub hardware_accelerated: Option<bool>,
    pub meta_data: Vec<MetaData>,
    pub intent_filters: Vec<IntentFilter>,
}
```

## Fields§

§`config_changes: Option<String>`§`label: Option<String>`§`launch_mode: Option<String>`§`name: Option<String>`§`orientation: Option<String>`§`window_soft_input_mode: Option<String>`§`exported: Option<bool>`§`hardware_accelerated: Option<bool>`§`meta_data: Vec<MetaData>`§`intent_filters: Vec<IntentFilter>`

If no `MAIN` action exists in any intent filter, a default `MAIN` filter is serialized.

## Trait Implementations§
