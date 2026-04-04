# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_default_columns_override_for_system_object.md

Categories:
:   [System functions](../functions-system.md) (Information)

# SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT

Returns the list of columns that were set by a previous call to
[SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_set_default_columns_override_for_system_object.md) for the specified Snowflake view (for
example, for a specific [ACCOUNT_USAGE view](../account-usage.md) or
[INFORMATION_SCHEMA view](../info-schema.md)).

For more information, see [Handling new columns in SHOW command output and Snowflake views](../../release-notes/behavior-changes-new-columns.md).

See also:
:   [SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_set_default_columns_override_for_system_object.md) ,
    [SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_unset_default_columns_override_for_system_object.md) ,
    [SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES](system_get_all_default_columns_overrides.md)

## Syntax

```sqlsyntax
SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  '<object_type>',
  '<database_name>',
  '<schema_name>',
  '<object_name>'
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

## Returns

Returns a VARCHAR value containing a comma-separated list of the columns specified by the previous call to
SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT. The column names are in uppercase.

If SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT was not called or if
[SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](system_unset_default_columns_override_for_system_object.md) was called to clear the list of columns, the function returns an
empty string.

## Access control requirements

Only account administrators (users who have been granted the ACCOUNTADMIN role) can call this function.

## Usage notes

* You must have a database in use (for example, by running [USE DATABASE](../sql/use-database.md)) in order to call this function.
  If no database is in use, the function call fails.

## Examples

The following example returns the list of columns specified by a previous call to
SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT for the
[TABLES view in the ACCOUNT_USAGE schema](../account-usage/tables.md):

```sqlexample
SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'TABLES'
);
```

```output
+--------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT( |
|   'VIEW',                                              |
|   'SNOWFLAKE',                                         |
|   'ACCOUNT_USAGE',                                     |
|   'TABLES'                                             |
| )                                                      |
|--------------------------------------------------------|
| TABLE_NAME,TABLE_SCHEMA,TABLE_TYPE                     |
+--------------------------------------------------------+
```

The following example returns the list of columns specified by a previous call to
SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT for the
[TABLES view in the INFORMATION_SCHEMA schema](../info-schema/tables.md):

```sqlexample
SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  '',
  'ACCOUNT_USAGE',
  'TABLES'
);
```

```output
+--------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT( |
|   'VIEW',                                              |
|   '',                                                  |
|   'INFORMATION_SCHEMA',                                |
|   'TABLES'                                             |
| )                                                      |
|--------------------------------------------------------|
| TABLE_NAME,TABLE_SCHEMA,TABLE_TYPE                     |
+--------------------------------------------------------+
```

If SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT was not called or if
SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT was called to clear the list, the function returns an empty string:

```sqlexample
SELECT SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'TABLES'
);

SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'TABLES'
);
```

```output
+--------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT( |
|   'VIEW',                                              |
|   'SNOWFLAKE',                                         |
|   'ACCOUNT_USAGE',                                     |
|   'TABLES'                                             |
| )                                                      |
|--------------------------------------------------------|
```
