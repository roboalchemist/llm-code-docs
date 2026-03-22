image
# Trait ImageDecoderRect 
Source 

```
pub trait ImageDecoderRect: ImageDecoder {
    // Required method
    fn read_rect(
        &mut self,
        x: u32,
        y: u32,
        width: u32,
        height: u32,
        buf: &mut [u8],
        row_pitch: usize,
    ) -> ImageResult<()>;
}
```

## Required Methods§