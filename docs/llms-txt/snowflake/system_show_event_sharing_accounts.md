# Source: https://docs.snowflake.com/en/sql-reference/functions/system_show_event_sharing_accounts.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$SHOW_EVENT_SHARING_ACCOUNTS

Shows event accounts in a provider organization.

This system function returns a string in JSON format containing a list of event accounts within the organization.
Because the metadata takes some time to propagate to all regions, this function might experience some delay when
showing latest events account after the user sets or unsets an events account for the organization.

## Syntax

```sqlsyntax
SYSTEM$SHOW_EVENT_SHARING_ACCOUNTS()
```

## Arguments

None.

## Access control requirements

* Only [organization administrators](../../user-guide/organization-administrators.md) can execute this SQL function.

## Examples

```sqlexample
SELECT SYSTEM$SHOW_EVENT_SHARING_ACCOUNTS();
```
