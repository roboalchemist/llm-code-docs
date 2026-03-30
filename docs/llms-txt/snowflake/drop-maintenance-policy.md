# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-maintenance-policy.md

# DROP MAINTENANCE POLICY

Removes a [maintenance policy](../../developer-guide/native-apps/consumer-maintenance-policies.md) from the current or specified schema. The command
fails if the maintenance policy is applied to an app or account.

See also:
:   [CREATE MAINTENANCE POLICY](create-maintenance-policy.md), [ALTER MAINTENANCE POLICY](alter-maintenance-policy.md), [SHOW MAINTENANCE POLICIES](show-maintenance-policies.md)

## Syntax

```sqlsyntax
DROP MAINTENANCE POLICY [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier of the maintenance policy to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| DROP MAINTENANCE POLICY | Maintenance policy |  |
| OWNERSHIP | Maintenance policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

## Examples

The following example drops a maintenance policy named `my_maintenance_policy`:

```sqlexample
DROP MAINTENANCE POLICY my_maintenance_policy;
```
