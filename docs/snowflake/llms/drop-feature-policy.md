# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-feature-policy.md

# DROP FEATURE POLICY

Removes the specified [feature policy](../../developer-guide/native-apps/ui-consumer-feature-policies.md).

See also:
:   [CREATE FEATURE POLICY](create-feature-policy.md) , [ALTER FEATURE POLICY](alter-feature-policy.md), [DESCRIBE FEATURE POLICY](desc-feature-policy.md), [SHOW FEATURE POLICIES](show-feature-policies.md)

## Syntax

```sqlsyntax
DROP FEATURE POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the feature policy to drop.

If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
Identifiers enclosed in double quotes are also case-sensitive.

For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Feature policy | This privilege is required to drop a feature policy. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage Notes

* A feature policy can’t be dropped if it is currently applied to an object. Use the
  [ALTER FEATURE POLICY](alter-feature-policy.md) command to un-apply the feature policy
  from the object, then drop the feature policy.

## Examples

The following example drops the feature policy named `block_db_policy`:

```sqlexample
DROP FEATURE POLICY block_db_policy;
```

```output
+---------------------------------------+
| status                                |
|---------------------------------------|
| BLOCK_DB_POLICY successfully dropped. |
+---------------------------------------+
```
