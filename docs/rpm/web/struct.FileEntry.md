rpm
# Struct FileEntry 
Source 

```
pub struct FileEntry {
    pub path: PathBuf,
    pub mode: FileMode,
    pub ownership: FileOwnership,
    pub modified_at: Timestamp,
    pub size: usize,
    pub flags: FileFlags,
    pub digest: Option<FileDigest>,
    pub caps: Option<String>,
    pub linkto: String,
    pub ima_signature: Option<String>,
}
```

## Fields§
§`path: PathBuf`

Full path of the file entry and where it will be installed to.
§`mode: FileMode`

The file mode of the file.
§`ownership: FileOwnership`

Defines the owning user and group.
§`modified_at: Timestamp`

Clocks the last access time.
§`size: usize`

The size of this file, dirs have the inode size (which is insane)
§`flags: FileFlags`

Flags describing the file or directory into three groups.
§`digest: Option<FileDigest>`§`caps: Option<String>`

Defines any capabilities on the file.
§`linkto: String`

Defines a target of a symlink (if the file is a symbolic link).
§`ima_signature: Option<String>`

Integrity Measurement Architecture (IMA) signature.

## Trait Implementations§