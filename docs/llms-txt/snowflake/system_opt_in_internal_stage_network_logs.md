# Source: https://docs.snowflake.com/en/sql-reference/functions/system_opt_in_internal_stage_network_logs.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$OPT_IN_INTERNAL_STAGE_NETWORK_LOGS

Starts record collection of network access attempts to internal stage locations for this account. You can view these records in the
[INTERNAL_STAGE_NETWORK_ACCESS_HISTORY view](../account-usage/internal_stage_network_access_history.md).

See also:
:   [SYSTEM$OPT_OUT_INTERNAL_STAGE_NETWORK_LOGS](system_opt_out_internal_stage_network_logs.md)

## Syntax

```sqlsyntax
SYSTEM$OPT_IN_INTERNAL_STAGE_NETWORK_LOGS()
```

## Arguments

None.

## Returns

Returns a VARCHAR status message, which states that record collection of network access attempts to internal stage locations has been enabled.

## Access control requirements

Only account administrators (users with the ACCOUNTADMIN role) can execute this function.

## Usage notes

Latency between running this function and record collection is up to 6 hours.

## Example

Start record collection of network access attempts to internal stage locations for this account:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$OPT_IN_INTERNAL_STAGE_NETWORK_LOGS();
```

```output
+-------------------------------------------------------------------+
| Record collection has been successfully enabled for this account. |
+-------------------------------------------------------------------+
```
