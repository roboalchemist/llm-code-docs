cargo::ops

# Struct PublishOpts

Source

```
pub struct PublishOpts<'gctx> {
    pub gctx: &'gctx GlobalContext,
    pub token: Option<Secret<String>>,
    pub reg_or_index: Option<RegistryOrIndex>,
    pub verify: bool,
    pub allow_dirty: bool,
    pub jobs: Option<JobsConfig>,
    pub keep_going: bool,
    pub to_publish: Packages,
    pub targets: Vec<String>,
    pub dry_run: bool,
    pub cli_features: CliFeatures,
}
```

## Fields§

§`gctx: &'gctx GlobalContext`§`token: Option<Secret<String>>`§`reg_or_index: Option<RegistryOrIndex>`§`verify: bool`§`allow_dirty: bool`§`jobs: Option<JobsConfig>`§`keep_going: bool`§`to_publish: Packages`§`targets: Vec<String>`§`dry_run: bool`§`cli_features: CliFeatures`

## Auto Trait Implementations§

§

### impl<'gctx> Freeze for PublishOpts<'gctx>
