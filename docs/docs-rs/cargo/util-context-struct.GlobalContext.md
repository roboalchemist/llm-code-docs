cargo::util::context

# Struct GlobalContext

Source

```
pub struct GlobalContext {
    pub nightly_features_allowed: bool,
    /* private fields */
}
```

## Fields§

§`nightly_features_allowed: bool`

This should be false if:

- this is an artifact of the rustc distribution process for “stable” or for “beta”

- this is an `#[test]` that does not opt in with `enable_nightly_features`

- this is an integration test that uses `ProcessBuilder`
that does not opt in with `masquerade_as_nightly_cargo`
This should be true if:

- this is an artifact of the rustc distribution process for “nightly”

- this is being used in the rustc distribution process internally

- this is a cargo executable that was built from source

- this is an `#[test]` that called `enable_nightly_features`

- this is an integration test that uses `ProcessBuilder`
that called `masquerade_as_nightly_cargo`
It’s public to allow tests use nightly features.
NOTE: this should be set before `configure()`. If calling this from an integration test,
consider using `ConfigBuilder::enable_nightly_features` instead.

## Implementations§
