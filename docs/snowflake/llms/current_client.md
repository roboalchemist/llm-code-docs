# Source: https://docs.snowflake.com/en/sql-reference/functions/current_client.md

Categories:
:   [Context functions](../functions-context.md) (General)

# CURRENT_CLIENT

Returns the version of the client from which the function was called. If called from an application using the JDBC or ODBC driver to connect to Snowflake, returns the version of the driver.

## Syntax

```sqlsyntax
CURRENT_CLIENT()
```

## Usage notes

* The Worksheet in the Snowflake web interface connects to Snowflake directly through the interface; it doesn’t use the JDBC or ODBC driver. As such, calling CURRENT_CLIENT in the Worksheet returns a
  different value than calling the function from a client application.

## Examples

Call CURRENT_CLIENT from within SnowSQL:

> ```sqlexample
> SELECT CURRENT_CLIENT();
>
> +------------------+
> | CURRENT_CLIENT() |
> |------------------|
> | SnowSQL 1.1.18   |
> +------------------+
> ```

Call CURRENT_CLIENT from within the Worksheet in Snowsight:

> ```sqlexample
> SELECT CURRENT_CLIENT();
> ```
>
> Results
>
> |  |  |
> | --- | --- |
> | row# | CURRENT_CLIENT() |
> | 1 | Snowflake UI 1434236365 |
