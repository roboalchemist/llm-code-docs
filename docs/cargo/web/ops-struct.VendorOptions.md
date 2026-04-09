cargo::ops

# Struct VendorOptions

Source

```
pub struct VendorOptions<'a> {
    pub no_delete: bool,
    pub versioned_dirs: bool,
    pub destination: &'a Path,
    pub extra: Vec<PathBuf>,
    pub respect_source_config: bool,
}
```

## Fields§

§`no_delete: bool`§`versioned_dirs: bool`§`destination: &'a Path`§`extra: Vec<PathBuf>`§`respect_source_config: bool`

## Auto Trait Implementations§

§

### impl<'a> Freeze for VendorOptions<'a>
