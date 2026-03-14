# Source: https://docs.snowflake.com/en/user-guide/tables-external-auto.md

# Refresh external tables automatically

Event notifications for cloud storage can start refreshes of the external table metadata or add or drop file references.

> **Important:**
>
> If you transfer ownership on an external table or its parent database by using the [GRANT OWNERSHIP](../sql-reference/sql/grant-ownership.md) command,
> this sets the table’s `AUTO_REFRESH` property to `FALSE`. This blocks automatic refreshes of the table metadata.
> To restore automatic refreshes after you transfer ownership, set `AUTO_REFRESH = TRUE`
> by using the [ALTER EXTERNAL TABLE](../sql-reference/sql/alter-external-table.md) command.

**Next topics:**

* [Refresh external tables automatically for Amazon S3](tables-external-s3.md)
* [Refresh external tables automatically for Google Cloud Storage](tables-external-gcs.md)
* [Refresh external tables automatically for Azure Blob Storage](tables-external-azure.md)
