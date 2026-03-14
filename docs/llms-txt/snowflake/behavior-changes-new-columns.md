# Source: https://docs.snowflake.com/en/release-notes/behavior-changes-new-columns.md

# Handling new columns in SHOW command output and Snowflake views

Periodically, new columns will be introduced in the output of [SHOW <objects>](../sql-reference/sql/show.md) commands and in Snowflake views
(such as the views in the [ACCOUNT_USAGE schema](../sql-reference/account-usage.md) in the
[SNOWFLAKE database](../sql-reference/snowflake-db.md) and the views in the
[INFORMATION_SCHEMA schema](../sql-reference/info-schema.md)).

If you have a script or code that depends on the result set including a specific number of columns or that depend on the order
of the columns, the introduction of a new column might affect that script or code.

## Temporarily working around a problem introduced by a new column

If your script or code encounters problems due to the introduction of new columns, your Snowflake administrator (a user who has
been granted the ACCOUNTADMIN role) can change the columns that are returned for executions of a specific SHOW command or SELECT \*
queries of a Snowflake view. These columns are referred to as the *default columns*.

### Overriding the default columns for a SHOW command

To exclude newly introduced columns from the output of a SHOW command, call the
[SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](../sql-reference/functions/system_set_default_columns_override_for_show_command.md) function, specifying the type of object and
the list of columns that should be returned.

Suppose that a new `direction` column has been introduced in the output of the
[SHOW NOTIFICATION INTEGRATIONS](../sql-reference/sql/show-notification-integrations.md) command. To prevent the new `direction` column from being included in
the output of the command, call SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND, specifying `'NOTIFICATION INTEGRATIONS'`
as the type of object. Pass in a comma-separated list of the columns that should be returned in the output (a list that excludes
`direction`):

```sqlexample
SELECT SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'NOTIFICATION INTEGRATIONS',
  'name, type, category, enabled, comment, created_on'
);
```

When anyone in your account runs the SHOW NOTIFICATION INTEGRATIONS command, the new `direction` column will not be returned in
the output.

```sqlexample
SHOW NOTIFICATION INTEGRATIONS;
```

```output
+--------------------------------+---------+--------------+---------+---------+-------------------------------+
| name                           | type    | category     | enabled | comment | created_on                    |
|--------------------------------+---------+--------------+---------+---------+-------------------------------|
| SLACK_NOTIFICATION_INTEGRATION | WEBHOOK | NOTIFICATION | true    | NULL    | 2025-07-02 06:14:53.859 -0700 |
+--------------------------------+---------+--------------+---------+---------+-------------------------------+
```

### Resetting the default columns for a SHOW command

If you need to undo a previous SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND call and return all columns in the SHOW
command for a specific object type, call the
[SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](../sql-reference/functions/system_unset_default_columns_override_for_show_command.md) function, specifying the type of object.
For example:

```sqlexample
SELECT SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'NOTIFICATION INTEGRATIONS'
);
```

### Getting the list of default columns for a SHOW command

If you need to determine if SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND was called for a specific object type and you
want the list of columns that will be returned in the output of the command, call the
[SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND](../sql-reference/functions/system_get_default_columns_override_for_show_command.md) function, specifying the type of object. For
example:

```sqlexample
SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'NOTIFICATION INTEGRATIONS'
);
```

```output
+-------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND( |
|   'NOTIFICATION INTEGRATIONS'                         |
| )                                                     |
|-------------------------------------------------------|
| name,type,category,enabled,comment,created_on         |
+-------------------------------------------------------+
```

If SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND was not previously called or if
SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND was called, the function returns an empty string.

```sqlexample
SELECT SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'NOTIFICATION INTEGRATIONS'
);

SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND(
  'NOTIFICATION INTEGRATIONS'
);
```

```output
+-------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SHOW_COMMAND( |
|   'NOTIFICATION INTEGRATIONS'                         |
| )                                                     |
|-------------------------------------------------------|
|                                                       |
+-------------------------------------------------------+
```

### Overriding the default columns for a Snowflake view

To exclude newly introduced columns from the results of a `SELECT *` query of a Snowflake view, call the
[SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](../sql-reference/functions/system_set_default_columns_override_for_system_object.md) function, specifying the type of object, the
database and schema containing the view, the name of the view, and the list of columns that should be returned.

Suppose that a new `replicable_with_failover_groups` column has been introduced in the
[DATABASES view in the ACCOUNT_USAGE schema](../sql-reference/account-usage/databases.md). To prevent the new
`replicable_with_failover_groups` column from being returned in the results of a `SELECT *` query of the view,
call SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT, specifying `'VIEW'` as the type of object, `'SNOWFLAKE'` as the
database, `'ACCOUNT_USAGE'` as the schema, and `'TABLES'` as the view. Pass in a comma-separated list of the columns that
should be returned in the output (a list that excludes `replicable_with_failover_groups`):

```sqlexample
SELECT SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'DATABASES',
  'database_id, database_name, database_owner, is_transient, ' ||
  'comment, created, last_altered, deleted, retention_time, '  ||
  'resource_group, type, owner_role_type, object_visibility'
);
```

The example uses the [||](../sql-reference/functions/concat.md) operator to construct a string that contains the comma-separated
list of columns.

When anyone in your account performs a `SELECT *` query of the DATABASES view, the new `replicable_with_failover_groups`
column will not be returned in the output.

```sqlexample
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES;
```

```output
+-------------+---------------+----------------+--------------+---------+-------------------------------+-------------------------------+-------------------------------+----------------+----------------+----------+-----------------+-------------------+
| DATABASE_ID | DATABASE_NAME | DATABASE_OWNER | IS_TRANSIENT | COMMENT | CREATED                       | LAST_ALTERED                  | DELETED                       | RETENTION_TIME | RESOURCE_GROUP | TYPE     | OWNER_ROLE_TYPE | OBJECT_VISIBILITY |
|-------------+---------------+----------------+--------------+---------+-------------------------------+-------------------------------+-------------------------------+----------------+----------------+----------+-----------------+-------------------|
|          55 | MY_DATABASE   | NULL           | NO           | NULL    | 2025-07-16 15:17:55.990 -0700 | 2025-07-17 15:19:52.305 -0700 | 2025-07-16 15:18:32.973 -0700 |              1 | NULL           | STANDARD | NULL            | NULL              |
+-------------+---------------+----------------+--------------+---------+-------------------------------+-------------------------------+-------------------------------+----------------+----------------+----------+-----------------+-------------------+
```

If you need to call this function for an INFORMATION_SCHEMA view, pass in an empty string for the database name. For example, to
exclude the `replicable_with_failover_groups` column from the results of `SELECT *` queries of the
[DATABASES view in the INFORMATION_SCHEMA schema](../sql-reference/info-schema/databases.md):

```sqlexample
SELECT SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  '',
  'INFORMATION_SCHEMA',
  'DATABASES',
  'database_name, database_owner, is_transient, comment, ' ||
  'created, last_altered, retention_time, type, '          ||
  'owner_role_type'
);
```

### Resetting the default columns for a Snowflake view

If you need to undo a previous SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT call and return all columns in a
`SELECT *` query of a Snowflake view, call the
[SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](../sql-reference/functions/system_unset_default_columns_override_for_system_object.md) function, specifying the type of object,
the database and schema that contain the view, and the name of the view. For example:

```sqlexample
SELECT SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'DATABASES'
);
```

If you need to call this function for an INFORMATION_SCHEMA view, pass in an empty string for the database name. For example:

```sqlexample
SELECT SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  '',
  'INFORMATION_SCHEMA',
  'DATABASES'
);
```

### Getting the list of default columns for a Snowflake view

If you need to determine if SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT was called for a specific view and you
want the list of columns that will be returned in a `SELECT *` query of that view, call the
[SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT](../sql-reference/functions/system_get_default_columns_override_for_system_object.md) function, specifying the type of object, the
database and schema containing the view, and the name of the view. For example:

```sqlexample
SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'DATABASES'
);
```

```output
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(                                                                                                          |
|   'VIEW',                                                                                                                                                       |
|   'SNOWFLAKE',                                                                                                                                                  |
|   'ACCOUNT_USAGE',                                                                                                                                              |
|   'DATABASES'                                                                                                                                                   |
| )                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DATABASE_ID,DATABASE_NAME,DATABASE_OWNER,IS_TRANSIENT,COMMENT,CREATED,LAST_ALTERED,DELETED,RETENTION_TIME,RESOURCE_GROUP,TYPE,OWNER_ROLE_TYPE,OBJECT_VISIBILITY |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

If you need to call this function for an INFORMATION_SCHEMA view, pass in an empty string for the database name. For example:

```sqlexample
SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  '',
  'INFORMATION_SCHEMA',
  'DATABASES'
);
```

```output
+------------------------------------------------------------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(                                                     |
|   'VIEW',                                                                                                  |
|   '',                                                                                                      |
|   'INFORMATION_SCHEMA',                                                                                    |
|   'DATABASES'                                                                                              |
| )                                                                                                          |
|------------------------------------------------------------------------------------------------------------|
| DATABASE_NAME,DATABASE_OWNER,IS_TRANSIENT,COMMENT,CREATED,LAST_ALTERED,RETENTION_TIME,TYPE,OWNER_ROLE_TYPE |
+------------------------------------------------------------------------------------------------------------+
```

If SYSTEM$SET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT was not previously called or if
SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT was called, the function returns an empty string.

```sqlexample
SELECT SYSTEM$UNSET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'DATABASES'
);

SELECT SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT(
  'VIEW',
  'SNOWFLAKE',
  'ACCOUNT_USAGE',
  'DATABASES'
);
```

```output
+--------------------------------------------------------+
| SYSTEM$GET_DEFAULT_COLUMNS_OVERRIDE_FOR_SYSTEM_OBJECT( |
|   'VIEW',                                              |
|   'SNOWFLAKE',                                         |
|   'ACCOUNT_USAGE',                                     |
|   'DATABASES'                                          |
| )                                                      |
|--------------------------------------------------------|
|                                                        |
+--------------------------------------------------------+
```

### Getting the list of columns from all previous calls for SHOW commands and Snowflake views

To get the list of columns that are overridden for all SHOW commands and Snowflake views, call the
[SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES](../sql-reference/functions/system_get_all_default_columns_overrides.md) function. For example:

```sqlexample
SELECT SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES();
```

The function returns a string containing a JSON array of objects. Each object represents the list of columns for a specific SHOW
command or Snowflake view. For example:

```output
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [{"domain":"VIEW","isShowCommand":false,"dbName":"","schemaName":"INFORMATION_SCHEMA","objectName":"DATABASES","serializedDefaultColumns":"DATABASE_NAME,DATABASE_OWNER,IS_TRANSIENT,COMMENT,CREATED,LAST_ALTERED,RETENTION_TIME,TYPE,OWNER_ROLE_TYPE"},{"domain":"VIEW","isShowCommand":false,"dbName":"SNOWFLAKE","schemaName":"ACCOUNT_USAGE","objectName":"DATABASES","serializedDefaultColumns":"DATABASE_ID,DATABASE_NAME,DATABASE_OWNER,IS_TRANSIENT,COMMENT,CREATED,LAST_ALTERED,DELETED,RETENTION_TIME,RESOURCE_GROUP,TYPE,OWNER_ROLE_TYPE,OBJECT_VISIBILITY"},{"isShowCommand":true,"showCommandType":"NOTIFICATION INTEGRATIONS","serializedDefaultColumns":"name,type,category,enabled,comment,created_on"}] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

For an explanation of the name/value pairs in each object, see
[SYSTEM$GET_ALL_DEFAULT_COLUMNS_OVERRIDES](../sql-reference/functions/system_get_all_default_columns_overrides.md).

## Updating scripts and code to prevent problems when new columns are introduced

To prevent problems from occurring due to the introduction of new columns, your scripts and code should select specific columns
from the output of SHOW commands and when querying Snowflake views.

To select specific columns from the output of SHOW commands, you can use the
[pipe operator](../sql-reference/operators-flow.md). See the example in [Select a list of columns for the output of a SHOW command](../sql-reference/operators-flow.md).
