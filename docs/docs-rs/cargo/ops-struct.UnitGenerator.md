cargo::ops

# Struct UnitGenerator

Source

```
pub struct UnitGenerator<'a, 'gctx> {}
```

## Fields§

§`ws: &'a Workspace<'gctx>`§`packages: &'a [&'a Package]`§`spec: &'a Packages`§`target_data: &'a RustcTargetData<'gctx>`§`filter: &'a CompileFilter`§`requested_kinds: &'a [CompileKind]`§`explicit_host_kind: CompileKind`§`intent: UserIntent`§`resolve: &'a Resolve`§`workspace_resolve: &'a Option<Resolve>`§`resolved_features: &'a ResolvedFeatures`§`package_set: &'a PackageSet<'gctx>`§`profiles: &'a Profiles`§`interner: &'a UnitInterner`§`has_dev_units: HasDevUnits`

## Implementations§
