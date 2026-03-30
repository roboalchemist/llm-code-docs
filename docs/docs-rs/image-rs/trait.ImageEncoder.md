image
# Trait ImageEncoder 
Source 

```
pub trait ImageEncoder {
    // Required method
    fn write_image(
        self,
        buf: &[u8],
        width: u32,
        height: u32,
        color_type: ExtendedColorType,
    ) -> ImageResult<()>;

    // Provided methods
    fn set_icc_profile(
        &mut self,
        icc_profile: Vec<u8>,
    ) -> Result<(), UnsupportedError> { ... }
    fn set_exif_metadata(
        &mut self,
        exif: Vec<u8>,
    ) -> Result<(), UnsupportedError> { ... }
}
```

## Required Methods§