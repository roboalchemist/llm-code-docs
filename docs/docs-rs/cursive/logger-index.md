cursive
# Module logger 
Source 
## Structs§
CursiveLoggerSaves all log records in a global deque.LOGSCircular buffer for logs. Use it to implement `DebugView`.RecordA log record.
## Functions§
get_loggerReturn a logger that stores records in cursive’s log queue.initInitialize the Cursive logger.logLog a record in cursive’s log queue.reserve_logsAdds `n` more entries to cursive’s log queue.set_external_filter_levelSets the external log filter level.set_filter_levels_from_envSets log filter levels based on environment variables `RUST_LOG` and `CURSIVE_LOG`.
If `RUST_LOG` is set, then both internal and external log levels are set to match.
If `CURSIVE_LOG` is set, then the internal log level is set to match with precedence over
`RUST_LOG`.set_internal_filter_levelSets the internal log filter level.