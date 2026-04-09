image
# Function load 
Source 

```
pub fn load<R: BufRead + Seek>(
    r: R,
    format: ImageFormat,
) -> ImageResult<DynamicImage>
```