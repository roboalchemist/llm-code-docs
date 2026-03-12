# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-dynamic-table.md

# DROP DYNAMIC TABLE

Removes a [dynamic table](../../user-guide/dynamic-tables-about.md) from the current/specified schema.

See also:
:   [CREATE DYNAMIC TABLE](create-dynamic-table.md), [ALTER DYNAMIC TABLE](alter-dynamic-table.md), [DESCRIBE DYNAMIC TABLE](desc-dynamic-table.md),
    [SHOW DYNAMIC TABLES](show-dynamic-tables.md), [UNDROP DYNAMIC TABLE](undrop-dynamic-table.md)

## Syntax

```sqlsyntax
DROP DYNAMIC TABLE [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the dynamic table to drop. If the identifier contains spaces, special characters, or mixed-case
    characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive
    (e.g. `"My Object"`).

    If the table identifier is not fully-qualified (in the form of `db_name.schema_name.table_name` or
    `schema_name.table_name`), the command looks for the table in the current schema for the session.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | The dynamic table that you want to drop. |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* To drop a dynamic table, you must be using a role that has OWNERSHIP privilege on that dynamic table.
* You can also drop a dynamic table using the [DROP TABLE](drop-table.md) command.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop `my_dynamic_table`:

> ```sqlexample
> DROP DYNAMIC TABLE my_dynamic_table;
> ```
>
> ```sqlexample
> DROP TABLE my_dynamic_table;
> ```
