cargo::ops

# Struct FetchOptions

Source

```
pub struct FetchOptions<'a> {
    pub gctx: &'a GlobalContext,
    pub targets: Vec<String>,
}
```

## Fields§

§`gctx: &'a GlobalContext`§`targets: Vec<String>`

The target arch triple to fetch dependencies for

## Auto Trait Implementations§

§

### impl<'a> Freeze for FetchOptions<'a>
