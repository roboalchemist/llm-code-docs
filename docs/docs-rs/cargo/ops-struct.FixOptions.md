cargo::ops

# Struct FixOptions

Source

```
pub struct FixOptions {
    pub edition: Option<EditionFixMode>,
    pub idioms: bool,
    pub compile_opts: CompileOptions,
    pub allow_dirty: bool,
    pub allow_no_vcs: bool,
    pub allow_staged: bool,
    pub broken_code: bool,
    pub requested_lockfile_path: Option<PathBuf>,
}
```

## Fields§

§`edition: Option<EditionFixMode>`§`idioms: bool`§`compile_opts: CompileOptions`§`allow_dirty: bool`§`allow_no_vcs: bool`§`allow_staged: bool`§`broken_code: bool`§`requested_lockfile_path: Option<PathBuf>`

## Auto Trait Implementations§

§

### impl Freeze for FixOptions
