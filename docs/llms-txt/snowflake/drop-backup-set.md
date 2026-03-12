# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-backup-set.md

# DROP BACKUP SET

Deletes a [backup](../../user-guide/backups.md) set.

See also:
:   [CREATE BACKUP SET](create-backup-set.md),
    [ALTER BACKUP SET](alter-backup-set.md),
    [SHOW BACKUP SETS](show-backup-sets.md)

## Syntax

```sqlsyntax
DROP BACKUP SET <name>
```

## Parameters

`name`
:   Specifies the identifier for the backup set.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Backup set | The role used to modify the backup policy for a backup set must have the OWNERSHIP privilege on the set. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

> **Important:**
>
> If the backup policy has a retention lock applied to it, and there are any
> unexpired backups in the backup set, then you can’t delete the backup set.
> In that case, you must wait for all the backups in the set to expire.
> This restriction applies even to privileged roles such as ACCOUNTADMIN, and to Snowflake support.
> For that reason, be careful when specifying retention lock and a long expiration
> period in a backup policy.
>
> You also can’t drop a backup set if any of the backups it contains have a legal hold applied.

## Examples

Delete the backup set `t1_backups`:

```sqlexample
DROP BACKUP SET t1_backups;
```
