image::buffer
# Struct EnumeratePixelsPar 
Source 

```
pub struct EnumeratePixelsPar<'a, P>where
    P: Pixel + Sync + 'a,
    P::Subpixel: Sync + 'a,{ /* private fields */ }
```
Available on **crate feature `rayon`** only.
## Trait Implementations§