cargo

# Module util

Source

## Re-exports§

`pub use self::context::ConfigValue;``pub use self::context::GlobalContext;``pub use self::context::homedir;``pub use self::diagnostic_server::RustfixDiagnosticServer;``pub use self::edit_distance::closest;``pub use self::edit_distance::closest_msg;``pub use self::edit_distance::edit_distance;``pub use self::errors::CliError;``pub use self::errors::CargoResult;``pub use self::errors::CliResult;``pub use self::errors::internal;``pub use self::flock::FileLock;``pub use self::flock::Filesystem;``pub use self::graph::Graph;``pub use self::hex::hash_u64;``pub use self::hex::short_hash;``pub use self::hex::to_hex;``pub use self::into_url::IntoUrl;``pub use self::logger::BuildLogger;``pub use self::rustc::Rustc;`

## Modules§

authRegistry authentication support.cache_lockSupport for locking the package and index caches.command_preludecontextCargo’s config system.cpucredentialBuilt-in Cargo credential providersdiagnostic_serverA small TCP server to handle collection of diagnostics information in a
cross-platform way for the `cargo fix` command.edit_distanceerrorsflockFile-locking support.frontmattergraphheximportant_pathsinterninginto_urljobJob management (mostly for windows)log_messageMessages for logging.loggerBuild analysis logging infrastructure.machine_messagenetworkUtilities for networking.openFor opening files or URLs with the preferred application.restricted_namesHelpers for validating and checking names like package and crate names.rustcsqliteUtilities to help with working with sqlite.styletomltoml_mutUtilities for in-place editing of Cargo.toml manifests.

## Structs§

CanonicalUrlA newtype wrapper around `Url` which represents a “canonical” version of an
original URL.DependencyQueueFossilRepoGitRepoHgRepoHumanBytesFormats a number of bytes into a human readable SI-prefixed size.LockServerLockServerClientLockServerStartedPijulRepoProgressCLI progress bar.QueueA simple, threadsafe, queue of items of type `T`

## Enums§

OptVersionReqProgressStyleIndicates the style of information for displaying the amount of progress.

## Traits§

IntoUrlWithBaseA type that can be interpreted as a relative Url and converted to
a Url.OnceExtVersionExt

## Functions§

add_path_argselapsedexisting_vcs_repoget_umaskGet the current `umask` value.hostnameReturns the hostname of the current system.indented_linesis_rustuppath_argsThe source path and its current dir for use in compilation.print_available_benchesprint_available_binariesprint_available_examplesprint_available_packagesprint_available_teststruncate_with_ellipsistry_canonicalize

## Type Aliases§

StableHasherStable 128-bits Sip Hasher
