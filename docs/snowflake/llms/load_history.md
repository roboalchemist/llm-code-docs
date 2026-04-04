# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/load_history.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/load_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/load_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# LOAD_HISTORY view

This Account Usage view enables you to retrieve the history of data loaded into tables using the [COPY INTO <table>](../sql/copy-into-table.md) command within the last 365 days (1 year). The view displays one row for each file loaded.

> **Note:**
>
> This view does not return the history of data loaded using Snowpipe. For this historical information, query the [COPY_HISTORY](copy_history.md) view instead.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| TABLE_ID | NUMBER | Internal/system-generated identifier for the target table |
| TABLE_NAME | VARCHAR | Name of target table |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the target table |
| SCHEMA_NAME | VARCHAR | Schema of target table |
| CATALOG_ID | NUMBER | Internal/system-generated identifier for the database of the target table |
| CATALOG_NAME | VARCHAR | Database of target table |
| FILE_NAME | VARCHAR | Name of source file |
| LAST_LOAD_TIME | TIMESTAMP_LTZ | Date and time (in the UTC time zone) of the load record |
| STATUS | VARCHAR | Status: `LOADED`, `LOAD FAILED`, or `PARTIALLY LOADED` |
| ROW_COUNT | NUMBER | Number of rows loaded from the source file |
| ROW_PARSED | NUMBER | Number of rows parsed from the source file |
| FIRST_ERROR_MESSAGE | VARCHAR | First error of the source file |
| FIRST_ERROR_LINE_NUMBER | NUMBER | Line number of the first error |
| FIRST_ERROR_CHARACTER_POSITION | NUMBER | Position of the first error character |
| FIRST_ERROR_COL_NAME | VARCHAR | Column name of the first error |
| ERROR_COUNT | NUMBER | Number of error rows in the source file |
| ERROR_LIMIT | NUMBER | If the number of error reach this limit, then abort |

## Usage notes

* In most cases, latency for the view may be up to 90 minutes. The latency for a given table’s load history in the view may be up to 2 days if both of the following conditions are true:

  * Fewer than 32 DML statements have been added to the given table since it was last updated in LOAD_HISTORY.
  * Fewer than 100 rows have been added to the given table since it was last updated in LOAD_HISTORY.

* The view only includes COPY INTO commands that executed to completion, with or without errors. No record is added if the transaction is rolled back, for example, or if the ON_ERROR = ABORT_STATEMENT copy option is included in the COPY INTO *<table>* statement and a detected error in a data file aborts the load operation.
* When including a WHERE clause that references the `LAST_LOAD_TIME` column, you can specify any day of the week. For example, April 1, 2016 was a Friday; however, specifying Sunday instead does not
  affect the query results:

  ```sqlexample
  WHERE last_load_time > 'Sun, 01 Apr 2016 16:00:00 -0800'
  ```

* After the replication of load history, the LOAD_HISTORY Account Usage view shows the history only after the latest truncate operation on the target table. This is different from the view without replication, which shows a complete data loading history.

## Examples

Retrieve records for the 10 most recent COPY INTO commands executed:

> ```sqlexample
> SELECT file_name, last_load_time FROM snowflake.account_usage.load_history
>   ORDER BY last_load_time DESC
>   LIMIT 10;
> ```
