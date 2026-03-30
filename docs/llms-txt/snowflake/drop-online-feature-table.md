# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-online-feature-table.md

# DROP ONLINE FEATURE TABLE

Removes the specified [online feature table](create-online-feature-table.md) from the current/specified
schema.

See also:
:   [CREATE ONLINE FEATURE TABLE](create-online-feature-table.md) , [ALTER ONLINE FEATURE TABLE](alter-online-feature-table.md), [DESCRIBE ONLINE FEATURE TABLE](desc-online-feature-table.md) , [SHOW ONLINE FEATURE TABLES](show-online-feature-tables.md)

## Syntax

```sqlsyntax
DROP ONLINE FEATURE TABLE [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the online feature table to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`IF EXISTS`
:   Specifies to not return an error if the online feature table does not exist.

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Online feature table | Role that has the OWNERSHIP privilege on the online feature table. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage Notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

The following example drops the online feature table named `my_online_feature_table`:

```sqlexample
DROP ONLINE FEATURE TABLE my_online_feature_table;
```

```output
+------------------------------------------------+
| status                                         |
|------------------------------------------------|
| MY_ONLINE_FEATURE_TABLE successfully dropped. |
+------------------------------------------------+
```

The following example drops the online feature table named `my_online_feature_table` if it exists:

```sqlexample
DROP ONLINE FEATURE TABLE IF EXISTS my_online_feature_table;
```
