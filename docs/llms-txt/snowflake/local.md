# Source: https://docs.snowflake.com/en/sql-reference/local.md

# LOCAL schema

Some Snowflake features use the LOCAL schema of the SNOWFLAKE database to store telemetry data for logging and results analysis. The tables, views, and functions available in the LOCAL schema depend on which features you use in an account. Visibility of available objects in the LOCAL schema are access-controlled.

## LOCAL tables

All tables in the LOCAL schema use the [event table structure](../developer-guide/logging-tracing/event-table-columns.md).

The LOCAL schema provides the following tables:

| Table | Associated Snowflake feature | Notes |
| --- | --- | --- |
| AI_OBSERVABILITY_EVENTS | [AI Observability](../user-guide/snowflake-cortex/ai-observability.md) | Raw event data for AI Observability. For information about querying this table, see [Observability data](../user-guide/snowflake-cortex/ai-observability/reference.md). |
| CORTEX_ANALYST_REQUESTS_RAW | [Cortex Analyst](../user-guide/snowflake-cortex/cortex-analyst.md) | Raw event data for Cortex Analyst. For information about querying this table, see [Querying logs with SQL](../user-guide/snowflake-cortex/cortex-analyst/admin-observability.md) |
| DATA_QUALITY_MONITORING_RESULTS_RAW | [Data Quality](../user-guide/data-quality-intro.md) | Raw event data for Data Quality. For information about querying this table, see [Query the DATA_QUALITY_MONITORING_RESULTS_RAW table](../user-guide/data-quality-results.md). |

> **Note:**
>
> Data stored in LOCAL tables incurs Snowflake storage charges. For information about storage costs, see [Understanding storage cost](../user-guide/cost-understanding-data-storage.md).

## LOCAL views

The LOCAL schema provides the following views:

| View | Associated Snowflake feature | Notes |
| --- | --- | --- |
| [CORTEX_ANALYST_REQUESTS_V](local/cortex_analyst_requests_v.md) | [Cortex Analyst](../user-guide/snowflake-cortex/cortex-analyst.md) | For information about querying this view, see [Querying logs with SQL](../user-guide/snowflake-cortex/cortex-analyst/admin-observability.md). |
| [DATA_QUALITY_MONITORING_RESULTS](local/data_quality_monitoring_results.md) | [Data Quality](../user-guide/data-quality-intro.md) | For information about querying this view, see [Query the DATA_QUALITY_MONITORING_RESULTS view](../user-guide/data-quality-results.md). |
| [DATA_QUALITY_MONITORING_ANOMALY_DETECTION_STATUS](local/data_quality_monitoring_anomaly_detection_status.md) | [Data quality anomaly detection](../user-guide/data-quality-anomaly.md) |  |
| [DATA_QUALITY_MONITORING_EXPECTATION_STATUS](local/data_quality_monitoring_expectation_status.md) | [Data quality expectations](../user-guide/data-quality-expectations.md) |  |

## LOCAL functions

The LOCAL schema provides the following functions:

| Function | Associated Snowflake feature | Notes |
| --- | --- | --- |
| CORTEX_ANALYST_REQUESTS | [Cortex Analyst](../user-guide/snowflake-cortex/cortex-analyst.md) | For information about how to call this function, see [Querying logs with SQL](../user-guide/snowflake-cortex/cortex-analyst/admin-observability.md). |
| [DATA_QUALITY_MONITORING_RESULTS](functions/data_quality_monitoring_results.md) | [Data Quality](../user-guide/data-quality-intro.md) | For information about how to call this function, see [Call the DATA_QUALITY_MONITORING_RESULTS function](../user-guide/data-quality-results.md) |
| GET_AI_OBSERVABILITY_EVENTS | [AI Observability](../user-guide/snowflake-cortex/ai-observability.md) | For information about AI Observability data, see [Observability data](../user-guide/snowflake-cortex/ai-observability/reference.md). |
