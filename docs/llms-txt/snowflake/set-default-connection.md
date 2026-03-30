# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/connection-commands/set-default-connection.md

# snow connection set-default

Changes default connection to provided value.

## Syntax

```console
snow connection set-default
  <name>
  --format <format>
  --verbose
  --debug
  --silent
  --enhanced-exit-codes
  --decimal-precision <decimal_precision>
```

## Arguments

`name`
:   Name of the connection, as defined in your `config.toml` file.

## Options

`--format [TABLE|JSON|JSON_EXT|CSV]`
:   Specifies the output format. Default: TABLE.

`--verbose, -v`
:   Displays log entries for log levels `info` and higher. Default: False.

`--debug`
:   Displays log entries for log levels `debug` and higher; debug logs contain additional information. Default: False.

`--silent`
:   Turns off intermediate output to console. Default: False.

`--enhanced-exit-codes`
:   Differentiate exit error codes based on failure type. Default: False.

`--decimal-precision INTEGER`
:   Number of decimal places to display for decimal values. Uses Python’s default precision if not specified. [env var: SNOWFLAKE_DECIMAL_PRECISION].

`--help`
:   Displays the help text for this command.

## Usage notes

This command lets you change the default connection from the command line instead of changing the value of `default_connection_name` in the `config.toml` file each time. Using this command can simplify changing between multiple connections.

## Examples

```bash
snow connection set-default "my_test_connection"
```

```output
Default connection set to: my_test_connection
```
