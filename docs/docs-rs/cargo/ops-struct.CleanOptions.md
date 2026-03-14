cargo::ops

# Struct CleanOptions

Source

```
pub struct CleanOptions<'gctx> {
    pub gctx: &'gctx GlobalContext,
    pub spec: IndexSet<String>,
    pub targets: Vec<String>,
    pub profile_specified: bool,
    pub requested_profile: InternedString,
    pub doc: bool,
    pub dry_run: bool,
}
```

## Fields§

§`gctx: &'gctx GlobalContext`§`spec: IndexSet<String>`

A list of packages to clean. If empty, everything is cleaned.
§`targets: Vec<String>`

The target arch triple to clean, or None for the host arch
§`profile_specified: bool`

Whether to clean the release directory
§`requested_profile: InternedString`

Whether to clean the directory of a certain build profile
§`doc: bool`

Whether to just clean the doc directory
§`dry_run: bool`

If set, doesn’t delete anything.

## Auto Trait Implementations§

§

### impl<'gctx> Freeze for CleanOptions<'gctx>
