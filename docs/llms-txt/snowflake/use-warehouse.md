# Source: https://docs.snowflake.com/en/sql-reference/sql/use-warehouse.md

# USE WAREHOUSE

Specifies the active/current [virtual warehouse](../../user-guide/warehouses-overview.md) for the session.
You must specify a warehouse for a session, and the warehouse must be running
before you can execute queries and DML statements in the session.

To view the current warehouse for a session, call the [CURRENT_WAREHOUSE](../functions/current_warehouse.md) context function.

See also:
:   [ALTER WAREHOUSE](alter-warehouse.md) , [CREATE WAREHOUSE](create-warehouse.md) , [SHOW WAREHOUSES](show-warehouses.md)

## Syntax

```sqlsyntax
USE WAREHOUSE <name>
```

## Parameters

`name`
:   Specifies the identifier for the warehouse to use for the session. If the identifier contains spaces or special characters, the entire
    string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Examples

The following example specifies the warehouse where the current session
performs its work:

```sqlexample
USE WAREHOUSE mywarehouse;
```

The following example changes from one warehouse to another, then back to
the original warehouse. The name of the original warehouse is stored in a
variable. Run the following commands:

```sqlexample
SELECT CURRENT_WAREHOUSE();
SET original_warehouse = (SELECT CURRENT_WAREHOUSE());
USE WAREHOUSE warehouse_two;
SELECT CURRENT_WAREHOUSE();
USE WAREHOUSE IDENTIFIER($original_warehouse);
SELECT CURRENT_WAREHOUSE();
```

The output for these commands shows how the current warehouse value changes:

```output
>SELECT CURRENT_WAREHOUSE();
+---------------------+
| WAREHOUSE_ONE       |
+---------------------+

>SET original_warehouse = (SELECT CURRENT_WAREHOUSE());

>USE WAREHOUSE warehouse_two;
>SELECT CURRENT_WAREHOUSE();
+---------------------+
| WAREHOUSE_TWO       |
+---------------------+

>USE WAREHOUSE IDENTIFIER($original_warehouse);
>SELECT CURRENT_WAREHOUSE();
+---------------------+
| WAREHOUSE_ONE       |
+---------------------+
```
