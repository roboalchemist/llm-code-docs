# Crate cargo

Source

## Re-exports§

`pub use crate::util::errors::AlreadyPrintedError;``pub use crate::util::errors::InternalError;``pub use crate::util::errors::VerboseError;``pub use crate::util::CargoResult;``pub use crate::util::CliError;``pub use crate::util::CliResult;``pub use crate::util::GlobalContext;``pub use crate::util::indented_lines;`

## Modules§

corelintsopssourcesThe trait for sources of Cargo packages and its built-in implementations.util

## Macros§

__shell_printdrop_eprintdrop_eprintlndrop_printdrop_printlntry_old_curlWhen dynamically linked against libcurl, we want to ignore some failures
when using old versions that don’t support certain features.try_old_curl_http2_pipewaitEnable HTTP/2 and pipewait to be used as it’ll allow true multiplexing
which makes downloads much faster.

## Constants§

CARGO_ENV

## Functions§

display_errorDisplays an error, and all its causes, to stderr.display_warning_with_errorDisplays a warning, with an error object providing detailed information
and context.exit_with_errorversionReturns information about cargo’s version.
