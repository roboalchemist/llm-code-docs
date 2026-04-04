# Source: https://docs.snowflake.com/en/sql-reference/functions/current_account.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# CURRENT_ACCOUNT

Returns the [account locator](../../user-guide/admin-account-identifier.md) used by the user’s current session.

> **Note:**
>
> If you want to find the [account name](../../user-guide/admin-account-identifier.md) rather than the account locator, use
> [CURRENT_ACCOUNT_NAME](current_account_name.md) instead. The preferred account identifier (`orgname-account_name`) uses
> the account name, not the account locator.

## Syntax

```sqlsyntax
CURRENT_ACCOUNT()
```

## Arguments

None.

## Returns

The data type of the returned value is `VARCHAR`.

## Examples

This shows how to call the `CURRENT_ACCOUNT` function:

> ```sqlexample
> SELECT CURRENT_ACCOUNT();
> ```
>
> Output:
>
> ```sqlexample
> +-------------------+
> | CURRENT_ACCOUNT() |
> |-------------------|
> | XY12345           |
> +-------------------+
> ```
