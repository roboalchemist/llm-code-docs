image
# Trait PixelWithColorType 
Source 

```
pub trait PixelWithColorType: Pixel + SealedPixelWithColorType<TransformableSubpixel = <Self as Pixel>::Subpixel> {
    const COLOR_TYPE: ExtendedColorType;
}
```

## Required Associated Constants§