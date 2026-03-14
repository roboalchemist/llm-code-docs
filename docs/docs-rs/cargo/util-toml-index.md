cargo::util

# Module toml

Source

## Structs§

InheritableFieldsA group of fields that are inheritable by members of the workspace

## Traits§

ResolveToPath

## Functions§

is_embeddedSee also `bin/cargo/commands/run.rs`s `is_manifest_command`normalize_path_string_sepprepare_for_publishMake the `Package` self-contained so its ready for packagingprepare_target_for_publishprepare_targets_for_publishread_manifestLoads a `Cargo.toml` from a file on disk.to_real_manifestvalidate_profileChecks syntax validity and unstable feature gate for a given profile.
