# Source: https://docs.snowflake.com/en/sql-reference/functions/system_initiate_move_organization_account.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$INITIATE_MOVE_ORGANIZATION_ACCOUNT

Starts the process of moving an [organization account](../../user-guide/organization-accounts.md) to a new region.

See also:
:   [SYSTEM$COMMIT_MOVE_ORGANIZATION_ACCOUNT](system_commit_move_organization_account.md) , [SYSTEM$SHOW_MOVE_ORGANIZATION_ACCOUNT_STATUS](system_show_move_organization_account_status.md)

## Syntax

```sqlsyntax
SYSTEM$INITIATE_MOVE_ORGANIZATION_ACCOUNT(
    '<temp_name>' ,
    '<region>' ,
    { 'ALL' | '<object> [, <object> ...]' } )
```

## Arguments

`'temp_name'`
:   Specifies a temporary account name by which the organization account in the new region can be identified until the move is finalized. The
    name must start with a letter and can only contain uppercase letters, numbers, and underscores.

    The name of the organization account in the new region changes from this temporary account name to the name of the original organization
    account when the [SYSTEM$COMMIT_MOVE_ORGANIZATION_ACCOUNT](system_commit_move_organization_account.md) function finishes successfully.

`'region'`
:   [Snowflake Region ID](../../user-guide/admin-account-identifier.md) of the region where the organization account will be moved.

`{ 'ALL' | 'object [, object ...]' }`
:   List of objects that will be moved to the organization account in its new region. Because Snowflake uses replication groups to move the
    objects, you can only move objects that are supported by replication groups, which varies depending on your Snowflake edition. For a list
    of objects that can be moved, see [Replicated objects](../../user-guide/account-replication-intro.md).

    To move all objects that can be replicated, specify `ALL`.

## Access control requirements

Only users with the GLOBALORGADMIN role can call this function.

## Usage notes

* You cannot sign in to the organization account in the new region until the initiation process is complete. To check the status of the
  process, call the [SYSTEM$SHOW_MOVE_ORGANIZATION_ACCOUNT_STATUS](system_show_move_organization_account_status.md) function.
* After the initiation process completes, you can sign in to the organization account in the new region using its temporary name, but cannot
  execute any SQL statement other than SELECT, USE, and SHOW.

## Examples

```sqlexample
SELECT SYSTEM$INITIATE_MOVE_ORGANIZATION_ACCOUNT('TEMP_ACCT', 'aws_us_west_2', 'ALL');
```
