apk::manifest

# Struct Feature

Source

```
pub struct Feature {
    pub name: Option<String>,
    pub required: Option<bool>,
    pub version: Option<u32>,
    pub opengles_version: Option<(u8, u8)>,
}
```

## Fields§

§`name: Option<String>`§`required: Option<bool>`§`version: Option<u32>`

The `version` field is currently used for the following features:

-

`name="android.hardware.vulkan.compute"`: The minimum level of compute features required. See the Android documentation
for available levels and the respective Vulkan features required/provided.

-

`name="android.hardware.vulkan.level"`: The minimum Vulkan requirements. See the Android documentation
for available levels and the respective Vulkan features required/provided.

-

`name="android.hardware.vulkan.version"`: Represents the value of Vulkan’s `VkPhysicalDeviceProperties::apiVersion`. See the Android documentation
for available levels and the respective Vulkan features required/provided.

§`opengles_version: Option<(u8, u8)>`

## Trait Implementations§
