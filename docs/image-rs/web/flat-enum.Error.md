image::flat
# Enum Error 
Source 

```
pub enum Error {
    TooLarge,
    NormalFormRequired(NormalForm),
    ChannelCountMismatch(u8, u8),
    WrongColor(ColorType),
}
```

## Variants§
§
### TooLarge