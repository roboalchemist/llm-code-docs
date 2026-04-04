# Source: https://docs.snowflake.com/en/sql-reference/info-schema/cortex_search.md

# CORTEX_SEARCH_SERVICES view

This view shows existing Cortex Search Services in the current or specified database.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SERVICE_CATALOG | VARCHAR | Database that the service belongs to. |
| SERVICE_SCHEMA | VARCHAR | Schema that the service belongs to. |
| SERVICE_NAME | VARCHAR | Name of the service. |
| CREATED | TIMESTAMP_LTZ | Creation time of the service. |
| DEFINITION | VARCHAR | SQL query used to create the service. |
| SEARCH_COLUMN | VARCHAR | Name of the search column. |
| ATTRIBUTE_COLUMNS | VARCHAR | Comma-separated list of attribute columns in the service. |
| COLUMNS | VARCHAR | Comma-separated list of all columns included in the service. |
| TARGET_LAG | VARCHAR | Target lag for refreshing the service. |
| WAREHOUSE | VARCHAR | Name of the warehouse used for refreshing the service. |
| COMMENT | VARCHAR | Comment for this service. |
| SERVICE_QUERY_URL | VARCHAR | URL for querying the service. |
| OWNER | VARCHAR | Role that owns the service. |
| OWNER_ROLE_TYPE | VARCHAR | Type of role of the service owner (one of DATABASE_ROLE or ROLE). |
| DATA_TIMESTAMP | TIMESTAMP_LTZ | Time at which the source data was checked for changes resulting in the currently serving index. |
| SOURCE_DATA_BYTES | NUMBER | Current size, in bytes, of the materialized source data. |
| SOURCE_DATA_NUM_ROWS | NUMBER | Current number of rows in the materialized source data. |
| INDEXING_STATE | VARCHAR | Indexing state of the service (one of SUSPENDED or RUNNING). |
| INDEXING_ERROR | VARCHAR | Error encountered in the last indexing pipeline, if one exists. |
| SERVING_STATE | VARCHAR | Serving state of the service (one of SUSPENDED or RUNNING). |
| SERVING_DATA_BYTES | NUMBER | Size of the billable serving data, in bytes. |
| EMBEDDING_MODEL | VARCHAR | The vector embedding model used by the service. |
| PRIMARY_KEY_COLUMNS | VARCHAR | Comma-separated list of primary key column names defined on the service. Empty if no primary key is set. |

## Example

```sqlexample
SELECT * FROM SNOWFLAKE.INFORMATION_SCHEMA.CORTEX_SEARCH_SERVICES;
```
