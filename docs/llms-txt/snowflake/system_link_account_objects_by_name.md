# Source: https://docs.snowflake.com/en/sql-reference/functions/system_link_account_objects_by_name.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$LINK_ACCOUNT_OBJECTS_BY_NAME

Adds a global identifier to account objects in the target (current) account that were created using scripts
and that match objects with the same names in the source account.

Global identifiers are only added to account objects that are included in a replication or failover group for the
following object types:

* `RESOURCE_MONITOR`
* `ROLE`
* `USER`
* `WAREHOUSE`

For more information, refer to [Apply global IDs to objects created by scripts in target accounts](../../user-guide/account-replication-config.md).

## Syntax

```sqlsyntax
SYSTEM$LINK_ACCOUNT_OBJECTS_BY_NAME('<group_name>')
```

## Arguments

`group_name`
:   Specifies the identifier for the replication or failover group.

## Usage notes

* Only account administrators (users with the ACCOUNTADMIN role) can execute this SQL function.
* To retain account objects that exist only in the target account, replicate them
  manually in the source account before executing this function.

## Examples

```sqlexample
SELECT SYSTEM$LINK_ACCOUNT_OBJECTS_BY_NAME('myfg');
```
