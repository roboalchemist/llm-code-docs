nix

# Module syslog

Source Available on **crate feature `syslog`** only.

## Structs§

LogFlagsOptions for system logging.LogMaskSystem log priority mask.PriorityThe priority for a log message.

## Enums§

FacilityFacilities for log messages.SeveritySeverity levels for log messages.

## Functions§

closelogCloses the log file.openlogLinuxLogging options of subsequent `syslog` calls can be set by calling `openlog`.setlogmaskSet the process-wide priority mask to `mask` and return the previous mask
value.syslogWrites message to the system message logger.
