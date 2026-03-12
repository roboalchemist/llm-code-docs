# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-database.md

# DESCRIBE DATABASE

Describes the database. For example, shows the schemas in the database.

DESCRIBE can be abbreviated to DESC.

See also:
:   [ALTER DATABASE](alter-database.md) , [CREATE DATABASE](create-database.md) , [DROP DATABASE](drop-database.md) , [SHOW DATABASES](show-databases.md) , [UNDROP DATABASE](undrop-database.md)

    [DATABASES view](../info-schema/databases.md) (Information Schema)

## Syntax

```sqlsyntax
DESC[RIBE] DATABASE <database_name>
```

## Parameters

`database_name`
:   Specifies the [identifier](../identifiers.md) of the database to describe.

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

This demonstrates the DESCRIBE DATABASE command:

```sqlexample
CREATE DATABASE desc_demo;

CREATE SCHEMA sample_schema_1;

CREATE SCHEMA sample_schema_2;

DESCRIBE DATABASE desc_demo;
```

```output
+-------------------------------+--------------------+--------+
| created_on                    | name               | kind   |
|-------------------------------+--------------------+--------|
| 2022-06-23 00:00:00.000 -0700 | INFORMATION_SCHEMA | SCHEMA |
| 2022-06-23 00:00:00.000 -0700 | PUBLIC             | SCHEMA |
| 2022-06-23 01:00:00.000 -0700 | SAMPLE_SCHEMA_1    | SCHEMA |
| 2022-06-23 02:00:00.000 -0700 | SAMPLE_SCHEMA_2    | SCHEMA |
+-------------------------------+--------------------+--------+
```
