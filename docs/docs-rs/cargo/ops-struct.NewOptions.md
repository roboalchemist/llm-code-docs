cargo::ops

# Struct NewOptions

Source

```
pub struct NewOptions {
    pub version_control: Option<VersionControl>,
    pub kind: NewProjectKind,
    pub auto_detect_kind: bool,
    pub path: PathBuf,
    pub name: Option<String>,
    pub edition: Option<String>,
    pub registry: Option<String>,
}
```

## Fields§

§`version_control: Option<VersionControl>`§`kind: NewProjectKind`§`auto_detect_kind: bool`§`path: PathBuf`

Absolute path to the directory for the new package
§`name: Option<String>`§`edition: Option<String>`§`registry: Option<String>`

## Implementations§
