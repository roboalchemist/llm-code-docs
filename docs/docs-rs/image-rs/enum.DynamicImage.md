image
# Enum DynamicImage 
Source 

```
#[non_exhaustive]pub enum DynamicImage {
    ImageLuma8(GrayImage),
    ImageLumaA8(GrayAlphaImage),
    ImageRgb8(RgbImage),
    ImageRgba8(RgbaImage),
    ImageLuma16(ImageBuffer<Luma<u16>, Vec<u16>>),
    ImageLumaA16(ImageBuffer<LumaA<u16>, Vec<u16>>),
    ImageRgb16(ImageBuffer<Rgb<u16>, Vec<u16>>),
    ImageRgba16(ImageBuffer<Rgba<u16>, Vec<u16>>),
    ImageRgb32F(Rgb32FImage),
    ImageRgba32F(Rgba32FImage),
}
```

## Variants (Non-exhaustive)§
§
### ImageLuma8(GrayImage)