image
# Trait GenericImage 
Source 

```
pub trait GenericImage: GenericImageView {
    // Required methods
    fn get_pixel_mut(&mut self, x: u32, y: u32) -> &mut Self::Pixel;
    fn put_pixel(&mut self, x: u32, y: u32, pixel: Self::Pixel);
    fn blend_pixel(&mut self, x: u32, y: u32, pixel: Self::Pixel);

    // Provided methods
    unsafe fn unsafe_put_pixel(&mut self, x: u32, y: u32, pixel: Self::Pixel) { ... }
    fn copy_from<O>(&mut self, other: &O, x: u32, y: u32) -> ImageResult<()>
       where O: GenericImageView<Pixel = Self::Pixel> { ... }
    fn copy_from_samples(
        &mut self,
        samples: ViewOfPixel<'_, Self::Pixel>,
        x: u32,
        y: u32,
    ) -> ImageResult<()> { ... }
    fn copy_within(&mut self, source: Rect, x: u32, y: u32) -> bool { ... }
    fn sub_image(
        &mut self,
        x: u32,
        y: u32,
        width: u32,
        height: u32,
    ) -> SubImage<&mut Self>
       where Self: Sized { ... }
}
```

## Required Methods§