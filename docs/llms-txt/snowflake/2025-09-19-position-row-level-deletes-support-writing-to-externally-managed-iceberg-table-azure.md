# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-09-19-position-row-level-deletes-support-writing-to-externally-managed-iceberg-table-azure.md

# Sep 19, 2025: Support for position row-level deletes when writing to externally managed Apache Iceberg™ tables or catalog-linked databases on Azure (*Preview*)

Snowflake now supports position row-level deletes for Azure when writing to externally managed tables.
These deletes are supported when Snowflake performs update, delete, and merge operations on
the table files. This feature is a performance improvement for these operations.

For more information, see [Write support for externally managed Apache Iceberg™ tables](../../../user-guide/tables-iceberg-externally-managed-writes.md) and [Use a catalog-linked database for Apache Iceberg™ tables](../../../user-guide/tables-iceberg-catalog-linked-database.md).
