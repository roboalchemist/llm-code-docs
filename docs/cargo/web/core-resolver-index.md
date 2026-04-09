cargo::core

# Module resolver

Source

## Re-exports§

`pub use self::features::CliFeatures;``pub use self::features::ForceAllTargets;``pub use self::features::HasDevUnits;`

## Modules§

featuresResolves conditional compilation for `features` section in the manifest.

## Structs§

ResolveRepresents a fully-resolved package dependency graph. Each node in the graph
is a package and edges represent dependencies between packages.ResolveErrorError during resolution providing a path of `PackageId`s.ResolveOptsOptions for how the resolve should work.VersionPreferencesA collection of preferences for particular package versions.

## Enums§

ActivateErrorResolveBehaviorResolver behavior, used to opt-in to new behavior that is
backwards-incompatible via the `resolver` field in the manifest.ResolveVersionA version to indicate how a `Cargo.lock` should be serialized.VersionOrdering

## Functions§

resolveBuilds the list of all packages required to build the first argument.

## Type Aliases§

ActivateResult
