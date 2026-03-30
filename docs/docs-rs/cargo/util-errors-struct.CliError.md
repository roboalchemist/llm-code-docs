cargo::util::errors

# Struct CliError

Source

```
pub struct CliError {
    pub error: Option<Error>,
    pub exit_code: i32,
}
```

## Fields§

§`error: Option<Error>`

The error to display. This can be `None` in rare cases to exit with a
code without displaying a message. For example `cargo run -q` where
the resulting process exits with a nonzero code (on Windows), or an
external subcommand that exits nonzero (we assume it printed its own
message).
§`exit_code: i32`

The process exit code.

## Implementations§
