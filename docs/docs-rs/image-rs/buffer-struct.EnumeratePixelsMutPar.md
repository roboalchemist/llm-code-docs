image::buffer
# Struct EnumeratePixelsMutPar 
Source 

```
pub struct EnumeratePixelsMutPar<'a, P>where
    P: Pixel + Send + Sync + 'a,
    P::Subpixel: Send + Sync + 'a,{ /* private fields */ }
```
Available on **crate feature `rayon`** only.
## Trait Implementations§