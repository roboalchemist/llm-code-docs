tenable::requests
# Trait AssetReq 
Source 

```
pub trait AssetReq {
    // Required methods
    fn assets(&self) -> AssetsReq<'_>;
    fn asset_by_uuid<'a, I: Into<Cow<'a, str>>>(
        &'a self,
        asset_uuid: I,
    ) -> AssetByUuidReq<'a>;
    fn acr_update<'a, I: Into<Cow<'a, [Acr]>>>(
        &'a self,
        acrs: I,
    ) -> AcrUpdate<'a>;
    fn assets_move<'a, I: Into<Cow<'a, AssetsMoveDef>>>(
        &'a self,
        assets_move_def: I,
    ) -> AssetsMove<'a>;
}
```

## Required Methods§