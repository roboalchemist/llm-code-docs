cargo

# Module core

Source

## Re-exports§

`pub use self::dependency::Dependency;``pub use self::dependency::Patch;``pub use self::dependency::PatchLocation;``pub use self::dependency::SerializedDependency;``pub use self::features::CliUnstable;``pub use self::features::Edition;``pub use self::features::Feature;``pub use self::features::Features;``pub use self::manifest::EitherManifest;``pub use self::manifest::VirtualManifest;``pub use self::manifest::Manifest;``pub use self::manifest::Target;``pub use self::manifest::TargetKind;``pub use self::package::Package;``pub use self::package::PackageSet;``pub use self::package_id::PackageId;``pub use self::registry::Registry;``pub use self::resolver::Resolve;``pub use self::resolver::ResolveVersion;``pub use self::shell::Shell;``pub use self::shell::Verbosity;``pub use self::summary::FeatureMap;``pub use self::summary::FeatureValue;``pub use self::summary::Summary;`

## Modules§

compilerInteract with the compilerdependencyfeaturesSupport for nightly features in Cargo itself.gcSupport for garbage collecting unused files from downloaded files or
artifacts from the target directory.global_cache_trackerSupport for tracking the last time files were used to assist with cleaning
up those files if they haven’t been used in a while.manifestpackagepackage_idprofilesHandles built-in and customizable compiler flag presets.registryTypes that hold source information for a group of packages.resolverResolution of the entire dependency graph for a crate.shellsummary

## Structs§

PackageIdSpecSome or all of the data required to identify a package:SourceIdUnique identifier for a source of packages.WorkspaceThe core abstraction in Cargo for working with a workspace of crates.WorkspaceRootConfigIntermediate configuration of a workspace root in a manifest.

## Enums§

GitReferenceInformation to find a specific commit in a Git repository.MaybePackageSourceKindThe possible kinds of code source.WorkspaceConfigConfiguration of a workspace in a manifest.

## Traits§

PackageIdSpecQuery

## Functions§

find_workspace_rootFinds the path of the root of the workspace.find_workspace_root_with_membership_checkFinds the workspace root for a manifest, with minimal verification.resolve_relative_path
