# Source: https://docs.snowflake.com/en/sql-reference/functions/system_show_move_organization_account_status.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$SHOW_MOVE_ORGANIZATION_ACCOUNT_STATUS

Returns the status of an attempt to move an [organization account](../../user-guide/organization-accounts.md).

See also:
:   [SYSTEM$INITIATE_MOVE_ORGANIZATION_ACCOUNT](system_initiate_move_organization_account.md) , [SYSTEM$COMMIT_MOVE_ORGANIZATION_ACCOUNT](system_commit_move_organization_account.md)

## Syntax

```sqlsyntax
SYSTEM$SHOW_MOVE_ORGANIZATION_ACCOUNT_STATUS( )
```

## Arguments

None.

## Returns

The following are the possible statuses:

| Code | Status |
| --- | --- |
| 060050 | Move of the current organization account has been initiated. |
| 060051 | Created a new organization account as the destination for migrating the existing organization account. |
| 060052 | Objects are being replicated from the current organization account to the target organization account. Target organization account is currently locked and not ready for use. |
| 060053 | Initial replication of objects is complete and the target organization account is ready to be reviewed. If you are ready to proceed with the move please run SYSTEM$COMMIT_MOVE_ORGANIZATION_ACCOUNT(<GRACE_PERIOD_IN_DAYS>). |
| 060054 | Commit of organization account move in progress. |
| 060055 | The move has been completed successfully. The original organization account is locked and will be deleted in x days. |
| 060056 | The organization account move failed. |
| 060057 | Cannot fetch status of organization account move. |

## Access control requirements

Only users with the GLOBALORGADMIN role can call this function.

## Usage notes

Only shows the status of the latest attempt to move the organization account.

## Example

```sqlexample
SELECT SYSTEM$SHOW_MOVE_ORGANIZATION_ACCOUNT_STATUS();
```
