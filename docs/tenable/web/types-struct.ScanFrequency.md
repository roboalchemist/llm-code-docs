tenable::types
# Struct ScanFrequency 
Source 

```
pub struct ScanFrequency {
    pub interval: Option<i32>,
    pub frequency: Option<i32>,
    pub licensed: Option<bool>,
}
```

## Fields§
§`interval: Option<i32>`

The number of days over which Tenable searches for scans involving the asset.
§`frequency: Option<i32>`

The number of times that a scan ran against the asset during the specified interval.
§`licensed: Option<bool>`

Indicates whether the asset was licensed at the time of the identified scans.

## Trait Implementations§