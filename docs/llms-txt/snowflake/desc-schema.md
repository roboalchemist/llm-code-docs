# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-schema.md

# DESCRIBE SCHEMA

Describes the schema. For example, lists the tables and views in the schema.

DESCRIBE can be abbreviated to DESC.

See also:
:   [ALTER SCHEMA](alter-schema.md) , [CREATE SCHEMA](create-schema.md) , [DROP SCHEMA](drop-schema.md) , [SHOW SCHEMAS](show-schemas.md) , [UNDROP SCHEMA](undrop-schema.md)

    [SCHEMATA view](../info-schema/schemata.md) (Information Schema)

## Syntax

```sqlsyntax
DESC[RIBE] SCHEMA <schema_name>
```

## Parameters

`schema_name`
:   Specifies the [identifier](../identifiers.md) of the schema to describe.

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

This demonstrates the DESCRIBE SCHEMA command:

```sqlexample
CREATE SCHEMA sample_schema_2;
USE SCHEMA sample_schema_2;

CREATE TABLE sample_table_1 (i INTEGER);

CREATE VIEW sample_view_1 AS
    SELECT i FROM sample_table_1;

CREATE MATERIALIZED VIEW sample_mview_1 AS
    SELECT i FROM sample_table_1 WHERE i < 100;

DESCRIBE SCHEMA sample_schema_2;

+-------------------------------+----------------+-------------------+
| created_on                    | name           | kind              |
|-------------------------------+----------------+-------------------|
| 2022-06-23 01:00:00.000 -0700 | SAMPLE_TABLE_1 | TABLE             |
| 2022-06-23 02:00:00.000 -0700 | SAMPLE_VIEW_1  | VIEW              |
| 2022-06-23 03:00:00.000 -0700 | SAMPLE_MVIEW_1 | MATERIALIZED_VIEW |
+-------------------------------+----------------+-------------------+
```
