# Source: https://docs.snowflake.com/en/sql-reference/functions/current_region.md

Categories:
:   [Context functions](../functions-context.md) (General)

# CURRENT_REGION

Returns the name of the region for the account where the current user is logged in.

For organizations that have accounts in multiple [region groups](../../user-guide/admin-account-identifier.md), returns `region_group.region`.

## Syntax

```sqlsyntax
CURRENT_REGION()
```

## Arguments

None.

## Examples

Show the current region:

> ```sqlexample
> SELECT CURRENT_REGION();
> ```
>
> Output:
>
> ```sqlexample
> +------------------+
> | CURRENT_REGION() |
> |------------------|
> | AWS_US_WEST_2    |
> +------------------+
> ```

Show the current region when the current user is logged into an account in an organization that spans multiple region groups:

> ```sqlexample
> SELECT CURRENT_REGION();
> ```
>
> Output:
>
> ```sqlexample
> +----------------------+
> | CURRENT_REGION()     |
> |----------------------|
> | PUBLIC.AWS_US_WEST_2 |
> +----------------------+
> ```
