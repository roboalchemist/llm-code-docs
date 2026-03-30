nix

# Trait NixPath

Source

```
pub trait NixPath {
    // Required methods
    fn is_empty(&self) -> bool;
    fn len(&self) -> usize;
    fn with_nix_path<T, F>(&self, f: F) -> Result<T>
       where F: FnOnce(&CStr) -> T;
}
```

Available on **Unix** only.

## Required Methods§
