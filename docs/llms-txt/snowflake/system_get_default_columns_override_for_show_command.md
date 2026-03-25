# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_default_columns_override_for_show_command.md

Categories:
:   [System functions](../functions-system.md) (Information)

# SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND

Returns the list of columns that were set by a previous call to
[SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_set_default_columns_override_for_show_command.md).

For more information, see [Handling new columns in SHOW command output and Snowflake views](../../release-notes/behavior-changes-new-columns.md).

See also:
:   [SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_set_default_columns_override_for_show_command.md) ,
    [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_unset_default_columns_override_for_show_command.md) ,
    [SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES](system_get_all_default_columns_overrides.md)

## Syntax

```sqlsyntax
SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  '<object_type>'
)
```

## Arguments

`'object_type'`
:   Type of object for the SHOW command. For example, for the SHOW TABLES command, specify `'TABLES'`. For the SHOW NOTIFICATION
    INTEGRATIONS command, specify `'NOTIFICATION INTEGRATIONS'`.

## Returns

Returns a VARCHAR value containing a comma-separated list of the columns specified by the previous call to
SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND. The column names are in lowercase.

If SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND was not called or if
[SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_unset_default_columns_override_for_show_command.md) was called to clear the list of columns, the function returns an
empty string.

## Access control requirements

Only account administrators (users who have been granted the ACCOUNTADMIN role) can call this function.

## Examples

The following example returns the list of columns specified by a previous call to
SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND for the SHOW TABLES command:

```sqlexample
SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'TABLES'
);
```

```output
+-------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND( |
|   'TABLES'                                            |
| )                                                     |
|-------------------------------------------------------|
| name,database_name,kind,comment                       |
+-------------------------------------------------------+
```

If SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND was not called or if
SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND was called to clear the list, the function returns an empty string:

```sqlexample
SELECT SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'TABLES'
);

SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'TABLES'
);
```

```output
+-------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND( |
|   'TABLES'                                            |
| )                                                     |
|-------------------------------------------------------|
|                                                       |
+-------------------------------------------------------+
```
