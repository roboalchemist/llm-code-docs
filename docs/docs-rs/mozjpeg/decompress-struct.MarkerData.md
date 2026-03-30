mozjpeg::decompress
# Struct MarkerData 
Source 

```
pub struct MarkerData<'a> {
    pub marker: Marker,
    pub data: &'a [u8],
}
```

## Fields§
§`marker: Marker`§`data: &'a [u8]`
## Auto Trait Implementations§
§
### impl<'a> Freeze for MarkerData<'a>