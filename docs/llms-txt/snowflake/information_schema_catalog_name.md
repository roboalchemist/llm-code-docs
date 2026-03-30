# Source: https://docs.snowflake.com/en/sql-reference/info-schema/information_schema_catalog_name.md

# INFORMATION_SCHEMA_CATALOG_NAME view

This Information Schema view identifies the database (or catalog, in SQL terminology) that contains the INFORMATION_SCHEMA schema.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| CATALOG_NAME | VARCHAR | The name of the database in which this information_schema resides. |

## Usage notes

* This view always contains a single row.
