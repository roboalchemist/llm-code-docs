# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_all_default_columns_overrides.md

Categories:
:   [System functions](../functions-system.md) (Information)

# SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES

Returns the list of columns that were set by previous calls to
[SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_set_default_columns_override_for_show_command.md) and
[SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_set_default_columns_override_for_system_object.md).

For more information, see [Handling new columns in SHOW command output and Snowflake views](../../release-notes/behavior-changes-new-columns.md).

See also:
:   [SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_set_default_columns_override_for_show_command.md) ,
    [SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_get_default_columns_override_for_show_command.md) ,
    [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](system_unset_default_columns_override_for_show_command.md) ,
    [SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_set_default_columns_override_for_system_object.md) ,
    [SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_get_default_columns_override_for_system_object.md) ,
    [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_unset_default_columns_override_for_system_object.md)

## Syntax

```sqlsyntax
SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES()
```

## Arguments

None.

## Returns

Returns a VARCHAR value (a string) in JSON format. The string is a JSON array that contains an object for each SHOW command and
Snowflake view that has an overridden list of columns.

If the object represents the overridden list of default columns for a SHOW command, the object contains the following name/value
pairs:

| Name | Description |
| --- | --- |
| `isShowCommand` | Indicates if the object represents the list of columns for a SHOW command. In this case, the value is `true`. |
| `showCommandType` | Type of the object for the SHOW command. For example, for SHOW NOTIFICATION INTEGRATIONS, the value is `"NOTIFICATION INTEGRATIONS"`. |
| `serializedDefaultColumns` | Comma-separated list of columns specified in a previous SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND call. The column names are in uppercase. |

If the object represents the overridden list of default columns for a Snowflake view, the object contains the following
name/value pairs:

| Name | Description |
| --- | --- |
| `domain` | Type of the object. In this case, the value is `"VIEW"`. |
| `isShowCommand` | Indicates if the object represents the list of columns for a SHOW command. In this case, the value is `false`. |
| `dbName` | Name of the database containing the view. For INFORMATION_SCHEMA views, the value is an empty string (`""`). |
| `schemaName` | Name of the schema containing the view. |
| `objectName` | Name of the view. |
| `serializedDefaultColumns` | Comma-separated list of columns specified in a previous SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT call. The column names are in uppercase. |

## Access control requirements

Only account administrators (users who have been granted the ACCOUNTADMIN role) can call this function.

## Examples

The following example returns the list of columns specified by previous calls to
SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND and SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT:

```sqlexample
SELECT SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES();
```

```output
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [{"domain":"VIEW","isShowCommand":false,"dbName":"","schemaName":"INFORMATION_SCHEMA","objectName":"DATABASES","serializedDefaultColumns":"DATABASE_NAME,DATABASE_OWNER,IS_TRANSIENT,COMMENT,CREATED,LAST_ALTERED,RETENTION_TIME,TYPE,OWNER_ROLE_TYPE"},{"domain":"VIEW","isShowCommand":false,"dbName":"SNOWFLAKE","schemaName":"ACCOUNT_USAGE","objectName":"DATABASES","serializedDefaultColumns":"DATABASE_ID,DATABASE_NAME,DATABASE_OWNER,IS_TRANSIENT,COMMENT,CREATED,LAST_ALTERED,DELETED,RETENTION_TIME,RESOURCE_GROUP,TYPE,OWNER_ROLE_TYPE,OBJECT_VISIBILITY"},{"isShowCommand":true,"showCommandType":"NOTIFICATION INTEGRATIONS","serializedDefaultColumns":"name,type,category,enabled,comment,created_on"}] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
