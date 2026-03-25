carton::info
# Struct CartonInfoWithExtras 
Source 

```
pub struct CartonInfoWithExtras<T>where
    T: TensorStorage,{
    pub info: CartonInfo<T>,
    pub manifest_sha256: Option<String>,
}
```

## Fields§
§`info: CartonInfo<T>`§`manifest_sha256: Option<String>`

The sha256 of the MANIFEST file (if available)
This should always be available unless we’re running an unpacked model

## Auto Trait Implementations§
§
### impl<T> Freeze for CartonInfoWithExtras<T>