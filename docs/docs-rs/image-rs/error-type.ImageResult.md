image::error
# Type Alias ImageResult 
Source 

```
pub type ImageResult<T> = Result<T, ImageError>;
```

## Aliased Type§

```
pub enum ImageResult<T> {
    Ok(T),
    Err(ImageError),
}
```

## Variants§
§1.0.0
### Ok(T)