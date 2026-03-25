# Source: https://docs.snowflake.com/en/sql-reference/sql/undrop-table.md

# UNDROP TABLE

Restores the most recent version of a dropped table.

See also:
:   [CREATE TABLE](create-table.md) , [ALTER TABLE](alter-table.md) , [DROP TABLE](drop-table.md) , [SHOW TABLES](show-tables.md) , [DESCRIBE TABLE](desc-table.md)

## Syntax

```sqlsyntax
UNDROP TABLE <name>
```

## Parameters

`name`
:   Specifies the identifier for the table to restore. If the identifier contains spaces or special characters, the entire string must
    be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* Tables can only be restored to the database and schema that contained the table at the time of deletion. For example, if you
  create and drop table `t1` in schema `s1`, then change the current schema to `s2` and attempt to restore table `t1`
  by ID (or qualified name, `s1.t1`), table `t1` is restored in schema `s1` rather than in the current schema, `s2`.
* If a table with the same name already exists, an error is returned.
* If you have multiple dropped tables with the same name, you can use the [IDENTIFIER keyword](../identifier-literal.md)
  with the system-generated identifier (from the [TABLES view](../account-usage/tables.md)) to specify which table to restore.
  The name of the restored table remains the same. See Examples.

  > **Note:**
  >
  > You can only use the system-generated identifier with the IDENTIFIER() keyword when executing the UNDROP command for notebooks, tables, block storage snapshots, schemas, and databases.

* UNDROP relies on the Snowflake [Time Travel](../../user-guide/data-time-travel.md) feature. An object can be restored only if
  the object was deleted within the [Data retention period](../../user-guide/data-time-travel.md). The default value is 24 hours.

* You cannot undrop a hybrid table.

## Examples

### Basic example

Restore the most recent version of a dropped table (this example builds on the examples provided for [DROP TABLE](drop-table.md)):

```sqlexample
UNDROP TABLE t2;
```

```output
+---------------------------------+
| status                          |
|---------------------------------|
| Table T2 successfully restored. |
+---------------------------------+
```

### UNDROP table using the table ID

Restore a dropped table by ID using IDENTIFIER(). You can find the table ID of the specific table to undrop using the `table_id`
column in the [TABLES view](../account-usage/tables.md). For example, if you have multiple dropped tables named `my_table`, and
you want to restore the second-to-last dropped table `my_table`, follow these steps:

1. Find the table ID of the dropped table in the Account Usage TABLES view:

   ```sqlexample
   SELECT table_id,
     table_name,
     table_schema,
     table_catalog,
     created,
     deleted,
     comment
   FROM SNOWFLAKE.ACCOUNT_USAGE.TABLES
   WHERE table_catalog = 'DB1'
   AND table_schema = 'S1'
   AND table_name = 'MY_TABLE'
   AND deleted IS NOT NULL
   ORDER BY deleted;
   ```

   ```output
   +----------+------------+--------------+---------------+-------------------------------+-------------------------------+---------+
   | TABLE_ID | TABLE_NAME | TABLE_SCHEMA | TABLE_CATALOG | CREATED                       | DELETED                       | COMMENT |
   |----------+------------+--------------+---------------+-------------------------------+-------------------------------+---------|
   |   408578 | MY_TABLE   | S1           | DB1           | 2024-07-01 15:39:07.565 -0700 | 2024-07-01 15:40:28.161 -0700 | NULL    |
   +----------+------------+--------------+---------------+-------------------------------+-------------------------------+---------+
   |   408607 | MY_TABLE   | S1           | DB1           | 2024-07-01 17:43:07.565 -0700 | 2024-07-01 17:44:28.161 -0700 | NULL    |
   +----------+------------+--------------+---------------+-------------------------------+-------------------------------+---------+
   ```

2. Undrop `my_table` by table ID. To restore the second-to-last deleted table, use table ID `408578` from the output of the previous
   statement. After you execute the following statement, the table is restored with its original name, `my_table`:

   ```sqlexample
   UNDROP TABLE IDENTIFIER(408578);
   ```
