# Source: https://docs.snowflake.com/en/sql-reference/functions/system_unset_event_sharing_account_for_region.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$UNSET_EVENT_SHARING_ACCOUNT_FOR_REGION

Unsets the events account for a region.

See also:
:   [SYSTEM$SET_EVENT_SHARING_ACCOUNT_FOR_REGION](system_set_event_sharing_account_for_region.md)

## Syntax

```sqlsyntax
SYSTEM$UNSET_EVENT_SHARING_ACCOUNT_FOR_REGION( '<snowflake_region>' , '<region_group>' , '<account_name>' )
```

## Arguments

`snowflake_region`
:   Specifies the region where the account is located, for example: `AWS_US_WEST_2, AWS_US_EAST_1`.

`region_group`
:   Specifies the region group, for example: `PUBLIC`.

`account_name`
:   Specifies the account name.

## Access control requirements

* Only [organization administrators](../../user-guide/organization-administrators.md) can execute this SQL function.

## Examples

```sqlexample
SELECT SYSTEM$UNSET_EVENT_SHARING_ACCOUNT_FOR_REGION('aws_us_west_2', 'public', 'myaccount');
```
