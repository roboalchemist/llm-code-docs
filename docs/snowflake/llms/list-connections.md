# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/connection-commands/list-connections.md

# snow connection list

Lists configured connections.

## Syntax

```console
snow connection list
  --format <format>
  --verbose
  --debug
  --silent
  --enhanced-exit-codes
  --decimal-precision <decimal_precision>
```

## Arguments

None

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

The `snow connection list` command lists the connections in your default `config.toml` file.
For more information, see [Configuring Snowflake CLI and connecting to Snowflake](../../connecting/connect.md).

## Examples

```snowcli
snow connection list
```

```output
+--------------------------------------------------------------------------------------------------------------------------------+
| connection_name | parameters                                                                                                   |
|-----------------+--------------------------------------------------------------------------------------------------------------|
| my-prod         | {'account': 'po52878', 'user': 'JDOE', 'password': '****', 'role': 'integration_tests', 'database':          |
|                 | 'SNOWFLAKE'}                                                                                                 |
|-----------------+--------------------------------------------------------------------------------------------------------------|
| my-test         | {'account': 'po52878', 'user': 'SSMITH', 'password': '****', 'role': 'integration_tests', 'database':        |
|                 | 'SNOWFLAKE'}                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------+
```
