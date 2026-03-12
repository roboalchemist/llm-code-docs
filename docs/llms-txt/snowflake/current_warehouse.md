# Source: https://docs.snowflake.com/en/sql-reference/functions/current_warehouse.md

Categories:
:   [Context functions](../functions-context.md) (Session Object)

# CURRENT_WAREHOUSE

Returns the name of the warehouse in use for the current session.

To specify a different warehouse for the session, execute the [USE WAREHOUSE](../sql/use-warehouse.md)
command.

## Syntax

```sqlsyntax
CURRENT_WAREHOUSE()
```

## Arguments

None.

## Examples

Show the current warehouse, database, and schema:

> ```sqlexample
> SELECT CURRENT_WAREHOUSE(), CURRENT_DATABASE(), CURRENT_SCHEMA();
> ```
>
> Output:
>
> ```sqlexample
> +---------------------+--------------------+------------------+
> | CURRENT_WAREHOUSE() | CURRENT_DATABASE() | CURRENT_SCHEMA() |
> |---------------------+--------------------+------------------|
> | DEV_WAREHOUSE       | TEST_DATABASE      | UDF_TEST_SCHEMA  |
> +---------------------+--------------------+------------------+
> ```
