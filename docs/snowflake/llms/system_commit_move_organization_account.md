# Source: https://docs.snowflake.com/en/sql-reference/functions/system_commit_move_organization_account.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$COMMIT_MOVE_ORGANIZATION_ACCOUNT

Finalizes the process of moving an [organization account](../../user-guide/organization-accounts.md) from one region to another.

The process of moving the organization account began when the [SYSTEM$INITIATE_MOVE_ORGANIZATION_ACCOUNT](system_initiate_move_organization_account.md) was
called.

See also:
:   [SYSTEM$INITIATE_MOVE_ORGANIZATION_ACCOUNT](system_initiate_move_organization_account.md) , [SYSTEM$SHOW_MOVE_ORGANIZATION_ACCOUNT_STATUS](system_show_move_organization_account_status.md)

## Syntax

```sqlsyntax
SYSTEM$COMMIT_MOVE_ORGANIZATION_ACCOUNT( <grace_period> )
```

## Arguments

`grace_period`
:   Specifies the number of days after which the organization account in the original region (that is, the source region) will be deleted.

## Access control requirements

Only users with the GLOBALORGADMIN role can call this function.

## Usage notes

* You are automatically logged out of Snowflake immediately after calling this function.
* Until the process of finalizing the move completes (usually within a few minutes), you cannot sign in to the organization account in the
  source region nor the organization account in the target region.
* When the finalization process completes, the name of the organization account in the new region changes from the temporary name that was
  specified by the [SYSTEM$INITIATE_MOVE_ORGANIZATION_ACCOUNT](system_initiate_move_organization_account.md) function to the original name of the
  organization account.
* To check the status of the finalization process, call the [SYSTEM$SHOW_MOVE_ORGANIZATION_ACCOUNT_STATUS](system_show_move_organization_account_status.md)
  function.

## Examples

Delete the original organization account 14 days after the move is finalized:

```sqlexample
SELECT SYSTEM$COMMIT_MOVE_ORGANIZATION_ACCOUNT(14);
```
