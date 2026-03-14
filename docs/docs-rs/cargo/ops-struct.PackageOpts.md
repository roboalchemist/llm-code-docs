cargo::ops

# Struct PackageOpts

Source

```
pub struct PackageOpts<'gctx> {}
```

## Fields§

§`gctx: &'gctx GlobalContext`§`list: bool`§`fmt: PackageMessageFormat`§`check_metadata: bool`§`allow_dirty: bool`§`include_lockfile: bool`§`verify: bool`§`jobs: Option<JobsConfig>`§`keep_going: bool`§`to_package: Packages`§`targets: Vec<String>`§`cli_features: CliFeatures`§`reg_or_index: Option<RegistryOrIndex>`§`dry_run: bool`

Whether this packaging job is meant for a publishing dry-run.

Packaging on its own has no side effects, so a dry-run doesn’t
make sense from that point of view. But dry-run publishing needs
special packaging behavior, which this flag turns on.

Specifically, we want dry-run packaging to work even if versions
have not yet been bumped. But then if you dry-run packaging in
a workspace with some declared versions that are already published,
the package verification step can fail with checksum mismatches.
So when dry-run is true, the verification step does some extra
checksum fudging in the lock file.

## Trait Implementations§
