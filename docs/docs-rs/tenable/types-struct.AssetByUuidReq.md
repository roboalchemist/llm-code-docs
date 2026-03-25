tenable::types
# Struct AssetByUuidReq 
Source 

```
pub struct AssetByUuidReq<'a> {
    pub tenable: &'a Tenable<'a>,
    pub asset_uuid: Cow<'a, str>,
}
```

## Fields§
§`tenable: &'a Tenable<'a>`

Inner tenable Client
§`asset_uuid: Cow<'a, str>`

UUID which identifies the asset

## Trait Implementations§