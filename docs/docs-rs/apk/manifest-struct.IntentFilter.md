apk::manifest

# Struct IntentFilter

Source

```
pub struct IntentFilter {
    pub actions: Vec<String>,
    pub categories: Vec<String>,
    pub data: Vec<IntentFilterData>,
}
```

## Fields§

§`actions: Vec<String>`

Serialize strings wrapped in `<action android:name="..." />`
§`categories: Vec<String>`

Serialize as vector of structs for proper xml formatting
§`data: Vec<IntentFilterData>`

## Trait Implementations§
