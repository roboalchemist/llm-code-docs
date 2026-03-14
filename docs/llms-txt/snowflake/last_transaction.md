# Source: https://docs.snowflake.com/en/sql-reference/functions/last_transaction.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# LAST_TRANSACTION

Returns the transaction ID of the last transaction that was either committed or rolled back in the current session.

See also:
:   [CURRENT_TRANSACTION](current_transaction.md) , [DESCRIBE TRANSACTION](../sql/desc-transaction.md)

## Syntax

```sqlsyntax
LAST_TRANSACTION()
```

## Arguments

None

## Examples

This example calls the `LAST_TRANSACTION` function:

> ```sqlexample
> SELECT LAST_TRANSACTION();
> ```
>
> Output:
>
> ```sqlexample
> +---------------------+
> | LAST_TRANSACTION()  |
> |---------------------|
> | 1661899308790000000 |
> +---------------------+
> ```
