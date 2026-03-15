env_logger
# Module fmt 
Source 
## Re-exports§
`pub use anstyle as style;``color`
## Structs§
ConfigurableFormatA custom format with settings for which fields to showFormatterA formatter to write logs into.Timestamp`humantime`An RFC3339 formatted timestamp.
## Enums§
TargetLog target, either `stdout`, `stderr` or a custom pipe.TimestampPrecisionFormatting precision of timestamps.WriteStyleWhether or not to print styles to the target.
## Functions§
default_kv_format`kv`Default Key Value Formathidden_kv_format`kv`Null Key Value Format