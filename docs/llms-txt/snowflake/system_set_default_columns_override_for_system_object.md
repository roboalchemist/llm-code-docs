# Source: https://docs.snowflake.com/en/sql-reference/functions/system_set_default_columns_override_for_system_object.md

Categories:
:   [System functions](../functions-system.md) (Control)

# SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT

Controls the columns that should be returned when you select all columns (`SELECT *`) from the specified Snowflake view (for
example, from a specific [ACCOUNT_USAGE view](../account-usage.md) or
[INFORMATION_SCHEMA view](../info-schema.md)).

> **Note:**
>
> This function does not affect queries that select specific columns from the view.

You can call this function if the introduction of new columns in a Snowflake view introduces a problem with a script or code that
selects all columns and depends on a fixed number or order of columns in the results. See
[Handling new columns in SHOW command output and Snowflake views](../../release-notes/behavior-changes-new-columns.md).

See also:
:   [SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_get_default_columns_override_for_system_object.md) ,
    [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_unset_default_columns_override_for_system_object.md) ,
    [SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES](system_get_all_default_columns_overrides.md)

## Syntax

```sqlsyntax
SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  '<object_type>',
  '<database_name>',
  '<schema_name>',
  '<object_name>',
  '<list_of_columns>'
)
```

## Arguments

`'object_type'`
:   Type of the object. You must specify `'VIEW'` for this argument.

`'database_name'`
:   Name of the database that contains the object. You must specify `'SNOWFLAKE'` or, for INFORMATION_SCHEMA views, an empty
    string.

`'schema_name'`
:   Name of the schema that contains the object. You must specify the name of a schema in the
    [SNOWFLAKE database](../snowflake-db.md) or `'INFORMATION_SCHEMA'`.

`'object_name'`
:   Name of the object.

`list_of_columns`
:   Comma-separated or space-separated list of columns that should be returned when you select all columns from this view.

    You can specify the column names in uppercase, lowercase, or mixed case.

    To return all columns, specify an empty string or call SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT.

## Returns

Returns TRUE if the operation was successful.

## Access control requirements

Only account administrators (users who have been granted the ACCOUNTADMIN role) can call this function.

## Usage notes

* You must have a database in use (for example, by running [USE DATABASE](../sql/use-database.md)) in order to call this function.
  If no database is in use, the function call fails.

## Examples

The following example configures queries that select all columns from the [TABLES view](../account-usage/tables.md) view in the
ACCOUNT_USAGE schema to return only the `table_name`, `table_schema`, and `table_type` columns:

```sqlexample
SELECT SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'TABLES',
  'table_name, table_schema, table_type'
);
```

Selecting all columns from that view returns only the specified columns:

```sqlexample
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.TABLES;
```

```output
+------------+---------------------+------------+
| TABLE_NAME | TABLE_SCHEMA        | TABLE_TYPE |
|------------+---------------------+------------|
| MY_TABLE   | MY_SCHEMA           | BASE TABLE |
+------------+---------------------+------------+
```

The following example configures queries that select all columns from the [TABLES view](../info-schema/tables.md) view in the
INFORMATION_SCHEMA schema to return only the `table_name`, `table_schema`, and `table_type` columns:

```sqlexample
SELECT SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  '',
  'INFORMATION_SCHEMA',
  'TABLES',
  'table_name, table_schema, table_type'
);
```

Selecting all columns from that view returns only the specified columns:

```sqlexample
SELECT * FROM INFORMATION_SCHEMA.TABLES;
```

```output
+--------------+------------+------------+
| TABLE_SCHEMA | TABLE_NAME | TABLE_TYPE |
|--------------+------------+------------|
| MY_SCHEMA    | MY_TABLE   | BASE TABLE |
+--------------+------------+------------+
```
