# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-replication-group.md

# DROP REPLICATION GROUP

Removes a [replication group](../../user-guide/account-replication-intro.md) from the account.

See also:
:   [CREATE REPLICATION GROUP](create-replication-group.md) , [ALTER REPLICATION GROUP](alter-replication-group.md) , [SHOW REPLICATION GROUPS](show-replication-groups.md)

## Syntax

```sqlsyntax
DROP REPLICATION GROUP [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the replication group.

## Usage notes

* Only a user with a role with the OWNERSHIP privilege on the group can execute this SQL command.
* A primary replication group can only be successfully dropped if no linked secondary replication groups exist.
* A database that is included in a replication group is not dropped when the replication group is dropped.

  * If a secondary replication group is dropped, any database previously included in the group loses read-only protection and becomes writable.
  * If the secondary replication group is re-created from the same primary replication group as before, the databases in the group are
    overwritten by the databases in the primary replication group during the first refresh. These databases are read-only.
* To retrieve the set of accounts in your organization that are enabled for replication, use
  [SHOW REPLICATION ACCOUNTS](show-replication-accounts.md).
* To retrieve the list of replication groups in your organization, use [SHOW REPLICATION GROUPS](show-replication-groups.md). The
  `allowed_accounts` column lists all target accounts enabled for object replication from a source account.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop the replication group `myrg`:

```sqlexample
DROP REPLICATION GROUP myrg;
```
