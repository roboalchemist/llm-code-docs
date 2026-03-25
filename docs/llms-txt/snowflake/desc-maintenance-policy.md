# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-maintenance-policy.md

# DESCRIBE MAINTENANCE POLICY

Shows the details of a [maintenance policy](../../developer-guide/native-apps/consumer-maintenance-policies.md).

See also:
:   [CREATE MAINTENANCE POLICY](create-maintenance-policy.md), [ALTER MAINTENANCE POLICY](alter-maintenance-policy.md), [DROP MAINTENANCE POLICY](drop-maintenance-policy.md), [SHOW MAINTENANCE POLICIES](show-maintenance-policies.md)

## Syntax

```sqlsyntax
DESCRIBE MAINTENANCE POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier of the maintenance policy to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| APPLY MAINTENANCE POLICY | Account |  |
| OWNERSHIP | Maintenance policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

## Examples

The following example describes a maintenance policy named `my_maintenance_policy`:

```sqlexample
DESCRIBE MAINTENANCE POLICY my_maintenance_policy;
```
