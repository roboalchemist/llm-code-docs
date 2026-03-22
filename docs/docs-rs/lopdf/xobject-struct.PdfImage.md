lopdf::xobject
# Struct PdfImage 
Source 

```
pub struct PdfImage<'a> {
    pub id: ObjectId,
    pub width: i64,
    pub height: i64,
    pub color_space: Option<String>,
    pub filters: Option<Vec<String>>,
    pub bits_per_component: Option<i64>,
    pub content: &'a [u8],
    pub origin_dict: &'a Dictionary,
}
```

## Fields§
§`id: ObjectId`§`width: i64`§`height: i64`§`color_space: Option<String>`§`filters: Option<Vec<String>>`§`bits_per_component: Option<i64>`§`content: &'a [u8]`

Image Data
§`origin_dict: &'a Dictionary`

Origin Stream Dictionary

## Trait Implementations§