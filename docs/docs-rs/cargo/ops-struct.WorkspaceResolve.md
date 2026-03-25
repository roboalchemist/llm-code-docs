cargo::ops

# Struct WorkspaceResolve

Source

```
pub struct WorkspaceResolve<'gctx> {
    pub pkg_set: PackageSet<'gctx>,
    pub workspace_resolve: Option<Resolve>,
    pub targeted_resolve: Resolve,
    pub specs_and_features: Vec<SpecsAndResolvedFeatures>,
}
```

## Fields§

§`pkg_set: PackageSet<'gctx>`

Packages to be downloaded.
§`workspace_resolve: Option<Resolve>`

The resolve for the entire workspace.

This may be `None` for things like `cargo install` and `-Zavoid-dev-deps`.
This does not include `paths` overrides.
§`targeted_resolve: Resolve`

The narrowed resolve, with the specific features enabled.
§`specs_and_features: Vec<SpecsAndResolvedFeatures>`

Package specs requested for compilation along with specific features enabled. This usually
has the length of one but there may be more specs with different features when using the
`package` feature resolver.

## Auto Trait Implementations§

§

### impl<'gctx> !Freeze for WorkspaceResolve<'gctx>
