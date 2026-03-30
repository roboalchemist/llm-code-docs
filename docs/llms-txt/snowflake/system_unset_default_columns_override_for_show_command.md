# Source: https://docs.snowflake.com/en/sql-reference/functions/system_unset_default_columns_override_for_show_command.md

Categories:
:   [System functions](../functions-system.md) (Control)

# SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND

Clears the list of columns specified by a previous call to
[SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_set_default_columns_override_for_show_command.md) for a type of object.

For more information, see [Handling new columns in SHOW command output and Snowflake views](../../release-notes/behavior-changes-new-columns.md).

See also:
:   [SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_set_default_columns_override_for_show_command.md) ,
    [SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_get_default_columns_override_for_show_command.md) ,
    [SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES](system_get_all_default_columns_overrides.md)

## Syntax

```sqlsyntax
SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  '<object_type>'
)
```

## Arguments

`'object_type'`
:   Type of object for the SHOW command. For example, for the SHOW TABLES command, specify `'TABLES'`. For the SHOW NOTIFICATION
    INTEGRATIONS command, specify `'NOTIFICATION INTEGRATIONS'`.

## Returns

Returns TRUE if the operation was successful.

## Access control requirements

Only account administrators (users who have been granted the ACCOUNTADMIN role) can call this function.

## Examples

The following example clears the list of columns set by a previous SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND call for
the [SHOW TABLES](../sql/show-tables.md) command:

```sqlexample
SELECT SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'TABLES'
);
```
