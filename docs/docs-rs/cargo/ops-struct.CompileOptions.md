cargo::ops

# Struct CompileOptions

Source

```
pub struct CompileOptions {
    pub build_config: BuildConfig,
    pub cli_features: CliFeatures,
    pub spec: Packages,
    pub filter: CompileFilter,
    pub target_rustdoc_args: Option<Vec<String>>,
    pub target_rustc_args: Option<Vec<String>>,
    pub target_rustc_crate_types: Option<Vec<String>>,
    pub rustdoc_document_private_items: bool,
    pub honor_rust_version: Option<bool>,
}
```

## Fields§

§`build_config: BuildConfig`

Configuration information for a rustc build
§`cli_features: CliFeatures`

Feature flags requested by the user.
§`spec: Packages`

A set of packages to build.
§`filter: CompileFilter`

Filter to apply to the root package to select which targets will be
built.
§`target_rustdoc_args: Option<Vec<String>>`

Extra arguments to be passed to rustdoc (single target only)
§`target_rustc_args: Option<Vec<String>>`

The specified target will be compiled with all the available arguments,
note that this only accounts for the *final* invocation of rustc
§`target_rustc_crate_types: Option<Vec<String>>`

Crate types to be passed to rustc (single target only)
§`rustdoc_document_private_items: bool`

Whether the `--document-private-items` flags was specified and should
be forwarded to `rustdoc`.
§`honor_rust_version: Option<bool>`

Whether the build process should check the minimum Rust version
defined in the cargo metadata for a crate.

## Implementations§
