# Source: https://docs.snowflake.com/en/sql-reference/functions/current_account_name.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# CURRENT_ACCOUNT_NAME

Returns the name of the current account.

The preferred [account identifier](../../user-guide/admin-account-identifier.md) for the account consists of this account name along with the organization of the account (`orgname-account_name`).

## Syntax

```sqlsyntax
CURRENT_ACCOUNT_NAME()
```

## Arguments

None.

## Returns

Returns the name of the current account.

The data type of the returned value is `VARCHAR`.

## Example

This shows how to call the CURRENT_ACCOUNT_NAME function:

> ```sqlexample
> SELECT CURRENT_ACCOUNT_NAME();
> ```
>
> Output:
>
> ```output
> +-----------------------------+
> | CURRENT_ACCOUNT_NAME()      |
> |-----------------------------|
> | my_account1                 |
> +-----------------------------+
> ```
