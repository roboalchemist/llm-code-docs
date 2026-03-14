supernova::models
# Struct ClassInstanceFile 
Source 

```
pub struct ClassInstanceFile {
    pub id: u32,
    pub file: File,
    pub name: String,
    pub category: FileCategory,
    pub upload_datetime: String,
    pub uploader: Option<u32>,
    pub uploader_teacher: Option<u32>,
    pub url: String,
}
```

## Fields§
§`id: u32`§`file: File`§`name: String`§`category: FileCategory`§`upload_datetime: String`§`uploader: Option<u32>`§`uploader_teacher: Option<u32>`§`url: String`
## Trait Implementations§