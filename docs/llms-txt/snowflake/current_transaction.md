# Source: https://docs.snowflake.com/en/sql-reference/functions/current_transaction.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# CURRENT_TRANSACTION

Returns the transaction id of an open transaction in the current session.

See also:
:   [LAST_TRANSACTION](last_transaction.md) , [DESCRIBE TRANSACTION](../sql/desc-transaction.md)

## Syntax

```sqlsyntax
CURRENT_TRANSACTION()
```

## Arguments

None.

## Examples

This shows the transaction ID of the current transaction:

> ```sqlexample
> SELECT CURRENT_TRANSACTION();
> ```
>
> Output:
>
> ```sqlexample
> +-----------------------+
> | CURRENT_TRANSACTION() |
> |-----------------------|
> | 1661899308790000000   |
> +-----------------------+
> ```
