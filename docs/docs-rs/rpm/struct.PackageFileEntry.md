rpm
# Struct PackageFileEntry 
Source 

```
pub struct PackageFileEntry {
    pub mode: FileMode,
    pub modified_at: Timestamp,
    pub link: String,
    pub flags: FileFlags,
    pub user: String,
    pub group: String,
    pub base_name: String,
    pub dir: String,
    pub caps: Option<FileCaps>,
    pub verify_flags: FileVerifyFlags,
    pub source: ContentSource,
}
```

## Fields§
§`mode: FileMode`§`modified_at: Timestamp`§`link: String`§`flags: FileFlags`§`user: String`§`group: String`§`base_name: String`§`dir: String`§`caps: Option<FileCaps>`§`verify_flags: FileVerifyFlags`§`source: ContentSource`
## Auto Trait Implementations§
§
### impl Freeze for PackageFileEntry