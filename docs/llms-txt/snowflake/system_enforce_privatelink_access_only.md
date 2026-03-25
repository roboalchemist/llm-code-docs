# Source: https://docs.snowflake.com/en/sql-reference/functions/system_enforce_privatelink_access_only.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$ENFORCE_PRIVATELINK_ACCESS_ONLY

Enforces the behavior that successful connections to your Snowflake account use only your private endpoints.
Blocks connections for inbound network traffic that are routed over the public internet.

## Syntax

```sqlsyntax
SYSTEM$ENFORCE_PRIVATELINK_ACCESS_ONLY()
```

## Arguments

None.

## Returns

Returns a VARCHAR message that successful inbound connections now use only private endpoints.

## Access control requirements

Only account administrators — users with the ACCOUNTADMIN role — can run this function.

## Example

To enforce the behavior that successful connections to your Snowflake account use only your private endpoints:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$ENFORCE_PRIVATELINK_ACCESS_ONLY();
```
