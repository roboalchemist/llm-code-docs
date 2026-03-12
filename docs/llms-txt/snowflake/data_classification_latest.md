# Source: https://docs.snowflake.com/en/sql-reference/account-usage/data_classification_latest.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# DATA_CLASSIFICATION_LATEST view

This Account Usage view displays one row for the most recent result of a classified table for each classified table. Each row corresponds
to a different table.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| TABLE_ID | Number | Internal/system-generated identifier for the table that was classified. |
| TABLE_NAME | VARCHAR | Name of the table. |
| SCHEMA_ID | Number | Internal/system-generated identifier for the schema that contains the table. |
| SCHEMA_NAME | VARCHAR | Name of the schema that contains the table. |
| DATABASE_ID | Number | Internal/system-generated identifier for the database that contains the table. |
| DATABASE_NAME | VARCHAR | Name of the database that contains the table. |
| RESULT | VARIANT | Latest classification result. For a description of the JSON object, see the output of the [SYSTEM$GET_CLASSIFICATION_RESULT](../functions/system_get_classification_result.md) function. |
| STATUS | VARCHAR | One of the following: `CLASSIFIED` or `REVIEWED`. |
| TRIGGER_TYPE | VARCHAR | Mode of the classification trigger: `MANUAL` or `AUTO CLASSIFICATION`, where `MANUAL` indicates that someone called a system function to initiate the classification process. |
| LAST_CLASSIFIED_ON | TIMESTAMP_LTZ | Time when the table was last successfully classified. |
| LAST_CLASSIFICATION_ATTEMPT | TIMESTAMP_LTZ | Timestamp of the last sensitive data classification attempt. If the value is greater than `LAST_CLASSIFIED_ON`, it indicates that the last sensitive data classification attempt resulted in a failure. |
| ERROR_MESSAGE | VARCHAR | Error message from the last sensitive data classification attempt, if it resulted in a failure. |

## Usage notes

* Latency for this view might be up to three hours.
* This view retains data for as long as the table exists.
* A row in the view is removed when the following occur:

  * A table is dropped or renamed.
  * The table is reclassified.
