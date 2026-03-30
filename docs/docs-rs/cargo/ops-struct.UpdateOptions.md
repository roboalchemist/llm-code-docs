cargo::ops

# Struct UpdateOptions

Source

```
pub struct UpdateOptions<'a> {
    pub gctx: &'a GlobalContext,
    pub to_update: Vec<String>,
    pub precise: Option<&'a str>,
    pub recursive: bool,
    pub dry_run: bool,
    pub workspace: bool,
}
```

## Fields§

§`gctx: &'a GlobalContext`§`to_update: Vec<String>`§`precise: Option<&'a str>`§`recursive: bool`§`dry_run: bool`§`workspace: bool`

## Auto Trait Implementations§

§

### impl<'a> Freeze for UpdateOptions<'a>
