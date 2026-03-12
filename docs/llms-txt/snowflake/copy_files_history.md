# Source: https://docs.snowflake.com/en/sql-reference/account-usage/copy_files_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# COPY_FILES_HISTORY view

This Account Usage view includes information about compute credit usage, number of bytes copied, and number of files copied for the
following operations:

* Using [COPY FILES](../sql/copy-files.md) to copy files from a source stage to an output stage.
* Cloning named internal stages.

See also:
:   [COPY FILES](../sql/copy-files.md) , [CREATE <object> … CLONE](../sql/create-clone.md)

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| DATABASE_ID | NUMBER | ID of the database from which the files are copied. You can map this to the ENTITY_ID in the [METERING_HISTORY view](metering_history.md) view. |
| DATABASE_NAME | VARCHAR | Name of the database from which the staged files are copied. |
| SUB_SERVICE_TYPE | VARCHAR | Type of service that is copying files, which can be one of the following:   *`COPY STAGE FILES`: See [COPY FILES](../sql/copy-files.md).* `SCHEMA CLONE`: See [CREATE <object> … CLONE](../sql/create-clone.md). * `DATABASE CLONE`: See [CREATE <object> … CLONE](../sql/create-clone.md). |
| JOB_ROOT_ENTITY_ID | NUMBER | Entity ID for the root job; varies by SUB_SERVICE_TYPE. For COPY STAGE FILES, indicates the ID of the stage from which files are copied. For SCHEMA CLONE, indicates the schema ID. For DATABASE CLONE, indicates the database ID. |
| START_TIME | TIMESTAMP_LTZ | The date and beginning of the hour (in the local time zone) in which the copy operation took place. |
| END_TIME | TIMESTAMP_LTZ | The date and end of the hour (in the local time zone) in which the copy operation took place. |
| CREDITS_USED | NUMBER | Number of compute credits used by warehouses and serverless compute resources between the START_TIME and END_TIME. |
| BYTES_COPIED | NUMBER | Number of bytes copied from the root entity (stage, schema, or database) between the START_TIME and END_TIME. |
| FILES_COPIED | NUMBER | Number of files copied from the root entity (stage, schema, or database) between the START_TIME and END_TIME. |
