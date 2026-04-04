# Source: https://docs.snowflake.com/en/sql-reference/functions/system_set_default_columns_override_for_show_command.md

Categories:
:   [System functions](../functions-system.md) (Control)

# SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND

Controls the columns that should be returned when the specified [SHOW <objects>](../sql/show.md) command is executed.

You can call this function if the introduction of new columns in a SHOW COMMAND introduces a problem with a script or code that
depends on a fixed number or order of columns in the results. See [Handling new columns in SHOW command output and Snowflake views](../../release-notes/behavior-changes-new-columns.md).

See also:
:   [SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_get_default_columns_override_for_show_command.md) ,
    [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_unset_default_columns_override_for_show_command.md) ,
    [SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES](system_get_all_default_columns_overrides.md)

## Syntax

```sqlsyntax
SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  '<object_type>',
  '<list_of_columns>'
)
```

## Arguments

`'object_type'`
:   Type of object for the SHOW command. For example, for the SHOW TABLES command, specify `'TABLES'`. For the SHOW NOTIFICATION
    INTEGRATIONS command, specify `'NOTIFICATION INTEGRATIONS'`.

`list_of_columns`
:   Comma-separated or space-separated list of columns that should be returned in the output of the SHOW command.

    You can specify the column names in uppercase, lowercase, or mixed case.

    To return all columns, specify an empty string or call
    [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_unset_default_columns_override_for_show_command.md).

## Returns

Returns TRUE if the operation was successful.

## Access control requirements

Only account administrators (users who have been granted the ACCOUNTADMIN role) can call this function.

## Examples

The following example configures the [SHOW TABLES](../sql/show-tables.md) command to return only the `name`, `database_name`,
`kind`, and `comment` columns:

```sqlexample
SELECT SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'TABLES',
  'name, database_name, kind, comment'
);
```

Executing the SHOW TABLES command returns only the specified columns:

```sqlexample
SHOW TABLES;
```

```output
+------------------+---------------+-------+---------+
| name             | database_name | kind  | comment |
|------------------+---------------+-------+---------|
| DEPARTMENT_TABLE | MY_DB         | TABLE |         |
| EMPLOYEE_TABLE   | MY_DB         | TABLE |         |
+------------------+---------------+-------+---------+
```

Executing the SHOW TERSE TABLES command returns only the specified columns except for `comment`, which isn’t normally returned
when you specify TERSE:

```sqlexample
SHOW TERSE TABLES;
```

```output
+------------------+-------+---------------+
| name             | kind  | database_name |
|------------------+-------+---------------|
| DEPARTMENT_TABLE | TABLE | MY_DB         |
| EMPLOYEE_TABLE   | TABLE | MY_DB         |
+------------------+-------+---------------+
```
