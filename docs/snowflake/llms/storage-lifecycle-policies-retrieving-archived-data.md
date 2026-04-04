# Source: https://docs.snowflake.com/en/user-guide/storage-management/storage-lifecycle-policies-retrieving-archived-data.md

# Retrieve archived data

Read archived data by using the [CREATE TABLE … FROM ARCHIVE OF](../../sql-reference/sql/create-table.md) command.

For example, the following statement creates a new table from archived rows where the value in the `event_timestamp` column is between
January 15 and January 20 of 2023:

```sqlexample
CREATE TABLE my_table
  FROM ARCHIVE OF my_source_table AS st
  WHERE st.event_timestamp BETWEEN '01/15/2023' AND '01/20/2023';
```

For syntax details and parameter descriptions, see [CREATE TABLE … FROM ARCHIVE OF](../../sql-reference/sql/create-table.md)
in the [CREATE TABLE](../../sql-reference/sql/create-table.md) documentation.

> **Note:**
>
> * Using this command requires the OWNERSHIP privilege on the source table.
> * Specifying column definitions, policies, tags, or other constraints isn’t supported. Snowflake automatically retrieves
>   the table schema, policies, tags, and constraints from the source table.
> * The WHERE clause is required. Reading archived data is expensive, and should be performed infrequently.
>   Filtering results using the WHERE clause helps you minimize costs by ensuring that Snowflake reads only the data that you
>   require from archival storage.
> * To estimate the number of files that Snowflake will retrieve from archive storage, run the [EXPLAIN](../../sql-reference/sql/explain.md) command before
>   this operation. The output includes a `createTableFromArchiveData` operation and displays `ARCHIVE OF <table>` in
>   the `objects` column for the TableScan operation. For more information, see Estimate retrieval costs with EXPLAIN.
> * To see a history of data retrieval from archive storage, use the [ARCHIVE_STORAGE_DATA_RETRIEVAL_USAGE_HISTORY view](../../sql-reference/account-usage/archive_storage_data_retrieval_usage_history.md).
> * To retrieve data from the COLD tier of archive storage, Snowflake must first restore the files from external cloud storage. This process
>   can take up to 48 hours.
>
>   To support this process, set the following parameters appropriately:
>
>   * [STATEMENT_TIMEOUT_IN_SECONDS](../../sql-reference/parameters.md) must be at least 48 hours.
>   * [ABORT_DETACHED_QUERY](../../sql-reference/parameters.md) must be FALSE.
>
>   COLD storage tier restore operations support a maximum of 1 million files per restore operation.
> * If you cancel a CREATE TABLE operation that retrieves data from archive storage, you might still incur retrieval costs.

## Estimate retrieval costs with EXPLAIN

To estimate how many files Snowflake will retrieve from archive storage, use the [EXPLAIN](../../sql-reference/sql/explain.md) command.

The command output includes the following data:

* A `createTableFromArchiveData` operation in the `operation` column.
* `ARCHIVE OF <table>` in the `objects` column for the TableScan operation.
* The number of partitions that will be retrieved in the `assignedPartitions` column for the archive
  TableScan operation. This value indicates the number of partitions
  that Snowflake will restore from cold tier to retrieve the data from archive storage.

For example:

```sqlexample
EXPLAIN
CREATE TABLE my_table
  FROM ARCHIVE OF my_source_table AS st
  WHERE st.event_timestamp BETWEEN '01/15/2023' AND '01/20/2023';
```
