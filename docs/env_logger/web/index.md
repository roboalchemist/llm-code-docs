# Crate env_logger 
Source 
## Re-exports§
`pub use self::fmt::Target;``pub use self::fmt::TimestampPrecision;``pub use self::fmt::WriteStyle;`
## Modules§
fmtFormatting for log records.
## Structs§
Builder`Builder` acts as builder for initializing a `Logger`.EnvSet of environment variables to configure from.LoggerThe env logger.
## Constants§
DEFAULT_FILTER_ENVThe default name for the environment variable to read filters from.DEFAULT_WRITE_STYLE_ENVThe default name for the environment variable to read style preferences from.
## Functions§
builderCreate a new builder with the default environment variables.from_envDeprecatedCreate a builder from the given environment variables.initInitializes the global logger with an env logger.init_from_envInitializes the global logger with an env logger from the given environment
variables.try_initAttempts to initialize the global logger with an env logger.try_init_from_envAttempts to initialize the global logger with an env logger from the given
environment variables.