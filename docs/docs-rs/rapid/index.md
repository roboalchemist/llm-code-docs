# Crate rapid 
Source 
## Re-exports§
`pub extern crate time;`
## Modules§
_coreThe Rust Core Libraryfail_methodslogger
## Macros§
__lazy_static_createbaildebugLogs a message at the debug level.ensureExits a function early with an `Error` if the condition is not satisfied.errorLogs a message at the error level.format_errConstructs an `Error` using the standard string interpolation syntax.infoLogs a message at the info level.lazy_staticlogThe standard logging macro.log_enabledDetermines if a message logged at the specified level in that module will
be logged.log_processrun_and_measuretraceLogs a message at the trace level.warnLogs a message at the warn level.
## Structs§
AppBacktraceA `Backtrace`.CausesA iterator over the causes of a `Fail`CompatA compatibility wrapper around an error type from this crate.ContextAn error with context around it.CumulativeErrorErrorThe `Error` type, which can contain any failure.LogLocationThe location of a log message.LogMetadataMetadata about a log message.LogRecordThe “payload” of a log message.MaxLogLevelFilterA token providing read and write access to the global maximum log level
filter.SetLoggerErrorThe type returned by `set_logger` if `set_logger` has already been called.ShutdownLoggerErrorThe type returned by `shutdown_logger_raw` if `shutdown_logger_raw` has
already been called or if `set_logger_raw` has not been called yet.SyncFailureWrapper for `std` errors to make them `Sync`.
## Enums§
LogLevelAn enum representing the available verbosity levels of the logging frameworkLogLevelFilterAn enum representing the available verbosity level filters of the logging
framework.StdResult`Result` is a type that represents either success (`Ok`) or failure (`Err`).
## Traits§
AsFailThe `AsFail` traitCumulativeErrorCollectorErrorMethodsFailThe `Fail` trait.FailMethodsLazyStaticSupport trait for enabling a few common operation on lazy static values.LogA trait encapsulating the operations required of a loggerOptionMethodsResultExtExtension methods for `Result`.ResultMethods__DerefUsed for immutable dereferencing operations, like `*v`.
## Functions§
err_msgConstructs a `Fail` type from a string.initializeTakes a shared reference to a lazy static and initializes
it if it has not been already.max_log_levelReturns the current maximum log level.set_loggerSets the global logger.set_logger_raw⚠Sets the global logger from a raw pointer.shutdown_loggerShuts down the global logger.shutdown_logger_rawShuts down the global logger.
## Type Aliases§
FallibleA common result with an `Error`.Result
## Derive Macros§
DeserializeFailSerialize