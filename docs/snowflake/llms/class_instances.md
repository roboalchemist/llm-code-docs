# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/class_instances.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/class_instances.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/class_instances.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CLASS_INSTANCES view

This Account Usage view displays a row for each instance of a class defined in the account.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | NUMBER | Internal/system-generated identifier for the instance. |
| NAME | VARCHAR | Name of the instance. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the instance. |
| SCHEMA_NAME | VARCHAR | Name of the schema the instance belongs to. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database of the instance. |
| DATABASE_NAME | VARCHAR | Name of the database the instance belongs to. |
| CLASS_ID | NUMBER | Internal/system-generated identifier for the class the instance is instantiated from. |
| CLASS_NAME | VARCHAR | Name of the class the instance is instantiated from. |
| CLASS_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the class the instance is instantiated from. |
| CLASS_SCHEMA_NAME | VARCHAR | Name of the schema of the class the instance is instantiated from. |
| CLASS_DATABASE_ID | NUMBER | Internal/system-generated identifier for the database of the class the instance is instantiated from. |
| CLASS_DATABASE_NAME | VARCHAR | Name of the database of the class the instance is instantiated from. |
| OWNER_NAME | VARCHAR | Name of the role that owns the instance. |
| OWNER_ROLE_TYPE | VARCHAR | The internal/system-generated identifier of the role that owns the instance of the class. |
| CREATED | TIMESTAMP_LTZ | Date and time when the instance was created. |
| DELETED | TIMESTAMP_LTZ | Date and time when the instance was deleted. |
| COMMENT | VARCHAR | Comment for the instance. |

## Usage notes

* Latency for the view may be up to 180 minutes (3 hours).

* The view only displays the instances for which the current role for the session has been granted access privileges.

## Examples

The following example finds all instances of the [ANOMALY_DETECTION](../classes/anomaly_detection.md) class:

```sqlexample
SELECT NAME, DATABASE_NAME, SCHEMA_NAME, CLASS_NAME
  FROM SNOWFLAKE.ACCOUNT_USAGE.CLASS_INSTANCES
  WHERE CLASS_NAME = 'ANOMALY_DETECTION';
```

The following example joins this view with [TABLES view](tables.md) on the INSTANCE_ID column to find the tables
that belong to each instance:

```sqlexample
SELECT a.TABLE_NAME,
       b.NAME AS instance_name,
       b.CLASS_NAME
  FROM SNOWFLAKE.ACCOUNT_USAGE.TABLES a
  JOIN SNOWFLAKE.ACCOUNT_USAGE.CLASS_INSTANCES b
  ON a.INSTANCE_ID = b.ID
  WHERE b.DELETED IS NULL;
```
