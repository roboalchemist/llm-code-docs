# Source: https://docs.snowflake.com/en/sql-reference/functions/current_ip_address.md

Categories:
:   [Context functions](../functions-context.md)

# CURRENT_IP_ADDRESS

Returns the IP address of the client that submitted the request.

## Syntax

```sqlsyntax
CURRENT_IP_ADDRESS()
```

## Arguments

None.

## Examples

Return the current IP address of the client that is connected to Snowflake:

> ```sqlexample
> select current_ip_address();
>
> +----------------------+
> | CURRENT_IP_ADDRESS() |
> +----------------------+
> | 192.0.2.255          |
> +----------------------+
> ```
