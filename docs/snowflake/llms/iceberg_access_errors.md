# Source: https://docs.snowflake.com/en/sql-reference/monitoring/iceberg_access_errors.md

Schema:
:   [MONITORING](../monitoring.md)

# ICEBERG_ACCESS_ERRORS view

This MONITORING schema view displays [external volume](../../user-guide/tables-iceberg.md)
access errors for the account.

Use the information in this view to search for and troubleshoot access errors, which can result from situations like the following:

* Snowflake loses privileges to access the external volume storage location.
* Snowflake tries to access files that have been deleted or overwritten.
* Snowflake encounters other storage access issues.

See also:
:   [Apache Iceberg™ tables](../../user-guide/tables-iceberg.md)

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| EXTERNAL_VOLUME_ID | NUMBER | The unique ID of the external volume associated with the error. |
| EXTERNAL_VOLUME_NAME | VARCHAR | The name of the external volume associated with the error. |
| CREATED_ON | TIMESTAMP_LTZ | Date and time when the error was raised. |
| EXTERNAL_VOLUME_PATH | VARCHAR | Full path to the file on the external volume associated with the error. |
| MESSAGE | VARCHAR | The Snowflake error message. |
| STORAGE_METHOD_NAME | VARCHAR | The method (action) tried against the storage location; for example, `findRegionForLocation` or `deleteCurrentFiles`. |
| STORAGE_PROVIDER_ERROR_MESSAGE | VARCHAR | The error message received from your cloud service provider. |

## Examples

Retrieve all storage access errors for the external volume named `my_s3_external_volume`:

```sqlexample
SELECT * FROM snowflake.monitoring.iceberg_access_errors
  WHERE EXTERNAL_VOLUME_NAME ILIKE 'my_s3_external_volume';
```

Retrieve storage access errors that started within the last hour for the external volume named `my_external_volume`:

```sqlexample
SELECT * FROM snowflake.monitoring.iceberg_access_errors
  WHERE EXTERNAL_VOLUME_NAME ILIKE 'my_external_volume'
  AND CREATED_ON > DATEADD(HOUR, -1, CURRENT_TIMESTAMP());
```
