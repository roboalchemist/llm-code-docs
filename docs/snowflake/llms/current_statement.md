# Source: https://docs.snowflake.com/en/sql-reference/functions/current_statement.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# CURRENT_STATEMENT

Returns the SQL text of the statement that is currently executing.

## Syntax

```sqlsyntax
CURRENT_STATEMENT()
```

## Arguments

None.

## Examples

This shows a simple example of using the `CURRENT_STATEMENT` function:

> ```sqlexample
> SELECT 2.71, CURRENT_STATEMENT();
> ```
>
> Output:
>
> ```sqlexample
> +------+-----------------------------------+
> | 2.71 | CURRENT_STATEMENT()               |
> |------+-----------------------------------|
> | 2.71 | SELECT 2.71, CURRENT_STATEMENT(); |
> +------+-----------------------------------+
> ```
