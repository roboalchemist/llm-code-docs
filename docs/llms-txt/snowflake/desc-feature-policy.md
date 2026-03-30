# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-feature-policy.md

# DESCRIBE FEATURE POLICY

Describes the properties of a [feature policy](../../developer-guide/native-apps/ui-consumer-feature-policies.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE FEATURE POLICY](create-feature-policy.md) , [ALTER FEATURE POLICY](alter-feature-policy.md), [DROP FEATURE POLICY](drop-feature-policy.md), [SHOW FEATURE POLICIES](show-feature-policies.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } FEATURE POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the feature policy to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Output

The command displays properties of a feature policy in the following columns:

| Column | Description |
| --- | --- |
| `property` | The name of the feature property policy. This column can include the properties listed in the following table. |
| `value` | The value assigned to the property of the feature policy. |

The `property` column can include the following properties of a feature policy:

| Property | Description |
| --- | --- |
| `created_on` | The timestamp when the feature policy was created. |
| `name` | The name of the feature policy. |
| `owner` | The role that owns the feature policy. |
| `owner_role_type` | The type of role that owns the object: ROLE or DATABASE_ROLE |
| `comment` | A description of the feature policy. |
| `blocked_object_types_for_creation` | The list of objects that the feature policy blocks for creation. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| APPLY FEATURE POLICY | Account |  |
| OWNERSHIP or APPLY | Feature policy |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

The following example describes the feature policy named `block_db_policy`:

```sqlexample
DESCRIBE FEATURE POLICY block_db_policy;
```

```output
+------------------------------------+-------------------------------+
| property                           | value                         |
+------------------------------------|-------------------------------+
| created_on                         | 2025-05-23 08:19:49.483 -0700 |
| name                               | BLOCK_CREATE_DB_POLICY        |
| owner                              | ACCOUNTADMIN                  |
| owner_role_type                    | ROLE                          |
| comment                            |                               |
| blocked_object_types_for_creation  | DATABASES                     |
+------------------------------------+-------------------------------+
```
