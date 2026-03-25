cross::rustc
# Trait VersionMetaExt 
Source 

```
pub trait VersionMetaExt {
    // Required methods
    fn host(&self) -> Host;
    fn needs_interpreter(&self) -> bool;
    fn commit_hash(&self) -> String;
}
```

## Required Methods§
Source
#### fn host(&self) -> Host