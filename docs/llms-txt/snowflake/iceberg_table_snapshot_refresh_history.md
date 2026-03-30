# Source: https://docs.snowflake.com/en/sql-reference/functions/iceberg_table_snapshot_refresh_history.md

Categories:
:   [Table functions](../functions-table.md)

# ICEBERG_TABLE_SNAPSHOT_REFRESH_HISTORY

Returns metadata and [snapshot](../../user-guide/tables-iceberg.md) information about the most recent
refresh history for a specified externally managed Apache Iceberg™ table.

> **Note:**
>
> Snowflake version 9.16 added Delta-based table support for this function.
> The function only displays Delta-based table refresh data from version 9.16 and later.

See also:
:   [Apache Iceberg™ tables](../../user-guide/tables-iceberg.md) , [Metadata and retention for Apache Iceberg™ tables](../../user-guide/tables-iceberg-metadata.md) , [ALTER ICEBERG TABLE … REFRESH](../sql/alter-iceberg-table-refresh.md)

## Syntax

```sqlsyntax
ICEBERG_TABLE_SNAPSHOT_REFRESH_HISTORY(
  TABLE_NAME => '<table_name>'
)
```

## Arguments

`TABLE_NAME => 'table_name'`
:   The name of the [externally managed Iceberg table](../../user-guide/tables-iceberg.md)
    for which you want to retrieve the snapshot refresh history.

## Output

The function returns the following columns:

| Column name | Data type | Description | Delta-based table note |
| --- | --- | --- | --- |
| REFRESHED_ON | TIMESTAMP_LTZ | The timestamp when the table was last refreshed. |  |
| METADATA_FILE_NAME | TEXT | The full path to the metadata file. | The full path to the commit or checkpoint file. |
| SNAPSHOT_ID | TEXT | The snapshot ID of the last refresh. | The resulting commit ID of the last refresh. |
| SEQUENCE_NUMBER | TEXT | The sequence number of the last refresh; NULL for Iceberg v1. | Not applicable for Delta-based tables; displays as NULL. |
| ICEBERG_SCHEMA_ID | TEXT | The schema ID of the refresh (from metadata). | Not applicable for Delta-based tables; displays as NULL. |
| QUERY_ID | TEXT | The ID of the query that performed the refresh. For tables that use [automated refresh](../../user-guide/tables-iceberg-auto-refresh.md), this column contains a sentinel value, which indicates that the refresh was automated. |  |
| IS_CURRENT_SNAPSHOT | BOOLEAN | TRUE if the table is refreshed on this snapshot; otherwise, FALSE. | TRUE if the table is refreshed on this version (commit); otherwise, FALSE. |
| SNAPSHOT_SUMMARY | VARIANT | The Iceberg snapshot summary from the `metadata.json` file. NULL if not present in the metadata file. | Not applicable for Delta-based tables; displays as NULL. |

## Examples

Retrieve information for the current version of an externally managed Iceberg table named `my_iceberg_table`:

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.ICEBERG_TABLE_SNAPSHOT_REFRESH_HISTORY(
    TABLE_NAME => 'my_iceberg_table'
  ));
```

Output:

```output
+-------------------------------+----------------------------------------------------------------------------------+---------------------+-----------------+-------------------+--------------------------------------+---------------------+---------------------------------+
| REFRESHED_ON                  | METADATA_FILE_NAME                                                               | SNAPSHOT_ID         | SEQUENCE_NUMBER | ICEBERG_SCHEMA_ID | QUERY_ID                             | IS_CURRENT_SNAPSHOT | SNAPSHOT_SUMMARY                |
|-------------------------------+----------------------------------------------------------------------------------+---------------------+-----------------+-------------------+--------------------------------------+---------------------+---------------------------------|
| 2024-12-09 11:00:50.506 -0800 | s3://my-bucket/metadata/00000-e3bf7230-283f-4626-a770-fe97a3ca239e.metadata.json | NULL                | NULL            | 0                 | 01b8ebb4-0002-3a10-0000-012903c7e42a | False               | NULL                            |
| 2024-12-09 11:01:35.543 -0800 | s3://my-bucket/metadata/00001-bf116652-b5b0-479a-947e-6c799e4ca124.metadata.json | 6201065399847600377 | NULL            | 0                 | 01b8ebb5-0002-3a14-0000-012903c7f336 | True                | {                               |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "added-data-files": "4",      |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "added-files-size": "144896", |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "added-records": "150000",    |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "manifests-created": "1",     |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "manifests-kept": "0",        |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "manifests-replaced": "0",    |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "total-data-files": "4",      |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "total-files-size": "144896", |
|                               |                                                                                  |                     |                 |                   |                                      |                     |   "total-records": "150000"     |
|                               |                                                                                  |                     |                 |                   |                                      |                     | }                               |
+-------------------------------+----------------------------------------------------------------------------------+---------------------+-----------------+-------------------+--------------------------------------+---------------------+---------------------------------+
```
