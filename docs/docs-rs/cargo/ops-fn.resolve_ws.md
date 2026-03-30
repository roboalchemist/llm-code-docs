cargo::ops

# Function resolve_ws

Source

```
pub fn resolve_ws<'a>(
    ws: &Workspace<'a>,
    dry_run: bool,
) -> CargoResult<(PackageSet<'a>, Resolve)>
```
