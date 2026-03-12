# Source: https://docs.snowflake.com/en/sql-reference/sql/undrop-dynamic-table.md

# UNDROP DYNAMIC TABLE

Restores the most recent version of a dropped [dynamic table](../../user-guide/dynamic-tables-about.md).

See also:
:   [CREATE DYNAMIC TABLE](create-dynamic-table.md), [ALTER DYNAMIC TABLE](alter-dynamic-table.md), [DESCRIBE DYNAMIC TABLE](desc-dynamic-table.md),
    [SHOW DYNAMIC TABLES](show-dynamic-tables.md), [DROP DYNAMIC TABLE](drop-dynamic-table.md)

## Syntax

```sqlsyntax
UNDROP DYNAMIC TABLE <name>
```

## Parameters

`name`
:   Specifies the identifier for the dynamic table to restore.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | The dynamic table that you want to undrop. |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* To undrop a dynamic table, you must be using a role that has OWNERSHIP privilege
  on that dynamic table.
* If a table with the same name already exists, an error is returned.

* UNDROP relies on the Snowflake [Time Travel](../../user-guide/data-time-travel.md) feature. An object can be restored only if
  the object was deleted within the [Data retention period](../../user-guide/data-time-travel.md). The default value is 24 hours.

## Examples

Restore the most recent version of a dropped dynamic table:

```sqlexample
UNDROP DYNAMIC TABLE my_dynamic_table;
```
