# Source: https://docs.snowflake.com/en/sql-reference/functions/system_disable_privatelink_access_only.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$DISABLE_PRIVATELINK_ACCESS_ONLY

Unblocks connections for inbound network traffic that are routed over the public internet.

## Syntax

```sqlsyntax
SYSTEM$DISABLE_PRIVATELINK_ACCESS_ONLY()
```

## Arguments

None.

## Returns

Returns a VARCHAR message that inbound connections can use the public internet.

## Access control requirements

Only account administrators — users with the ACCOUNTADMIN role — can run this function.

## Example

Restore public access for inbound network traffic to your Snowflake account:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$DISABLE_PRIVATELINK_ACCESS_ONLY();
```
