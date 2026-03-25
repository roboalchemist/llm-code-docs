# Source: https://docs.snowflake.com/en/sql-reference/functions/current_organization_name.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# CURRENT_ORGANIZATION_NAME

Returns the name of the organization to which the current account belongs.

## Syntax

```sqlsyntax
CURRENT_ORGANIZATION_NAME()
```

## Arguments

None.

## Returns

The data type of the returned value is `VARCHAR`.

## Example

This shows how to call the CURRENT_ORGANIZATION_NAME function:

> ```sqlexample
> SELECT CURRENT_ORGANIZATION_NAME();
> ```
>
> Output:
>
> ```output
> +-----------------------------+
> | CURRENT_ORGANIZATION_NAME() |
> |-----------------------------|
> | bazco                       |
> +-----------------------------+
> ```
