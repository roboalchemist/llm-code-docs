# Source: https://docs.silabs.com/openthread/3.0.0/using-co-processor-communication-daemon/04-troubleshooting.md

# Troubleshooting

If an error or a warning occurs during CPCd runtime, it prints to the console STDERR. If additional debugging is required, tracing can be enabled.

> **Note**: Enabling traces may impact performance.

## Tracing to the Standard Output (stdout)

When the configuration STDOUT_TRACE is enabled, the CPC daemon prints traces to the console.

## Tracing to a File

When the configuration TRACE_TO_FILE is enabled. the CPC daemon prints traces to a file. The tracing file name contains the date and timestamp. This file is placed in the folder specified in the configuration TRACES_FOLDER.

The trace file has the following format:

```sh
trace-<year>-<month>-<day>-<hour>-<minute>-<second>.txt
```

The timestamp uses the operating system’s local time zone.

> **Note**: Only enable tracing to a file when debugging, as log file size increases over time.