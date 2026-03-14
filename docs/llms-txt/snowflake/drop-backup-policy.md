# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-backup-policy.md

# DROP BACKUP POLICY

Deletes a [backup](../../user-guide/backups.md) policy.

See also:
:   [CREATE BACKUP POLICY](create-backup-policy.md),
    [ALTER BACKUP POLICY](alter-backup-policy.md),
    [SHOW BACKUP POLICIES](show-backup-policies.md)

## Syntax

```sqlsyntax
DROP BACKUP POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the backup policy.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Backup policy | The role used to delete a backup policy must have the OWNERSHIP privilege on the policy. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

A backup policy can’t be deleted if it is attached to any backup set.

## Examples

Delete the backup policy `hourly_backup_policy`:

```sqlexample
DROP BACKUP POLICY hourly_backup_policy;
```
