# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/fetchdatabasemetadata.md

# FetchDatabaseMetadata 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-horizon-catalog-processors-nar

## Description

Fetches complete database metadata for all tables and outputs them to a FlowFile. The output is a JSON array containing database information and schema details for all tables, including column names, data types, and metadata. The schema fetching supports PostgreSQL, MySQL, and SQL Server. For SQL Server, this processor can retrieve metadata from ALL accessible databases when connected with appropriate permissions. For PostgreSQL and MySQL, it retrieves metadata from the connected database. Output format (array of database objects): [ { “source”: “<database_type>”, “database_name”: “<database_name>”, “schemas”: [ { “name”: “<schema_name>”, “entities”: [ { “name”: “<table_name>”, “type”: “table”, “comment”: “<table_comment>”, “total_rows”: <number_of_rows>, “columns”: [ { “name”: “<column_name>”, “comment”: “<column_comment>”, “data_type”: “<data_type>” } ], “created_on”: <epoch_millis>, “updated_on”: <epoch_millis> } ] } ] } ] Note: For SQL Server connections, if the connection has access to multiple databases, the array will contain multiple database objects. For PostgreSQL and MySQL, the array will contain a single database object. Table and column comments, created_on, updated_on timestamps, and total_rows are included when available from the database metadata, but may be omitted if not supported by the database system. Timestamps are represented as epoch milliseconds, or -1 if not available. Total rows represents an approximate/estimated value from database statistics (not an exact count) and is set to -1 if it cannot be determined due to permissions or other database-specific limitations.

## Tags

database, metadata, schema, table

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Connection Pool | The connection pool to use to fetch the schema information |

## Relationships

| Name | Description |
| --- | --- |
| failure | FlowFiles are routed to this relationship when the schema information cannot be fetched |
| no tables found | FlowFiles are routed to this relationship when no tables are found in any accessible database |
| retryable failure | FlowFiles are routed to this relationship when fetching the schema information failed, but might be able to succeed when the operation is retried |
| success | FlowFiles are routed to this relationship when the schema information is successfully fetched |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | application/json |
| dbms.type | The type of database management system (DBMS). E.g. `POSTGRESQL` |
| database.count | The number of databases found and processed |
| schema.count | The total number of schemas found across all databases |
| table.count | The total number of tables found across all databases and schemas |
