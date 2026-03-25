apk::manifest

# Struct AndroidManifest

Source

```
pub struct AndroidManifest {
    pub package: Option<String>,
    pub version_code: Option<u32>,
    pub version_name: Option<String>,
    pub compile_sdk_version: Option<u32>,
    pub compile_sdk_version_codename: Option<u32>,
    pub platform_build_version_code: Option<u32>,
    pub platform_build_version_name: Option<u32>,
    pub sdk: Sdk,
    pub uses_feature: Vec<Feature>,
    pub uses_permission: Vec<Permission>,
    pub application: Application,
    /* private fields */
}
```

## Fields§

§`package: Option<String>`§`version_code: Option<u32>`§`version_name: Option<String>`§`compile_sdk_version: Option<u32>`§`compile_sdk_version_codename: Option<u32>`§`platform_build_version_code: Option<u32>`§`platform_build_version_name: Option<u32>`§`sdk: Sdk`§`uses_feature: Vec<Feature>`§`uses_permission: Vec<Permission>`§`application: Application`

## Trait Implementations§
