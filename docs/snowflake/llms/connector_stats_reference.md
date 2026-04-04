# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/connector_stats_reference.md

# Connector stats reference

## Database objects and procedures

The following database objects are created through the file `observability/connector_stats.sql`.

### PUBLIC.GENERIC_CONNECTOR_STATS

View not available for any role, access via view `CONNECTOR_STATS`. View providing the data about ongoing and finished
ingestion runs. A view that retrieves and maps the data from the union of [`STATE.INGESTION_RUN` /
`STATE.RESOURCE_INGESTION_DEFINITION` / `STATE.INGESTION_PROCESS`] internal tables.

View structure with mapping is as follows:

1. ID (col) → RUN_ID (col);
2. RESOURCE_INGESTION_DEFINITION_ID (col)
3. INGESTION_CONFIGURATION_ID (col)
4. INGESTION_PROCESS_ID (col)
5. NAME (col)
6. STARTED_AT (col)
7. UPDATED_AT (col)
8. COMPLETED_AT (col)
9. STATUS (col)
10. INGESTED_ROWS (col)
11. DATEDIFF(second from STARTED_AT and COMPLETED_AT) (col) → DURATION_S (col);
12. INGESTED_ROWS (col) / DURATION_S (col) → THROUGHPUT_RPS (col);
13. METADATA (col)

### PUBLIC.AGGREGATED_CONNECTOR_STATS

This view is exposed to the `ADMIN` and `VIEWER` roles. It returns aggregated data from the above view and allows
access for the defined user. The rows will be grouped by truncated hours and displayed with summed updated rows.
View providing the aggregated data about daily ingestion runs.

A view that retrieves and maps the data from the `GENERIC_CONNECTOR_STATS` internal table
The mapping is as follows:

1. GROUPED BY(hours from STARTED_AT (col)) → RUN_DATE (col);
2. SUM(INGESTED_ROWS (col)) → UPDATED_ROWS (col);

Example `AGGREGATED_CONNECTOR_STATS` view created on example GENERIC_CONNECTOR_STATS:

| RUN_DATE | UPDATED_ROWS |
| --- | --- |
| <timestamp_ntz> | 20 |
| <timestamp_ntz> | 40 |
| … | … |

Overwriting this view is not recommended.

### PUBLIC.CONNECTOR_STATS

This view is exposed to the `ADMIN` role. It returns data from the connector stats view and allows access for the defined user.
In the default implementation this view exists only as an additional layer above `GENERIC_CONNECTOR_STATS`.
This implementation should be overwritten if some additional custom data needs to be added.

## Related tables and views

Connector stats are related to and dependent on the objects from the following files:

* `ingestion/ingestion_run.sql` (See: [STATE.INGESTION_RUN](resource_definition_and_ingestion_processes_reference.md))
* `ingestion/resource_ingestion_definition.sql` (See: [STATE.RESOURCE_INGESTION_DEFINITION](resource_definition_and_ingestion_processes_reference.md))
* `ingestion/ingestion_process.sql` (See: [STATE.INGESTION_PROCESS](resource_definition_and_ingestion_processes_reference.md))
