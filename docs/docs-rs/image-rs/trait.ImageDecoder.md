image
# Trait ImageDecoder 
Source 

```
pub trait ImageDecoder {
    // Required methods
    fn dimensions(&self) -> (u32, u32);
    fn color_type(&self) -> ColorType;
    fn read_image(self, buf: &mut [u8]) -> ImageResult<()>
       where Self: Sized;
    fn read_image_boxed(self: Box<Self>, buf: &mut [u8]) -> ImageResult<()>;

    // Provided methods
    fn original_color_type(&self) -> ExtendedColorType { ... }
    fn icc_profile(&mut self) -> ImageResult<Option<Vec<u8>>> { ... }
    fn exif_metadata(&mut self) -> ImageResult<Option<Vec<u8>>> { ... }
    fn xmp_metadata(&mut self) -> ImageResult<Option<Vec<u8>>> { ... }
    fn iptc_metadata(&mut self) -> ImageResult<Option<Vec<u8>>> { ... }
    fn orientation(&mut self) -> ImageResult<Orientation> { ... }
    fn total_bytes(&self) -> u64 { ... }
    fn set_limits(&mut self, limits: Limits) -> ImageResult<()> { ... }
}
```

## Required Methods§