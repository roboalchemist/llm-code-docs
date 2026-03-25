image
# Trait Pixel 
Source 

```
pub trait Pixel: Copy + Clone {
    type Subpixel: Primitive;

    const CHANNEL_COUNT: u8;
    const COLOR_MODEL: &'static str;
    const HAS_ALPHA: bool = false;
}
```

## Required Associated Constants§