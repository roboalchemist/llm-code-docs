image
# Trait GenericImageView 
Source 

```
pub trait GenericImageView {
    type Pixel: Pixel;

    // Required methods
    fn dimensions(&self) -> (u32, u32);
    fn get_pixel(&self, x: u32, y: u32) -> Self::Pixel;

    // Provided methods
    fn width(&self) -> u32 { ... }
    fn height(&self) -> u32 { ... }
    fn in_bounds(&self, x: u32, y: u32) -> bool { ... }
    unsafe fn unsafe_get_pixel(&self, x: u32, y: u32) -> Self::Pixel { ... }
    fn pixels(&self) -> Pixels<'_, Self> ⓘ
       where Self: Sized { ... }
    fn view(&self, x: u32, y: u32, width: u32, height: u32) -> SubImage<&Self>
       where Self: Sized { ... }
    fn try_view(
        &self,
        x: u32,
        y: u32,
        width: u32,
        height: u32,
    ) -> Result<SubImage<&Self>, ImageError>
       where Self: Sized { ... }
    fn buffer_like(
        &self,
    ) -> ImageBuffer<Self::Pixel, Vec<<Self::Pixel as Pixel>::Subpixel>> { ... }
    fn buffer_with_dimensions(
        &self,
        width: u32,
        height: u32,
    ) -> ImageBuffer<Self::Pixel, Vec<<Self::Pixel as Pixel>::Subpixel>> { ... }
    fn to_pixel_view(&self) -> Option<ViewOfPixel<'_, Self::Pixel>> { ... }
}
```

## Required Associated Types§